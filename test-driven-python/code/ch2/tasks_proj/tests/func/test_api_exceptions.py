import py
import pytest
import tasks

@pytest.mark.smoke
def test_add_rases():
    """add() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')

@pytest.mark.smoke
@pytest.mark.get
def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as excinfo: # raise -> excinfo
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

class TestUpdate():
    """Test expected exceptions with tasks.update()"""

    def test_bad_id(self):
        """A non-int id should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead':1}, task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')
