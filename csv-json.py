import sys, getopt
import csv
import json
import logging
from numpy import genfromtxt

class CsvJson:

    def __init__(self, fname):
        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        self.data = None
        self.read_csv(fname) # error, states I am supplying 3 args

    #Read CSV File
    def read_csv(self, fname):

        data_csv = genfromtxt(fname, delimiter=',')
        self.write_json(data_csv)

        #try:
        #    data_csv = genfromtxt(fname, delimiter=',')
        #    write_json(data_csv)
        #except Exception: # this is always getting flagged. Try to write it in a diferent way. # ALWAYS CAUGHT HERE /////
        #    logging.debug('Exception: not a csv file')
        #    raise Exception("Exception: not a csv file")

    #Convert csv data into json and write it
    def write_json(self, data_csv):
        convert = data_csv.tolist() 
        data_json = json.dumps(convert) 
        self.data = data_json
