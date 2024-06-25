"""
Data module for data importing, analysis, and exporting
"""

from src.data.input import read_file_data
from src.data.process import generate_angles
from src.data.process import extract_sectors
from src.data.analyze import analyze_and_write_gaps_data
from src.data.analyze import analyze_and_write_flhl_data

def analyze(sectors):
    analyze_and_write_gaps_data(sectors)
    analyze_and_write_flhl_data(sectors)
