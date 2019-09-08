#!/usr/bin/env python3

try:
    from include.meta.__init__ import *

    from argparse import ArgumentParser
    from datetime import datetime
    from sys import path
    from xeger import Xeger

    import os

    import include.fetch_html as path_finder
    import include.parser as parser
    import include.scraper as scraper

except ModuleNotFoundError:
    print("\nIncomplete installation. Install required pip packages.")
    print("List of required packages in 'requirements.txt' file.")
    print("\nRun following command to install required packages:")
    print("\n\npip install - r requirements.txt\n")
    exit(-11)

RESOURCE_PATH = "./resources"
SAVE_DIR = "output"
OUTPUT_FILE = "facebook_birthdays.ics"
LOG_FILE = "missed_entries.log"
INSTRUCTION_STRING = "\nGoto 'www.facebook.com/events/birthdays/',"\
                    + " remember to SCROLL DOWN TO THE BOTTOM and save the webpage in '"\
                     + RESOURCE_PATH.strip(".\\").strip("/") + "' folder.\n"


def main():

    # Set CWD to project directory.
    os.chdir(path[0])

    # Search for HTML file(s) in RESOURCE_PATH directory.
    filename = path_finder.target_file(RESOURCE_PATH, INSTRUCTION_STRING)

    # Argument(s) parser.
    args = argparser(filename)

    # Get string with birthday info. Performance optimizer.
    # Disable if ValueError exception is raised.
    scrape_line = scraper.scrape_line_selector(args.filename)

    # Check for birthday info in HTML file. Raise ValueError if info not found.
    try:
        if not scrape_line:
            raise ValueError('Invalid input. ' + filename + ' does not contain birthday info.', INSTRUCTION_STRING)
    except ValueError as valerr:
        print('\n' + valerr.args[0] + '\n' + valerr.args[1])
        exit(-12)

    # Scrape list with birthday info from string.
    scrape_list = scraper.collective_scraper(scrape_line)[0]

    # Return list of tuples with uid(unique identifier, needed in ics module), name and birthday.
    processed_tuple = flat_list_to_tuple_list(scrape_list)

    # Parse fetched info to final ICS (calendar) file.
    try:
        parsed_output = parser.ics_parser(processed_tuple, 0)
    except ValueError:
        try:
            parsed_output = parser.ics_parser(processed_tuple, 1)
        except ValueError:                                          # In case neither of two locale signatures match.
            print("\nBad input: '" + args.filename + "' contains unsupported format." +
                  "\n\nExiting program...")
            exit(-14)

    # Check for SAVE_DIR folder in project directory. Create if not exist.
    if not os.path.exists(SAVE_DIR): os.mkdir(SAVE_DIR)
    os.chdir(SAVE_DIR)

    # Write ICS file.
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as calendar_file:
        calendar_file.writelines(parsed_output)
        calendar_file.close()

    # Check for missed entries.
    if scraper.collective_scraper(scrape_line)[1]:
        with open(LOG_FILE, mode='w', encoding='utf-8') as log_file:
            for each_entry in scraper.collective_scraper(scrape_line)[1]:
                log_file.write(each_entry + '\n')
            log_file.close()
        print("\n\nWARNING:\n" + os.path.basename(__file__) + " v" + __version__ + " (current) " +
              "is unable to process birthday events which include brackets." +
              "\nTip: Check for people with nicknames in your friend list.")
    else:
        pass

    # Check if ICS and LOG file(s) are written.
    if os.path.isfile(OUTPUT_FILE):
        print("\n\nProcess completed successfully.")
        print("Check '" + SAVE_DIR + "' folder for '" + OUTPUT_FILE + "' file.")
        if scraper.collective_scraper(scrape_line)[1] and os.path.isfile(LOG_FILE):
            print("Also check '" + LOG_FILE + "' for missed birthdays." +
                  " You may add these events manually to the calendar.\n")
        else:
            print("\n")


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


def argparser(filepath):

    parser = ArgumentParser(prog='fb2ics', add_help=False,
                            description="Process saved facebook webpage for birthdays: "
                                        + "generates ICS (calendar) file.",
                            epilog="See instructions: "
                                    + "https://github.com/hardeepnarang10/fb2ics#Instructions")
    parser.add_argument('--filename', type=str, default= filepath,
                        help=("Specify name of file(text/html) to scrape birthdays data from. Selected default: '" + filepath + "'"))
    parser.add_argument('--help', '-H', action='help', help="Show this help message and exit.")
    parser.add_argument('--version', '-V', action='version', version=f'%(prog)s {__version__}',
                        help="Show program's version number and exit.")

    # Check if unknown argument given.
    args, unknown_args = parser.parse_known_args()
    if unknown_args:
        parser.print_help()
        print("\nInvalid arguments given. Please read help message, or try adding --help argument.\n")
        exit(-13)

    return args


if __name__ == "__main__":
    main()