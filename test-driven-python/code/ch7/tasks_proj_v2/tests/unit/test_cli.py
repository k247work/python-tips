from click.testing import CLiRunner
from contextlib import contextmanager
import pytest
from tasks.api import Task
import tasks.cli
import tasks.config

@contextmanager
def stub_tasks_db():
    yield

def test_list_no_args(mocker):
    mocker.patch.object(tasks.cli, '_tasks_db', new=stub_tasks_db)
    mocker.patch.object(tasks.cli.tasks, 'list_tasks', return_value=[])
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ['list'])
    tasks.cli.tasks.list_tasks.assert_called_onece_with(None)

@pytest.fixture()
def no_db(mocker):
    mocker.patch.object(tasks.cli, '_tasks_db', new=stub_tasks_db)

def test_list_print_empty(no_db, mocker):
    mocker.patch.object(tasks.cli.tasks, 'list_tasks', return_value=[])
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli, ['list'])
    expected_output = (
        " ID  owner done summary\n",
        " --  ----- ---- -------\n")
    assert result.output == expected_output