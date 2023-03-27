from typing import List, Dict
from src.insights.jobs import read

file = "data/jobs.csv"


def get_unique_industries(path: str) -> List[str]:
    table = read(path)
    list_industries = set()
    for industries in table:
        list_industries.add(industries["industry"])
    return list(list_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
