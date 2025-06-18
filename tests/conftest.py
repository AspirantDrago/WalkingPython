import os
from os import path, makedirs, removedirs
import shutil

import pytest


@pytest.fixture(autouse=True)
def app():
    makedirs('samples', exist_ok=True)
    makedirs(path.join('samples', '1'), exist_ok=True)
    makedirs(path.join('samples', '1', '11'), exist_ok=True)
    makedirs(path.join('samples', '2'), exist_ok=True)
    yield
    shutil.rmtree('samples')
