# Railway Waiting List
import tkinter as tk
from tkinter import messagebox

waiting_list = []

# Main Window
root = tk.Tk()        
root.title("Railway Waiting List")
root.geometry("600x600")
root.configure(bg="lightgray")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

# Title
tk.Label(root,text="Railway Waiting List",font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

# Passenger Name
tk.Label(root,text="Passenger Name").grid(row=1, column=0, sticky="w", padx=20, pady=5)

name = tk.Entry(root, width=30)
name.grid(row=1, column=1, padx=20, pady=5)

# Waiting List
tk.Label(root,text="Waiting List").grid(row=2, column=0, sticky="nw", padx=20, pady=5)

waiting_box = tk.Listbox(root, height=10, width=30)
waiting_box.grid(row=2, column=1, padx=20, pady=5)

# Add Passenger
def add_passenger():
    passenger = name.get()

    if passenger == "":
        messagebox.showwarning("Warning", "Enter passenger name")
    else:
        waiting_list.append(passenger)
        waiting_box.insert(tk.END, passenger)
        messagebox.showinfo("Success",passenger + " has been added to the waiting list.")
        name.delete(0, tk.END)

# Confirm Ticket
def confirm_ticket():
    if len(waiting_list) == 0:
        messagebox.showwarning("Warning","Waiting list is empty.")
    else:
        passenger = waiting_list.pop(0)
        waiting_box.delete(0)

        messagebox.showinfo("Ticket Confirmed","Ticket confirmed for: " + passenger)

# Display Waiting List
def display_list():
    if len(waiting_list) == 0:
        messagebox.showinfo("Waiting List","Waiting list is empty.")
    else:
        info = "--- Waiting List ---\n\n"

        for i in range(len(waiting_list)):
            info += str(i + 1) + ". " + waiting_list[i] + "\n"

        messagebox.showinfo("Waiting List", info)

# View First Passenger
def view_first():
    if len(waiting_list) == 0:
        messagebox.showinfo("First Passenger","Waiting list is empty.")
    else:
        messagebox.showinfo("First Passenger","First passenger: " + waiting_list[0])

# Search Passenger
def search_passenger():
    passenger = name.get()

    if passenger == "":
        messagebox.showwarning("Warning","Enter passenger name to search.")
    elif passenger in waiting_list:
        position = waiting_list.index(passenger) + 1

        messagebox.showinfo("Passenger Found",passenger + " is in the waiting list.\n"+ "Waiting position: " + str(position))
    else:
        messagebox.showinfo("Passenger Not Found",passenger + " is not in the waiting list.")

# Cancel Passenger
def cancel_passenger():
    passenger = name.get()

    if passenger == "":
        messagebox.showwarning("Warning","Enter passenger name to cancel.")
    elif passenger in waiting_list:
        waiting_list.remove(passenger)
        
        position = waiting_box.get(0, tk.END).index(passenger)
        waiting_box.delete(position)
        
        messagebox.showinfo("Cancelled",passenger + " has been removed from the waiting list.")
        name.delete(0, tk.END)
    else:
        messagebox.showinfo("Not Found",passenger + " is not in the waiting list.")

# Count Passengers
def count_passengers():
    messagebox.showinfo("Passenger Count","Total passengers waiting: "+ str(len(waiting_list)))

#Exit
def exit_program():
    root.destroy()

# Buttons

tk.Button(root,text="Add Passenger",width=20,command=add_passenger).grid(row=3, column=0, padx=10, pady=8)

tk.Button(root,text="Confirm Ticket",width=20,command=confirm_ticket).grid(row=3, column=1, padx=10, pady=8)

tk.Button(root,text="Display Waiting List",width=20,command=display_list).grid(row=4, column=0, padx=10, pady=8)

tk.Button(root,text="View First Passenger",width=20,command=view_first).grid(row=4, column=1, padx=10, pady=8)

tk.Button(root,text="Search Passenger",width=20,command=search_passenger).grid(row=5, column=0, padx=10, pady=8)

tk.Button(root,text="Cancel Passenger",width=20,command=cancel_passenger).grid(row=5, column=1, padx=10, pady=8)

tk.Button(root,text="Count Passengers",width=20,command=count_passengers).grid(row=6, column=0, padx=10, pady=8)

tk.Button(root,text="Exit",width=20,command=exit_program).grid(row=6, column=1, padx=10, pady=8)


# Start Application
root.mainloop()
