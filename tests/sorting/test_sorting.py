from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    sort_by(read("data/jobs.csv"), "max_salary")

    assert read("data/jobs.csv")[0]["min_salary"] == "195818"

    assert read("data/jobs.csv")[0]["max_salary"] == "383416"

    assert read("data/jobs.csv")[0]['date_posted'] == '2020-05-07'
