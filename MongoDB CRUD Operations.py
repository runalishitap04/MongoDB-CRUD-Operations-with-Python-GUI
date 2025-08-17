import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["furniture_store"]
collection = db["inventory"]

# GUI setup
root = tk.Tk()
root.title("Furniture Store Inventory")

# Entries
labels = ["Name", "Category", "Price", "Quantity"]
entries = {}
for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries[text.lower()] = entry

# Functions
def clear():
    for e in entries.values(): e.delete(0, tk.END)

def refresh():
    listbox.delete(0, tk.END)
    for item in collection.find():
        listbox.insert(tk.END, f"{item['_id']} - {item['name']} ({item['category']}, ${item['price']}, Qty:{item['quantity']})")

def create():  # Add
    try:
        doc = {
            "name": entries["name"].get(),
            "category": entries["category"].get(),
            "price": float(entries["price"].get()),
            "quantity": int(entries["quantity"].get())
        }
        if not doc["name"] or not doc["category"]:
            raise ValueError
        collection.insert_one(doc)
        messagebox.showinfo("Created", "Item added.")
        clear(); refresh()
    except:
        messagebox.showerror("Error", "Invalid input.")

def update():
    try:
        _id = listbox.get(tk.ACTIVE).split(" - ")[0]
        doc = {
            "name": entries["name"].get(),
            "category": entries["category"].get(),
            "price": float(entries["price"].get()),
            "quantity": int(entries["quantity"].get())
        }
        collection.update_one({"_id": ObjectId(_id)}, {"$set": doc})
        messagebox.showinfo("Updated", "Item updated.")
        clear(); refresh()
    except:
        messagebox.showerror("Error", "Select item and enter valid data.")

def delete():
    try:
        _id = listbox.get(tk.ACTIVE).split(" - ")[0]
        collection.delete_one({"_id": ObjectId(_id)})
        messagebox.showinfo("Deleted", "Item removed.")
        clear(); refresh()
    except:
        messagebox.showerror("Error", "Select a valid item.")

def select(event):
    try:
        item = listbox.get(tk.ACTIVE).split(" - ")[1]
        name, rest = item.split(" (")
        category, prq = rest.split(", $")
        price, qty = prq.split(", Qty:")
        entries["name"].delete(0, tk.END); entries["name"].insert(0, name)
        entries["category"].delete(0, tk.END); entries["category"].insert(0, category)
        entries["price"].delete(0, tk.END); entries["price"].insert(0, price)
        entries["quantity"].delete(0, tk.END); entries["quantity"].insert(0, qty.strip(")"))
    except:
        pass

# Buttons
tk.Button(root, text="Create", command=create).grid(row=4, column=0)
tk.Button(root, text="Update", command=update).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete).grid(row=4, column=2)

# Listbox
listbox = tk.Listbox(root, width=80)
listbox.grid(row=5, column=0, columnspan=3)
listbox.bind("<<ListboxSelect>>", select)

refresh()
root.mainloop()
