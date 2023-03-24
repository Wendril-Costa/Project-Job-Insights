from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path) as jobs_path_file:
            return [jobs for jobs in csv.DictReader(jobs_path_file)]
    except FileNotFoundError:
        print('Aquivo não foi encontrado')


def get_unique_job_types(path: str) -> List[str]:
    return list(set(jobs['job_type'] for jobs in read(path)))


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
