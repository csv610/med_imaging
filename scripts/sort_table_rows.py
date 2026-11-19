#!/usr/bin/env python3
"""Alphabetize data rows in LaTeX tables by their first cell, keeping headers intact."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ENV = re.compile(r"\\begin\{(longtable|tabular|tabularx)\}(.*?)\\end\{\1\}", re.S)
ROW = re.compile(r"\\\\(?:\[[^\]]*\])?\s*(?:%.*)?$")
COMMAND = re.compile(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?")
HEADER = re.compile(r"\b(disease|condition|feature|parameter|category|procedure|finding|modality|characteristic|measurement|technique|score|application|system|classification|name|type|stage|grade|term|abbreviation|abnormality|indication|sign|method|sequence|property|process|target|criterion|criteria|organ|region|structure|contrast|radiopharmaceutical|tracer|value|range|level|effect|cause|artifact|pattern|protocol|step|year|date|milestone|phase|component|role|task|metric|dataset|resource|source|status|clinical question|imaging question|clinical use)\b", re.I)


def first_cell(line: str) -> str:
    cell = line.split("&", 1)[0]
    cell = re.sub(r"\\(?:textbf|textit|emph|underline)\s*\{([^{}]*)\}", r"\1", cell)
    cell = COMMAND.sub(" ", cell).replace("{", " ").replace("}", " ")
    return re.sub(r"\\[^\s{}]+", " ", cell).strip().casefold()


def sort_key(line: str):
    value = first_cell(line)
    # Natural ordering for numeric first columns, alphabetical otherwise.
    parts = re.split(r"(\d+(?:\.\d+)?)", value)
    return tuple((0, float(p)) if re.fullmatch(r"\d+(?:\.\d+)?", p) else (1, p) for p in parts)


changed_files = 0
changed_tables = 0
table_count = 0
sortable_tables = 0
for path in ROOT.rglob("*.tex"):
    original = path.read_text(encoding="utf-8")

    def replace(match):
        global changed_tables, table_count, sortable_tables
        table_count += 1
        body = match.group(2)
        lines = body.splitlines(keepends=True)
        row_indices = [i for i, line in enumerate(lines) if ROW.search(line.rstrip("\r\n"))]
        # Keep column headings and spanning section labels in place, but do not
        # exempt bold data labels from alphabetization.
        data_indices = [i for i in row_indices if r"\multicolumn" not in lines[i]
                       and not (r"\textbf{" in lines[i] and HEADER.search(first_cell(lines[i])))]
        if len(data_indices) < 2:
            return match.group(0)
        sortable_tables += 1
        # Tables conventionally begin with a column heading; preserve it if it is not explicitly identified.
        first_data = data_indices[0]
        if first_data == row_indices[0]:
            data_indices = data_indices[1:]
        if len(data_indices) < 2:
            return match.group(0)
        before = [lines[i] for i in data_indices]
        after = sorted(before, key=sort_key)
        if before != after:
            changed_tables += 1
            for i, row in zip(data_indices, after):
                lines[i] = row
        return match.group(0).replace(body, "".join(lines), 1)

    updated = ENV.sub(replace, original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        changed_files += 1

print(f"Alphabetically ordered {sortable_tables} of {table_count} tables; changed {changed_tables} tables across {changed_files} TeX files.")
