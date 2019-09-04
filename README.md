<p align="center">
<img src="https://i.imgur.com/ToHPLjD.png" height="110px" width="auto"/>
<br/>
<h3 align="center">fb2ics</h3>
<p align="center">Facebook Birthdays to ICS (Calendar) File</p>
<h2></h2>
</p>

## Description

Around 20 June 2019, Facebook removed their Facebook Birthday ics export option.  
This change was unannounced and no reason was ever released.

fb2ics is a workaround tool to restore this functionality.
It requires a saved copy (same day) of facebook birthdays webpage.
After gathering a list of birthdays for all the user's friends for a full year, it generates an ICS (calendar) file.

ICS file can be used with Google Calendar or Apple Calendar to import birthday events.

This tool **does not** require facebook credentials.

## Requirements

- python3.6+ (and all required python3 modules)
- Saved <a href="https://www.facebook.com/events/birthdays/">facebook birthdays page</a>.
- ~~pip modules:~~ Although still required, packages are automatically handled by 'Installer_Windows.bat' (in Windows) and 'Installer_Linux.sh' (in Linux) and specified in 'requirements.txt' file.
  - ~~python-dateutil~~
  - ~~ics~~
  - ~~xeger~~

## Instructions

1. Clone repo  
   `git clone https://github.com/hardeepnarang10/fb2ics.git`
   
   **Or simply click [here](https://codeload.github.com/hardeepnarang10/fb2ics/zip/master) to download zip file**. Extract it's content.
   
2. Save Facebook Birthdays page:
   
   - Visit <a href=" https://www.facebook.com/events/birthdays/">facebook birthdays page</a>.
   - **Scroll till the end (must reach the current month of next year)**.
   - Save page (Press Ctrl + S or Command +S).
3. Copy the saved HTML file to 'resources' folder in the project directory.
   (**HTML file must be saved the same day this script is executed**).

4. Windows users run `Installer_Windows.bat` file.
   Linux users run `Installer_Linux.sh` file. (Linux users may need to issue `chmod +x Installer_Linux.sh` command first).

5. Check 'output' folder for .ical file. 

## Version

Version update: v2.0.0 released:

- Crossplatform support (Mac, Linux, Windows).
- [Resolved: Issue #3](../../issues/3).

Version update: v1.1.0 released:

- [Resolved: Issue #1](../../issues/1).

## Contributions

Contributions are welcome.
Make a [pull request](../../pulls).

## Licence

MIT License.