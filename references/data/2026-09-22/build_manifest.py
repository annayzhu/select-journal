"""Rebuild the source inventory. Requires openpyxl; leaves source files unchanged."""
import csv
import hashlib
import json
from pathlib import Path

import openpyxl

root = Path(__file__).resolve().parent
records = []
for path in sorted(root.iterdir()):
    if path.suffix not in {".csv", ".xlsx"}:
        continue
    record = {"file": path.name, "bytes": path.stat().st_size,
              "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    if path.suffix == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = csv.reader(handle)
            record["columns"] = next(rows)
            record["data_rows"] = sum(1 for _ in rows)
    else:
        workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
        record["sheets"] = []
        for sheet in workbook:
            rows = sheet.iter_rows(values_only=True)
            columns = list(next(rows))
            record["sheets"].append({"name": sheet.title, "columns": columns,
                                     "data_rows": sum(1 for _ in rows)})
        workbook.close()
    records.append(record)
manifest = {"received_date": "2026-09-22", "status": "user-file provided",
            "files": records}
(root / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({r["file"]: r.get("data_rows", r.get("sheets")) for r in records},
                 ensure_ascii=False))
