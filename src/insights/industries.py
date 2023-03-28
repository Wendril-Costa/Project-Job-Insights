from typing import List, Dict
from src.insights.jobs import get_unique_types, filter_by


def get_unique_industries(path: str) -> List[str]:
    return get_unique_types(path, "industry")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return filter_by(jobs, 'industry', industry)
