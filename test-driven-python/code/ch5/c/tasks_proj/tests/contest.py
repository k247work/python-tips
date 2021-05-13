import pytest

def pytest_report_header():
    """Thank tester for running tests."""
    return "Thanks for running the tests."

def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call' and report.failed:
        return (report.outcome, 'O', 'Opportunity for improvement')

def pytest_addoption(parser):
    """Turn nice features on with --nice option."""
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
            help="nice: turn failures into opportunities")

def pytest_report_header():
    """Thank tester for running tests."""
    if pytest.config.get_option('nice'):
        return "Thanks for running the tests."

def pytest_report_teststatus(report):
    """Turn failuers into opportunities"""
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return (report.ooutcome, 'O', 'Opportunity for improvement')