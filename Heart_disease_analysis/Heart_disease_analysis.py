# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:35:58 2022

@author: nikola

Analiza, vizualizacije i obrada bolesti srca

Nikola Banić
"""

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


df = pd.read_csv('input_data/heart.csv') # data frame
nRows, nCol = df.shape
print(f'Broj ispitanika {nRows}, Broj pitanja u anketi {nCol}')

dict = {'age':'Broj godina', 'sex':'Spol', 'cp':'Bol u prsima', 'trestbps':'Tlak', 'chol':'Razina kolesterola' \
        , 'fbs':'Razina šečera', 'restecg':'Ekg', 'thalach':'Max bts' \
        , 'exang':'Angina uslijed tjelovježbe', 'oldpeak':'ST depresija', 'slope':'Nagib ST' \
        , 'ca':'Krvne žile', 'thal':'Povrativost', 'target':'Bolest srca' }

df.rename(columns = dict, inplace = True)

# Preimenovanje data frame-a
df['Spol'].replace([1, 0], ['Muški ispitanici', 'Ženski ispitanici'], inplace = True)
df['Bol u prsima'].replace([0, 1, 2, 3], ['Tipična angina', 'Atipična angina', 'Neanginalna bol', 'Asimptomatska bol'], inplace = True)
df['Razina šečera'].replace([0, 1], ['Ispod 120 mg/dl', 'Iznad 120 mg/dl'], inplace = True)
df['Ekg'].replace([0, 1, 2], ['Normalan', 'ST-T abnormalija', 'Ventikularna hipertrofija'], inplace = True)
df['Angina uslijed tjelovježbe'].replace([0, 1], ['Ne pojavljuje se', 'Pojavljuje se'], inplace = True)
df['Nagib ST'].replace([0, 1, 2], ['Rastući', 'Ravan', 'Padajući'], inplace = True)
df['Povrativost'].replace([0, 1, 2, 3], ['Bez informacija', 'Normalno stanje', 'Stalni defekt', 'Povrativi efekt'], inplace = True)
df['Bolest srca'].replace([0, 1], ['Zdravi ispitanici', 'Bolesni ispitanici'], inplace = True)

cols_1 = ('Bolest srca', 'Spol')
cols_2 = list(df.columns)

# Podijela data frame-a na zdrave i bolesne
zdravi_info = df[df['Bolest srca'] == 'Zdravi ispitanici']
bolesni_info = df[df['Bolest srca'] == 'Bolesni ispitanici']

# Podijela data frame-a na muškarce i žene
M_info = df[df['Spol'] == 'Muški ispitanici']
Z_info = df[df['Spol'] == 'Ženski ispitanici']

def makeplot():
    val_1, val_2 = variable_1.get(), variable_2.get()
    print ("Podjela po: " + val_1)
    print ("Osnovni parametri: " + val_2)
    
    if val_1 == val_2:
        messagebox.showwarning(title = 'Isti parametri', message = 'Parametri ne mogu biti isti, odaberite druge parametre')
        return
    
    if val_1 == 'Bolest srca':
        data = [zdravi_info, bolesni_info]
    else:
        data = [M_info, Z_info]

    CPLOT = ['Spol', 'Bol u prsima', 'Razina šečera', 'Ekg', 'Angina uslijed tjelovježbe', 'Nagib ST', 'Krvne žile', 'Povrativost', 'Bolest srca']
    HPLOT = ['Broj godina', 'Tlak', 'Razina kolesterola', 'Max bts', 'ST depresija']
    Hplot_labels = ['', 'u mirovanju', 'u mg/dl', 'Maksimalan ostvaren tlak', '']

    
    fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (10, 8))
    fig.tight_layout(pad = 4)
    for i in range(len(HPLOT)):
        for j in range(2):
                if val_2 == HPLOT[i]:
                    fig = sns.histplot(data = data[j], x = val_2, bins = 40, ax = axes[j], kde = True)
                    if val_1 == 'Bolest srca':
                        title = f'Raspodjela ispitanika na zdrave i bolesne s obzirom na parametar {val_2}'
                        plt.suptitle(f'Raspodjela ispitanika na zdrave i bolesne s obzirom na parametar: {val_2}')
                        axes[0].set_title(f'Zdravi ispitanici s obzirom na paremetar: {val_2}')
                        axes[1].set_title(f'Bolesni ispitanici s obzirom na paremetar: {val_2}')
                        axes[0].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                        axes[1].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                        axes[0].set_ylabel('Broj zdravih ispitanika')
                        axes[1].set_ylabel('Broj bolesnih ispitanika')
                        axes[j].legend(['KDE',val_2])
                    else:
                        title = f'Raspodjela ispitanika na muškarce i žene s obzirom na parametar {val_2}'
                        plt.suptitle(f'Raspodjela ispitanika na muškarce i žene s obzirom na parametar: {val_2}')
                        axes[0].set_title(f'Muški ispitanici s obzirom na paremetar: {val_2}')
                        axes[1].set_title(f'Ženski ispitanici s obzirom na paremetar: {val_2}')
                        axes[0].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                        axes[1].set_xlabel(f'{val_2} {Hplot_labels[i]}')
                        axes[0].set_ylabel('Broj muških ispitanika')
                        axes[1].set_ylabel('Broj ženskih ispitanika')
                        axes[j].legend(['KDE',val_2])

                    plt.show()
                        
    for i in range(len(CPLOT)):
        for j in range(2):
                if val_2 == CPLOT[i]:
                    fig = sns.countplot(data = data[j], x = val_2, ax = axes[j])
                    if val_1 == 'Bolest srca':
                        title = f'Raspodjela ispitanika na zdrave i bolesne s obzirom na parametar {val_2}'
                        plt.suptitle(f'Raspodjela ispitanika na zdrave i bolesne s obzirom na parametar: {val_2}')
                        axes[0].set_title(f'Zdravi ispitanici s obzirom na paremetar: {val_2}')
                        axes[1].set_title(f'Bolesni ispitanici s obzirom na paremetar: {val_2}')
                        axes[0].set_ylabel('Broj zdravih ispitanika')
                        axes[1].set_ylabel('Broj bolesnih ispitanika')
                        if val_2 == 'Krvne žile':
                            axes[0].set_xlabel('Broj krvnih žila objane postupkom floroskopije')
                            axes[1].set_xlabel('Broj krvnih žila objane postupkom floroskopije')
                    else:
                        title = f'Raspodjela ispitanika na muškarce i žene s obzirom na parametar {val_2}'
                        plt.suptitle(f'Raspodjela ispitanika na muškarce i žene s obzirom na parametar: {val_2}')
                        axes[0].set_title(f'Muški ispitanici s obzirom na paremetar: {val_2}')
                        axes[1].set_title(f'Ženski ispitanici s obzirom na paremetar: {val_2}')
                        axes[0].set_ylabel('Broj muških ispitanika')
                        axes[1].set_ylabel('Broj ženskih ispitanika')
                        if val_2 == 'Krvne žile':
                            axes[0].set_xlabel('Broj krvnih žila objane postupkom floroskopije')
                            axes[1].set_xlabel('Broj krvnih žila objane postupkom floroskopije')
                        
                    plt.show()
                        
    if (clicker == 1):
        plt.savefig(f'{title}.png', dpi = 300)
        plt.close()
        messagebox.showinfo(title = 'Informacija', message = f'Odabrani graf je spremljen')
        
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
    if val_1 == 'Bolest srca':
        ime_txt = 'zdravih i bolesnih'
        data = [zdravi_info, bolesni_info]
        S_info = []
        for i in range(2):
            podjela = ['zdravih', 'bolesnih']
            S_info.append(data[i][val_2].describe(include = all))
            text.insert(INSERT, f'Statističke informacije {podjela[i]} ispitanika \nParametar: {val_2}\n')
            text.insert(INSERT, f'\n{S_info[i]} \n\n')
    else:
        ime_txt = 'muških i ženskih'
        data = [M_info, Z_info]
        S_info = []
        for i in range(2):
            podjela = ['muških', 'ženskih']
            S_info.append(data[i][val_2].describe(include = all))
            text.insert(INSERT, f'Statističke informacije {podjela[i]} ispitanika \nParametar: {val_2}\n')
            text.insert(INSERT, f'\n{S_info[i]} \n\n')
            
    if (clicker_txt == 1):
        text_file = open(f'Statistika {ime_txt} ispitanika o parametru {val_2}.txt', 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()
        messagebox.showinfo(title = 'Informacija', message = f'Odabrana statistika je spremljena')
        
    clicker = 0


def savetxt():
    global clicker_txt
    clicker_txt = 1
    stats()
    clicker_txt = 0

clicker_txt = 0

def delete_txt():
    text.delete(1.0, END)

def close():
    plt.close('all')
    
def exit():
    window.destroy()
    print('Aplikacija je ugašena')
    
window = Tk()
window.title('Analiza i vizualizacija bolesti srca')
window.geometry("1000x700")

image1 = Image.open('slika.png')
image1 = image1.resize((150, 150))
test = ImageTk.PhotoImage(image1)
label_img = Label(image = test)
label_img.image = test

label_img.place(x = 800, y = 0)

lbl_1 = Label(window, text = 'Podjela ispitanika po parametru:')
lbl_2 = Label(window, text = 'Prikaz ispitanika po parametru:')
label_title = Label(window, text = 'Analiza i vizualizacija \nbolesti srca', font = 22)

variable_1 = StringVar(window)
variable_1.set(cols_1[0]) 
variable_2 = StringVar(window)
variable_2.set(cols_2[0]) 

# Drop down menu 1 i 2
DD1 = OptionMenu(window, variable_1, *cols_1)
DD2 = OptionMenu(window, variable_2, *cols_2)

DD1width = len(max(cols_1, key=len))
DD2width = len(max(cols_2, key=len))
lbl_1.pack()
lbl_1.place(x = 35, y = 10)
DD1.pack()
DD1.place(x = 35, y = 35)
DD1.config(width = DD2width)
lbl_2.pack()
lbl_2.place(x = 35, y = 85)
DD2.pack()
DD2.place(x = 35, y = 110)
DD2.config(width = DD2width)
label_title.pack()
label_title.place(x = 430, y = 35)

button_plot = Button(master = window, text="Nacrtaj graf", activebackground = "green", command = makeplot)
button_plot.pack()
button_plot.place(x = 775 , y = 160)
button_plot.config(width = DD2width, height = 10)

button_save = Button(master = window, text = 'Spremi graf ', activebackground = "yellow", command = saveimage)
button_save.pack()
button_save.place(x = 775, y = 340)
button_save.config(width = DD2width, height = 10)

button_stats = Button(master = window, text = 'Ispiši statističke informacije', activebackground = "green", command = stats)
button_stats.pack()
button_stats.place(x = 35, y = 160)
button_stats.config(width = DD2width, height = 10)

button_txt = Button(master = window, text = 'Spremi statističke informacije', activebackground = "yellow", command = savetxt)
button_txt.pack()
button_txt.place(x = 35, y = 340)
button_txt.config(width = DD2width, height = 10)

button_delete_txt = Button(master = window, text = 'Izbriši ispisani text', activebackground = "orange", command = delete_txt)
button_delete_txt.pack()
button_delete_txt.place(x = 400, y = 575)
button_delete_txt.config(width = DD2width)

button_close = Button(master = window, text = 'Zatvori sve grafove', activebackground = "orange", command = close)
button_close.pack()
button_close.place(x = 775, y = 515)
button_close.config(width = DD2width)

button_exit = Button(master = window, text = 'Ugasni aplikaciju', command = exit)
button_exit.pack()
button_exit.place(x = 850, y = 650)
button_exit.config(width = 15)

# Dodavanje teksta
text = Text(master = window, width = 60, height = 40)

text.bindtags((str(text), str(window), "all"))
text.pack(pady = 150)
window.resizable(False, False)
window.mainloop()

