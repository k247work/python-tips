import pytest
import tasks
from tasks import Task

def test_tmpdir(tmpdir):
    # path name attached to tmpdir
    # join() extends path to include file name
    # file will be created when data is written
    a_file = tmpdir.join('something.txt')

    # make directory
    a_sub_dir = tmpdir.mkdir('anything')

    # make file in directory
    another_file = a_sub_dir.join('something_else.txt')

    # 'something.txt' is created with this writing
    a_file.write('contents may settle during shpping')

    # 'anything/something_else.txt' is created with this writing
    another_file.write('something different')

    # file read is possible
    assert a_file.read() == 'contents may settle during shpping'
    assert another_file.read() == 'something different'

