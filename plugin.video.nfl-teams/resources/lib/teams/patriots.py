import resources.lib.nflcs


class Team(resources.lib.nflcs.NFLCS):
    _short = "patriots"
    _cdaweb_url = "http://www.patriots.com/cda-web/"
    _categories = [
        "Video - All Access",
        "Video - Belichick Breakdowns",
        "Video - Cheerleaders",
        "Video - Coffee with the Coach",
        "Video - Draft",
        "Video - Interviews",
        "Video - NFL",
        "Video - Patriots This Week",
        "Video - Patriots Today",
        "Video - Patriots Today: Locker Room Uncut",
        "Video - PFW TV",
        "Video - Press Conference",
        "Video - Super Bowl",
        "Video - Totally Patriots",
    ]

    def __init__(self, parameters):
        self._parameters = parameters
        self.go()
