"""
Tools for reading data from various sources

TODO: Make into abstract class
"""

import pathlib
import healpy as hp


def read_file_data(path: pathlib.Path):
    """
    Reads data from the path specified by `path`
    """

    intensity_map, _, _ = hp.read_map(path, field=(0, 1, 2))
    return intensity_map
