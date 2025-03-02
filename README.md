# Module 8 Final Project Submission
Khristin Schenk<br>
Last Updated: on March 1, 2025<br>
SDEV220 | Final

# Python Application for Bath & Body Works

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/kschenk10-ivy-tech/SDEV-220_M08.git)
[![Trello Board](https://img.shields.io/badge/Trello-Board-blue)](https://trello.com/invite/b/67b7abfc18f18ce15b085bfb/ATTI33b20571a5d8fcfcf77f75b7131772531A707EB3/sdev-220)

![Screenshot of Final Project running](https://github.com/kschenk10-ivy-tech/SDEV-220_M08/blob/main/Screenshots/Screenshot%202025-03-01%20191317.png?raw=true)


### Overview

This Python application is designed for Bath & Body Works customers to log and track their favorite fragrances by year and season. Users can create shopping lists linked to birthdays, holidays, and special occasions, organizing purchases by week, day, and year. The application provides a user-friendly interface to manage fragrance collections, organize shopping lists, and track preferences over time.

-->
---

### Dependencies:
- Python 3.x
- tkinter (standard Python library)
- json (standard Python library)
- datetime (standard Python library)

### How it works:
1. Fragrance Management:
   - Users can add new fragrances with details like name, year, season, and status.
   - Fragrances can be removed or updated (e.g., changing the status).
   - Fragrance data is saved to and loaded from a JSON file (`fragrances.json`).

2. Shopping List Management:
   - Users can create shopping lists for specific occasions (e.g., birthdays, holidays).
   - Lists can include items, and for birthdays, users can add a person's name and birthdate.
   - Shopping lists can be edited, exported to a text file, or viewed with detailed information.
   - Shopping list data is saved to and loaded from a JSON file (`shopping_lists.json`).

3. Birthday Tracking:
   - For shopping lists with a birthday occasion, the program calculates the person's age and the number of days 
     until their next birthday.
   - A dedicated "Calendar" tab displays all birthday-related shopping lists with age and days until the next birthday.

4. User Interface:
   - The program uses a tabbed interface (Notebook) to separate fragrance management, shopping list management, 
     and birthday tracking.
   - Users interact with the program through forms, buttons, and treeview widgets to manage their data.

### Usage:
- Run the program, and the GUI will open.
- Use the "Fragrances" tab to manage fragrance records.
- Use the "Shopping Lists" tab to create, edit, and view shopping lists.
- Use the "Calendar" tab to view upcoming birthdays and related shopping lists.


### Testing

```bash
python -m unittest test_final_project.py
```
