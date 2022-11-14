import requests
import matplotlib.pyplot as plt
import numpy as np

result = requests.get(
    "http://api.semanticscholar.org/graph/v1/paper/search?query=deepfake&limit=50"
)

if result.reason != "OK":
    print(result.status_code, result.reason)
    exit

paper_records = result.json()
hits = paper_records["data"]
print("Total number of papers: {}".format(len(hits)))
years = []

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
    years.append(year)

fig = plt.figure()
counts, bins = np.histogram(years)
plt.bar(counts, bins)
plt.xlabel("Year")
plt.ylabel("Number of Papers")
title = "Number of Deepfake Paper Publications Over Time"
fig.suptitle(title, wrap=True)
plt.show()
