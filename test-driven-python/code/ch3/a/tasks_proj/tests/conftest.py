import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # setup: start connection to db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield # execute tests

    # teardown: terminate connection to db
    tasks.stop_tasks_db()