import os.path
import tkinter
from tkinter import ttk
from tkinter import filedialog as fd
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
from tkinter import messagebox

mainWindow = tkinter.Tk()
mainWindow.title("Wave App")
mainWindow.geometry("800x500")
tabControl = ttk.Notebook(mainWindow)
readSignalTab = ttk.Frame(tabControl)
createSignalTab = ttk.Frame(tabControl)
tabControl.add(readSignalTab, text="Read Signal")
tabControl.add(createSignalTab, text="Create Signal")
tabControl.pack(expand=1, fill="both")
# -------------------------------Read Signal-------------------------

openSignalDirectory = tkinter.Text(readSignalTab, height=0, width=85)
openSignalDirectory.place(x=0, y=20)

dirc = ""
radio_var = tkinter.IntVar(value=0)
discrete_radio_button = tkinter.Radiobutton(readSignalTab, text="Discrete", variable=radio_var, value=1)
discrete_radio_button.place(x=20, y=40)
continious_radio_button = tkinter.Radiobutton(readSignalTab, text="Continious", variable=radio_var, value=2)
continious_radio_button.place(x=20, y=60)


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    if os.path.split(filenames)[1].split('.')[1] != 'txt':
        messagebox.showerror("Error!", "Please select a text file!")
        return
    global dirc
    dirc = os.path.split(filenames)[0] + "/" + os.path.split(filenames)[1]
    openSignalDirectory.insert("1.0", dirc)
    """
    showinfo(
        title='Selected Files',
        message=filenames
    )
    """""


openSignalButton = tkinter.Button(readSignalTab, text="Choose File", command=select_files)
openSignalButton.place(x=700, y=15)

x = []
y = []


def read_signal():
    if dirc == '':
        messagebox.showerror("Error!", "Please choose a file!")
        return

    if radio_var == 0:
        messagebox.showerror("Error!", "Please choose a graph type!")
        return

    print(dirc)
    signalfile = open(dirc, 'r')
    signalfiletext = signalfile.readlines()
    for i in range(3, 2 + int(signalfiletext[2])):
        text = signalfiletext[i]
        text = text.split(" ")
        x.append(float(text[0]))
        y.append(float(text[1]))
    print(x)
    print(y)
    if radio_var.get() == 1:
        plt.figure().clear()
        plt.close()
        plt.cla()
        plt.clf()
        plt.stem(x, y)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.show()
    else:
        if radio_var.get() == 2:
            x_smooth = np.array(x)
            y_smooth = np.array(y)
            x_y_spline = make_interp_spline(x_smooth, y_smooth)
            x_ = np.linspace(x_smooth.min(), x_smooth.max(), 500)
            y_ = x_y_spline(x_)
            plt.figure().clear()
            plt.close()
            plt.cla()
            plt.clf()
            plt.plot(x_, y_)
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.show()


print_signal_button = tkinter.Button(readSignalTab, text="Print Signal", command=read_signal)
print_signal_button.place(x=700, y=50)

# -----------------------------------------------Create Signal----------------------------------------------


tkinter.Label(createSignalTab, text="Wave Type:").place(x=20, y=10)
wave_options = ["Sin","Cos"]
clicked_wave = tkinter.StringVar()
clicked_wave.set("Sin")
wave_menu = tkinter.OptionMenu(createSignalTab, clicked_wave, *wave_options)
wave_menu.place(x=85, y=5)
amplitude_text = tkinter.Text(createSignalTab, height=0, width=10)
tkinter.Label(createSignalTab, text="Amplitude (A):").place(x=20, y=70)
amplitude_text.place(x=110, y=70)
tkinter.Label(createSignalTab, text="Phase Shift (Θ):").place(x=20, y=100)
theta_text = tkinter.Text(createSignalTab,height=0, width=10)
theta_text.place(x=110, y=100)
tkinter.Label(createSignalTab, text="Analog Frequency:").place(x=20, y=130)
analog_text = tkinter.Text(createSignalTab, height=0, width=10)
analog_text.place(x=130, y=130)
tkinter.Label(createSignalTab, text="Sampling Frequency:").place(x=20, y=160)
sampling_text = tkinter.Text(createSignalTab, height=0, width=10)
sampling_text.place(x=140, y=160)

mainWindow.mainloop()
