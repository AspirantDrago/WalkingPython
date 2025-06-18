from os import path
import subprocess

import pytest


class TestUtil:
    def test_empty_dirs(self):
        out = subprocess.check_output([
            'python',
            r'..\..\src\main.py',
            'samples'
        ], encoding='utf-8')
        assert out == ''

    def test_one_file(self):
        filename = path.join('samples', 'one.txt')
        open(filename, 'w').close()
        out = subprocess.check_output([
            'python',
            r'..\..\src\main.py',
            'samples'
        ], encoding='utf-8')
        assert out.strip() == filename

    def test_one_file_in_subdirectory(self):
        filename = path.join('samples', '1', '11', 'one.txt')
        open(filename, 'w').close()
        out = subprocess.check_output([
            'python',
            r'..\..\src\main.py',
            'samples'
        ], encoding='utf-8')
        assert out.strip() == filename

    def test_many_files(self):
        files = [
            path.join('samples', '0.txt'),
            path.join('samples', '1', 'a.txt'),
            path.join('samples', '1', 'b.txt'),
            path.join('samples', '1', '11', 'c.txt'),
            path.join('samples', '2', 'd.txt'),
        ]
        for file in files:
            open(file, 'w').close()
        out = subprocess.check_output([
            'python',
            r'..\..\src\main.py',
            'samples'
        ], encoding='utf-8')
        assert out.splitlines() == files

    def test_many_files_with_random_creation(self):
        files = [
            path.join('samples', '2', 'd.txt'),
            path.join('samples', '1', '11', 'c.txt'),
            path.join('samples', '0.txt'),
            path.join('samples', '1', 'b.txt'),
            path.join('samples', '1', 'a.txt'),
        ]
        for file in files:
            open(file, 'w').close()
        out = subprocess.check_output([
            'python',
            r'..\..\src\main.py',
            'samples'
        ], encoding='utf-8')
        assert out.splitlines() == sorted(files)
