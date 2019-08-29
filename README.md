<p align="center">
<img src="https://i.imgur.com/DdzpT8O.png" height="96px" width="96px"/>
<br/>
<h3 align="center">fb2ics</h3>
<p align="center">Facebook Birthdays to ICS (Calendar) File.</p>
<h2></h2>
</p>

## Description

Around 20 June 2019, Facebook removed their Facebook Birthday ics export option.  
This change was unannounced and no reason was ever released.

fb2ics is a workaround tool to restore this functionality.
It requires a saved copy of facebook birthdays webpage.
After gathering a list of birthdays for all the user's friends for a full year, it generates an ICS (calendar) file.

ICS file can be used with Google Calendar or Apple Calendar to import birthday events.

This tool **does not** require facebook credentials.

## Requirements

- python3.6+ (and all required python3 modules)
- pip modules:
  - python-dateutil
  - ics
  - xeger
- Saved <a href="https://www.facebook.com/events/birthdays/">facebook birthdays page</a>.

## Instructions

1. Clone repo  
   `git clone https://github.com/hardeepnarang10/fb2ics.git`
2. Save Facebook Birthdays page:
   1. Visit <a href=" https://www.facebook.com/events/birthdays/">facebook birthdays page</a>.
   2. **Scroll till the end (must reach the current month of next year)**.
   3. Save page.
3. Copy the saved HTML file to 'resources' folder in the project directory.
4. Install requirements:
   `pip install -r requirements.txt`
5. Run script manually:
   `python fb2ics.py`
6. Check 'output' folder for .ical file. 

## Version

Version update: v1.1.0 released:

- [Resolved: Issue #1](../../issues/1).

## Contributions

Contributions are welcome.
Make a [pull request](../../pulls).

## Licence

MIT License.