import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime, date

class Fragrance:
    def __init__(self, name, year, season, status):
        self.name = name
        self.year = year
        self.season = season
        self.status = status

class ShoppingList:
    def __init__(self, name, year, occasion, items, person_name=None, birthdate=None):
        self.name = name
        self.year = year
        self.occasion = occasion
        self.items = items
        self.person_name = person_name
        self.birthdate = birthdate  # Stored as 'YYYY-MM-DD'

    def get_birthdate_date(self):
        if self.birthdate:
            return datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        return None

class FragranceManager:
    def __init__(self):
        self.fragrances = []

    def add_fragrance(self, fragrance):
        self.fragrances.append(fragrance)

    def remove_fragrance(self, name):
        self.fragrances = [f for f in self.fragrances if f.name != name]

    def update_status(self, name, new_status):
        for fragrance in self.fragrances:
            if fragrance.name == name:
                fragrance.status = new_status
                break

    def save_to_json(self, filename):
        data = [{'name': f.name, 'year': f.year, 'season': f.season, 'status': f.status} for f in self.fragrances]
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load_from_json(cls, filename):
        manager = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    fragrance = Fragrance(item['name'], item['year'], item['season'], item['status'])
                    manager.add_fragrance(fragrance)
        except FileNotFoundError:
            pass
        return manager

class ShoppingListManager:
    def __init__(self):
        self.shopping_lists = []

    def create_list(self, name, year, occasion, items, person_name=None, birthdate=None):
        self.shopping_lists.append(ShoppingList(name, year, occasion, items, person_name, birthdate))

    def edit_list(self, list_name, new_items=None, new_occasion=None, new_year=None, new_person_name=None, new_birthdate=None):
        for lst in self.shopping_lists:
            if lst.name == list_name:
                if new_items is not None:
                    lst.items = new_items
                if new_occasion is not None:
                    lst.occasion = new_occasion
                if new_year is not None:
                    lst.year = new_year
                if new_person_name is not None:
                    lst.person_name = new_person_name
                if new_birthdate is not None:
                    lst.birthdate = new_birthdate
                break

    def export_list(self, list_name, filename):
        for lst in self.shopping_lists:
            if lst.name == list_name:
                with open(filename, 'w') as f:
                    for item in lst.items:
                        f.write(f"{item}\n")
                return True
        return False

    def save_to_json(self, filename):
        data = []
        for lst in self.shopping_lists:
            list_data = {
                'name': lst.name,
                'year': lst.year,
                'occasion': lst.occasion,
                'items': lst.items,
                'person_name': lst.person_name,
                'birthdate': lst.birthdate
            }
            data.append(list_data)
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load_from_json(cls, filename):
        manager = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    lst = ShoppingList(
                        item['name'],
                        item['year'],
                        item['occasion'],
                        item['items'],
                        item.get('person_name'),
                        item.get('birthdate')
                    )
                    manager.shopping_lists.append(lst)
        except FileNotFoundError:
            pass
        return manager

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bath & Body Works Organizer")

        self.fragrance_manager = FragranceManager.load_from_json('fragrances.json')
        self.shopping_list_manager = ShoppingListManager.load_from_json('shopping_lists.json')

        self.notebook = ttk.Notebook(self.root)
        self.fragrance_frame = ttk.Frame(self.notebook)
        self.shopping_list_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.fragrance_frame, text="Fragrances")
        self.notebook.add(self.shopping_list_frame, text="Shopping Lists")
        self.notebook.pack(expand=1, fill='both')

        self.setup_fragrance_tab()
        self.setup_shopping_list_tab()

    def setup_fragrance_tab(self):
        self.fragrance_tree = ttk.Treeview(self.fragrance_frame, columns=('Name', 'Year', 'Season', 'Status'), show='headings')
        self.fragrance_tree.heading('Name', text='Name')
        self.fragrance_tree.heading('Year', text='Year')
        self.fragrance_tree.heading('Season', text='Season')
        self.fragrance_tree.heading('Status', text='Status')
        self.fragrance_tree.pack(fill='both', expand=True)

        self.refresh_fragrance_tree()

        entry_frame = ttk.Frame(self.fragrance_frame)
        entry_frame.pack(fill='x')

        ttk.Label(entry_frame, text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(entry_frame)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(entry_frame, text="Year:").grid(row=0, column=2)
        self.year_entry = ttk.Entry(entry_frame)
        self.year_entry.grid(row=0, column=3)

        ttk.Label(entry_frame, text="Season:").grid(row=0, column=4)
        self.season_var = tk.StringVar()
        season_dropdown = ttk.Combobox(entry_frame, textvariable=self.season_var, values=['Spring', 'Summer', 'Fall', 'Winter'])
        season_dropdown.grid(row=0, column=5)

        ttk.Label(entry_frame, text="Status:").grid(row=0, column=6)
        self.status_var = tk.StringVar()
        status_dropdown = ttk.Combobox(entry_frame, textvariable=self.status_var, values=['SHOPPING LIST', 'I Have Not Smelled', 'I Like This One'])
        status_dropdown.grid(row=0, column=7)

        ttk.Button(entry_frame, text="Add", command=self.add_fragrance).grid(row=0, column=8, padx=5)
        ttk.Button(entry_frame, text="Remove Selected", command=self.remove_fragrance).grid(row=0, column=9, padx=5)

    def refresh_fragrance_tree(self):
        for item in self.fragrance_tree.get_children():
            self.fragrance_tree.delete(item)
        for fragrance in self.fragrance_manager.fragrances:
            self.fragrance_tree.insert('', 'end', values=(fragrance.name, fragrance.year, fragrance.season, fragrance.status))

    def add_fragrance(self):
        name = self.name_entry.get()
        year = self.year_entry.get()
        season = self.season_var.get()
        status = self.status_var.get()

        if not name or not year or not season or not status:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            year = int(year)
        except ValueError:
            messagebox.showerror("Error", "Year must be a number.")
            return

        self.fragrance_manager.add_fragrance(Fragrance(name, year, season, status))
        self.fragrance_manager.save_to_json('fragrances.json')
        self.refresh_fragrance_tree()
        self.name_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.season_var.set('')
        self.status_var.set('')

    def remove_fragrance(self):
        selected = self.fragrance_tree.selection()
        if not selected:
            return
        name = self.fragrance_tree.item(selected[0])['values'][0]
        self.fragrance_manager.remove_fragrance(name)
        self.fragrance_manager.save_to_json('fragrances.json')
        self.refresh_fragrance_tree()

    def setup_shopping_list_tab(self):
        self.shopping_tree = ttk.Treeview(self.shopping_list_frame, columns=('Name', 'Occasion', 'Year'), show='headings')
        self.shopping_tree.heading('Name', text='Name')
        self.shopping_tree.heading('Occasion', text='Occasion')
        self.shopping_tree.heading('Year', text='Year')
        self.shopping_tree.pack(fill='both', expand=True)

        self.refresh_shopping_tree()

        button_frame = ttk.Frame(self.shopping_list_frame)
        button_frame.pack(fill='x')

        ttk.Button(button_frame, text="Create List", command=self.create_shopping_list).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Edit List", command=self.edit_shopping_list).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Export List", command=self.export_shopping_list).pack(side='left', padx=5)
        ttk.Button(button_frame, text="View Details", command=self.view_shopping_list).pack(side='left', padx=5)

    def refresh_shopping_tree(self):
        for item in self.shopping_tree.get_children():
            self.shopping_tree.delete(item)
        for lst in self.shopping_list_manager.shopping_lists:
            self.shopping_tree.insert('', 'end', values=(lst.name, lst.occasion, lst.year))

    def create_shopping_list(self):
        window = tk.Toplevel(self.root)
        window.title("Create Shopping List")

        ttk.Label(window, text="List Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(window, text="Occasion:").grid(row=1, column=0, padx=5, pady=5)
        occasion_var = tk.StringVar()
        occasion_dropdown = ttk.Combobox(window, textvariable=occasion_var, values=['Birthday', 'Holiday', 'Other'])
        occasion_dropdown.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(window, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        year_entry = ttk.Entry(window)
        year_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(window, text="Items:").grid(row=3, column=0, padx=5, pady=5)
        items_frame = ttk.Frame(window)
        items_frame.grid(row=3, column=1, padx=5, pady=5)
        items_listbox = tk.Listbox(items_frame, height=5)
        items_listbox.pack(side='left', fill='both', expand=True)
        scrollbar = ttk.Scrollbar(items_frame, command=items_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        items_listbox.config(yscrollcommand=scrollbar.set)

        item_entry = ttk.Entry(window)
        item_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(window, text="Add Item", command=lambda: self.add_item(item_entry, items_listbox)).grid(row=4, column=2, padx=5)

        person_name_entry = ttk.Entry(window)
        birthdate_entry = ttk.Entry(window)

        def on_occasion_change(*args):
            if occasion_var.get() == 'Birthday':
                ttk.Label(window, text="Person Name:").grid(row=5, column=0, padx=5, pady=5)
                person_name_entry.grid(row=5, column=1, padx=5, pady=5)
                ttk.Label(window, text="Birthdate (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5)
                birthdate_entry.grid(row=6, column=1, padx=5, pady=5)
            else:
                person_name_entry.grid_remove()
                birthdate_entry.grid_remove()

        occasion_var.trace_add('write', on_occasion_change)

        def submit():
            name = name_entry.get()
            year = year_entry.get()
            occasion = occasion_var.get()
            items = items_listbox.get(0, tk.END)
            person_name = person_name_entry.get() if occasion == 'Birthday' else None
            birthdate = birthdate_entry.get() if occasion == 'Birthday' else None

            if not name or not year or not occasion:
                messagebox.showerror("Error", "Name, Year, and Occasion are required.")
                return
            try:
                year = int(year)
            except ValueError:
                messagebox.showerror("Error", "Year must be a number.")
                return
            if occasion == 'Birthday' and (not person_name or not birthdate):
                messagebox.showerror("Error", "Person Name and Birthdate are required for birthdays.")
                return
            if occasion == 'Birthday':
                try:
                    datetime.strptime(birthdate, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Error", "Birthdate must be in YYYY-MM-DD format.")
                    return

            self.shopping_list_manager.create_list(name, year, occasion, list(items), person_name, birthdate)
            self.shopping_list_manager.save_to_json('shopping_lists.json')
            self.refresh_shopping_tree()
            window.destroy()

        ttk.Button(window, text="Create", command=submit).grid(row=7, column=1, pady=10)

    def add_item(self, entry, listbox):
        item = entry.get()
        if item:
            listbox.insert(tk.END, item)
            entry.delete(0, tk.END)

    def edit_shopping_list(self):
        selected = self.shopping_tree.selection()
        if not selected:
            return
        list_name = self.shopping_tree.item(selected[0])['values'][0]
        lst = next((lst for lst in self.shopping_list_manager.shopping_lists if lst.name == list_name), None)
        if not lst:
            return

        window = tk.Toplevel(self.root)
        window.title("Edit Shopping List")

        ttk.Label(window, text="List Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(window)
        name_entry.insert(0, lst.name)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(window, text="Occasion:").grid(row=1, column=0, padx=5, pady=5)
        occasion_var = tk.StringVar(value=lst.occasion)
        occasion_dropdown = ttk.Combobox(window, textvariable=occasion_var, values=['Birthday', 'Holiday', 'Other'])
        occasion_dropdown.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(window, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        year_entry = ttk.Entry(window)
        year_entry.insert(0, str(lst.year))
        year_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(window, text="Items:").grid(row=3, column=0, padx=5, pady=5)
        items_frame = ttk.Frame(window)
        items_frame.grid(row=3, column=1, padx=5, pady=5)
        items_listbox = tk.Listbox(items_frame, height=5)
        items_listbox.pack(side='left', fill='both', expand=True)
        scrollbar = ttk.Scrollbar(items_frame, command=items_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        items_listbox.config(yscrollcommand=scrollbar.set)
        for item in lst.items:
            items_listbox.insert(tk.END, item)

        item_entry = ttk.Entry(window)
        item_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(window, text="Add Item", command=lambda: self.add_item(item_entry, items_listbox)).grid(row=4, column=2, padx=5)

        person_name_entry = ttk.Entry(window)
        birthdate_entry = ttk.Entry(window)

        if lst.occasion == 'Birthday':
            ttk.Label(window, text="Person Name:").grid(row=5, column=0, padx=5, pady=5)
            person_name_entry.insert(0, lst.person_name)
            person_name_entry.grid(row=5, column=1, padx=5, pady=5)
            ttk.Label(window, text="Birthdate (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5)
            birthdate_entry.insert(0, lst.birthdate)
            birthdate_entry.grid(row=6, column=1, padx=5, pady=5)

        def on_occasion_change(*args):
            if occasion_var.get() == 'Birthday':
                ttk.Label(window, text="Person Name:").grid(row=5, column=0, padx=5, pady=5)
                person_name_entry.grid(row=5, column=1, padx=5, pady=5)
                ttk.Label(window, text="Birthdate (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5)
                birthdate_entry.grid(row=6, column=1, padx=5, pady=5)
            else:
                person_name_entry.grid_remove()
                birthdate_entry.grid_remove()

        occasion_var.trace_add('write', on_occasion_change)

        def submit():
            new_name = name_entry.get()
            new_year = year_entry.get()
            new_occasion = occasion_var.get()
            new_items = list(items_listbox.get(0, tk.END))
            new_person_name = person_name_entry.get() if new_occasion == 'Birthday' else None
            new_birthdate = birthdate_entry.get() if new_occasion == 'Birthday' else None

            if not new_name or not new_year or not new_occasion:
                messagebox.showerror("Error", "Name, Year, and Occasion are required.")
                return
            try:
                new_year = int(new_year)
            except ValueError:
                messagebox.showerror("Error", "Year must be a number.")
                return
            if new_occasion == 'Birthday' and (not new_person_name or not new_birthdate):
                messagebox.showerror("Error", "Person Name and Birthdate are required for birthdays.")
                return
            if new_occasion == 'Birthday':
                try:
                    datetime.strptime(new_birthdate, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Error", "Birthdate must be in YYYY-MM-DD format.")
                    return

            self.shopping_list_manager.edit_list(
                lst.name,
                new_items=new_items,
                new_occasion=new_occasion,
                new_year=new_year,
                new_person_name=new_person_name,
                new_birthdate=new_birthdate
            )
            if new_name != lst.name:
                lst.name = new_name
            self.shopping_list_manager.save_to_json('shopping_lists.json')
            self.refresh_shopping_tree()
            window.destroy()

        ttk.Button(window, text="Save", command=submit).grid(row=7, column=1, pady=10)

    def export_shopping_list(self):
        selected = self.shopping_tree.selection()
        if not selected:
            return
        list_name = self.shopping_tree.item(selected[0])['values'][0]
        if self.shopping_list_manager.export_list(list_name, f"{list_name}.txt"):
            messagebox.showinfo("Success", f"Exported list to {list_name}.txt")
        else:
            messagebox.showerror("Error", "List not found.")

    def view_shopping_list(self):
        selected = self.shopping_tree.selection()
        if not selected:
            return
        list_name = self.shopping_tree.item(selected[0])['values'][0]
        lst = next((lst for lst in self.shopping_list_manager.shopping_lists if lst.name == list_name), None)
        if not lst:
            return

        window = tk.Toplevel(self.root)
        window.title(f"Details: {list_name}")

        ttk.Label(window, text=f"Occasion: {lst.occasion}").pack(padx=10, pady=5)
        ttk.Label(window, text=f"Year: {lst.year}").pack(padx=10, pady=5)

        if lst.occasion == 'Birthday' and lst.birthdate:
            birthdate = lst.get_birthdate_date()
            today = date.today()
            age = today.year - birthdate.year
            if (today.month, today.day) < (birthdate.month, birthdate.day):
                age -= 1
            next_birthday = date(today.year, birthdate.month, birthdate.day)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_until = (next_birthday - today).days

            ttk.Label(window, text=f"Person: {lst.person_name}").pack(padx=10, pady=5)
            ttk.Label(window, text=f"Birthdate: {lst.birthdate}").pack(padx=10, pady=5)
            ttk.Label(window, text=f"Age This Year: {age}").pack(padx=10, pady=5)
            ttk.Label(window, text=f"Days Until Next Birthday: {days_until}").pack(padx=10, pady=5)

        ttk.Label(window, text="Items:").pack(padx=10, pady=5)
        items_text = "\n".join(lst.items)
        ttk.Label(window, text=items_text).pack(padx=10, pady=5)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = UserInterface()
    app.run()
