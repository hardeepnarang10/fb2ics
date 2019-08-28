#!/usr/bin/env python3

import os
from sys import path

try:
    from xeger import Xeger
except ModuleNotFoundError:
    print("\nIncomplete installation. Install required pip packages.")
    print("List of required packages in 'requirements.txt' file.")
    print("\nRun following command to install required packages:")
    print("\n\npip install - r requirements.txt\n")
    exit(404)

import include.fetch_html as path_finder
import include.parser as parser
import include.scraper as scraper

RESOURCE_PATH = r".\resources"
SAVE_DIR = "output"
OUTPUT_FILE = "facebook_birthdays.ics"
INSTRUCTION_STRING = "\nGoto 'www.facebook.com/events/birthdays/' Scroll down to the bottom and save the webpage in '"\
                     + RESOURCE_PATH.strip(".\\") + "' folder."

# Search for HTML file(s) in RESOURCE_PATH directory.
FILEPATH = path_finder.target_file(RESOURCE_PATH, INSTRUCTION_STRING)


def main():

    # Set CWD to project directory.
    os.chdir(path[0])

    # Get string with birthday info. Performance optimizer.
    scrape_line = scraper.scrape_line_selector(FILEPATH)

    # Check for birthday info in HTML file.
    if not scrape_line:
        print("\nInvalid input.")
        print(INSTRUCTION_STRING)
        exit(404)

    # Scrape list with birthday info from string.
    scrape_list = scraper.collective_scraper(scrape_line)

    # Return list of tuples with uid(unique identifier, needed in ics module), name and birthday.
    processed_tuple = flat_list_to_tuple_list(scrape_list)

    # Parse fetched info to final ICS (calendar) file.
    parsed_output = parser.ics_parser(processed_tuple)

    # Check for SAVE_DIR folder in project directory. Create if not exist.
    if not os.path.exists(SAVE_DIR): os.mkdir(SAVE_DIR)
    os.chdir(SAVE_DIR)

    # Write ICS file.
    with open(OUTPUT_FILE, mode='w', newline='') as calendar_file:
        calendar_file.writelines(parsed_output)
        calendar_file.close()

    # Check if ICS file written.
    if os.path.isfile(OUTPUT_FILE):
        print("\n\nProcess completed successfully.\n\nCheck " + SAVE_DIR + " folder for '" + OUTPUT_FILE + "' file.")


def flat_list_to_tuple_list(flat_list):
    tuple_list = []
    uid_generator = Xeger(limit=36)             # Default limit = 10.
    for each_element in flat_list:
        name = each_element[0:each_element.index(' (')]
        date = each_element[(each_element.index('(') + 1):each_element.index(')')]

        # Create random string from regex pattern.
        # ICS module needs uid for each event.
        uid = uid_generator.xeger("(\d\d\d\w\d\w\d\w)-(\d\w\d\w)-(\d\w\d\w)-(\d\w\d\w)-(\d\w\d\w\d\w\d\w\d\w\d\w)").lower()

        uid_name_date_tuple = (uid, name, date)
        tuple_list.append(uid_name_date_tuple)
    return tuple_list


if __name__ == "__main__":
    main()