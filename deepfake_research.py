import requests

result = requests.get(
    "http://api.semanticscholar.org/graph/v1/paper/search?query=deepfake&limit=50"
)

if result.reason != "OK":
    print(result.status_code, result.reason)
    exit

paper_records = result.json()
hits = paper_records["data"]
papers_by_year = {}

for hit in hits:
    result = requests.get(
        "https://api.semanticscholar.org/graph/v1/paper/{id}?fields=url,year,title".format(
            id=hit["paperId"]
        )
    )

    if result.reason != "OK":
        print(result.status_code, result.reason)
    exit

    paper_info = result.json()
    year = paper_info["year"]
    if year in papers_by_year:
        papers_by_year[year] += 1
    else:
        papers_by_year[year] = 1

    print(papers_by_year)
