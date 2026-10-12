#!/usr/bin/env python3
"""Сверка плана на день с ключом.

    python3 sverka.py plan.md inbox.md chat.md key.json

plan.md  — результат по INSTRUCTION.md (раздел «1. План» с таблицей).
inbox.md, chat.md — данные, по которым собран план (для проверки ссылок).
key.json — ключ (см. make_key.py).

Печатает сверку в Markdown; код возврата 0, если все пункты ключа найдены в верном
разделе, даты верны, шума в плане нет и у каждой строки есть рабочая ссылка на источник.
"""
import json
import re
import sys

ID = re.compile(r"\b([EC]\d{2,3})\b")
LINK = re.compile(r"\]\(([^)#\s]+)#([a-z]\d{2,3})\)")
DATE = re.compile(r"\b(\d{2}\.\d{2}\.\d{4})\b")


def anchors(path):
    return set(re.findall(r'<a id="([a-z]\d{2,3})"></a>', open(path, encoding="utf-8").read()))


def section(text, n):
    parts = re.split(r"(?m)^#{2,3}\s*(\d)\.", text)
    for i in range(1, len(parts) - 1, 2):
        if parts[i] == str(n):
            return parts[i + 1]
    return ""


def read_plan(path):
    rows = []
    for line in section(open(path, encoding="utf-8").read(), 1).splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*:?-", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7 or not re.match(r"^P\d+", cells[0]):
            continue
        rows.append({"id": cells[0], "section": cells[1].lower().replace("ё", "е"),
                     "what": cells[2], "due": cells[3], "src": cells[4],
                     "draft": " | ".join(cells[6:]),
                     "ids": [x.upper() for x in ID.findall(cells[4])],
                     "links": LINK.findall(cells[4])})
    return rows


def main(plan_path, inbox_path, chat_path, key_path):
    key = json.load(open(key_path, encoding="utf-8"))
    rows = read_plan(plan_path)
    have = {"inbox.md": anchors(inbox_path), "chat.md": anchors(chat_path)}
    out, ok = [], True

    out.append("| Ключ | Строка плана | Раздел (ключ → план) | Срок (ключ → план) | Ссылка на закрывшее сообщение | Черновик: «Кому» и 2+ фразы |")
    out.append("|---|---|---|---|---|---|")
    used = set()
    for kid, k in key["items"].items():
        cand = sorted(((len(set(r["ids"]) & set(k["ids"])), r) for r in rows), key=lambda x: -x[0])
        if not cand or cand[0][0] == 0:
            ok = False
            out.append(f"| {kid} | — | {k['section']} → — ✗ | — | — | — |")
            continue
        r = cand[0][1]
        used.add(r["id"])
        sec_ok = r["section"] == k["section"].replace("ё", "е")
        ok &= sec_ok
        due = "—"
        if k["date"]:
            dates = DATE.findall(r["due"])
            d_ok = bool(dates) and dates[0] == k["date"]
            if k["time"]:
                d_ok &= k["time"] in r["due"]
            ok &= d_ok
            due = f"{k['date']} {k['time'] or ''} → {r['due'][:40]} {'✓' if d_ok else '✗'}"
        clo = "—"
        if k["closing"]:
            c_ok = k["closing"].lower() in [a for _, a in r["links"]]
            ok &= c_ok
            clo = f"{k['closing']} {'да' if c_ok else 'нет'}"
        dr_ok = bool(re.search(r"кому", r["draft"], re.I)) and len(re.findall(r"[.!?…]", r["draft"])) >= 2
        ok &= dr_ok
        out.append(f"| {kid} | {r['id']} | {k['section']} → {r['section']} {'✓' if sec_ok else '✗'} "
                   f"| {due} | {clo} | {'есть' if dr_ok else 'нет'} |")

    out.append("")
    noise = set(key["noise"])
    noisy = [(r["id"], sorted(set(r["ids"]) & noise)) for r in rows if set(r["ids"]) & noise]
    ok &= not noisy
    out.append(f"Шум в плане (проверка 4): {'нет' if not noisy else noisy}.")

    extra = [r for r in rows if r["id"] not in used]
    personal = set(key.get("personal", []))
    out.append(f"Лишних строк плана: {len(extra)}.")
    for r in extra:
        tag = " (личное письмо без дела)" if set(r["ids"]) & personal else ""
        out.append(f"- {r['id']} {r['section']} {', '.join(r['ids'])}: {r['what']}{tag}")

    out.append("")
    bad = []
    for r in rows:
        if not r["links"]:
            bad.append(f"{r['id']}: нет ссылки")
        for f, a in r["links"]:
            if a not in have.get(f.split("/")[-1], set()):
                bad.append(f"{r['id']}: ссылка {f}#{a} никуда не ведёт")
    ok &= not bad
    out.append(f"Ссылки (проверка 5): у {len(rows) - len({b.split(':')[0] for b in bad})} из {len(rows)} строк все ссылки ведут на письмо или сообщение.")
    out += [f"- {b}" for b in bad]

    print("\n".join(out))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:5]))
