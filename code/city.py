import csv
import calendar


class city:
    def __init__(self, Stadt):
        self.Stadt = Stadt
        self.ShortForm = Stadt["ShortForm"]
        self.BoulderName = Stadt["BoulderName"]
        self.WebsiteUrl = Stadt["WebsiteUrl"]
        self.BoulderadoUrl= Stadt["BoulderadoUrl"]
        self.Times = []
        self.OldAverage = 0
        self.besucher = 0
        self.frei = 1
        self.pngfile = ""
        for i in range(0,7):
            weekday = calendar.day_name[i]
            self.Times.append([int(Stadt[f"Open{weekday}"]), int(Stadt[f"Close{weekday}"])])


def getcsv():
    with open('Cities.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        d = []
        key = [char.strip() for char in next(reader)]
        for row in reader:
            ro = [char.strip() for char in row]
            d.append(dict(zip(key, ro)))
        return d
    return []