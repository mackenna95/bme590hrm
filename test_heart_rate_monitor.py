def test_heart_rate_monitor():
    import pytest
    from heart_rate_monitor import HeartRateMonitor

    tolerance = 0.0000001

    output = HeartRateMonitor("test_data1.csv", [1, 1], [1, 1])
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes[0] - 1.05 < tolerance
    assert output.voltage_extreemes[1] + 0.68 < tolerance
    assert output.duration == 27.775
    assert output.num_beats == 35
    assert output.beats == 1

    output = HeartRateMonitor("test_data10.csv", [1, 1], [1, 1])
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes[0] - 1.555 < tolerance
    assert output.voltage_extreemes[1] + 1.58 < tolerance
    assert output.duration == 27.775
    assert output.num_beats == 43
    assert output.beats == 1

    output = HeartRateMonitor("test_data15.csv", [1, 1], [1, 1])
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes[0] - 0.7 < tolerance
    assert output.voltage_extreemes[1] + 0.33077 < tolerance
    assert output.duration == 13.887
    assert output.num_beats == 29
    assert output.beats == 1

    # errors:
    pytest.raises(TypeError, HeartRateMonitor, [1, 1], [1, 1])
    pytest.raises(TypeError, HeartRateMonitor, "testdata.csv",
                                               "data.csv", [1, 1])
    pytest.raises(ValueError, HeartRateMonitor, "testdata_empty.csv",
                                                [1, 1], [1, 1])
    pytest.raises(TypeError, HeartRateMonitor, "testdata.txt",
                                               [1, 1], [1, 1])
    return
