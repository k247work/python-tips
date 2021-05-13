import pytest
import tasks
from tasks import Task

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    """Calling unique_id twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # get unique ID
    uid = tasks.unique_id()
    assert uid not in ids


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # setup: start db connection
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # execute test

    # teardown: terminate db connection
    tasks.stop_tasks_db()