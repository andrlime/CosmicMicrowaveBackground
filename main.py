"""
src.main

Main file
"""

import sys

from src.util import CLI
from src.util import process_raw
from src.data import (
    read_file_data,
    generate_angles,
    extract_sectors,
    analyze
)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    cli_instance = CLI(arguments)

    data_source = read_file_data(cli_instance.get_path())
    processed_data = process_raw(data_source, cli_instance.get_threshold())
    angles_to_sample = generate_angles(data_source) # TODO

    sectors = extract_sectors(processed_data, angles_to_sample)
    analyze(sectors) # TODO
