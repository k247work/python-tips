from click.testing import CLiRunner
from contextlib import contextmanager
import pytest
from tasks.api import Task
import tasks.cli
import tasks.config

@contextmanager
def stub_tasks_db():
    yield