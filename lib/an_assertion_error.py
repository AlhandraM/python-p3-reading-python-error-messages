#!/usr/bin/env python3

import pytest

def test_intentional_failure():
    with pytest.raises(AssertionError):
        assert(1 == 2)

