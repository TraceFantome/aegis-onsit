import os

import pandas as pd
import requests

BASE = "https://www.courtlistener.com/api/rest/v3/opinions/"
PARAMS = {"q": "money laundering OR shell company", "page_size": 10}


def fetch():
    ua = os.environ.get("AEGIS_UA", "Aegis-OSINT/0.1 (+contact: tracefantome@pm.me)")
    headers = {"User-Agent": ua, "Accept": "application/json"}
    r = requests.get(BASE, params=PARAMS, headers=headers, timeout=30)
    if r.status_code == 403:
        raise SystemExit(
            "403 Forbidden: CourtListener requires a real User-Agent with contact info.\n"
            "Set one like: export AEGIS_UA='Aegis-OSINT/0.1 (+contact: you@example.com)'"
        )
    r.raise_for_status()
    data = r.json().get("results", [])
    if not data:
        return pd.DataFrame()
    df = pd.json_normalize(data)
    keep = [
        c
        for c in df.columns
        if c in ("date_filed", "caseName", "absolute_url", "court", "citation")
    ]
    return df[keep] if keep else df


if __name__ == "__main__":
    df = fetch()
    print(f"Rows: {len(df)}")
    print(df.head(10).to_string(index=False))
    print("\nNote: Data via CourtListener (Free Law Project).")
