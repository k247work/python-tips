import pytest

def pytest_report_header():
    """Thank tester for running tests."""
    return "Thanks for running the tests."

def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call' and report.failed:
        return (report.outcome, 'O', 'Opportunity for improvement')