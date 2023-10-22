# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:35:58 2022

@author: nikola

Analysis, Visualization, and Processing of Heart Disease Data

Nikola Banić
"""

# Import necessary libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Read heart disease data from a CSV file into a data frame
df = pd.read_csv('input_data/heart.csv')
nRows, nCol = df.shape
print(f'Number of subjects {nRows}, Number of survey questions {nCol}')

# Create a dictionary to rename columns for better readability
column_dict = {
    'age': 'Age', 'sex': 'Sex', 'cp': 'Chest Pain Type', 'trestbps': 'Blood Pressure', 'chol': 'Cholesterol Level',
    'fbs': 'Fasting Blood Sugar', 'restecg': 'ECG Results', 'thalach': 'Max Heart Rate',
    'exang': 'Exercise-Induced Angina', 'oldpeak': 'ST Depression', 'slope': 'ST Slope',
    'ca': 'Number of Major Vessels', 'thal': 'Thalassemia', 'target': 'Heart Disease'
}


# Rename columns in the data frame using the dictionary
df.rename(columns=column_dict, inplace=True)

# Rename categorical values for better understanding
df['Sex'].replace([1, 0], ['Male', 'Female'], inplace=True)
df['Chest Pain Type'].replace([0, 1, 2, 3],
    ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic Pain'], inplace=True)
df['Fasting Blood Sugar'].replace([0, 1], ['Below 120 mg/dl', 'Above 120 mg/dl'], inplace=True)
df['ECG Results'].replace([0, 1, 2], ['Normal', 'ST-T Abnormality', 'Ventricular Hypertrophy'], inplace=True)
df['Exercise-Induced Angina'].replace([0, 1], ['Absent', 'Present'], inplace=True)
df['ST Slope'].replace([0, 1, 2], ['Upsloping', 'Flat', 'Downsloping'], inplace=True)
df['Thalassemia'].replace([0, 1, 2, 3], ['No Information', 'Normal', 'Fixed Defect', 'Reversible Defect'], inplace=True)
df['Heart Disease'].replace([0, 1], ['Healthy Subjects', 'Diseased Subjects'], inplace=True)

# Define column categories for further analysis
cols_1 = ('Heart Disease', 'Sex')
cols_2 = list(df.columns)

# Split the data frame into healthy and diseased subjects
healthy_info = df[df['Heart Disease'] == 'Healthy Subjects']
diseased_info = df[df['Heart Disease'] == 'Diseased Subjects']

# Split the data frame into male and female subjects
male_info = df[df['Sex'] == 'Male']
female_info = df[df['Sex'] == 'Female']

def makeplot():
    val_1, val_2 = variable_1.get(), variable_2.get()
    print("Split by: " + val_1)
    print("Primary parameters: " + val_2)
    
    if val_1 == val_2:
        messagebox.showwarning(title='Same Parameters', message='Parameters cannot be the same, please choose different parameters')
        return
    
    if val_1 == 'Heart Disease':
        data = [healthy_info, diseased_info]
    else:
        data = [male_info, female_info]

    CPLOT = ['Sex', 'Chest Pain Type', 'Fasting Blood Sugar', 'ECG Results', 'Exercise-Induced Angina', 'ST Slope', 'Number of Major Vessels', 'Thalassemia', 'Heart Disease']
    HPLOT = ['Age', 'Blood Pressure', 'Cholesterol Level', 'Max Heart Rate', 'ST Depression']
    Hplot_labels = ['', 'at Rest', 'in mg/dl', 'Max Achieved Blood Pressure', '']

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
    fig.tight_layout(pad=4)
    
    for i in range(len(HPLOT)):
        for j in range(2):
            if val_2 == HPLOT[i]:
                fig = sns.histplot(data=data[j], x=val_2, bins=40, ax=axes[j], kde=True)
                if val_1 == 'Heart Disease':
                    title = f'Distribution of subjects for healthy and diseased based on the parameter {val_2}'
                    plt.suptitle(f'Distribution of subjects for healthy and diseased based on parameter: {val_2}')
                    axes[0].set_title(f'Healthy subjects based on parameter: {val_2}')
                    axes[1].set_title(f'Diseased subjects based on parameter: {val_2}')
                    axes[0].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                    axes[1].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                    axes[0].set_ylabel('Number of healthy subjects')
                    axes[1].set_ylabel('Number of diseased subjects')
                    axes[j].legend(['KDE', val_2])
                else:
                    title = f'Distribution of subjects for male and female based on the parameter {val_2}'
                    plt.suptitle(f'Distribution of subjects for male and female based on parameter: {val_2}')
                    axes[0].set_title(f'Male subjects based on parameter: {val_2}')
                    axes[1].set_title(f'Female subjects based on parameter: {val_2}')
                    axes[0].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                    axes[1].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                    axes[0].set_ylabel('Number of male subjects')
                    axes[1].set_ylabel('Number of female subjects')
                    axes[j].legend(['KDE', val_2])

                plt.show()
                        
    for i in range(len(CPLOT)):
        for j in range(2):
            if val_2 == CPLOT[i]:
                fig = sns.countplot(data=data[j], x=val_2, ax=axes[j])
                if val_1 == 'Heart Disease':
                    title = f'Distribution of subjects for healthy and diseased based on the parameter {val_2}'
                    plt.suptitle(f'Distribution of subjects for healthy and diseased based on parameter: {val_2}')
                    axes[0].set_title(f'Healthy subjects based on parameter: {val_2}')
                    axes[1].set_title(f'Diseased subjects based on parameter: {val_2}')
                    axes[0].set_ylabel('Number of healthy subjects')
                    axes[1].set_ylabel('Number of diseased subjects')
                    if val_2 == 'Number of Major Vessels':
                        axes[0].set_xlabel('Number of major vessels determined by fluoroscopy')
                        axes[1].set_xlabel('Number of major vessels determined by fluoroscopy')
                else:
                    title = f'Distribution of subjects for male and female based on the parameter {val_2}'
                    plt.suptitle(f'Distribution of subjects for male and female based on parameter: {val_2}')
                    axes[0].set_title(f'Male subjects based on parameter: {val_2}')
                    axes[1].set_title(f'Female subjects based on parameter: {val_2}')
                    axes[0].set_ylabel('Number of male subjects')
                    axes[1].set_ylabel('Number of female subjects')
                    if val_2 == 'Number of Major Vessels':
                        axes[0].set_xlabel('Number of major vessels determined by fluoroscopy')
                        axes[1].set_xlabel('Number of major vessels determined by fluoroscopy')
                    
                plt.show()
                        
    if (clicker == 1):
        plt.savefig(f'{title}.png', dpi=300)
        plt.close()
        messagebox.showinfo(title='Information', message='Selected plot has been saved')



        
def saveimage():
    global clicker
    clicker = 1
    makeplot()
    clicker = 0

clicker = 0

def stats():
    global clicker
    clicker = 1
    if (clicker == 1):
        text.delete(1.0, END)
    val_1, val_2 = variable_1.get(), variable_2.get()
    if val_1 == 'Heart Disease':
        group_name = 'healthy and diseased'
        data = [healthy_info, diseased_info]
        S_info = []
        for i in range(2):
            division = ['healthy', 'diseased']
            S_info.append(data[i][val_2].describe(include='all'))
            text.insert(INSERT, f'Statistical Information for {division[i]} Subjects \nParameter: {val_2}\n')
            text.insert(INSERT, f'\n{S_info[i]} \n\n')
    else:
        group_name = 'male and female'
        data = [male_info, female_info]
        S_info = []
        for i in range(2):
            division = ['male', 'female']
            S_info.append(data[i][val_2].describe(include='all'))
            text.insert(INSERT, f'Statistical Information for {division[i]} Subjects \nParameter: {val_2}\n')
            text.insert(INSERT, f'\n{S_info[i]} \n\n')
            
    if (clicker_txt == 1):
        text_file = open(f'Statistics for {group_name} Subjects on Parameter {val_2}.txt', 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()
        messagebox.showinfo(title='Information', message=f'Selected statistics have been saved')
        
    clicker = 0



def save_text():
    global clicker_txt
    clicker_txt = 1
    stats()
    clicker_txt = 0

clicker_txt = 0

def delete_text():
    text.delete(1.0, END)

def close_plots():
    plt.close('all')

def exit_app():
    window.destroy()
    print('Application has been closed')

window = Tk()
window.title('Analysis and Visualization of Heart Disease')
window.geometry("1000x700")

image1 = Image.open('image.png')
image1 = image1.resize((150, 150))
image = ImageTk.PhotoImage(image1)
image_label = Label(image=image)
image_label.image = image

image_label.place(x=800, y=0)

label_1 = Label(window, text='Split subjects by parameter:')
label_2 = Label(window, text='Display subjects by parameter:')
label_title = Label(window, text='Analysis and Visualization of Heart Disease', font=22)

variable_1 = StringVar(window)
variable_1.set(cols_1[0]) 
variable_2 = StringVar(window)
variable_2.set(cols_2[0]) 

# Drop-down menu 1 and 2
dropdown_1 = OptionMenu(window, variable_1, *cols_1)
dropdown_2 = OptionMenu(window, variable_2, *cols_2)

DD1width = len(max(cols_1, key=len))
DD2width = len(max(cols_2, key=len))
label_1.pack()
label_1.place(x=35, y=10)
dropdown_1.pack()
dropdown_1.place(x=35, y=35)
dropdown_1.config(width=DD2width)
label_2.pack()
label_2.place(x=35, y=85)
dropdown_2.pack()
dropdown_2.place(x=35, y=110)
dropdown_2.config(width=DD2width)
label_title.pack()
label_title.place(x=430, y=35)


button_plot = Button(master=window, text="Draw Plot", activebackground="green", command=makeplot)
button_plot.pack()
button_plot.place(x=775, y=160)
button_plot.config(width=DD2width, height=10)

button_save = Button(master=window, text='Save Plot', activebackground="yellow", command=saveimage)
button_save.pack()
button_save.place(x=775, y=340)
button_save.config(width=DD2width, height=10)

button_stats = Button(master=window, text='Print Statistical Information', activebackground="green", command=stats)
button_stats.pack()
button_stats.place(x=35, y=160)
button_stats.config(width=DD2width, height=10)

button_txt = Button(master=window, text='Save Statistical Information', activebackground="yellow", command=save_text)
button_txt.pack()
button_txt.place(x=35, y=340)
button_txt.config(width=DD2width, height=10)

button_delete_txt = Button(master=window, text='Delete Printed Text', activebackground="orange", command=delete_text)
button_delete_txt.pack()
button_delete_txt.place(x=400, y=575)
button_delete_txt.config(width=DD2width)

button_close = Button(master=window, text='Close All Plots', activebackground="orange", command=close_plots)
button_close.pack()
button_close.place(x=775, y=515)
button_close.config(width=DD2width)

button_exit = Button(master=window, text='Exit Application', command=exit_app)
button_exit.pack()
button_exit.place(x=850, y=650)
button_exit.config(width=15)

# Adding text
text = Text(master=window, width=60, height=40)

text.bindtags((str(text), str(window), "all"))
text.pack(pady=150)
window.resizable(False, False)
window.mainloop()

