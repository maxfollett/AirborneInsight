from tkinter import filedialog as fd
from tkinter import simpledialog
import pandas as pd
import numpy as np
import tkinter as tk

def GetInputs():
    # Create a root window to initialize Tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt for file paths for Survey 1 and Survey 2
    data_path1 = fd.askopenfilename(filetypes=[('CSV files', '*.csv')], title='Provide location of Survey 1')
    if not data_path1:
        raise FileNotFoundError("No file given or it no longer exists")

    data_path2 = fd.askopenfilename(filetypes=[('CSV files', '*.csv')], title='Provide location of Survey 2')
    if not data_path2:
        raise FileNotFoundError("No file given or it no longer exists")

    # Function to ask for integer input with a default value
    def ask_for_value(title, prompt, default):
        param = simpledialog.askstring(title, prompt)
        try:
            return int(param) if param is not None else default
        except ValueError:
            print(f"Invalid input, using default {default}")
            return default

    # Get patch size, number of grid points, and EPSG code from user
    studyarealength = ask_for_value(
        "Please Provide a Patch Size",
        "Please enter an integer value or dismiss this window to use the default value of 50",
        50
    )
    
    xlength = ask_for_value(
        "Please Provide a Number of Grid Points",
        "Please enter an integer value or dismiss this window to use the default value of 1000",
        1000
    )

    epsg_code = ask_for_value(
        "Please Provide an EPSG Code",
        "Please enter an integer value or dismiss this window to use the default value of 0",
        0
    )

    # Get interpolation method from user
    interp_method = None
    while True:
        interp_method = simpledialog.askstring(
            "Interpolation Method",
            "Type 0 for nearest, 1 for linear, 2 for cubic. This will reprompt until a valid value is given."
        )
        if interp_method in {'0', '1', '2'}:
            interp_method = 'nearest' if interp_method == '0' else 'linear' if interp_method == '1' else 'cubic'
            break

    # Get Landsat option from user
    landsat_selector = None
    while True:
        landsat_selector = simpledialog.askstring(
            "Landsat ON or OFF",
            "Type 0 for OFF, 1 for ON. This will reprompt until a valid value is given."
        )
        if landsat_selector in {'0', '1'}:
            break

    # Create a dictionary to store the collected inputs
    data_ = {
        'data_path1': data_path1,
        'data_path2': data_path2,
        'studyarealength': studyarealength,
        'xlength': xlength,
        'epsg_code': epsg_code,
        'interp_method': interp_method,
        'landsat_selector': landsat_selector
    }

    return data_

# Run the function to get inputs
inputs = GetInputs()
print(inputs)

import warnings
warnings.filterwarnings("ignore")

