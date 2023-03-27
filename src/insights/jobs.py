from functools import lru_cache
from typing import List, Dict

import csv

file = "data/jobs.csv"


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as table:
        table_list = list(csv.DictReader(table))
        return table_list


def get_unique_job_types(path: str) -> List[str]:
    table = read(path)
    list_job_type = set()
    for job_type in table:
        list_job_type.add(job_type["job_type"])
    return list(list_job_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
