import datetime


class drange:
    """
    Return an object that produces a sequence of datetime's from "start_date" (inclusive)
    to "stop_date" (exclusive) by "time_step".

     Examples:
        import datetime

        import pymince.datetime

        ini = datetime.datetime.fromisoformat("2022-10-30")
        end = datetime.datetime.fromisoformat("2022-11-02")
        day = datetime.timedelta(days=1)

        obj = pymince.datetime.drange(ini, stop_date=end, time_step=day)
        next(obj) # --> datetime.datetime(2022, 10, 30, 0, 0)
        next(obj) # --> datetime.datetime(2022, 10, 31, 0, 0)
        next(obj) # --> datetime.datetime(2022, 11, 1, 0, 0)
        next(obj) # --> StopIteration
    """

    def __init__(self, start_date, stop_date=None, time_step=None):
        """
        :param datetime.datetime start_date: Inclusive.
        :param datetime.datetime stop_date: Exclusive. `utcnow` is used by default.
        :param datetime.delta time_step: one-day `timedelta` is used by default.
        """

        self.init = start_date
        self.stop = stop_date or datetime.datetime.utcnow()
        self.step = time_step or datetime.timedelta(days=1)

    def __iter__(self):
        yield from self.consume()

    def consume(self):
        this = self.init
        while this < self.stop:
            yield this
            this += self.step

    def __contains__(self, any_datetime):
        return any(d == any_datetime for d in self.consume())

    def __len__(self):
        return sum(1 for _ in self.consume())
