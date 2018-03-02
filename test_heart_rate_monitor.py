def test_heart_rate_monitor():
    import pytest
    import numpy as np
    from heart_rate_monitor import HeartRateMonitor

    tolerance = 0.0000001

    output = HeartRateMonitor("test_data1.csv", [1, 1], [1, 1])
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes[0] - 1.05 < tolerance
    assert output.voltage_extreemes[1] + 0.68 < tolerance
    assert output.duration == 27.775
    assert output.num_beats == 35
    assert all(output.beats == np.array([8.00000000e-03, 8.17000000e-01,
                                         1.60800000e+00, 2.36700000e+00,
                                         3.30300000e+00, 4.06400000e+00,
                                         4.87500000e+00, 5.69200000e+00,
                                         6.50000000e+00, 7.27500000e+00,
                                         8.07800000e+00, 8.90300000e+00,
                                         9.70600000e+00, 1.06000000e+01,
                                         1.14220000e+01, 1.21780000e+01,
                                         1.30110000e+01, 1.38190000e+01,
                                         1.46080000e+01, 1.54000000e+01,
                                         1.62720000e+01, 1.70690000e+01,
                                         1.78860000e+01, 1.86920000e+01,
                                         1.94860000e+01, 2.02940000e+01,
                                         2.10720000e+01, 2.18830000e+01,
                                         2.27310000e+01, 2.35360000e+01,
                                         2.43530000e+01, 2.51530000e+01,
                                         2.59610000e+01, 2.67670000e+01,
                                         2.75830000e+01]))

    output = HeartRateMonitor("test_data10.csv", [1, 1], [1, 1])
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes[0] - 1.555 < tolerance
    assert output.voltage_extreemes[1] + 1.58 < tolerance
    assert output.duration == 27.775
    assert output.num_beats == 43
    assert all(output.beats == np.array([0.631, 1.261, 1.928, 2.55, 3.178,
                                         3.811, 4.45, 5.081, 5.569, 6.206,
                                         6.861, 7.5, 8.128, 8.756, 9.386,
                                         10.011, 10.642, 11.3, 11.806,
                                         12.436, 13.069, 13.694, 14.328,
                                         14.972, 15.619, 16.25, 16.878,
                                         17.517, 18.167, 18.831, 19.486,
                                         20.136, 20.739, 21.319, 21.961,
                                         22.633, 23.3, 23.944, 24.594,
                                         25.244, 25.894, 26.542, 27.2]))

    output = HeartRateMonitor("test_data15.csv", [1, 1], [1, 1])
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes[0] - 0.7 < tolerance
    assert output.voltage_extreemes[1] + 0.33077 < tolerance
    assert output.duration == 13.887
    assert output.num_beats == 29
    assert all(output.beats == np.array([6.00000000e-03, 6.57000000e-01,
                                         1.33900000e+00, 1.99600000e+00,
                                         2.28300000e+00, 2.65400000e+00,
                                         3.33600000e+00, 3.99300000e+00,
                                         4.27900000e+00, 4.65000000e+00,
                                         5.33300000e+00, 5.70300000e+00,
                                         5.99000000e+00, 6.27600000e+00,
                                         6.64900000e+00, 7.33100000e+00,
                                         7.70000000e+00, 7.98700000e+00,
                                         8.64600000e+00, 9.69600000e+00,
                                         9.98500000e+00, 1.02710000e+01,
                                         1.06430000e+01, 1.16970000e+01,
                                         1.19820000e+01, 1.22680000e+01,
                                         1.26420000e+01, 1.33250000e+01,
                                         1.36360000e+01]))

    # errors:
    pytest.raises(TypeError, HeartRateMonitor, [1, 1], [1, 1])
    pytest.raises(TypeError, HeartRateMonitor, "testdata.csv",
                                               "data.csv", [1, 1])
    pytest.raises(ValueError, HeartRateMonitor, "testdata_empty.csv",
                                                [1, 1], [1, 1])
    pytest.raises(TypeError, HeartRateMonitor, "testdata.txt",
                                               [1, 1], [1, 1])
    return
