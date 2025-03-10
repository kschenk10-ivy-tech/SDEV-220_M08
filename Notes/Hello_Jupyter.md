# Overview

This program is designed to help users organize and manage their Bath & Body Works fragrances and shopping lists. It provides a user-friendly interface to add, remove, and update fragrance records, create and edit shopping lists, and track birthdays with age and days until the next birthday calculations. The program features a graphical user interface (GUI) built with Tkinter and saves data to JSON files for persistence.

## Features

- **Fragrance Management**: Add, remove, and update fragrance records.
- **Shopping Lists**: Create and edit shopping lists for different occasions.
- **Birthday Tracking**: Track birthdays with age and days until the next birthday.
- **Data Persistence**: Data is saved to JSON files, ensuring that your information is retained between sessions.


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

## Usage Instructions

### Running the Program

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Install Required Libraries**: The program uses the `tkinter` library, which is included with Python. No additional installations are required.
3. **Run the Program**: Execute the program by running the Python script. A new interactive window will open.

### Using the Program

- **Fragrances Tab**:

  - **Add a Fragrance**: Enter the fragrance name, year, season, and status, then click "Add".
  - **Remove a Fragrance**: Select a fragrance from the list and click "Remove Selected".
  - **Update Status**: Select a fragrance and update its status in the dropdown menu.
- **Shopping Lists Tab**:

  - **Create a Shopping List**: Click "Create List", enter the list name, occasion, year, and items. For birthdays, provide the person's name and birthdate.
  - **Edit a Shopping List**: Select a list and click "Edit List" to modify its details.
  - **Export a Shopping List**: Select a list and click "Export List" to save it as a text file.
  - **View Details**: Select a list and click "View Details" to see more information, including birthday details if applicable.
- **Calendar Tab**:

  - **View Birthdays**: The calendar tab displays a list of birthdays with the person's name, birthdate, age, and days until their next birthday.

### Data Persistence

- The program automatically saves your data to `fragrances.json` and `shopping_lists.json` files. These files are updated as you make changes, ensuring that your data is preserved between sessions.

## Jupyter Notebook Instructions

### Purpose of Jupyter Notebook

Jupyter Notebook is an interactive computing environment that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It is widely used for data analysis, machine learning, and scientific computing.

### Using Jupyter Notebook with This Program

1. **Install Jupyter Notebook**: If you haven't already, you can install Jupyter Notebook using pip:
   ```bash
   pip install notebook
   ```
2. **Open the Notebook**: Navigate to the directory containing the `.ipynb` file and run:
   ```bash
   jupyter notebook
   ```
3. **Run the Code**: Open the `.ipynb` file in Jupyter Notebook and run the code cells. The program will launch in a new window.
