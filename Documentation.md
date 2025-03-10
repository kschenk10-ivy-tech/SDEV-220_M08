# Bath & Body Works Fragrance Organizer - User Guide

## Overview
This Jupyter Notebook contains a GUI application designed to help users manage their Bath & Body Works fragrance collection, shopping lists, and birthday tracking. The program features:
- **Fragrance Management**: Track fragrances with details like name, year, season, and status.
- **Shopping Lists**: Create and edit occasion-based lists (e.g., birthdays, holidays) with item tracking.
- **Birthday Calendar**: Calculate ages and days until next birthdays for gift planning.
- **Data Persistence**: Automatically saves data to JSON files (`fragrances.json` and `shopping_lists.json`).

---

## How to Run the Program
1. **Prerequisites**:
   - Ensure you have Python 3.x installed.
   - Required libraries: `tkinter` (included in standard Python installations), `json`, and `datetime`.
2. **Launch the GUI**:
   - Run the code cell in this notebook. A new interactive window titled **"Bath & Body Works Organizer"** will open.
   - *Note*: Keep the Jupyter Notebook kernel running while using the GUI. Closing the notebook will terminate the program.
3. **Tabs Overview**:
   - **Fragrances**: Add, remove, or update fragrance records.
   - **Shopping Lists**: Create, edit, export, or view detailed lists.
   - **Calendar**: Track birthdays with age and days-until calculations.

---

## Usage Instructions

### Fragrances Tab
- **Add a Fragrance**:
  1. Fill in the fields: `Name`, `Year`, `Season` (dropdown), and `Status` (dropdown).
  2. Click **Add** to save. The data will auto-save to `fragrances.json`.
- **Remove a Fragrance**:
  1. Select an entry in the table.
  2. Click **Remove Selected**.

### Shopping Lists Tab
- **Create a List**:
  1. Click **Create List**.
  2. Enter a name, occasion (e.g., "Birthday"), year, and items.
  3. For birthdays, provide the person’s name and birthdate in `YYYY-MM-DD` format.
- **Edit/Export a List**:
  - Select a list and use **Edit List** to modify details or **Export List** to save items to a `.txt` file.
- **View Details**: Select a list and click **View Details** to see age calculations and items.

### Calendar Tab
- Automatically displays birthdays from shopping lists. Shows:
  - Birthdate
  - Age for the current year
  - Days until the next birthday

---

## Data Persistence
- Data is saved automatically to:
  - `fragrances.json`: Stores fragrance records.
  - `shopping_lists.json`: Stores shopping lists and birthday details.
- **Do not delete these files** to retain your data between sessions.

---

## Notes
- The GUI may take a few seconds to load after running the cell.
- For birthdays, ensure the birthdate format is `YYYY-MM-DD` (e.g., `2005-03-10`).
- Exporting a shopping list creates a `.txt` file in the same directory as this notebook.
