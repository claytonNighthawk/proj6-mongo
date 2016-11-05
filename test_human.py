from human import *
import arrow

def same(real, expected):
    print(real, expected)
    return real == expected

today = arrow.now().floor('day')
yesterday = arrow.now().replace(days=-1).floor('day')
tomorrow = arrow.now().replace(days=+1).floor('day')
day_after_tomorrow = arrow.now().replace(days=+2).floor('day')

def test_yesterday():
    assert same(human(yesterday), "Yesterday")

def test_tomorrow():
    assert same(human(tomorrow), "Tomorrow")

def test_today():
    assert same(human(today), "Today")

def test_day_after_tomorrow():
    assert same(human(day_after_tomorrow), "in 2 days")

