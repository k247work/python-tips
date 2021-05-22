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

def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        '*::test_fail OPPORTUNITY for improvement*',
    ])

    assert result.ret == 1

def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED*'])
    assert result.ret == 1

def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['Thanks for running thte tests.'])

def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'Thanks for running thte tests.'
    assert thanks_message not in result.stdout.str()

def test_help_message(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice:turn FAILED into Opportunity for improvement'])

