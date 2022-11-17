import requests
import matplotlib.pyplot as plt
import csv
import pandas as pd
import plotly.express as px


def writeToFile(papers_by_year, save_path):
    field_names = ["Year", "NumPapers"]
    with open(save_path, "w+") as file:
        csvWriter = csv.writer(file, delimiter=",")
        csvWriter.writerow(field_names)
        for key in papers_by_year.keys():
            file.write("%s, %s\n" % (key, papers_by_year[key]))


def fetchDeepfakeAndEthicsPapers():
    papers_by_year = {}
    for year in range(2000, 2023):
        result = requests.get(
            "http://api.semanticscholar.org/graph/v1/paper/search?query=deepfake+ethic&year={}".format(
                year
            )
        )

        if result.reason != "OK":
            print("Error: ", result.status_code, result.reason)
            exit

        paper_records = result.json()
        num_papers = paper_records["total"]
        print(
            "Total number of deepfake+ethic papers in {}: {}".format(year, num_papers)
        )
        papers_by_year[year] = num_papers

    return papers_by_year


def fetchDeepfakePapers():
    papers_by_year = {}
    for year in range(2000, 2023):
        result = requests.get(
            "http://api.semanticscholar.org/graph/v1/paper/search?query=deepfake&year={}".format(
                year
            )
        )

        if result.reason != "OK":
            print("Error: ", result.status_code, result.reason)
            exit

        paper_records = result.json()
        num_papers = paper_records["total"]
        print("Total number of deepfake papers in {}: {}".format(year, num_papers))
        papers_by_year[year] = num_papers

        return papers_by_year


def plotData(file):
    df = pd.read_csv(file)

    fig = px.line(
        df,
        y="NumPapers",
        x="Year",
        title="Number of Deepfake Paper Publications Over Time",
    )
    fig.show()


deepfake_file = "num_deepfake_papers_by_year.csv"
deepfake_ethics_file = "num_deepfake_ethics_papers_by_year.csv"

# deepfake_papers_by_year = fetchDeepfakePapers()
deepfake_ethics_papers_by_year = fetchDeepfakeAndEthicsPapers()
# writeToFile(deepfake_papers_by_year, save_path=deepfake_file)
writeToFile(deepfake_ethics_papers_by_year, save_path=deepfake_ethics_file)
# plotData(deepfake_papers_by_year)
plotData(deepfake_ethics_papers_by_year)
