import datetime

import pymince.datetime


def test_iter_by_day():
    ini = datetime.datetime.fromisoformat("2022-10-30T14:10:30")
    end = datetime.datetime.fromisoformat("2022-11-02T10:40:10")
    day = datetime.timedelta(days=1)

    expected = (
        datetime.datetime(2022, 10, 30, 14, 10, 30),
        datetime.datetime(2022, 10, 31, 14, 10, 30),
        datetime.datetime(2022, 11, 1, 14, 10, 30),
    )

    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert tuple(obj) == expected


def test_iter_by_min():
    ini = datetime.datetime.fromisoformat("2022-11-29T14:59:58")
    end = datetime.datetime.fromisoformat("2022-11-29T15:01:00")
    day = datetime.timedelta(minutes=1)

    expected = (
        datetime.datetime(2022, 11, 29, 14, 59, 58),
        datetime.datetime(2022, 11, 29, 15, 0, 58)
    )
    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert tuple(obj) == expected


def test_contains_at_beginning():
    ini = datetime.datetime.fromisoformat("2022-10-30")
    end = datetime.datetime.fromisoformat("2022-11-02")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert ini in obj


def test_contains_in_middle():
    ini = datetime.datetime.fromisoformat("2022-10-30")
    end = datetime.datetime.fromisoformat("2022-11-02")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert datetime.datetime.fromisoformat("2022-10-31") in obj


def test_not_contains_in_middle():
    ini = datetime.datetime.fromisoformat("2022-10-30")
    end = datetime.datetime.fromisoformat("2022-11-02")
    day = datetime.timedelta(days=2)
    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert not datetime.datetime.fromisoformat("2022-10-31") in obj


def test_not_contains_at_ending():
    ini = datetime.datetime.fromisoformat("2022-10-30")
    end = datetime.datetime.fromisoformat("2022-11-02")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert end not in obj


def test_length():
    ini = datetime.datetime.fromisoformat("2022-10-30")
    end = datetime.datetime.fromisoformat("2022-11-02")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
    assert len(obj) == 3
