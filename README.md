# Cosmic Microwave Background Project
[![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

Write-up will go here eventually.

## Installing development utilities
To install **[Taskfile](https://taskfile.dev/installation)**, run `brew install go-task` on MacOS. Then, **assuming you have [Homebrew](https://brew.sh/) installed**, run `task init` to install Poetry, or alternatively, run `pipx install poetry`. Instructions to install `pipx` can be widely found on the internet.

## Running
Everything is piped into `src/main.py`. To run this file, run `task run -- ...` where `...` are all of your command line arguments. Alternatively, you can run `poetry run python -m src.main ...` (`...` are the arguments) to run the program without using Taskfile. If you anticipate running a lot of stuff, run `poetry shell` to activate a shell in this repository's `venv`, and just run `python -m src.main` (you can omit the `poetry run`). Taskfile is the easiest way to run the program.

## Architecture
Instead of shoving everything into one file, we split this program into three layers: data fetching, data processing and piping, and data analysis:

1. Data fetching fetches data from a remote source (e.g. a SQL database or curl) and saves it. This layer does not do any data processing.
2. Data processing and piping processes data from some input format into some output format. The output format is preferably a CSV, but if a function to read some other format exists, other formats work too. This data is then piped into the data processing scripts by writing what is effectively an iterator with `.next()` (the data processor simply calls `.next()` to get more data to process).
3. Data analysis analyzes processed data into the output we want. This layer is the bottleneck in terms of performance, and should be parallelized extensively.

One approach would be to write these as separate binaries and use the OS to pipe data between them (possibly using gRPC), but for submitting on Quest, is simpler as a single binary where each layer is a separate instance of a class. Data analysis can easily be vertically scaled by adding a middle-man layer that contains multiple `DataAnalysis` instances and distributes data amongst them evenly.

# Details
## Taskfile tasks
- `init` installs Poetry and installs dependencies. You must have Homebrew installed, which you have to do on your own.
- `run` runs `src.main` which is the main script for the program. Command line arguments are directly forwarded into the program.
- `format` runs `black` on all code
- `lint` runs `pylint` and `black --check` on all code and forces adherence to the Google style guide. This decreases spaghetti code and increases readability/maintainability
- `test` runs `pytest` and runs all test cases

## Data Fetching
Write-up later

## Data Processing
Write-up later

## Data Piping
Write-up later

## Data Analysis
Write-up later

