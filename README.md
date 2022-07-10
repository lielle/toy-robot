## Description
This is a Python program for the toy robot exam.

## Setup
Please use python version `3.10.3`. Create a virtual environment and install the dependencies via `pip install -r requirements.txt`.

If you plan on doing code changes, use pre-commit hook via `pre-commit install` to run the hooks before every commit.

## Usage
Enter inputs in `input.txt` and save the file before running `main.py` via `python -m main`. The output will be in the standard I/O.

## Running tests
To run all tests, enter the command `python -m pytest`. If you want to include the coverage report, run `coverage run -m pytest && coverage report -m`.