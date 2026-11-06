"""Read an Excel brief without editing it or executing formulas."""

import argparse
import json
import sys
from datetime import date, datetime, time
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.utils.cell import range_boundaries


def serializable(value):
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()
    if isinstance(value, CellRichText):
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def cell_record(cell, cached_cell):
    value = cell.value
    record = {"cell": cell.coordinate, "value": serializable(value),
              "bold": bool(cell.font.bold), "type": cell.data_type}
    if isinstance(value, CellRichText):
        runs = []
        for part in value:
            inline_bold = part.font.b if isinstance(part, TextBlock) else None
            runs.append({"text": part.text if isinstance(part, TextBlock) else str(part),
                         "bold": bool(cell.font.bold if inline_bold is None else inline_bold)})
        record["runs"] = runs
    if cell.data_type == "f":
        record["formula"] = value
        record["value"] = serializable(cached_cell.value)
        record["cached_value_available"] = cached_cell.value is not None
    if cell.hyperlink:
        record["hyperlink"] = cell.hyperlink.target or cell.hyperlink.location
    if cell.comment:
        record["comment"] = cell.comment.text
    return record


def extract(path, sheet_name=None, selected_range=None, max_cells=20000):
    workbook = load_workbook(path, rich_text=True, data_only=False)
    cached = load_workbook(path, data_only=True)
    try:
        if sheet_name and sheet_name not in workbook.sheetnames:
            raise ValueError(f"Unknown sheet: {sheet_name}")
        sheets = [workbook[sheet_name]] if sheet_name else workbook.worksheets
        result = {"source": str(path.resolve()), "formula_policy": "cached values only; no recalculation",
                  "sheets": []}
        total = 0
        for sheet in sheets:
            bounds = range_boundaries(selected_range or sheet.calculate_dimension())
            c1, r1, c2, r2 = bounds
            if any(v is None for v in bounds) or min(bounds) < 1 or c2 < c1 or r2 < r1:
                raise ValueError("Use a finite cell range such as A1:G30")
            total += (c2 - c1 + 1) * (r2 - r1 + 1)
            if total > max_cells:
                raise ValueError("Selected area is too large; choose --sheet/--range or increase --max-cells")
            cells = []
            cached_sheet = cached[sheet.title]
            for row in sheet.iter_rows(min_row=r1, max_row=r2, min_col=c1, max_col=c2):
                for cell in row:
                    if cell.value is not None or cell.hyperlink or cell.comment:
                        cells.append(cell_record(cell, cached_sheet[cell.coordinate]))
            merges = [str(area) for area in sheet.merged_cells.ranges
                      if area.min_col <= c2 and area.max_col >= c1
                      and area.min_row <= r2 and area.max_row >= r1]
            result["sheets"].append({"name": sheet.title, "range": selected_range or sheet.calculate_dimension(),
                                     "merged_ranges": merges, "cells": cells})
        return result
    finally:
        workbook.close()
        cached.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--output", required=True, type=Path, help="New JSON path; existing files are preserved")
    parser.add_argument("--sheet")
    parser.add_argument("--range", dest="selected_range", help="Cell range, e.g. A1:G30")
    parser.add_argument("--max-cells", type=int, default=20000)
    args = parser.parse_args()
    try:
        if args.output.exists():
            raise FileExistsError(f"Output already exists: {args.output}")
        if args.max_cells < 1:
            raise ValueError("--max-cells must be positive")
        result = extract(args.workbook, args.sheet, args.selected_range, args.max_cells)
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        print(f"Saved {len(result['sheets'])} sheet(s): {args.output}")
    except (OSError, ValueError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
