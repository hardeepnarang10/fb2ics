import datetime as dt
from re import findall


WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def scrape_line_selector(file_name):
    html_file = open(file_name, mode='r', encoding="utf-8")
    raw_content = html_file.readlines()
    html_file.close()

    # MATCH_LINE already known.
    MATCH_LINE = '" class="link" data-jsid="anchor" data-hover="tooltip" data-tooltip-content="'

    for each_line in raw_content:
        try:
            if MATCH_LINE in each_line:
                return each_line
        except UnicodeDecodeError:
            pass


def collective_scraper(scrape_line):

    # Scrape all needed content at once. Easy processing.
    raw_scrape_list = str(findall(r'\w*\s?\w*\s\w+\s\(\w*\d*/?\d*\)', scrape_line))

    name_date_list = name_date_scraper(raw_scrape_list)
    name_day_list = name_day_scraper(raw_scrape_list)
    return name_date_list + name_day_list


def name_date_scraper(raw_list):
    name_date = findall(r'\w*\s?\w*\s\w+\s\(\d*/\d*\)', raw_list)
    bday_list = []
    for each_day in name_date:
        if not each_day in bday_list:
            bday_list.append(each_day)
    return bday_list


# Facebook page displays recent birthdays with day instead of numerical date.
# Translate day info to relative date.
# Need to save webpage the same day this program is run.
def name_day_scraper(raw_list):
    name_day = findall(r'\w*\s?\w*\s\w+\s\(\w+\)', raw_list)
    bday_list = []
    for each_element in name_day:
        name = each_element[0:each_element.index('(')]
        date = each_element[(each_element.index('(') + 1):each_element.index(')')]
        if (name + get_bday(date)) not in bday_list:
            bday_list.append(name + get_bday(date))
    return bday_list


def get_bday(day_of_the_week):
    present_day = dt.date(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day).weekday()
    two_weeks = list(WEEKDAYS + WEEKDAYS)
    two_weeks.remove(day_of_the_week)
    difference_in_date = two_weeks.index(day_of_the_week) - two_weeks.index(WEEKDAYS[present_day])
    bday_date = dt.datetime.now() + dt.timedelta(days=difference_in_date)
    return ('(' + str(bday_date.month) + '/' + str(bday_date.day) + ')')
