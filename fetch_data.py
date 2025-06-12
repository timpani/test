import json
from urllib.request import urlopen

URL = "https://service.taipower.com.tw/data/opendata/apply/file/d006001/001.json"

def fetch_data(url: str = URL):
    """Fetch JSON data from the given URL."""
    with urlopen(url) as response:
        charset = response.headers.get_content_charset() or 'utf-8'
        # Handle potential UTF-8 BOM by using utf-8-sig
        if charset.lower() == 'utf-8':
            charset = 'utf-8-sig'
        data = response.read().decode(charset)
        return json.loads(data)

def main():
    data = fetch_data()
    # Pretty-print the JSON content
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
