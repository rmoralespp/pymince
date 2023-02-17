# -*- coding: utf-8 -*-

import datetime

import pytest

import pymince.dates


@pytest.mark.parametrize(
    "attr, expected",
    [
        ("MONDAY", 0),
        ("TUESDAY", 1),
        ("WEDNESDAY", 2),
        ("THURSDAY", 3),
        ("FRIDAY", 4),
        ("SATURDAY", 5),
        ("SUNDAY", 6),
    ],
)
def test_weekday_attrs(attr, expected):
    assert getattr(pymince.dates.WeekDay, attr).value == expected


@pytest.mark.parametrize(
    "attr, expected",
    [
        ("MONDAY", 1),
        ("TUESDAY", 2),
        ("WEDNESDAY", 3),
        ("THURSDAY", 4),
        ("FRIDAY", 5),
        ("SATURDAY", 6),
        ("SUNDAY", 7),
    ],
)
def test_isoweekday_attrs(attr, expected):
    assert getattr(pymince.dates.IsoWeekDay, attr).value == expected


def test_weekday_of():
    date = datetime.datetime(2023, 2, 17)
    assert pymince.dates.WeekDay.of(date) == pymince.dates.WeekDay.FRIDAY


def test_isoweekday_of():
    date = datetime.datetime(2023, 2, 17)
    assert pymince.dates.IsoWeekDay.of(date) == pymince.dates.IsoWeekDay.FRIDAY


def test_weekday_standard():
    date = datetime.datetime(2023, 2, 17)
    assert pymince.dates.WeekDay.of(date).value == date.weekday()


def test_isoweekday_standard():
    date = datetime.datetime(2023, 2, 17)
    assert pymince.dates.IsoWeekDay.of(date).value == date.isoweekday()
