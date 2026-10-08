#Parking Lot Management
import tkinter as tk
from tkinter import messagebox

#Creating lists
parking = []
waiting = []
capacity = 3

#Main Window
root = tk.Tk()
root.title("Parking Lot Management System")
root.geometry("650x600")
root.configure(bg="lightgray")

#Menu
menu = tk.Menu(root)
root.config(menu=menu)

#Title
tk.Label(root,text="Parking Lot Management System",font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

#Vehicle Number
tk.Label(root,text="Vehicle Number").grid(row=1, column=0, sticky="w", padx=20, pady=5)

vehicle_entry = tk.Entry(root, width=30)
vehicle_entry.grid(row=1, column=1, padx=20, pady=5)

#Parking List
tk.Label(root,text="Parked Vehicles").grid(row=2, column=0, sticky="nw", padx=20, pady=5)

parking_box = tk.Listbox(root, height=8, width=30)
parking_box.grid(row=2, column=1, padx=20, pady=5)

#Waiting Queue
tk.Label(root,text="Waiting Queue").grid(row=3, column=0, sticky="nw", padx=20, pady=5)

waiting_box = tk.Listbox(root, height=8, width=30)
waiting_box.grid(row=3, column=1, padx=20, pady=5)

#Park Vehicle
def park_vehicle():
    vehicle = vehicle_entry.get().upper()
    if vehicle == "":
        messagebox.showwarning(
            "Warning",
            "Enter vehicle number.")
    elif vehicle in parking or vehicle in waiting:
        messagebox.showwarning("Warning","Vehicle already exists.")
        
    elif len(parking) < capacity:
        parking.append(vehicle)
        parking_box.insert(tk.END, vehicle)

        messagebox.showinfo("Success","Vehicle parked successfully.")
        vehicle_entry.delete(0, tk.END)
    else:
        waiting.append(vehicle)
        waiting_box.insert(tk.END, vehicle)

        messagebox.showinfo(
            "Parking Full","Parking is full.\n""Vehicle added to waiting queue.")
        vehicle_entry.delete(0, tk.END)

#Remove Vehicle
def remove_vehicle():
    vehicle = vehicle_entry.get().upper()
    if vehicle == "":
        messagebox.showwarning("Warning","Enter vehicle number.")
    elif vehicle in parking:
        parking.remove(vehicle)

        #Remove vehicle from parking Listbox
        position = parking_box.get(0, tk.END).index(vehicle)
        parking_box.delete(position)
        messagebox.showinfo("Success","Vehicle removed from parking.")
        
        #Move first waiting vehicle
        if len(waiting) > 0:

            next_vehicle = waiting.pop(0)
            parking.append(next_vehicle)

            waiting_box.delete(0)
            parking_box.insert(tk.END, next_vehicle)

            messagebox.showinfo("Vehicle Moved",next_vehicle +" moved from waiting queue.")
        vehicle_entry.delete(0, tk.END)
    elif vehicle in waiting:

        waiting.remove(vehicle)

        position = waiting_box.get(0, tk.END).index(vehicle)
        waiting_box.delete(position)

        messagebox.showinfo("Success","Vehicle removed from waiting queue.")
        vehicle_entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Not Found","Vehicle not found.")

#Display Parking
def display_parking():
    
    if len(parking) == 0:
        messagebox.showinfo("Parking","Parking lot is empty.")

    else:

        info = "----- PARKED VEHICLES -----\n\n"
        for vehicle in parking:
            info += vehicle + "\n"
        messagebox.showinfo("Parking",info)

#Display Waiting Queue
def display_waiting():

    if len(waiting) == 0:
        messagebox.showinfo("Waiting Queue","No vehicles waiting.")

    else:
        info = "----- WAITING QUEUE -----\n\n"
        for vehicle in waiting:
            info += vehicle + "\n"
        messagebox.showinfo("Waiting Queue",info)

#Exit
def exit_program():
    root.destroy()

#Buttons
tk.Button(root,text="Park Vehicle",width=20,command=park_vehicle).grid(row=4, column=0, padx=10, pady=8)

tk.Button(root,text="Remove Vehicle",width=20,command=remove_vehicle).grid(row=4, column=1, padx=10, pady=8)

tk.Button(root,text="Display Parking",width=20,command=display_parking).grid(row=5, column=0, padx=10, pady=8)

tk.Button(root,text="Display Waiting Queue",width=20,command=display_waiting).grid(row=5, column=1, padx=10, pady=8)

tk.Button(root,text="Exit",width=20,command=exit_program).grid(row=6, column=0, columnspan=2, pady=10)

#File Menu
file_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Exit",command=exit_program)

#Start Application
root.mainloop()
