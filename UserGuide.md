# **Overview**

This program helps users organize and manage their **Bath & Body Works** fragrance collection and shopping lists. It features a **user-friendly graphical interface** (GUI) built with **Tkinter**, allowing users to:

-   Add, remove, and update **fragrance records**.
-   Create and edit **shopping lists** for various occasions.
-   Track **birthdays**, calculating age and days until the next birthday.
-   Save data persistently using **JSON files**.

----------

# **Bath & Body Works Fragrance Organizer - User Guide**

## **Overview**

This Jupyter Notebook contains a **GUI application** for managing your **Bath & Body Works** fragrance collection, shopping lists, and birthday reminders. Key features include:

-   **Fragrance Management**: Store fragrance details such as name, year, season, and status.
-   **Shopping Lists**: Create and edit occasion-based lists (e.g., birthdays, holidays).
-   **Birthday Tracking**: Automatically calculates ages and days until upcoming birthdays.
-   **Data Persistence**: Saves data automatically to `fragrances.json` and `shopping_lists.json`.

----------

## **How to Run the Program**

### **1. Prerequisites**

-   Ensure **Python 3.x** is installed.
-   Required libraries: `tkinter` (included with Python), `json`, and `datetime`.

### **2. Launch the GUI**

-   Run the **code cell** in this notebook. A window titled **"Bath & Body Works Organizer"** will open.
-   ⚠ **Important**: Keep the Jupyter Notebook **kernel running** while using the GUI. Closing the notebook will terminate the program.

### **3. Interface Overview**

-   **Fragrances Tab**: Add, remove, or update fragrance records.
-   **Shopping Lists Tab**: Create, edit, and export shopping lists.
-   **Calendar Tab**: Track birthdays, showing age and countdown to the next birthday.

----------

## **Usage Instructions**

### **Fragrances Tab**

-   **Add a Fragrance**:
    
    1.  Enter details: `Name`, `Year`, `Season` (dropdown), `Status` (dropdown).
    2.  Click **Add** to save. Data is stored in `fragrances.json`.
-   **Remove a Fragrance**:
    
    1.  Select an entry from the list.
    2.  Click **Remove Selected**.

### **Shopping Lists Tab**

-   **Create a Shopping List**:
    
    1.  Click **Create List**.
    2.  Enter a `List Name`, `Occasion` (e.g., "Birthday"), `Year`, and `Items`.
    3.  If for a birthday, input the person’s name and birthdate (`YYYY-MM-DD`).
-   **Edit or Export a List**:
    
    -   Select a list and click **Edit List** to modify it.
    -   Click **Export List** to save as a `.txt` file.
-   **View List Details**:
    
    -   Click **View Details** to see the full list and birthday calculations.

### **Calendar Tab**

-   Displays birthdays from shopping lists, showing:
    -   `Name`
    -   `Birthdate`
    -   `Current Age`
    -   `Days Until Next Birthday`

----------

## **Data Persistence**

-   Data is **automatically saved** to:
    -   `fragrances.json` → Stores fragrance records.
    -   `shopping_lists.json` → Stores shopping lists and birthday details.
-   **Do not delete these files** to retain your data.

----------

## **Additional Notes**

-   The GUI **may take a few seconds** to load after running the cell.
-   Use the **correct birthdate format (`YYYY-MM-DD`)**, e.g., `2005-03-10`.
-   Exported shopping lists are saved as `.txt` files in the same directory.

----------

## **Running the Program Outside Jupyter Notebook**

To run this program as a standalone script:

### **1. Install Python**

Ensure Python is installed. Download it from [python.org](https://www.python.org/).

### **2. Run the Script**

Execute the Python script using:

```bash
python script_name.py

```

A new interactive window will open.

----------

## **Jupyter Notebook Instructions**

### **What is Jupyter Notebook?**

Jupyter Notebook is an interactive platform for writing and running live code. It is widely used for data analysis, machine learning, and scripting.

### **How to Use This Program in Jupyter Notebook**

1.  **Install Jupyter Notebook** (if not already installed):
    
    ```bash
    pip install notebook
    
    ```
    
2.  **Open Jupyter Notebook**:
    
    ```bash
    jupyter notebook
    
    ```
    
3.  **Run the Notebook**:
    -   Navigate to the `.ipynb` file.
    -   Open and **run the code cells**.
    -   The program will launch in a new window.

----------