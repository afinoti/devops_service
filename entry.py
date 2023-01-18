"""Main application file"""

from time import sleep
from service import my_example_service
import os


if __name__ == "__main__":

    for k, v in os.environ.items():
        print(f"{k}={v}")
