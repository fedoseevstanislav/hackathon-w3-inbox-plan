#!/usr/bin/env python3
"""Ключ для сверки из легенды и карты.

    python3 make_key.py answers/legend.json answers/map.json > answers/key.json
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

json.dump({"items": items, "noise": mp["noise"], "personal": mp.get("personal", [])},
          sys.stdout, ensure_ascii=False, indent=1)
print()
