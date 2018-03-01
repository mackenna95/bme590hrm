import csv
import logging
from numpy import genfromtxt


class ReadCsv:

    def __init__(self, fname):
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        if not self:
            logging.warning('data set is empty')
            raise ValueError("data set is empty")

        self.data = None
        self.read_csv(fname)

    # Read CSV File
    def read_csv(self, fname):

        data_np = genfromtxt(fname, delimiter=',')
        self.data = data_np
