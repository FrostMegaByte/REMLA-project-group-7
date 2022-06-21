#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 01:07:50 PM CEST 2022

This file is for fixtures. Pytest will automatically "discover" fixtures in
any file named `conftest.py` and there are more ways to "discover" fixtures.

@author hielke
"""
from os import listdir
from os.path import join
from pathlib import Path

import pytest


@pytest.fixture()
def root_folder():
    cwd = Path().absolute()
    if "test" in cwd.parts[-1]:
        # run inside the tests folder
        return cwd.parent
    return cwd


@pytest.fixture(autouse=True)
def data_folder(root_folder):
    yield root_folder / "data"


@pytest.fixture()
def test_folder(root_folder):
    yield root_folder / "tests"


def pytest_generate_tests(metafunc):
    root = Path().absolute()
    if "test" in root.parts[-1]:
        root = root.parent

    if "data_step" in metafunc.fixturenames and "data_set" in metafunc.fixturenames:
        params = []
        for step in ["raw", "interim"]:
            for filename in listdir(join(root, "data", step)):
                if ".tsv" in filename:
                    params.append((step, filename[:-4]))
        metafunc.parametrize("data_step, data_set", params)
