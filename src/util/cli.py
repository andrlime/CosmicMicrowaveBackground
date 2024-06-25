"""
CLI to parse command line arguments
"""

import argparse
import pathlib


class CLI:
    """
    Command line interface to take arguments for CMB data analysis
    which can be used to automagically spawn processes
    """

    def __init__(self, args):
        parser = argparse.ArgumentParser(
            description="CLI for CMB data analysis"
        )
        parser.add_argument(
            "--threshold", dest="threshold", type=float, required=True
        )
        parser.add_argument(
            "--data_source", dest="path", type=pathlib.Path, required=True
        )
        arguments = parser.parse_args(args)

        if arguments.threshold < 0 or arguments.threshold > 1:
            raise ValueError("Threshold must be between 0 and 1.")

        # self.longitude = arguments.longitude
        # self.latitude = arguments.latitude
        self.threshold = arguments.threshold
        self.path = arguments.path

    def get_threshold(self):
        return self.threshold

    def get_path(self):
        return self.path
