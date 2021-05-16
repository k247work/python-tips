import pytest

def pytest_addoption(parser):
    """Turn nice failure on with --nice option."""
    group = parser.getgroup('nice')
    group.addoption(
        "--nice", action="store_tru",
        help="nice: turn FAILED int OPPORTNITY for improvement"
    )

def pytest_report_header():
    """Thank tester for running tests"""
    if pytest.config.getoption('nice'):
        return "Thanks for running the tests"

def pytest_report_teststatus(report):
    """Turn failures into opportunities"""
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return (report.outcome, 'O', 'Opportunity for improvement')