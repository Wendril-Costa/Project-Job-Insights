from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    for jobs in read_brazilian_file("tests/mocks/brazilians_jobs.csv"):
        assert 'title' in jobs
        assert 'salary' in jobs
        assert 'type' in jobs
