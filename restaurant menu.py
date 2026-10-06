#Import tkinter for GUI and ttk for improved widgets
import tkinter as ttk
from tkinter import ttk, messagebox


#Define the RestaurantManagementApp Class
class RestaurantOrderManagment:
  #Initialize the Application
  def __init__(self, root):
    self.root = root #The main window of the app
    self.root.title(
      "Restaurant Management App") #Set the title of the window

    # A dictionary to store the menu items and their prices
    self.menu_items = {
      "BIRIYANI": 2,
      "STARTERS": 2,
      "NORTH AND SOUTH INDIAN MEALS": 3,
      "MAIN COURSE": 4,
      "DESSERTS": 2.5,
      "BEVERAGES": 1,
    }

    self.exchange_rate = 82 # Exgange rate for currency conversions

    self.setup_background(root) #Set up the background image

    #Create a frame to hold the widgets
    frame = ttk.Frame(root)
    frame.place(relx=0.5, rely=0.5, 
                anchor=ttk.CENTER)#Place it at the center of the window

    #Heading Label
    ttk.Label(frame,
             text="Restaurant Order Management",
             font=("Arial", 20, "bold")).grid(row=0
                                              columnspan=3
                                              padx=10
                                              pady=10))

    self.menu_labels = {} #To store references to menu item labels
    self.menu_quantities = {} #To store references to quantity entry widgets

    #Create labels and entry widgets for each menu item
    for i, (item, price) in enumerate(self.menu_items.items(), start=1):
      label = ttk.Label(frame, text=f"{item} (${price}):", font=("Arial", 12))
      label.grid(row=i, column=0, padx=10, pady=5)


      self.menu_labels[item] = label

      quantity_entry = ttk.Entry(frame, width=5)
      quantity_entry.grid(row=i, column=1, padx=10, pady=5)
      self.menu_quantities[item] = quantity_entry

    #Currency selection
    self. currency_var = tk.StringVar()
    ttk.Label(frame, text="Select Currency:",
              font=("Arial", 12)).grid(row=len(self.menu_items) + 1,
                                       column=0,
                                       padx=10,
                                       pady=5)

    #Dropdown for currency selection
    currency_dropdown = ttk.Combobox(frame,
                                    textvariable=self.currency_var,
                                    state="readonly",
                                    width=18
                                    values=('USD', 'INR'))
    currecy_dropdown.grid
