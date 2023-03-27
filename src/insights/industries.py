from typing import List, Dict
from src.insights.jobs import read

file = "data/jobs.csv"


def get_unique_industries(path: str) -> List[str]:
    table = read(path)
    list_industries = set()
    for industries in table:
        if industries["industry"] != '':
            list_industries.add(industries["industry"])
    return list(list_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_industries = list()
    for industries in jobs:
        if industries["industry"] == industry:
            list_industries.append(industries)
    return list_industries
