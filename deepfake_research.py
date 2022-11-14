import requests

result = requests.get(
    "http://api.semanticscholar.org/graph/v1/paper/search?query=deepfake&limit=50"
)

if result.reason != "OK":
    print(result.status_code, result.reason)
    exit

paper_records = result.json()
hits = paper_records["data"]
