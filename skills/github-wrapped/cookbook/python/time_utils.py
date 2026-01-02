from __future__ import annotations

import datetime as dt
from zoneinfo import ZoneInfo


def parse_iso8601(ts: str) -> dt.datetime:
    if not ts:
        raise ValueError("empty timestamp")
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return dt.datetime.fromisoformat(ts)


def to_local(ts: str, tz: ZoneInfo) -> dt.datetime:
    return parse_iso8601(ts).astimezone(tz)


def utc_month_range(year: int, month: int) -> tuple[int, int]:
    """
    Return (start_ms, end_ms) for the month in UTC milliseconds.
    Useful for converting timestamps into an x-position ratio within a month.
    """
    start = dt.datetime(year, month, 1, tzinfo=dt.timezone.utc)
    if month == 12:
        end = dt.datetime(year + 1, 1, 1, tzinfo=dt.timezone.utc)
    else:
        end = dt.datetime(year, month + 1, 1, tzinfo=dt.timezone.utc)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)


def hour_bucket(ts: str, tz: ZoneInfo) -> int:
    return to_local(ts, tz).hour

