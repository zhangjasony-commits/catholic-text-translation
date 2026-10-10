#!/usr/bin/env python3
"""Audit a translation coverage ledger; no linguistic or source validation."""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def audit(data):
    errors, pending = [], []
    if not isinstance(data, dict):
        return {"status": "ERROR", "errors": ["根对象必须为JSON对象"], "pending": []}
    sources, outputs = data.get("sources"), data.get("outputs")
    if not isinstance(sources, list) or not isinstance(outputs, list):
        return {"status": "ERROR", "errors": ["sources和outputs必须为数组"], "pending": []}
    output_map, source_ids, units, actions, used = {}, set(), {}, Counter(), set()
    for output in outputs:
        if not isinstance(output, dict) or not isinstance(output.get("id"), str) or not output["id"]:
            errors.append("译文单元缺少有效id")
            continue
        oid = output["id"]
        if oid in output_map:
            errors.append(f"译文ID重复: {oid}")
        output_map[oid] = output
        if not isinstance(output.get("text"), str) or not output["text"].strip():
            errors.append(f"空译文: {oid}")
    for source in sources:
        if not isinstance(source, dict) or not isinstance(source.get("id"), str) or not source["id"] or "/" in source["id"]:
            errors.append("来源缺少有效id，或id含斜线")
            continue
        sid = source["id"]
        if sid in source_ids:
            errors.append(f"来源ID重复: {sid}")
        source_ids.add(sid)
        if not isinstance(source.get("origin"), str) or source["origin"] not in {"supplied", "supplement"}:
            errors.append(f"来源类型无效: {sid}")
        if not isinstance(source.get("path_or_url"), str) or not source["path_or_url"].strip():
            errors.append(f"来源缺少路径或链接: {sid}")
        expected, entries = source.get("expected_unit_ids"), source.get("units")
        if not isinstance(expected, list) or not expected or not all(isinstance(x, str) and x and "/" not in x for x in expected):
            errors.append(f"缺少有效的预期单元清单: {sid}")
            expected = []
        if len(expected) != len(set(expected)):
            errors.append(f"预期单元ID重复: {sid}")
        if not isinstance(entries, list):
            errors.append(f"units必须为数组: {sid}")
            continue
        actual = set()
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get("id"), str) or not entry["id"] or "/" in entry["id"]:
                errors.append(f"源单元缺少有效id: {sid}")
                continue
            uid, key = entry["id"], f"{sid}/{entry['id']}"
            if key in units:
                errors.append(f"源单元ID重复: {key}")
            units[key] = entry
            actual.add(uid)
            if not isinstance(entry.get("locator"), str) or not entry["locator"].strip():
                errors.append(f"缺少定位: {key}")
            action = entry.get("action")
            if not isinstance(action, str) or action not in {"translate", "duplicate", "exclude", "pending"}:
                errors.append(f"处理状态无效: {key}")
                continue
            actions[action] += 1
            if action == "translate":
                refs = entry.get("output_ids")
                if not isinstance(refs, list) or not refs or not all(isinstance(x, str) and x for x in refs):
                    errors.append(f"缺少译文对应: {key}")
                    continue
                if len(refs) != len(set(refs)):
                    errors.append(f"重复的译文对应: {key}")
                for oid in refs:
                    used.add(oid)
                    if oid not in output_map:
                        errors.append(f"译文对应不存在: {key} -> {oid}")
            else:
                if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
                    errors.append(f"缺少处理理由: {key}")
                if entry.get("output_ids"):
                    errors.append(f"非翻译状态附带译文对应: {key}")
                if action == "pending":
                    pending.append({"unit": key, "reason": entry.get("reason", "")})
        for uid in sorted(set(expected) - actual):
            errors.append(f"清单漏项: {sid}/{uid}")
        for uid in sorted(actual - set(expected)):
            errors.append(f"未列入预期清单的单元: {sid}/{uid}")
    for key, entry in units.items():
        if entry.get("action") == "duplicate":
            target = entry.get("duplicate_of")
            if not isinstance(target, str) or target not in units:
                errors.append(f"重复项指向不存在: {key}")
            elif units[target].get("action") != "translate":
                errors.append(f"重复项必须直接指向翻译单元: {key} -> {target}")
    for oid in sorted(set(output_map) - used):
        errors.append(f"译文无来源对应: {oid}")
    if not sources:
        errors.append("来源清单为空")
    return {
        "status": "ERROR" if errors else "INCOMPLETE" if pending else "COMPLETE",
        "sources": len(source_ids), "source_units": len(units), "output_units": len(output_map),
        "actions": dict(actions), "errors": errors, "pending": pending,
        "scope": "仅检查覆盖记录结构；不证明原文范围完整或译文正确"
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        result = audit(json.loads(args.ledger.read_text(encoding="utf-8-sig")))
    except (OSError, ValueError) as exc:
        result = {"status": "ERROR", "errors": [str(exc)], "pending": []}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return {"COMPLETE": 0, "INCOMPLETE": 1, "ERROR": 2}[result["status"]]


if __name__ == "__main__":
    sys.exit(main())
