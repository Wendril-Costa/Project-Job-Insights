from functools import lru_cache
from typing import List, Dict
import csv


def get_unique_types(path: str, type: str) -> List[str]:
    return list(set(jobs[type] for jobs in read(path) if jobs[type]))


def filter_by(jobs: List[Dict], type: str, string: str) -> List[Dict]:
    return list(job for job in jobs if job[type] == string)


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path) as jobs_path_file:
            return [jobs for jobs in csv.DictReader(jobs_path_file)]
    except FileNotFoundError:
        print("Aquivo não foi encontrado")


def get_unique_job_types(path: str) -> List[str]:
    return get_unique_types(path, "job_type")


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return filter_by(jobs, 'job_type', job_type)
