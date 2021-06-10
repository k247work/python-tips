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
        " ID  owner done summary\n"
        " --  ----- ---- -------\n")
    assert result.output == expected_output

def test_list_print_many_items(no_db, mocker):
    many_tasks = (
        Task('write chapter', 'Brian', True, 1),
        Task('edit chapter', 'Katie', False, 2),
        Task('modify chapter', 'Brian', False, 3),
        Task('finalize chapter', 'Katie', False, 4)
    )
    mocker.patch.object(tasks.cli.tasks, 'list_tasks',
                return_value=many_tasks)
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli,['list'])
    expected_output = (
        " ID  owner done summary\n"
        " --  ----- ---- -------\n"
        "  1  Brian  True write chapter\n"
        "  2  Katie False edit chapter\n"
        "  1  Brian False modify chapter\n"
        "  1  Brian False finalize chapter\n")
    assert result.output == expected_output