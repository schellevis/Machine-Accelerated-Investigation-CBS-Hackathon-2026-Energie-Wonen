#!/usr/bin/env python3
"""
Live smoke test for CBS StatLine endpoints used in this repo.

Confirms that:
  1. The CBS OData v4 base service (datasets.cbs.nl) is reachable.
  2. Every table referenced in docs/skill-feedback.md still resolves.

Note: CBS table identifiers are case-sensitive at the OData v1/v4 API
(e.g. "80030ned", not "80030NED") — this catches that too.

Run with: make test-live
"""

import sys

import requests

BASE = "https://datasets.cbs.nl/odata/v1/CBS"
TIMEOUT = 15

# Table IDs referenced in docs/skill-feedback.md (case as used in the docs).
TABLES = {
    "83140NED": "Energiebalans; aanbod, omzetting en verbruik",
    "83989NED": "Energiebalans; aanbod en verbruik, sector",
    "86103NED": "Aardgasbalans; aanbod en verbruik",
    "84575NED": "Elektriciteitsbalans; aanbod en verbruik",
    "85929NED": "Grote batterijen voor opslag van elektriciteit",
    "80030ned": "Elektriciteit en warmte; productie en inzet naar energiedrager (discontinued, kept for historical 1998-2024 data — see 86266NED for the successor table)",
    "84918NED": "Vermeden verbruik fossiele energie en emissie CO2",
    "82610NED": "Hernieuwbare elektriciteit; productie en vermogen",
    "85004NED": "Hernieuwbare energie; zonnestroom, windenergie, RES-regio",
}


def check(url: str, label: str) -> bool:
    try:
        r = requests.get(url, timeout=TIMEOUT)
    except requests.RequestException as exc:
        print(f"  FAIL  {label:12s} {url}  ({exc})")
        return False
    ok = r.status_code == 200
    status = "OK  " if ok else "FAIL"
    print(f"  {status}  {label:12s} {url}  -> {r.status_code}")
    return ok


def main() -> int:
    print(f"Checking CBS OData v4 base service: {BASE}")
    all_ok = check(BASE, "base")

    print("\nChecking tables referenced in docs/skill-feedback.md:")
    for table_id, title in TABLES.items():
        ok = check(f"{BASE}/{table_id}", table_id)
        if not ok:
            print(f"        {title}")
        all_ok = all_ok and ok

    print()
    if all_ok:
        print("All CBS endpoints reachable.")
        return 0
    print("One or more CBS endpoints failed. See output above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
