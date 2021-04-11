import pytest
import tasks
from tasks import Task

def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

def equivalent(t1, t2):
    """Check two tasks for eqivalence"""
    # compare all fields except for ID
    return ((t1.summary == t2.summary) and
        (t1.owner == t2.owner) and (t1.done == t2.done))

@pytest.mark.parametrize('task',
    [Task('sleep', done=True),
     Task('wake', 'brian'),
     Task('breathe', 'BRIAN', True),
     Task('exercise', 'BrIaN', False)])
def test_add_2(task):
    """Demonstrate parametrize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('summary, owner, done',
    [('sleep', None, False),
     ('wake', 'brian', False),
     ('breathe', 'BRIAN', True),
     ('eat eggs', 'BrIaN', False)])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameter."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

tasks_to_try = (Task('sleep', done=True),
        Task('wake', 'brian'),
        Task('wake', 'brian'),
        Task('breathe', 'BRIAN', True),
        Task('exercise', 'BrIaN', False))

@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # setup: start db connection
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # execute test

    # teardown: terminate db connection
    tasks.stop_tasks_db()