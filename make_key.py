#!/usr/bin/env python3
"""Ключ для сверки из легенды и карты.

    python3 make_key.py answers/legend.json answers/map.json > answers/key.json
    python3 make_key.py answers/legend.json answers/map.json answers/legend-2.json > answers/key-2.json

Третий аргумент — ключ этапа 2: его дела добавляются к делам этапа 1 или заменяют их
(И3, И12 с новыми источниками), «no_row» добавляется к шуму.
"""
import json
import sys

legend = json.load(open(sys.argv[1], encoding="utf-8"))
mp = json.load(open(sys.argv[2], encoding="utf-8"))

items = {}
for iid, it in legend["items"].items():
    m = mp["items"][iid]
    date, _, time = it.get("date", "").partition(" ")
    items[iid] = {
        "section": it["section"],
        "what": it["what"],
        "ids": m.get("emails", []) + m.get("chat", []),
        "closing": m.get("closing"),
        "date": date or None,
        "time": time or None,
        "check": it.get("check"),
    }

key = {"items": items, "noise": mp["noise"], "personal": mp.get("personal", [])}

if len(sys.argv) > 3:
    l2 = json.load(open(sys.argv[3], encoding="utf-8"))
    for iid, it in l2["items"].items():
        old = items.get(iid, {})
        date = it.get("date", old.get("date"))
        items[iid] = {
            "section": it["section"],
            "what": it["what"],
            "ids": it["ids"],
            "closing": old.get("closing"),
            "date": date,
            "alt_dates": it.get("alt_dates", []),
            "time": old.get("time"),
            "check": old.get("check"),
            "guess": it.get("guess") == "обязательна",
            "promise": iid.startswith("О"),
            "contradiction": it.get("contradiction"),
        }
    key["noise"] = key["noise"] + list(l2["no_row"])
    key["not_open"] = {k: v["ids"] for k, v in l2["not_open"].items()}

json.dump(key,
          sys.stdout, ensure_ascii=False, indent=1)
print()
