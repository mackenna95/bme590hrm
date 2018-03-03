This README details the function and use of 'heart_rate_monitor.py' and 'read_csv.py'.

## 'heart_rate_monitor.py'
'heart_rate_monitor.py' contains the class HeartRateMonitor
    Attributes:
        mean_hr_bpm (int/float): heart rate over a user-specified minutes
        voltage_extreemes (tuple): minimum and maximum lead voltages
        duration (int/float): time duration of the ECG strip
        num_beats (int/float): number of detected beats in the strip
        beats (numpy array): times (s) when a beat occurred

    Arguments:
        data_csv (string): string containing name of csv file
        scale (list): x and y scaling factors for data
        (i.e. (60, 0.001) if the data is logged in minutes and milivolts)
        interval (list): time (s) interval for average heart rate

## 'read_csv.py'
'read_csv.py' contains the class ReadCsv
    Attributes:
        data (ndarray): Csv Values in single array

    Arguments:
        fname (str): file name of csv

## Test Files
* "test_data1.csv"
* "test_data10.csv"
* "test_data15.csv"
* "testdata_empty.csv"

## Test Data Source
This data is originally from the [PhysioBank
Database](https://physionet.org/physiobank/database/#ecg) for ECG data.

## Log Files
* "heart_rate_monitor_log.txt"
* "read_csv.txt"