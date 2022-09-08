import datetime


class irange:
    """
    Iterator class that produces a sequence of datetime's from "start_date" (inclusive)
    to "stop_date" (exclusive) by "time_step".
    Supporting __bool__.

    :param datetime.datetime start_date: Inclusive.
    :param datetime.datetime stop_date: Exclusive. `utcnow` is used by default.
    :param datetime.delta time_step: one-day `timedelta` is used by default.

     Examples:
        import datetime

        from pymince.datetime import irange

        ini = datetime.datetime.fromisoformat("2022-10-30")
        end = datetime.datetime.fromisoformat("2022-11-02")
        day = datetime.timedelta(days=1)

        it = irange(ini, stop_date=end, time_step=day)
        next(it) # --> datetime.datetime(2022, 10, 30, 0, 0)
        next(it) # --> datetime.datetime(2022, 10, 31, 0, 0)
        next(it) # --> datetime.datetime(2022, 11, 1, 0, 0)
        next(it) # --> StopIteration
    """

    __slots__ = ('_init', '_stop', '_step', '_this')

    def __init__(self, start_date, stop_date=None, time_step=None):
        self._init = start_date
        self._stop = stop_date or datetime.datetime.utcnow()
        self._step = time_step or datetime.timedelta(days=1)
        self._this = self._init

    def __iter__(self):
        return self

    def _consume(self):
        self._this += self._step

    def __next__(self):
        if self:
            incoming = self._this
            self._consume()
            return incoming
        else:
            raise StopIteration

    def __bool__(self):
        return self._this < self._stop
