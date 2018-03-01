def test_heart_rate_monitor():
    import pytest
    from heart_rate_monitor import HeartRateMonitor

    output = HeartRateMonitor("test_data1.csv", 1)
    assert output.scale == 1
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes == 1
    assert output.duration == 1
    assert output.num_beats == 1
    assert output.beats == 1

    output = HeartRateMonitor("test_data10.csv", 1)
    assert output.scale == 1
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes == 1
    assert output.duration == 1
    assert output.num_beats == 1
    assert output.beats == 1

    output = HeartRateMonitor("test_data15.csv", 1)
    assert output.scale == 1
    assert output.mean_hr_bpm == 1
    assert output.voltage_extreemes == 1
    assert output.duration == 1
    assert output.num_beats == 1
    assert output.beats == 1

    # errors: 
    pytest.raises(TypeError, HeartRateMonitor, 1, 1)
    pytest.raises(TypeError, HeartRateMonitor, "testdata.csv", "data.csv")
    pytest.raises(Error, HeartRateMonitor, "testdata_does_not_exist.csv", 1)
    pytest.raises(Error, HeartRateMonitor, "testdata_empty.csv", 1)
    pytest.raises(Error, HeartRateMonitor, "testdata.txt", 1)
    return
