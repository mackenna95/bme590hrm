This README details the function and use of 'heart_rate_monitor.py'.

## 'heart_rate_monitor.py'
heart_rate_monitor.py' contains the class HeartRateMonitor
    Attributes:
        mean_hr_bpm (int/float): estimated average heart rate over a user-specified number of minutes
        voltage_extreemes (tuple): minimum and maximum lead voltages
        duration (int/float): time duration of the ECG strip
        num_beats (int/float): number of detected beats in the strip
        beats (numpy array): times when a beat occurred
        
    Arguments: 
        data (string): string containing name of csv file
        scale (int/float): to convert time to seconds
        (i.e. 60 if the data is logged in minutes)

## Test Files
* "test_data1.csv"
* "test_data10.csv"
* "test_data15.csv"

## Test Data Source
This data is originally from the [PhysioBank
Database](https://physionet.org/physiobank/database/#ecg) for ECG data.