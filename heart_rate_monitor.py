import numpy as np
import scipy
from scipy import signal
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
        scale (list): x and y scaling factors for data
        (i.e. (60, 0.001) if the data is logged in minutes and milivolts)
        interval (list): time interval for average heart rate
    """

    def __init__(self, data_csv, scale, interval):
        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        if not isinstance(data_csv, str):
            logging.warning('Your file name is not a string')
            raise TypeError("file name is not a string")
        if ".csv" not in data_csv:
            logging.warning('Your file is not a .csv file')
            raise TypeError("file is not a .csv file")
        if not isinstance(scale, list):
            logging.warning('Your scale is not a list')
            raise TypeError("scale is not a list")
        if not isinstance(interval, list):
            logging.warning('Your interval is not a list')
            raise TypeError("interval is not a list")

        self.mean_hr_bpm = None
        self.voltage_extreemes = None
        self.duration = None
        self.num_beats = None
        self.beats = None
        data = self.Read_data(data_csv, scale)
        self.return_voltage_extreemes(data)
        self.return_duration(data)
        peak_times = self.beat_calculation(data)
        self.return_mean_hr_bpm(peak_times, interval)
        self.return_num_beats(peak_times)
        self.return_beats(peak_times)

    def Read_data(self, data_csv, scale):
        """
        :param self:    ECG data
        :returns data:  ECG data as np array
        """

        import logging
        logging.basicConfig(filename="heart_rate_monitor_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('data set is empty')
            raise ValueError("data set is empty")

        try:
            data_csv = ReadCsv(data_csv)
            scale_np = np.asarray(scale)
            data = data_csv.data * scale_np[np.newaxis, :]
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        logging.info("Success: data as np array returned.")
        return data

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
            voltage_extreemes = (vmax, vmin)
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
            tmax, vmax = np.max(data, axis=0)
            tmin, vmin = np.min(data, axis=0)
            duration = tmax-tmin
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.duration = duration
        logging.info("Success: duration returned.")

    def beat_calculation(self, data):
        """
        :param self:         ECG data
        :returns peak_times: all beat times in dataset
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
            mean = np.mean(data[:, 1])
            data[:,1] -= np.mean(data[:, 1])
            autocorr = np.correlate(data[:, 1], data[:, 1], mode='full')
            temp = autocorr[autocorr.size/2:]/autocorr[autocorr.size/2]
            autocorr_filtered = scipy.signal.savgol_filter(temp, 61, 2)
            peaks = scipy.signal.find_peaks_cwt(autocorr_filtered,
                                                np.arange(1, 300))
            peak_times = data[peaks, 0]

        # except TypeError:
        #     logging.debug('TypeError: non-numeric')
        #     raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        logging.info("Success: beats ran.")
        return peak_times

    def return_mean_hr_bpm(self, peak_times, interval):
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

    def return_num_beats(self, peak_times):
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
            num_beats = len(peak_times)
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.num_beats = num_beats
        logging.info("Success: num_beats returned.")

    def return_beats(self, peak_times):
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
