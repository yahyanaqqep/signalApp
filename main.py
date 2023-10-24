import math
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
continious_radio_button = tkinter.Radiobutton(readSignalTab, text="Continuous", variable=radio_var, value=2)
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

    signalfile = open(dirc, 'r')
    signalfiletext = signalfile.readlines()
    for i in range(3, 2 + int(signalfiletext[2])):
        text = signalfiletext[i]
        text = text.split(" ")
        x.append(float(text[0]))
        y.append(float(text[1]))
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
wave_options = ["Sin", "Cos"]
clicked_wave = tkinter.StringVar()
clicked_wave.set("Sin")
wave_menu = tkinter.OptionMenu(createSignalTab, clicked_wave, *wave_options)
wave_menu.place(x=85, y=5)
amplitude_text = tkinter.Text(createSignalTab, height=0, width=10)
tkinter.Label(createSignalTab, text="Amplitude (A):").place(x=20, y=70)
amplitude_text.place(x=110, y=70)
tkinter.Label(createSignalTab, text="Phase Shift (Θ):").place(x=20, y=100)
theta_text = tkinter.Text(createSignalTab, height=0, width=10)
theta_text.place(x=110, y=100)
tkinter.Label(createSignalTab, text="Analog Frequency:").place(x=20, y=130)
analog_text = tkinter.Text(createSignalTab, height=0, width=10)
analog_text.place(x=130, y=130)
tkinter.Label(createSignalTab, text="Sampling Frequency:").place(x=20, y=160)
sampling_text = tkinter.Text(createSignalTab, height=0, width=10)
sampling_text.place(x=140, y=160)


# ----------------------------Second Signal-------------------------


def activate_second_signal():
    if dual_signal_on.get() == 1:
        wave_type_label_2.pack()
        wave_menu_2.pack()
        amplitude_text_2.pack()
        amplitude_label_2.pack()
        phase_shift_label_2.pack()
        theta_text_2.pack()
        analog_frequency_label_2.pack()
        analog_text_2.pack()
        sampling_label_2.pack()
        sampling_text_2.pack()
        wave_type_label_2.place(x=220, y=10)
        wave_menu_2.place(x=285, y=5)
        amplitude_text_2.place(x=310, y=70)
        amplitude_label_2.place(x=220, y=70)
        phase_shift_label_2.place(x=220, y=100)
        theta_text_2.place(x=310, y=100)
        analog_frequency_label_2.place(x=220, y=130)
        analog_text_2.place(x=330, y=130)
        sampling_label_2.place(x=220, y=160)
        sampling_text_2.place(x=340, y=160)
    elif dual_signal_on.get() == 0:
        wave_type_label_2.pack_forget()
        wave_menu_2.pack_forget()
        amplitude_text_2.pack_forget()
        amplitude_label_2.pack_forget()
        phase_shift_label_2.pack_forget()
        theta_text_2.pack_forget()
        analog_frequency_label_2.pack_forget()
        analog_text_2.pack_forget()
        sampling_label_2.pack_forget()
        sampling_text_2.pack_forget()
        wave_type_label_2.place_forget()
        wave_menu_2.place_forget()
        amplitude_text_2.place_forget()
        amplitude_label_2.place_forget()
        phase_shift_label_2.place_forget()
        theta_text_2.place_forget()
        analog_frequency_label_2.place_forget()
        analog_text_2.place_forget()
        sampling_text_2.place_forget()
        sampling_label_2.place_forget()


dual_signal_on = tkinter.IntVar()
dual_signal = tkinter.Checkbutton(createSignalTab, variable=dual_signal_on, onvalue=1, offvalue=0,
                                  command=activate_second_signal)
dual_signal.place(x=85, y=35)
tkinter.Label(createSignalTab, text="Two Signals:").place(x=20, y=35)

wave_type_label_2 = tkinter.Label(createSignalTab, text="Wave Type:")
wave_options_2 = ["Sin", "Cos"]
clicked_wave_2 = tkinter.StringVar()
clicked_wave_2.set("Sin")
wave_menu_2 = tkinter.OptionMenu(createSignalTab, clicked_wave_2, *wave_options)
amplitude_text_2 = tkinter.Text(createSignalTab, height=0, width=10)
amplitude_label_2 = tkinter.Label(createSignalTab, text="Amplitude (A):")
phase_shift_label_2 = tkinter.Label(createSignalTab, text="Phase Shift (Θ):")
theta_text_2 = tkinter.Text(createSignalTab, height=0, width=10)
analog_frequency_label_2 = tkinter.Label(createSignalTab, text="Analog Frequency:")
analog_text_2 = tkinter.Text(createSignalTab, height=0, width=10)
sampling_label_2 = tkinter.Label(createSignalTab, text="Sampling Frequency:")
sampling_text_2 = tkinter.Text(createSignalTab, height=0, width=10)
wave_type_label_2.pack_forget()
wave_menu_2.pack_forget()
amplitude_text_2.pack_forget()
amplitude_label_2.pack_forget()
phase_shift_label_2.pack_forget()
theta_text_2.pack_forget()
analog_frequency_label_2.pack_forget()
analog_text_2.pack_forget()
sampling_label_2.pack_forget()
sampling_text_2.pack_forget()


# --------------------------------Second Signal end----------------

def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False


def draw_signal():
    x = []
    y = []
    if (amplitude_text.get(1.0, "end-1c") == '' or theta_text.get(1.0, "end-1c") == ''
            or analog_text.get(1.0, "end-1c") == '' or sampling_text.get(1.0, "end-1c") == ''):
        messagebox.showerror("Error!", "Please complete all fields!")
        return
    if (not str.isdigit(amplitude_text.get(1.0, "end-1c")) or not is_float(theta_text.get(1.0, "end-1c"))
            or not str.isdigit(analog_text.get(1.0, "end-1c")) or not str.isdigit(sampling_text.get(1.0, "end-1c"))):
        messagebox.showerror("Error!", "All fields should be numbers!")
        return
    if float(sampling_text.get(1.0, "end-1c")) < 2 * float(analog_text.get(1.0, "end-1c")):
        messagebox.showerror("Error!", "Sampling Frequency should be at least twice the Analog Frequency!")
        return
    angular_frequency = 2 * np.pi * (float(analog_text.get(1.0, "end-1c"))/float(sampling_text.get(1.0, "end-1c")))
    theta = float(theta_text.get(1.0, "end-1c"))
    amp = float(amplitude_text.get(1.0, 'end-1c'))
    if dual_signal_on.get() == 1:
        if (amplitude_text_2.get(1.0, "end-1c") == '' or theta_text_2.get(1.0, "end-1c") == ''
                or analog_text_2.get(1.0, "end-1c") == '' or sampling_text_2.get(1.0, "end-1c") == ''):
            messagebox.showerror("Error!", "Please complete all fields!")
            return
        if (not str.isdigit(amplitude_text_2.get(1.0, "end-1c")) or not is_float(theta_text_2.get(1.0, "end-1c"))
                or not str.isdigit(analog_text_2.get(1.0, "end-1c")) or not str.isdigit(
                    sampling_text_2.get(1.0, "end-1c"))):
            messagebox.showerror("Error!", "All fields should be numbers!")
            return
        if float(sampling_text_2.get(1.0, "end-1c")) < 2 * float(analog_text_2.get(1.0, "end-1c")):
            messagebox.showerror("Error!", "Sampling Frequency should be at least twice the Analog Frequency!")
            return
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        x_y_spline1 = None
        x_y_spline2 = None
        angular_frequency_2 = 2 * math.pi * (float(analog_text_2.get(1.0, "end-1c"))/float(sampling_text_2.get(1.0, "end-1c")))
        theta_2 = float(theta_text_2.get(1.0, "end-1c"))
        amp = float(amplitude_text_2.get(1.0, "end-1c"))
        if clicked_wave.get() == "Sin":
            for i in range(0, int(sampling_text.get(1.0, "end-1c"))):
                x1.append(i)
                y1.append(amp * math.sin((angular_frequency * i) + theta))
            x1 = np.array(x1)
            y1 = np.array(y1)
            x_y_spline1 = make_interp_spline(x1, y1)
            x1 = np.linspace(x1.min(), x1.max(), 500)
            y1 = x_y_spline1(x1)
        elif clicked_wave.get() == "Cos":
            for i in range(0, int(sampling_text.get(1.0, "end-1c"))):
                x1.append(i)
                y1.append(amp * math.cos((angular_frequency * i) + theta))
            x1 = np.array(x1)
            y1 = np.array(y1)
            x_y_spline1 = make_interp_spline(x1, y1)
            x1 = np.linspace(x1.min(), x1.max(), 500)
            y1 = x_y_spline1(x1)
        if clicked_wave_2.get() == "Sin":
            for i in range(0, int(sampling_text_2.get(1.0, "end-1c"))):
                x2.append(i)
                y2.append(amp * math.sin((angular_frequency_2 * i) + theta_2))
            x2 = np.array(x2)
            y2 = np.array(y2)
            x_y_spline2 = make_interp_spline(x2, y2)
            x2 = np.linspace(x2.min(), x2.max(), 500)
            y2 = x_y_spline2(x2)
        elif clicked_wave_2.get() == "Cos":
            for i in range(0, int(sampling_text_2.get(1.0, "end-1c"))):
                x2.append(i)
                y2.append(amp * math.cos((angular_frequency_2 * i) + theta_2))
            x2 = np.array(x2)
            y2 = np.array(y2)
            x_y_spline2 = make_interp_spline(x2, y2)
            x2 = np.linspace(x2.min(), x2.max(), 500)
            y2 = x_y_spline2(x2)
        # plt.subplot(121)
        plt.plot(x1, y1)
        # plt.subplot(122)
        plt.plot(x2, y2)
        plt.show()

    elif dual_signal_on.get() == 0:
        if clicked_wave.get() == "Sin":
            for i in range(0, int(sampling_text.get(1.0, "end-1c"))):
                x.append(i)
                y.append(amp * math.sin((angular_frequency * i) + theta))
            x_smooth = np.array(x)
            y_smooth = np.array(y)
            x_y_spline = make_interp_spline(x_smooth, y_smooth)
            x_ = np.linspace(x_smooth.min(), x_smooth.max(), 500)
            y_ = x_y_spline(x_)
            plt.plot(x_, y_)
            plt.show()
        elif clicked_wave.get() == "Cos":
            for i in range(0, int(sampling_text.get(1.0, "end-1c"))):
                x.append(i)
                y.append(amp * math.cos((angular_frequency * i) + theta))
            x_smooth = np.array(x)
            y_smooth = np.array(y)
            x_y_spline = make_interp_spline(x_smooth, y_smooth)
            x_ = np.linspace(x_smooth.min(), x_smooth.max(), 500)
            y_ = x_y_spline(x_)
            plt.plot(x_, y_)
            plt.show()


draw_signal_button = tkinter.Button(createSignalTab, text="Draw Signal", command=draw_signal)
draw_signal_button.place(x=80, y=190)

mainWindow.mainloop()
