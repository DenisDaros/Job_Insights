from typing import Union, List, Dict
from src.insights.jobs import read

file = "data/jobs.csv"


def get_max_salary(path: str) -> int:
    table = read(path)
    all_max_salary = set()
    for i in table:
        if i["max_salary"].isnumeric():
            all_max_salary.add(int(i["max_salary"]))
    return max(all_max_salary)


def get_min_salary(path: str) -> int:
    table = read(path)
    all_min_salary = set()
    for i in table:
        if i["min_salary"].isnumeric():
            all_min_salary.add(int(i["min_salary"]))
    return min(all_min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try: 
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])

        salary = int(salary)
        if max_salary < min_salary:
            raise ValueError('Error')
        return max_salary >= salary >= min_salary
    except (ValueError, TypeError, KeyError):
        raise ValueError('Error')


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
