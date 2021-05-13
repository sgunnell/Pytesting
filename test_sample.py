#content of test_sample.py
import pytest

#prints the temp directory
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0
