import pytest
import tasks
from tasks import Task

def test_tmpdir_factory(tmpdir_factory):
    # first, create directory
    # a_dir acts as object returned from tmpdir fixture
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_temp is parents directory of 'mydir'
    # getbasetemp() is not necessary to use: at here
    # We use it to show this function is available
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # remains of this test is the same as test_tmpdir()
    # except for using a_dir insteat of tmnpdir

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')
    
    a_file.write('contents may settle during shpping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shpping'
    assert another_file.read() == 'something different'

