import shelve
from datetime import datetime, timedelta
import datefinder
from re import compile


class Validator:
    def __init__(self, start, end):
        db = shelve.open('../Resouces/ConfigDB/TestConfig')  # Shelve will create data.db
        for startDatetime in datefinder.find_dates(db['EventStartTime']):
            self.startTimestamp = startDatetime
        for endDatetime in datefinder.find_dates(db['EventEndTime']):
            self.endTimestamp = endDatetime
        self._report = list()
        db.close()

    def getEnforcementReport(self):
        return self._report

    def searchByPattern(line):
        # basic re date patterns, these need refinement
        dp1 = compile("\w{3} \d{2} \d{2}:\d{2}:\d{2}")
        dp2 = compile("\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}")
        dp3 = compile("\d{2}/\w{3}/\d{4} \d{2}:\d{2}:\d{2}")
        datePatternList = [dp1, dp2, dp3]
        for each in datePatternList:
            match = each.search(line)
            if match is not None:
                # print(match.group())
                return match.group()
        return None

    def validate(self, file):
        if file:
            lines = [line for line in open(file, 'r').readlines()]
            enfReport = {'filePath': file,
                         'invalid_timeStamp': [],
                         'missing_timeStamp': []}

            for i in range(len(lines)):
                tempSearch = Validator.searchByPattern(lines[i])
                if tempSearch:
                    for match in datefinder.find_dates(tempSearch):
                        timestamp = match
                    if timestamp < self.startTimestamp or timestamp > self.endTimestamp:
                        enfReport['invalid_timeStamp'].append(i + 1)
                else:
                    enfReport['missing_timeStamp'].append(i + 1)
            self._report.append(enfReport)