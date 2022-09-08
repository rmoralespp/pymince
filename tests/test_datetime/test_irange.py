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

    obj = pymince.datetime.irange(ini, stop_date=end, time_step=day)
    assert tuple(obj) == expected


def test_iter_by_min():
    ini = datetime.datetime.fromisoformat("2022-11-29T14:59:58")
    end = datetime.datetime.fromisoformat("2022-11-29T15:01:00")
    day = datetime.timedelta(minutes=1)

    expected = (
        datetime.datetime(2022, 11, 29, 14, 59, 58),
        datetime.datetime(2022, 11, 29, 15, 0, 58)
    )
    obj = pymince.datetime.irange(ini, stop_date=end, time_step=day)
    assert tuple(obj) == expected


def test_bool_true():
    ini = datetime.datetime.fromisoformat("2022-11-29")
    end = datetime.datetime.fromisoformat("2022-11-30")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.irange(ini, stop_date=end, time_step=day)
    assert obj


def test_bool_false():
    ini = datetime.datetime.fromisoformat("2022-11-29")
    end = datetime.datetime.fromisoformat("2022-11-29")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.irange(ini, stop_date=end, time_step=day)
    assert not obj


def test_bool_false_after_consume():
    ini = datetime.datetime.fromisoformat("2022-11-29")
    end = datetime.datetime.fromisoformat("2022-11-30")
    day = datetime.timedelta(days=1)
    obj = pymince.datetime.irange(ini, stop_date=end, time_step=day)
    next(obj)
    assert not obj
