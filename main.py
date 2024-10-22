"""
ETL-Query script
"""

# from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

import os
import sys


def main():

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # Extract
    # print("Extracting data...")
    # extract()

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    print("Querying data...")
    query()

if __name__ == "__main__":
    main()