import pandas as pd
import requests

API_URL = "https://api.opencorporates.com/v0.4/companies/search"


def search_companies(query: str, per_page: int = 5) -> pd.DataFrame:
    params = {"q": query, "per_page": per_page}
    r = requests.get(API_URL, params=params, timeout=20)
    r.raise_for_status()
    data = r.json().get("results", {}).get("companies", [])
    return pd.json_normalize(data)


if __name__ == "__main__":
    df = search_companies("Tesla")
    print(df.head())
