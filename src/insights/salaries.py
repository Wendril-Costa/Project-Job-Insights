from typing import Union, List, Dict
from src.insights.utils import max_or_min_salary


def get_max_salary(path: str) -> int:
    return max(max_or_min_salary(path, "max_salary"))


def get_min_salary(path: str) -> int:
    return min(max_or_min_salary(path, "min_salary"))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], (int, str))
        or not isinstance(job["max_salary"], (int, str))
        or not isinstance(salary, (int, str))
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_ = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_.append(job)
        except ValueError:
            pass
    return jobs_
