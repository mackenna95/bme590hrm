import numpy as np
from read_csv import ReadCsv


class HeartRateMonitor:
    """This is a HeartRateMonitor class.

    __init__ sets the attributes

    Attributes:
        mean_hr_bpm (int/float): heart rate over a user-specified minutes
        voltage_extreemes (tuple): minimum and maximum lead voltages
        duration (int/float): time duration of the ECG strip
        num_beats (int/float): number of detected beats in the strip
        beats (numpy array): times when a beat occurred

    Arguments:
        data (string): string containing name of csv file
        scale (int/float): to convert time to seconds
        (i.e. 60 if the data is logged in minutes)
        interval (???): time interval for average heart rate
    """

    def __init__(self, data_csv, scale, interval):
        self.mean_hr_bpm = None
        self.voltage_extreemes = None
        self.duration = None
        self.num_beats = None
        self.beats = None
        data = self.ReadCsv(data_csv, scale)
        self.return_mean_hr_bpm(data, interval)
        self.return_voltage_extreemes(data)
        self.return_duration(data)
        self.return_num_beats(data)
        self.return_beats(data)

    def ReadCsv(self, data_csv, scale):
        """
        :param self:    ECG data
        :returns data:  ECG data as np array
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        data_csv = ReadCsv(data_csv)
        logging.info("Success: data as np array returned.")
        return data_csv.data

    def return_mean_hr_bpm(self, data, interval):
        """
        :param self:            ECG data
        :returns mean_hr_bpm:   heart rate over a user-specified minutes
        :raises TypeError:      value not int or float
        :raises ValueError:     list is empty
        :raises ImportError:    packages not found
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        try:
            mean_hr_bpm = 1  # "CODE HERE" /////
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.mean_hr_bpm = mean_hr_bpm
        logging.info("Success: mean_hr_bpm returned.")

    def return_voltage_extreemes(self, data):
        """
        :param self:                ECG data
        :returns voltage_extreemes: tuple containing min, max lead voltages
        :raises TypeError:          value not int or float
        :raises ValueError:         list is empty
        :raises ImportError:        packages not found
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        try:
             tmax, vmax = np.max(data, axis=0)
             tmin, vmin = np.min(data, axis=0)
             voltage_extreemes = (vmax, vmin);
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.voltage_extreemes = voltage_extreemes
        logging.info("Success: voltage_extreemes returned.")

    def return_duration(self, data):
        """
        :param self:            ECG data
        :returns duration:      time duration of the ECG strip
        :raises TypeError:      value not int or float
        :raises ValueError:     list is empty
        :raises ImportError:    packages not found
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        try:
            duration = 1  # "CODE HERE" /////
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.duration = duration  # SELF.BLANK HERE ////
        logging.info("Success: duration returned.")

    def return_num_beats(self, data):
        """
        :param self:         ECG data
        :returns num_beats:  number of detected beats in the strip
        :raises TypeError:   value not int or float
        :raises ValueError:  list is empty
        :raises ImportError: packages not found
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        try:
            num_beats = 1  # "CODE HERE" /////
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.num_beats = num_beats  # SELF.BLANK HERE ////
        logging.info("Success: num_beats returned.")

    def return_beats(self, data):
        """
        :param self:        ECG data
        :returns beats:     numpy array of times when a beat occurred
        :raises TypeError:  value not int or float
        :raises ValueError: list is empty
        :raises ImportError:packages not found
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        try:
            beats = 1  # "CODE HERE" /////
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.beats = beats  # SELF.BLANK HERE ////
        logging.info("Success: beats returned.")
