"""
Functional utilities that take Planck maps and return Planck maps
with some mathematical operation applied to them
"""

import numpy as np


def normalize_map(planck_map):
    """
    Normalize a map to be between 0 and 1. Subtracts the minimum,
    which forces the map min to be zero, and then divides by the max
    to scale everything down into [0,1].

    Arguments
    ---------
    map (np.array): map to normalize

    Returns
    -------
    normalized_map (np.array): normalized map
    """
    normalized_map = planck_map.copy()
    normalized_map -= np.min(normalized_map)

    # Avoid divide by zero by just returning the map of all zeros
    max_value = np.max(normalized_map)
    if max_value == 0:
        return normalized_map

    normalized_map = normalized_map / max_value
    return normalized_map


def threshold_map(planck_map, threshold):
    """
    Threshold a map to be either 0 and 1. When the map is below threshold,
    it becomes zero; when above, it becomes 1.

    Arguments
    ---------
    map (np.array): map to threshold

    Returns
    -------
    thresholded_map (np.array): thresholded map
    """
    thresholded_map = np.copy(planck_map)
    thresholded_map[thresholded_map < threshold] = 0
    thresholded_map[thresholded_map >= threshold] = 1
    return thresholded_map


def process_raw(data, threshold):
    normalized_map = normalize_map(data)
    return threshold_map(normalized_map, threshold * np.mean(normalized_map))
