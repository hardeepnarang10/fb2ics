from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from ics import Calendar, Event
from ics.parse import ContentLine


def ics_parser(bday_info_tuple, enable_date_swap):

    # Set calender info.
    c = Calendar()
    c.scale = 'GREGORIAN'
    c.method = 'PUBLISH'
    c.creator = 'Hardeep Singh Narang @hardeepnarang10'
    c._unused.append(ContentLine(name='X-WR-CALNAME', params={}, value='Facebook Birthdays Calendar (fb2ics)'))
    c._unused.append(ContentLine(name='X-PUBLISHED-TTL', params={}, value='PT12H'))
    c._unused.append(ContentLine(name='X-ORIGINAL-URL', params={}, value='/events/birthdays/'))

    # Get present date.
    present_date = datetime.now()

    # Process and add individual Events to the Calender object.
    for each_tuple in bday_info_tuple:
        # Calculate year for next birthday.
        # Add padding for day and month (2 digits - leading zero).
        tuple_date = each_tuple[2]
        year = present_date.year if int(tuple_date[0:tuple_date.index('/')]) >= present_date.month else (present_date + relativedelta(years=1)).year

        if enable_date_swap:
            day = '{:02d}'.format(int(tuple_date[0:tuple_date.index('/')]))
            month = '{:02d}'.format(int(tuple_date[tuple_date.index('/') + 1:]))
        else:
            month = '{:02d}'.format(int(tuple_date[0:tuple_date.index('/')]))
            day = '{:02d}'.format(int(tuple_date[tuple_date.index('/')+1:]))

        # Create Event object.
        e = Event()
        e.uid = each_tuple[0]
        e.name = f"{each_tuple[1]}'s Birthday!"
        e.description = "Facebook friend's birthday! Wish them well!"
        e.begin = f'{year}-{month}-{day} 00:00:00'
        e.make_all_day()
        e.duration = timedelta(days=1)
        e._unused.append(ContentLine(name='RRULE', params={}, value='FREQ=YEARLY'))

        c.events.add(e)

    return c
