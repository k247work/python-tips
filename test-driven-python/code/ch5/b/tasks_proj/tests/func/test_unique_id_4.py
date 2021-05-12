import pytest
import tasks
from tasks import Task

@pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='not supported until 0.2.0')
def test_unique_id_1():
    """Calling unique_id twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_is_not_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid != 'a duck'


def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # setup: start db connection
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # execute test

    # teardown: terminate db connection
    tasks.stop_tasks_db()