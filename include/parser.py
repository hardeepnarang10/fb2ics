from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import ics


def ics_parser(bday_info_tuple):

    # Set calender info.
    c = ics.Calendar()
    c.scale = 'GREGORIAN'
    c.method = 'PUBLISH'
    c.creator = 'Hardeep Narang'
    c._unused.append(ics.parse.ContentLine(name='X-WR-CALNAME', params={}, value='Facebook Birthdays Calendar (fb2ics)'))
    c._unused.append(ics.parse.ContentLine(name='X-PUBLISHED-TTL', params={}, value='PT12H'))
    c._unused.append(ics.parse.ContentLine(name='X-ORIGINAL-URL', params={}, value='/events/birthdays/'))

    # Get present date.
    present_date = datetime.now()

    # Process and add individual Events to the Calender object.
    for each_tuple in bday_info_tuple:
        # Calculate year for next birthday.
        # Add padding for day and month (2 digits - leading zero).
        tuple_date = each_tuple[2]
        year = present_date.year if int(tuple_date[0:tuple_date.index('/')]) >= present_date.month else (present_date + relativedelta(years=1)).year
        month = '{:02d}'.format(int(tuple_date[0:tuple_date.index('/')]))
        day = '{:02d}'.format(int(tuple_date[tuple_date.index('/')+1:]))

        # Create Event object.
        e = ics.Event()
        e.uid = each_tuple[0]
        e.name = f"{each_tuple[1]}'s Birthday!"
        e.description = "Facebook friend's birthday! Wish them well!"
        e.begin = f'{year}-{month}-{day} 00:00:00'
        e.make_all_day()
        e.duration = timedelta(days=1)
        e._unused.append(ics.parse.ContentLine(name='RRULE', params={}, value='FREQ=YEARLY'))

        c.events.add(e)

    return c
