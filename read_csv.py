import csv
import logging
from numpy import genfromtxt


class ReadCsv:

    def __init__(self, fname):
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        self.data = None
        self.read_csv(fname)

    # Read CSV File
    def read_csv(self, fname):

        data_np = genfromtxt(fname, delimiter=',')
        self.data = data_np

        # try:
        #     data_csv = genfromtxt(fname, delimiter=',')
        #     write_json(data_csv)
        # except Exception: # this is always getting flagged.
        # Try to write it in a diferent way.
        # ALWAYS CAUGHT HERE /////
        #     logging.debug('Exception: not a csv file')
        #     raise Exception("Exception: not a csv file")
