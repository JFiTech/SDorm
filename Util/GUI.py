"""
    Date: Created on Sunday, March 12 2023 @ 04:40 pm 
    Author: J
    Purpose: GUI development for SDorm (MVP)
"""

'''
EN:
Here we place the libraries that we import.

ES:
Aquí se ubican las bibliotecas (librerías) que importamos.
'''
import datetime
import locale
# import os
# import pandas as pd
# import Pmw
# import re # TODO: Remove if not used
# import requests
# import sys
# import time
import tkinter as tk
import ttkbootstrap as ttkbs
from datetime import date, datetime  # TODO: Remove if not used
# from decimal import Decimal as D
from PIL import Image, ImageTk
from tkinter import (Tk, ttk, messagebox)

'''
EN:
Constants
'''
ARIAL_7 = ("Arial", 7)
ARIAL_8 = ("Arial", 8)
ARIAL_10 = ("Arial", 10)
ARIAL_12 = ("Arial", 12)
DATE_RANGE_ENTRY_MAXIMUM = 5
INDIVIDUAL_DATE_ENTRY_MAXIMUM = 8

'''
EN:
Assigns the language-region so that Python sets up some items 
according to this.
'''
locale.setlocale(locale.LC_ALL, 'es_es')

# -------------------------------- GUI -------------------------------- #
class GUI(Tk):
    def __init__(self):
        '''
        EN:
        - We set up the GUI class' constructor: super().__init__()
        
        - The main window's title: self.title("SDorm")
        
        - The relative path of the main window's icon: 
        self.iconbitmap(r"D:\Ssjcorreac\Documents\Python\School\SDorm\Assets\Icons\bed-icon_ICO.ico")
        (Icon by Free Preloaders on https://freeicons.io)
        
        - Property that doesn't allow the user to resize the main window: 
        self.resizable(0,0)
        
        - We create the main window: self.setupMainWindow()
        '''
        
        super().__init__()
        self.title("SDorm")
        self.iconbitmap(r"D:\Ssjcorreac\Documents\Python\School\SDorm\Assets\Icons\bed-icon_ICO.ico")
        # self.resizable(0,0)
        # self.geometry("1000x500") # wodth x height
        self.setupMainWindow()

    def setupMainWindow(self):
        '''
        EN:
        Sets up the main window where all the elements are gonna be placed.
        '''
        # Main frame - Frame principal
        # frame = ttkbs.Window(themename="darkly")
        frame = tk.Frame(self).grid(padx=15, pady=15)
        
        '''
        EN:
        -- First frame 'Login' --
        '''
        login_form = tk.LabelFrame(frame, text="Inicio de Sesión",
                                    padx=50, pady=10, font=ARIAL_12)
        # login_form = ttkbs.LabelFrame(frame, text="Inicio de Sesión",
        #                             # padx=50, pady=10, font=ARIAL_12,
        #                             bootstyle="primary")
        login_form.grid(row=0, column=0, sticky="news", 
                                        padx=200, pady=100)
        
        '''
        EN:
        'Email' main text box & label.
        '''
        email_label = tk.Label(login_form, text="Email",
                                font=ARIAL_10, state="normal")
        email_label.grid(row=1, column=0, padx=10)
        email_entry = tk.Entry(login_form, 
                                state="normal",
                                textvariable='')
        email_entry.grid(row=1, column=1, padx=20)
        
        '''
        EN:
        'Pasword' main text box & label.
        '''
        password_label = tk.Label(login_form, text="Contraseña",
                                font=ARIAL_10, state="normal")
        password_label.grid(row=2, column=0, padx=10)
        password_entry = tk.Entry(login_form, 
                                state="normal",
                                textvariable='',
                                show="*")
        password_entry.grid(row=2, column=1, padx=20, pady=10)
        
        '''
        EN:
        Shows the login window when pressing the login button.
        '''
        
        def login():
            '''
            EN:
            Shows the find a dorm frame.
            '''
            find_a_dorm_frame = tk.LabelFrame(frame, text="Buscar dormitorio",
                                        padx=50, pady=10, font=ARIAL_12)
            # find_a_dorm_frame = ttkbs.LabelFrame(frame, text="Buscar dormitorio",
            #                             # padx=50, pady=10, font=ARIAL_12,
            #                             bootstyle="primary")
            find_a_dorm_frame.grid(row=0, column=0, sticky="news", 
                                    padx=20, pady=10)
            
            '''
            EN:
            First 'Fechas' label & text box.
            '''
            first_date_label = tk.Label(find_a_dorm_frame, text="Fechas:", 
                                            pady=10, font=ARIAL_10).grid(row=1, column=1)
            
            '''
            EN:
            First calendar entrybox & button.
            '''
            first_calendar_entry = ttkbs.DateEntry(find_a_dorm_frame,
                                                    dateformat='%d-%m-%Y',
                                                    firstweekday=0,
                                                    bootstyle="info")
            first_calendar_entry.grid(row=1, column=2)
            # first_calendar_entry.entry.config(textvariable=self.first_date_field)
            
            '''
            EN:
            'a fechas' label.
            '''
            to_date_label = tk.Label(find_a_dorm_frame, text="a", 
                                    font=ARIAL_10)
            to_date_label.grid(row=1, column=3, padx=20)
            '''
            EN:
            Second calendar entrybox & button.
            '''
            second_calendar_entry = ttkbs.DateEntry(find_a_dorm_frame,
                                                    dateformat='%d-%m-%Y',
                                                    firstweekday=0,
                                                    bootstyle="info")
            second_calendar_entry.grid(row=1, column=4)
            # second_calendar_entry.entry.config(textvariable=second_date_field)
            
            def search_dorm():
                '''
                EN:
                Shows the dorms when clicking on the search button.
                '''
                first_dorm_frame = tk.LabelFrame(find_a_dorm_frame)
                first_dorm_frame.grid(row=2, column=1, sticky="news", 
                                        pady=10)
                
                # -- First Dorm image --
                # Open the image
                first_dorm_image = Image.open(r"..\Assets\Dorm-Images\Dorm-1.jpeg")
                # Resize the image
                first_dorm_image_resized = first_dorm_image.resize((150, 150), Image.LANCZOS)
                # Create an object of tkinter ImageTk
                first_dorm_image_2_display = ImageTk.PhotoImage(first_dorm_image_resized)
                # Create a Label Widget to display the image
                first_dorm_image_label = tk.Label(first_dorm_frame, image=first_dorm_image_2_display)
                first_dorm_image_label.grid(row=2, column=0)
                
                # -- First Dorm image info label --
                first_dorm_image_info = tk.Label(find_a_dorm_frame, 
                                                    text="Ciudad: Medellín\nServicios:\n-WiFi\n-Baño privado", 
                                                    font=ARIAL_10)
                first_dorm_image_info.grid(row=2, column=2, padx=20)
                
                '''
                EN:
                See more info about the first dorm button
                # Search icon from https://freeicons.io/profile/3
                '''
                self.see_dorm_1_icon = tk.PhotoImage(file=r"..\Assets\Icons\see-more-icon.png")
                search_button = ttkbs.Button(find_a_dorm_frame, text="    Ver más\ninformación",
                                                image=self.see_dorm_1_icon,
                                                compound="right",
                                                width=15,
                                                # style="my.TButton",
                                                bootstyle="success-outline",
                                                command='')
                search_button.grid(row=3, column=1) 
                
                extra_pad = tk.Label(find_a_dorm_frame, text=" ")
                extra_pad.grid(row=2, column=3)
                
                # -- Second Dorm image --
                # Open the image
                second_dorm_image = Image.open(r"..\Assets\Dorm-Images\Dorm-2.jpeg")
                # Resize the image
                second_dorm_image_resized = second_dorm_image.resize((150, 150), Image.LANCZOS)
                # Create an object of tkinter ImageTk
                second_dorm_image_2_display = ImageTk.PhotoImage(second_dorm_image_resized)
                # Create a Label Widget to display the image
                second_dorm_image_label = tk.Label(first_dorm_frame, image=second_dorm_image_2_display)
                second_dorm_image_label.grid(row=2, column=4)
                
                # -- Second Dorm image info label --
                second_dorm_image_info = tk.Label(find_a_dorm_frame, 
                                                    text="Ciudad: Bello\nServicios:\n-WiFi\n-TV", 
                                                    font=ARIAL_10)
                second_dorm_image_info.grid(row=2, column=5, padx=20)
                '''
                EN:
                See more info about the first dorm button
                # Search icon from https://freeicons.io/profile/3
                '''
                self.see_dorm_2_icon = tk.PhotoImage(file=r"..\Assets\Icons\see-more-icon.png")
                search_button = ttkbs.Button(find_a_dorm_frame, text="    Ver más\ninformación",
                                                image=self.see_dorm_2_icon,
                                                compound="right",
                                                width=15,
                                                # style="my.TButton",
                                                bootstyle="success-outline",
                                                command='')
                search_button.grid(row=3, column=5) 
            
            '''
            EN:
            'Search dorm' button with icon.
            # Search icon from https://freeicons.io/profile/714
            '''
            self.search_icon = tk.PhotoImage(file=r"..\Assets\Icons\search-icon.png")
            search_button = ttkbs.Button(find_a_dorm_frame, text="Buscar",
                                            image=self.search_icon,
                                            compound="right",
                                            width=15,
                                            # style="my.TButton",
                                            bootstyle="primary-outline",
                                            command=search_dorm)
            search_button.grid(row=1, column=5, padx=20)
            
        
        '''
        EN:
        'Login' button with icon.
        # Login icon from https://icons8.com
        '''
        self.login_icon = tk.PhotoImage(file=r"..\Assets\Icons\login-16.png")
        login_button = ttkbs.Button(login_form, text="Iniciar sesión",
                                        image=self.login_icon,
                                        compound="right",
                                        width=20,
                                        # style="my.TButton",
                                        bootstyle="primary",
                                        command=login)
        login_button.grid(row=3, column=1, padx=20, pady=20)
        
        '''
        EN:
        'Sign up' button with icon.
        Icon by https://freeicons.io/profile/714
        '''
        self.register_icon = tk.PhotoImage(file=r"..\Assets\Icons\signup-icon.png")
        register_button = ttkbs.Button(login_form, text="Registrarse",
                                        image=self.register_icon,
                                        compound="right",
                                        width=20,
                                        # style="my.TButton",
                                        bootstyle="info-outline",
                                        command='')
        register_button.grid(row=4, column=1, padx=20, pady=10)
        
        
        
        
'''
EN:
This tells the human reader if the file's a script and if you can run it.
Otherwise if it doesn't have it, it'll say that it's a library that's gonna be imported.
'''
if __name__ == "__main__":
    app = GUI()
    app.mainloop()