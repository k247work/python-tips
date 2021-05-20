import pytest

def test_pass_fail(testdir):

    # create temp pytest module
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        def test_fail():
            assert 1 == 2
    """)

    # execute pytest
    result = testdir.runpytest()

    # fnmatch_lines execute assertion internally
    result.stdout.fnmatch_lines([
        '*.F*', # . means success, F means failure
    ])

    # check terminal code of test suite is 1
    assert result.ret == 1

@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        def test_fail():
            assert 1 == 2
    """)
    return testdir

def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.O*',]) # . means success, O means failure
    assert result.ret == 1

# def test_with_nice_verbose

# def test_not_nice_verbose