from typing import List
from src.insights.jobs import read


def max_or_min_salary(path: str, string: str) -> List[int]:
    salary = []
    for jobs in read(path):
        try:
            salary.append(int(jobs[string]))
        except ValueError:
            print("Valor Invalido")
    return salary
