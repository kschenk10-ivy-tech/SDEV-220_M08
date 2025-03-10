## Pseudocode

```pseudocode
CLASS Fragrance:
    METHOD __init__(name, year, season, status):
        SET self.name TO name
        SET self.year TO year
        SET self.season TO season
        SET self.status TO status

CLASS ShoppingList:
    METHOD __init__(name, year, occasion, items, person_name=None, birthdate=None):
        SET self.name TO name
        SET self.year TO year
        SET self.occasion TO occasion
        SET self.items TO items
        SET self.person_name TO person_name
        SET self.birthdate TO birthdate

    METHOD get_birthdate_date():
        IF self.birthdate IS NOT None:
            RETURN datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        RETURN None

CLASS FragranceManager:
    METHOD __init__():
        SET self.fragrances TO empty list

    METHOD add_fragrance(fragrance):
        APPEND fragrance TO self.fragrances

    METHOD remove_fragrance(name):
        SET self.fragrances TO [f FOR f IN self.fragrances IF f.name != name]

    METHOD update_status(name, new_status):
        FOR fragrance IN self.fragrances:
            IF fragrance.name == name:
                SET fragrance.status TO new_status
                BREAK

    METHOD save_to_json(filename):
        SET data TO [{'name': f.name, 'year': f.year, 'season': f.season, 'status': f.status} FOR f IN self.fragrances]
        OPEN filename IN write mode AS f:
            json.dump(data, f)

    CLASSMETHOD load_from_json(filename):
        CREATE manager AS new instance of FragranceManager
        TRY:
            OPEN filename IN read mode AS f:
                SET data TO json.load(f)
                FOR item IN data:
                    CREATE fragrance AS new instance of Fragrance(item['name'], item['year'], item['season'], item['status'])
                    CALL manager.add_fragrance(fragrance)
        EXCEPT FileNotFoundError:
            PASS
        RETURN manager

CLASS ShoppingListManager:
    METHOD __init__():
        SET self.shopping_lists TO empty list

    METHOD create_list(name, year, occasion, items, person_name=None, birthdate=None):
        APPEND new ShoppingList(name, year, occasion, items, person_name, birthdate) TO self.shopping_lists

    METHOD edit_list(list_name, new_items=None, new_occasion=None, new_year=None, new_person_name=None, new_birthdate=None):
        FOR lst IN self.shopping_lists:
            IF lst.name == list_name:
                IF new_items IS NOT None:
                    SET lst.items TO new_items
                IF new_occasion IS NOT None:
                    SET lst.occasion TO new_occasion
                IF new_year IS NOT None:
                    SET lst.year TO new_year
                IF new_person_name IS NOT None:
                    SET lst.person_name TO new_person_name
                IF new_birthdate IS NOT None:
                    SET lst.birthdate TO new_birthdate
                BREAK

    METHOD export_list(list_name, filename):
        FOR lst IN self.shopping_lists:
            IF lst.name == list_name:
                OPEN filename IN write mode AS f:
                    FOR item IN lst.items:
                        WRITE item TO f
                RETURN True
        RETURN False

    METHOD save_to_json(filename):
        SET data TO empty list
        FOR lst IN self.shopping_lists:
            SET list_data TO {
                'name': lst.name,
                'year': lst.year,
                'occasion': lst.occasion,
                'items': lst.items,
                'person_name': lst.person_name,
                'birthdate': lst.birthdate
            }
            APPEND list_data TO data
        OPEN filename IN write mode AS f:
            json.dump(data, f)

    CLASSMETHOD load_from_json(filename):
        CREATE manager AS new instance of ShoppingListManager
        TRY:
            OPEN filename IN read mode AS f:
                SET data TO json.load(f)
                FOR item IN data:
                    CREATE lst AS new instance of ShoppingList(item['name'], item['year'], item['occasion'], item['items'], item.get('person_name'), item.get('birthdate'))
                    APPEND lst TO manager.shopping_lists
        EXCEPT FileNotFoundError:
            PASS
        RETURN manager

CLASS UserInterface:
    METHOD __init__():
        CREATE self.root AS new instance of tk.Tk()
        SET self.root.title TO "Bath & Body Works Organizer"

        SET self.fragrance_manager TO FragranceManager.load_from_json('fragrances.json')
        SET self.shopping_list_manager TO ShoppingListManager.load_from_json('shopping_lists.json')

        CREATE self.notebook AS new instance of ttk.Notebook(self.root)
        CREATE self.fragrance_frame AS new instance of ttk.Frame(self.notebook)
        CREATE self.shopping_list_frame AS new instance of ttk.Frame(self.notebook)
        CALL self.notebook.add(self.fragrance_frame, text="Fragrances")
        CALL self.notebook.add(self.shopping_list_frame, text="Shopping Lists")
        CALL self.notebook.pack(expand=1, fill='both')

        CALL self.setup_fragrance_tab()
        CALL self.setup_shopping_list_tab()

    METHOD setup_fragrance_tab():
        CREATE self.fragrance_tree AS new instance of ttk.Treeview(self.fragrance_frame, columns=('Name', 'Year', 'Season', 'Status'), show='headings')
        SET self.fragrance_tree.heading('Name', text='Name')
        SET self.fragrance_tree.heading('Year', text='Year')
        SET self.fragrance_tree.heading('Season', text='Season')
        SET self.fragrance_tree.heading('Status', text='Status')
        CALL self.fragrance_tree.pack(fill='both', expand=True)

        CALL self.refresh_fragrance_tree()

        CREATE entry_frame AS new instance of ttk.Frame(self.fragrance_frame)
        CALL entry_frame.pack(fill='x')

        CREATE ttk.Label(entry_frame, text="Name:").grid(row=0, column=0)
        CREATE self.name_entry AS new instance of ttk.Entry(entry_frame)
        CALL self.name_entry.grid(row=0, column=1)

        CREATE ttk.Label(entry_frame, text="Year:").grid(row=0, column=2)
        CREATE self.year_entry AS new instance of ttk.Entry(entry_frame)
        CALL self.year_entry.grid(row=0, column=3)

        CREATE ttk.Label(entry_frame, text="Season:").grid(row=0, column=4)
        CREATE self.season_var AS new instance of tk.StringVar()
        CREATE season_dropdown AS new instance of ttk.Combobox(entry_frame, textvariable=self.season_var, values=['Spring', 'Summer', 'Fall', 'Winter'])
        CALL season_dropdown.grid(row=0, column=5)

        CREATE ttk.Label(entry_frame, text="Status:").grid(row=0, column=6)
        CREATE self.status_var AS new instance of tk.StringVar()
        CREATE status_dropdown AS new instance of ttk.Combobox(entry_frame, textvariable=self.status_var, values=['SHOPPING LIST', 'I Have Not Smelled', 'I Like This One'])
        CALL status_dropdown.grid(row=0, column=7)

        CREATE ttk.Button(entry_frame, text="Add", command=self.add_fragrance).grid(row=0, column=8, padx=5)
        CREATE ttk.Button(entry_frame, text="Remove Selected", command=self.remove_fragrance).grid(row=0, column=9, padx=5)

    METHOD refresh_fragrance_tree():
        FOR item IN self.fragrance_tree.get_children():
            CALL self.fragrance_tree.delete(item)
        FOR fragrance IN self.fragrance_manager.fragrances:
            CALL self.fragrance_tree.insert('', 'end', values=(fragrance.name, fragrance.year, fragrance.season, fragrance.status))

    METHOD add_fragrance():
        SET name TO self.name_entry.get()
        SET year TO self.year_entry.get()
        SET season TO self.season_var.get()
        SET status TO self.status_var.get()

        IF name IS empty OR year IS empty OR season IS empty OR status IS empty:
            CALL messagebox.showerror("Error", "All fields are required.")
            RETURN
        TRY:
            SET year TO int(year)
        EXCEPT ValueError:
            CALL messagebox.showerror("Error", "Year must be a number.")
            RETURN

        CALL self.fragrance_manager.add_fragrance(Fragrance(name, year, season, status))
        CALL self.fragrance_manager.save_to_json('fragrances.json')
        CALL self.refresh_fragrance_tree()
        CALL self.name_entry.delete(0, tk.END)
        CALL self.year_entry.delete(0, tk.END)
        CALL self.season_var.set('')
        CALL self.status_var.set('')

    METHOD remove_fragrance():
        SET selected TO self.fragrance_tree.selection()
        IF selected IS empty:
            RETURN
        SET name TO self.fragrance_tree.item(selected[0])['values'][0]
        CALL self.fragrance_manager.remove_fragrance(name)
        CALL self.fragrance_manager.save_to_json('fragrances.json')
        CALL self.refresh_fragrance_tree()

    METHOD setup_shopping_list_tab():
        CREATE self.shopping_tree AS new instance of ttk.Treeview(self.shopping_list_frame, columns=('Name', 'Occasion', 'Year'), show='headings')
        SET self.shopping_tree.heading('Name', text='Name')
        SET self.shopping_tree.heading('Occasion', text='Occasion')
        SET self.shopping_tree.heading('Year', text='Year')
        CALL self.shopping_tree.pack(fill='both', expand=True)

        CALL self.refresh_shopping_tree()

        CREATE button_frame AS new instance of ttk.Frame(self.shopping_list_frame)
        CALL button_frame.pack(fill='x')

        CREATE ttk.Button(button_frame, text="Create List", command=self.create_shopping_list).pack(side='left', padx=5)
        CREATE ttk.Button(button_frame, text="Edit List", command=self.edit_shopping_list).pack(side='left', padx=5)
        CREATE ttk.Button(button_frame, text="Export List", command=self.export_shopping_list).pack(side='left', padx=5)
        CREATE ttk.Button(button_frame, text="View Details", command=self.view_shopping_list).pack(side='left', padx=5)

    METHOD refresh_shopping_tree():
        FOR item IN self.shopping_tree.get_children():
            CALL self.shopping_tree.delete(item)
        FOR lst IN self.shopping_list_manager.shopping_lists:
            CALL self.shopping_tree.insert('', 'end', values=(lst.name, lst.occasion, lst.year))

    METHOD create_shopping_list():
        CREATE window AS new instance of tk.Toplevel(self.root)
        SET window.title TO "Create Shopping List"

        CREATE ttk.Label(window, text="List Name:").grid(row=0, column=0, padx=5, pady=5)
        CREATE name_entry AS new instance of ttk.Entry(window)
        CALL name_entry.grid(row=0, column=1, padx=5, pady=5)

        CREATE ttk.Label(window, text="Occasion:").grid(row=1, column=0, padx=5, pady=5)
        CREATE occasion_var AS new instance of tk.StringVar()
        CREATE occasion_dropdown AS new instance of ttk.Combobox(window, textvariable=occasion_var, values=['Birthday', 'Holiday', 'Other'])
        CALL occasion_dropdown.grid(row=1, column=1, padx=5, pady=5)

        CREATE ttk.Label(window, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        CREATE year_entry AS new instance of ttk.Entry(window)
        CALL year_entry.grid(row=2, column=1, padx=5, pady=5)

        CREATE ttk.Label(window, text="Items:").grid(row=3, column=0, padx=5, pady=5)
        CREATE items_frame AS new instance of ttk.Frame(window)
        CALL items_frame.grid(row=3, column=1, padx=5, pady=5)
        CREATE items_listbox AS new instance of tk.Listbox(items_frame, height=5)
        CALL items_listbox.pack(side='left', fill='both', expand=True)
        CREATE scrollbar AS new instance of ttk.Scrollbar(items_frame, command=items_listbox.yview)
        CALL scrollbar.pack(side='right', fill='y')
        CALL items_listbox.config(yscrollcommand=scrollbar.set)

        CREATE item_entry AS new instance of ttk.Entry(window)
        CALL item_entry.grid(row=4, column=1, padx=5, pady=5)
        CREATE ttk.Button(window, text="Add Item", command=lambda: self.add_item(item_entry, items_listbox)).grid(row=4, column=2, padx=5)

        CREATE person_name_entry AS new instance of ttk.Entry(window)
        CREATE birthdate_entry AS new instance of ttk.Entry(window)

        METHOD on_occasion_change(*args):
            IF occasion_var.get() == 'Birthday':
                CREATE ttk.Label(window, text="Person Name:").grid(row=5, column=0, padx=5, pady=5)
                CALL person_name_entry.grid(row=5, column=1, padx=5, pady=5)
                CREATE ttk.Label(window, text="Birthdate (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5)
                CALL birthdate_entry.grid(row=6, column=1, padx=5, pady=5)
            ELSE:
                CALL person_name_entry.grid_remove()
                CALL birthdate_entry.grid_remove()

        CALL occasion_var.trace_add('write', on_occasion_change)

        METHOD submit():
            SET name TO name_entry.get()
            SET year TO year_entry.get()
            SET occasion TO occasion_var.get()
            SET items TO list(items_listbox.get(0, tk.END))
            SET person_name TO person_name_entry.get() IF occasion == 'Birthday' ELSE None
            SET birthdate TO birthdate_entry.get() IF occasion == 'Birthday' ELSE None

            IF name IS empty OR year IS empty OR occasion IS empty:
                CALL messagebox.showerror("Error", "Name, Year, and Occasion are required.")
                RETURN
            TRY:
                SET year TO int(year)
            EXCEPT ValueError:
                CALL messagebox.showerror("Error", "Year must be a number.")
                RETURN
            IF occasion == 'Birthday' AND (person_name IS empty OR birthdate IS empty):
                CALL messagebox.showerror("Error", "Person Name and Birthdate are required for birthdays.")
                RETURN
            IF occasion == 'Birthday':
                TRY:
                    CALL datetime.strptime(birthdate, "%Y-%m-%d")
                EXCEPT ValueError:
                    CALL messagebox.showerror("Error", "Birthdate must be in YYYY-MM-DD format.")
                    RETURN

            CALL self.shopping_list_manager.create_list(name, year, occasion, items, person_name, birthdate)
            CALL self.shopping_list_manager.save_to_json('shopping_lists.json')
            CALL self.refresh_shopping_tree()
            CALL window.destroy()

        CREATE ttk.Button(window, text="Create", command=submit).grid(row=7, column=1, pady=10)

    METHOD add_item(entry, listbox):
        SET item TO entry.get()
        IF item IS NOT empty:
            CALL listbox.insert(tk.END, item)
            CALL entry.delete(0, tk.END)

    METHOD edit_shopping_list():
        SET selected TO self.shopping_tree.selection()
        IF selected IS empty:
            RETURN
        SET list_name TO self.shopping_tree.item(selected[0])['values'][0]
        SET lst TO next((lst FOR lst IN self.shopping_list_manager.shopping_lists IF lst.name == list_name), None)
        IF lst IS None:
            RETURN

        CREATE window AS new instance of tk.Toplevel(self.root)
        SET window.title TO "Edit Shopping List"

        CREATE ttk.Label(window, text="List Name:").grid(row=0, column=0, padx=5, pady=5)
        CREATE name_entry AS new instance of ttk.Entry(window)
        CALL name_entry.insert(0, lst.name)
        CALL name_entry.grid(row=0, column=1, padx=5, pady=5)

        CREATE ttk.Label(window, text="Occasion:").grid(row=1, column=0, padx=5, pady=5)
        CREATE occasion_var AS new instance of tk.StringVar(value=lst.occasion)
        CREATE occasion_dropdown AS new instance of ttk.Combobox(window, textvariable=occasion_var, values=['Birthday', 'Holiday', 'Other'])
        CALL occasion_dropdown.grid(row=1, column=1, padx=5, pady=5)

        CREATE ttk.Label(window, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        CREATE year_entry AS new instance of ttk.Entry(window)
        CALL year_entry.insert(0, str(lst.year))
        CALL year_entry.grid(row=2, column=1, padx=5, pady=5)

        CREATE ttk.Label(window, text="Items:").grid(row=3, column=0, padx=5, pady=5)
        CREATE items_frame AS new instance of ttk.Frame(window)
        CALL items_frame.grid(row=3, column=1, padx=5, pady=5)
        CREATE items_listbox AS new instance of tk.Listbox(items_frame, height=5)
        CALL items_listbox.pack(side='left', fill='both', expand=True)
        CREATE scrollbar AS new instance of ttk.Scrollbar(items_frame, command=items_listbox.yview)
        CALL scrollbar.pack(side='right', fill='y')
        CALL items_listbox.config(yscrollcommand=scrollbar.set)
        FOR item IN lst.items:
            CALL items_listbox.insert(tk.END, item)

        CREATE item_entry AS new instance of ttk.Entry(window)
        CALL item_entry.grid(row=4, column=1, padx=5, pady=5)
        CREATE ttk.Button(window, text="Add Item", command=lambda: self.add_item(item_entry, items_listbox)).grid(row=4, column=2, padx=5)

        CREATE person_name_entry AS new instance of ttk.Entry(window)
        CREATE birthdate_entry AS new instance of ttk.Entry(window)

        IF lst.occasion == 'Birthday':
            CREATE ttk.Label(window, text="Person Name:").grid(row=5, column=0, padx=5, pady=5)
            CALL person_name_entry.insert(0, lst.person_name)
            CALL person_name_entry.grid(row=5, column=1, padx=5, pady=5)
            CREATE ttk.Label(window, text="Birthdate (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5)
            CALL birthdate_entry.insert(0, lst.birthdate)
            CALL birthdate_entry.grid(row=6, column=1, padx=5, pady=5)

        METHOD on_occasion_change(*args):
            IF occasion_var.get() == 'Birthday':
                CREATE ttk.Label(window, text="Person Name:").grid(row=5, column=0, padx=5, pady=5)
                CALL person_name_entry.grid(row=5, column=1, padx=5, pady=5)
                CREATE ttk.Label(window, text="Birthdate (YYYY-MM-DD):").grid(row=6, column=0, padx=5, pady=5)
                CALL birthdate_entry.grid(row=6, column=1, padx=5, pady=5)
            ELSE:
                CALL person_name_entry.grid_remove()
                CALL birthdate_entry.grid_remove()

        CALL occasion_var.trace_add('write', on_occasion_change)

        METHOD submit():
            SET new_name TO name_entry.get()
            SET new_year TO year_entry.get()
            SET new_occasion TO occasion_var.get()
            SET new_items TO list(items_listbox.get(0, tk.END))
            SET new_person_name TO person_name_entry.get() IF new_occasion == 'Birthday' ELSE None
            SET new_birthdate TO birthdate_entry.get() IF new_occasion == 'Birthday' ELSE None

            IF new_name IS empty OR new_year IS empty OR new_occasion IS empty:
                CALL messagebox.showerror("Error", "Name, Year, and Occasion are required.")
                RETURN
            TRY:
                SET new_year TO int(new_year)
            EXCEPT ValueError:
                CALL messagebox.showerror("Error", "Year must be a number.")
                RETURN
            IF new_occasion == 'Birthday' AND (new_person_name IS empty OR new_birthdate IS empty):
                CALL messagebox.showerror("Error", "Person Name and Birthdate are required for birthdays.")
                RETURN
            IF new_occasion == 'Birthday':
                TRY:
                    CALL datetime.strptime(new_birthdate, "%Y-%m-%d")
                EXCEPT ValueError:
                    CALL messagebox.showerror("Error", "Birthdate must be in YYYY-MM-DD format.")
                    RETURN

            CALL self.shopping_list_manager.edit_list(
                lst.name,
                new_items=new_items,
                new_occasion=new_occasion,
                new_year=new_year,
                new_person_name=new_person_name,
                new_birthdate=new_birthdate
            )
            IF new_name != lst.name:
                SET lst.name TO new_name
            CALL self.shopping_list_manager.save_to_json('shopping_lists.json')
            CALL self.refresh_shopping_tree()
            CALL window.destroy()

        CREATE ttk.Button(window, text="Save", command=submit).grid(row=7, column=1, pady=10)

    METHOD export_shopping_list():
        SET selected TO self.shopping_tree.selection()
        IF selected IS empty:
            RETURN
        SET list_name TO self.shopping_tree.item(selected[0])['values'][0]
        IF self.shopping_list_manager.export_list(list_name, f"{list_name}.txt"):
            CALL messagebox.showinfo("Success", f"Exported list to {list_name}.txt")
        ELSE:
            CALL messagebox.showerror("Error", "List not found.")

    METHOD view_shopping_list():
        SET selected TO self.shopping_tree.selection()
        IF selected IS empty:
            RETURN
        SET list_name TO self.shopping_tree.item(selected[0])['values'][0]
        SET lst TO next((lst FOR lst IN self.shopping_list_manager.shopping_lists IF lst.name == list_name), None)
        IF lst IS None:
            RETURN

        CREATE window AS new instance of tk.Toplevel(self.root)
        SET window.title TO f"Details: {list_name}"

        CREATE ttk.Label(window, text=f"Occasion: {lst.occasion}").pack(padx=10, pady=5)
        CREATE ttk.Label(window, text=f"Year: {lst.year}").pack(padx=10, pady=5)

        IF lst.occasion == 'Birthday' AND lst.birthdate IS NOT None:
            SET birthdate TO lst.get_birthdate_date()
            SET today TO date.today()
            SET age TO today.year - birthdate.year
            IF (today.month, today.day) < (birthdate.month, birthdate.day):
                SET age TO age - 1
            SET next_birthday TO date(today.year, birthdate.month, birthdate.day)
            IF next_birthday < today:
                SET next_birthday TO next_birthday.replace(year=today.year + 1)
            SET days_until TO (next_birthday - today).days

            CREATE ttk.Label(window, text=f"Person: {lst.person_name}").pack(padx=10, pady=5)
            CREATE ttk.Label(window, text=f"Birthdate: {lst.birthdate}").pack(padx=10, pady=5)
            CREATE ttk.Label(window, text=f"Age This Year: {age}").pack(padx=10, pady=5)
            CREATE ttk.Label(window, text=f"Days Until Next Birthday: {days_until}").pack(padx=10, pady=5)

        CREATE ttk.Label(window, text="Items:").pack(padx=10, pady=5)
        SET items_text TO "\n".join(lst.items)
        CREATE ttk.Label(window, text=items_text).pack(padx=10, pady=5)

    METHOD run():
        CALL self.root.mainloop()

IF __name__ == "__main__":
    CREATE app AS new instance of UserInterface()
    CALL app.run()
```
