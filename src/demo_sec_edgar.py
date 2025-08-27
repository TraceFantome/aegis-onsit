import requests
import pandas as pd
import os

BASE = "https://data.sec.gov/submissions/CIK0000320193.json"  # Apple Inc
UA = os.environ.get("AEGIS_UA", "Aegis-OSINT/0.1 (+contact: tracefantome@pm.me)")

def fetch():
    headers = {"User-Agent": UA}
    r = requests.get(BASE, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()
    filings = data.get("filings", {}).get("recent", {})
    if not filings:
        return pd.DataFrame()
    df = pd.DataFrame(filings)
    keep = ["accessionNumber", "filingDate", "form", "primaryDocDescription"]
    return df[keep]

if __name__ == "__main__":
    df = fetch()
    print(f"Rows: {len(df)}")
    print(df.head(10).to_string(index=False))
    print("\nNote: Data via SEC EDGAR.")
