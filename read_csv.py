import csv
import logging
from numpy import genfromtxt


class ReadCsv:
    """This is a ReadCsv class.

    __init__ sets the attributes

    Attributes:
        data (ndarray): Csv Values in single array

    Arguments:
        fname (str): file name of csv
    """

    def __init__(self, fname):
        logging.basicConfig(filename="read_csv_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        if not self:
            logging.warning('file name is empty')
            raise ValueError("file name is empty")
        if not isinstance(fname, str):
            logging.warning('Your file name is not a string')
            raise TypeError("file name is not a string")
        if ".csv" not in fname:
            logging.warning('Your file is not a .csv file')
            raise TypeError("file is not a .csv file")

        self.data = None
        self.read_csv(fname)

    # Read CSV File
    def read_csv(self, fname):
        """
        :param fname:  csv file name
        :returns data: ndarray of all data in .csv
        """
        data_np = genfromtxt(fname, delimiter=',')
        self.data = data_np
