import math
import os.path
import tkinter
from tkinter import ttk
from tkinter import filedialog as fd
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
from tkinter import messagebox
import comparesignals
from functools import reduce
import operator
import QuanTest1
import QuanTest2
from helper_functions import *
import tksheet
import comparesignal2

mainWindow = tkinter.Tk()
mainWindow.title("Wave App")
mainWindow.geometry("800x500")
tabControl = ttk.Notebook(mainWindow)
readSignalTab = ttk.Frame(tabControl)
createSignalTab = ttk.Frame(tabControl)
arithmeticTab = ttk.Frame(tabControl)
quantizeTab = ttk.Frame(tabControl)
frequencyDomain = ttk.Frame(tabControl)
time_domain_tab = ttk.Frame(tabControl)
tabControl.add(readSignalTab, text="Read Signal")
tabControl.add(createSignalTab, text="Create Signal")
tabControl.add(arithmeticTab, text="Arithmetic Operation")
tabControl.add(quantizeTab, text="Quantize Signal")
tabControl.add(frequencyDomain, text='Frequency Domain')
tabControl.add(time_domain_tab, text='Time Domain')
tabControl.pack(expand=1, fill="both")
# ---------------------------------Read Signal---------------------------

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

# ---------------------------------Read Signal end-----------------------

# ---------------------------------Create Signal-------------------------


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
# ---------------------------------Create Signal end---------------------

# ---------------------------------Second Signal-------------------------


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
# ---------------------------------Second Signal end---------------------

# ---------------------------------Arithmetic Operation------------------
add_sub_directories = []
x_arithmetic = []
y_arithmetic = []


def show_arithmetic():
    global signals_directory
    global x_arithmetic
    global y_arithmetic
    if operation_radio_var.get() == 1:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        for i in range(1, len(signals_directory)):
            file = open(signals_directory[i], 'r')
            file = file.readlines()
            for j in range(3, 2 + int(file[2])):
                text = file[j]
                text = text.split(" ")
                y_arithmetic[j - 3] += float(text[1])
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() == 2:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        for i in range(1, len(signals_directory)):
            file = open(signals_directory[i], 'r')
            file = file.readlines()
            for j in range(3, 2 + int(file[2])):
                text = file[j]
                text = text.split(" ")
                y_arithmetic[j - 3] -= float(text[1])
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() == 3:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        const = float(multiply_signal_const.get(1.0, 'end-1c'))
        for i in range(0, len(y_arithmetic)):
            y_arithmetic[i] *= const
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() == 4:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        for i in range(0, len(y_arithmetic)):
            y_arithmetic[i] = math.pow(y_arithmetic[i], 2)
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() == 5:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        shift = float(multiply_signal_const.get(1.0, 'end-1c'))
        for i in range(0, len(x_arithmetic)):
            if x_arithmetic[i] < 0:
                x_arithmetic[i] -= shift
            elif x_arithmetic[i] > 0:
                x_arithmetic[i] += shift
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() == 6:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        left_max = max(y_arithmetic)
        left_min = min(y_arithmetic)
        left_span = left_max - left_min
        right_span = 0
        right_max = 0
        right_min = 0
        if normalization_radio_variable.get() == 1:
            right_span = 1
            right_max = 1
            right_min = 0
        elif normalization_radio_variable.get() == 2:
            right_span = 2
            right_max = 1
            right_min = -1
        for i in range(0, len(y_arithmetic)):
            y_arithmetic[i] = ((y_arithmetic[i] - left_min) / (left_max - left_min)) * right_span + right_min
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() == 7:
        file = open(signals_directory[0], 'r')
        file = file.readlines()
        for i in range(3, 2 + int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        for i in range(1, len(y_arithmetic)):
            y_arithmetic[i] += y_arithmetic[i - 1]
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()


def show_hide_arithmetic():
    if operation_radio_var.get() == 1 or operation_radio_var.get() == 2:
        choose_signals_button.place(x=500, y=20)
        choose_signals_text.place(x=0, y=20)
        display_signal.place(x=250, y=200)
        multiply_signal_label.place_forget()
        multiply_signal_const.place_forget()
        multiply_signal_file.place_forget()
        choose_multiply.place_forget()
        shift_signal_label.place_forget()
        normalization_radio_one.place_forget()
        normalization_radio_two.place_forget()

    elif operation_radio_var.get() == 3:
        multiply_signal_file.place(x=0, y=20)
        choose_multiply.place(x=500, y=15)
        multiply_signal_const.place(x=60, y=50)
        multiply_signal_label.place(x=0, y=50)
        display_signal.place(x=0, y=80)
        choose_signals_text.place_forget()
        choose_signals_button.place_forget()
        shift_signal_label.place_forget()
        normalization_radio_one.place_forget()
        normalization_radio_two.place_forget()

    elif operation_radio_var.get() == 4:
        multiply_signal_file.place(x=0, y=20)
        choose_multiply.place(x=500, y=15)
        display_signal.place(x=200, y=50)
        multiply_signal_label.place_forget()
        multiply_signal_const.place_forget()
        choose_signals_text.place_forget()
        choose_signals_button.place_forget()
        shift_signal_label.place_forget()
        normalization_radio_one.place_forget()
        normalization_radio_two.place_forget()

    elif operation_radio_var.get() == 5:
        shift_signal_label.place(x=0, y=50)
        display_signal.place(x=0, y=80)
        multiply_signal_file.place(x=0, y=20)
        choose_multiply.place(x=500, y=15)
        multiply_signal_const.place(x=40, y=50)
        choose_signals_text.place_forget()
        choose_signals_button.place_forget()
        multiply_signal_label.place_forget()
        normalization_radio_one.place_forget()
        normalization_radio_two.place_forget()

    elif operation_radio_var.get() == 6:
        multiply_signal_file.place(x=0, y=20)
        choose_multiply.place(x=500, y=15)
        normalization_radio_one.place(x=20, y=40)
        normalization_radio_two.place(x=20, y=60)
        display_signal.place(x=20, y=120)
        choose_signals_text.place_forget()
        choose_signals_button.place_forget()
        multiply_signal_label.place_forget()
        multiply_signal_const.place_forget()
        shift_signal_label.place_forget()

    elif operation_radio_var.get() == 7:
        multiply_signal_file.place(x=0, y=20)
        choose_multiply.place(x=500, y=15)
        display_signal.place(x=20, y=80)
        choose_signals_text.place_forget()
        choose_signals_button.place_forget()
        multiply_signal_label.place_forget()
        multiply_signal_const.place_forget()
        normalization_radio_one.place_forget()
        normalization_radio_two.place_forget()
        shift_signal_label.place_forget()


operation_radio_var = tkinter.IntVar(value=1)
addition_radio_button = tkinter.Radiobutton(arithmeticTab, text="Addition", variable=operation_radio_var, value=1,
                                            command=show_hide_arithmetic)
subtraction_radio_button = tkinter.Radiobutton(arithmeticTab, text="Subtraction", variable=operation_radio_var, value=2,
                                               command=show_hide_arithmetic)
multiplication_radio_button = tkinter.Radiobutton(arithmeticTab, text="Multiplication", variable=operation_radio_var,
                                                  value=3, command=show_hide_arithmetic)
squaring_radio_button = tkinter.Radiobutton(arithmeticTab, text="Squaring", variable=operation_radio_var, value=4,
                                            command=show_hide_arithmetic)
shifting_radio_button = tkinter.Radiobutton(arithmeticTab, text="Shift Signal", variable=operation_radio_var, value=5,
                                            command=show_hide_arithmetic)
normalization_radio_button = tkinter.Radiobutton(arithmeticTab, text="Normalize", variable=operation_radio_var, value=6,
                                                 command=show_hide_arithmetic)
accumulation_radio_button = tkinter.Radiobutton(arithmeticTab, text="Accumulate", variable=operation_radio_var, value=7,
                                                command=show_hide_arithmetic)
operation_radio_label = tkinter.Label(arithmeticTab, text="Operation")
operation_radio_label.place(x=720, y=15)
addition_radio_button.place(x=700, y=40)
subtraction_radio_button.place(x=700, y=60)
multiplication_radio_button.place(x=700, y=80)
squaring_radio_button.place(x=700, y=100)
shifting_radio_button.place(x=700, y=120)
normalization_radio_button.place(x=700, y=140)
accumulation_radio_button.place(x=700, y=160)
multiply_signal_const = tkinter.Text(arithmeticTab, height=0, width=20)
multiply_signal_label = tkinter.Label(arithmeticTab, text="Constant")
multiply_signal_file = tkinter.Text(arithmeticTab, height=0, width=60)

signals_directory = []


def select_signals():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    # if os.path.split(filenames)[1].split('.')[1] != 'txt':
    #     messagebox.showerror("Error!", "Please select a text file!")
    #     return
    global signals_directory
    if operation_radio_var.get() == 1 or operation_radio_var.get() == 2:
        for i in range(0, len(filenames)):
            signals_directory.append(os.path.split(filenames[i])[0] + "/" + os.path.split(filenames[i])[1])
            choose_signals_text.insert('1.0', signals_directory[i])
    else:
        for i in range(0, len(filenames)):
            signals_directory.append(os.path.split(filenames[i])[0] + "/" + os.path.split(filenames[i])[1])
            multiply_signal_file.insert('1.0', signals_directory[i])


choose_multiply = tkinter.Button(arithmeticTab, text="Choose Signal", command=select_signals)
choose_signals_button = tkinter.Button(arithmeticTab, text="Choose signal(s)", command=select_signals)
choose_signals_text = tkinter.Text(arithmeticTab, height=10, width=60)
display_signal = tkinter.Button(arithmeticTab, text="Show Signal", command=show_arithmetic)
choose_signals_button.place(x=500, y=20)
choose_signals_text.place(x=0, y=20)
display_signal.place(x=250, y=200)

shift_signal_label = tkinter.Label(arithmeticTab, text="Shift")

normalization_radio_variable = tkinter.IntVar(value=1)
normalization_radio_one = tkinter.Radiobutton(arithmeticTab, text="0 to 1", variable=normalization_radio_variable,
                                              value=1)
normalization_radio_two = tkinter.Radiobutton(arithmeticTab, text="-1 to 1", variable=normalization_radio_variable,
                                              value=2)


# ---------------------------------Arithmetic Operation End--------------


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
    angular_frequency = 2 * np.pi * (float(analog_text.get(1.0, "end-1c")) / float(sampling_text.get(1.0, "end-1c")))
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
        angular_frequency_2 = 2 * math.pi * (float(analog_text_2.get(1.0, "end-1c")) / float(sampling_text_2.get(1.0,
                                                                                                                 "end-1c")))
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
        comparesignals.SignalSamplesAreEqual("SinOutput.txt", x, y)


draw_signal_button = tkinter.Button(createSignalTab, text="Draw Signal", command=draw_signal)
draw_signal_button.place(x=80, y=190)
# ---------------------------------Quantize Signal-----------------------
quantize_direc = ""


def quantize_dir():
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
    global quantize_direc
    quantize_direc = os.path.split(filenames)[0] + "/" + os.path.split(filenames)[1]
    quantize_directory.insert("1.0", quantize_direc)


def quantize():
    if quantize_direc == "":
        messagebox.showerror("Error!", "Please select a file first!")
        return
    number_of_levels = 0
    if quantize_var.get() == 0:
        number_of_levels = math.pow(2, int(bits_levels_box.get(1.0, "end-1c")))
    elif quantize_var.get() == 1:
        number_of_levels = int(bits_levels_box.get(1.0, "end-1c"))
    file = open(quantize_direc, 'r')
    file = file.readlines()
    x = []
    y = []
    for i in range(3, len(file)):
        x.append(float(file[i].split(" ")[0]))
        y.append(float(file[i].split(" ")[1]))
    delta = (max(y) - min(y)) / number_of_levels
    levels = []
    midpoints = []
    eqn = []
    ydash_binary = []
    ydash_mid = []
    for i in np.arange(min(y), max(y) + delta, delta):
        levels.append(i)
    for i in range(0, len(levels) - 1):
        midpoints.append((levels[i] + levels[i + 1]) / 2)
    for i in y:
        for j in range(0, len(levels), 1):
            if j + 1 == len(levels):
                bina = bin(j)
                if len(bina.split('b')[1]) < math.pow(2, number_of_levels):
                    bina = '0' * int((math.log(number_of_levels, 2) - len(bina.split('b')[1]))) + bina.split('b')[1]
                ydash_binary.append(bina)
                eqn.append(midpoints[j] - i)
                ydash_mid.append(round(midpoints[j], 4))
                break
            if levels[j] <= i <= levels[j + 1]:
                bina = bin(j)
                if len(bina.split('b')[1]) < math.pow(2, number_of_levels):
                    bina = '0' * int((math.log(number_of_levels, 2) - len(bina.split('b')[1]))) + bina.split('b')[1]
                ydash_binary.append(bina)
                eqn.append(midpoints[j] - i)
                ydash_mid.append(round(midpoints[j], 4))
                break
            else:
                continue
    error = (1 / len(y)) * reduce(operator.add, map(lambda x: x * x, eqn))
    print(ydash_mid)
    print(ydash_binary)
    print(error)
    QuanTest1.QuantizationTest1('Quan1_Out.txt', ydash_binary, ydash_mid)


def task32():
    if quantize_direc == "":
        messagebox.showerror("Error!", "Please select a file first!")
        return
    number_of_levels = 0
    if quantize_var.get() == 0:
        number_of_levels = math.pow(2, int(bits_levels_box.get(1.0, "end-1c")))
    elif quantize_var.get() == 1:
        number_of_levels = int(bits_levels_box.get(1.0, "end-1c"))
    file = open(quantize_direc, 'r')
    file = file.readlines()
    x = []
    y = []
    for i in range(3, len(file)):
        x.append(float(file[i].split(" ")[0]))
        y.append(float(file[i].split(" ")[1]))
    delta = (max(y) - min(y)) / number_of_levels
    levels = []
    midpoints = []
    eqn = []
    ydash_binary = []
    ydash_mid = []
    quantized_indices = []
    quantized_error = []
    for i in np.arange(min(y), max(y) + delta, delta):
        levels.append(i)
    for i in range(0, len(levels) - 1):
        midpoints.append((levels[i] + levels[i + 1]) / 2)
    for i in y:
        for j in range(0, len(levels), 1):
            # if j+1 == len(levels):
            #     quantized_indices.append(j + 1)
            #     bina = bin(j)
            #     if len(bina.split('b')[1]) < math.pow(2, number_of_levels):
            #         bina = '0' * int((math.log(number_of_levels, 2) - len(bina.split('b')[1]))) + bina.split('b')[1]
            #     ydash_binary.append(bina)
            #     eqn.append(round(midpoints[j] - i,4))
            #     ydash_mid.append(round(midpoints[j], 4))
            #     break
            if levels[j] <= i <= levels[j + 1]:
                quantized_indices.append(j + 1)
                bina = bin(j)
                if len(bina.split('b')[1]) < math.pow(2, number_of_levels):
                    bina = '0' * int((math.log(number_of_levels, 2) - len(bina.split('b')[1]))) + bina.split('b')[1]
                ydash_binary.append(bina)
                eqn.append(round(midpoints[j] - i, 4))
                ydash_mid.append(round(midpoints[j], 4))
                break

    error = (1 / len(y)) * reduce(operator.add, map(lambda x: x * x, eqn))
    print(ydash_mid)
    print(ydash_binary)
    print(error)
    print(quantized_indices)
    print(eqn)
    # QuanTest2.QuantizationTest2('Quan2_Out.txt',)


quantize_directory = tkinter.Text(quantizeTab, height=0, width=100)
quantize_directory.pack()
quantize_dir_btn = tkinter.Button(quantizeTab, text="Choose Signal", command=quantize_dir)
quantize_dir_btn.pack()
quantize_btn = tkinter.Button(quantizeTab, text="Quantize", command=quantize)
quantize_var = tkinter.IntVar(value=0)
bits_radio = tkinter.Radiobutton(quantizeTab, text="Bits", variable=quantize_var, value=0)
levels_radio = tkinter.Radiobutton(quantizeTab, text="Levels", variable=quantize_var, value=1)
bits_levels_box = tkinter.Text(quantizeTab, height=0, width=50)
task3_2 = tkinter.Button(quantizeTab, text="part 2", command=task32)
bits_levels_box.pack()
bits_radio.pack()
levels_radio.pack()
quantize_btn.pack()
task3_2.pack()


# ---------------------------------Quantize Signal End-------------------

# ---------------------------------Frequency Domain----------------------

def convert_time_to_freq(x_in, y_in, sampling, operation):
    if operation == 0:
        real = []
        imaginary = []
        amplitude = []
        phase = []
        x_axis = []
        for sample in range(0, len(x_in)):
            real_harmonic = []
            imaginary_harmonic = []
            for i in range(0, len(x_in)):
                current_angle = (-2 * math.pi * sample * i) / len(x_in)
                real_part = y_in[i] * math.cos(current_angle)
                imaginary_part = y_in[i] * math.sin(current_angle)
                real_harmonic.append(real_part)
                imaginary_harmonic.append(imaginary_part)
            real.append(sum(real_harmonic))
            imaginary.append(sum(imaginary_harmonic))
        for i in range(0, len(real)):
            amplitude.append(math.sqrt(math.pow(real[i], 2) + math.pow(imaginary[i], 2)))
            if real[i] == 0:
                phase.append(0.5 * math.pi)
            else:
                phase.append(math.atan(imaginary[i] / real[i]))
        fundmental_frequency = (2 * np.pi) / (len(x_in) * (1 / sampling))
        for i in range(1, len(amplitude) + 1):
            x_axis.append(i * fundmental_frequency)

        file_write = open('Written_signal_polar', 'w')
        file_write.write('0\n1\n')
        file_write.write(f'{len(amplitude)}\n')
        for i in range(0, len(amplitude)):
            file_write.write(f'{amplitude[i]},{phase[i]}\n')
        file_write.close()
        fig = plt.figure()
        plt.stem(x_axis, amplitude)
        fig = plt.figure()
        plt.stem(x_axis, phase)
        plt.show()
    else:
        nums = []
        l = []
        y_out = []
        x_out = []
        for i in range(0, len(x_in)):
            nums.append(complex(x_in[i]*math.cos(y_in[i]), x_in[i]*math.sin(y_in[i])))
        for j in range(0, len(x_in)):
            finalNum = []
            for i in range(0, len(x_in)):
                constant = -2*j*i
                multiple = complex(math.cos((constant*math.pi) / len(x_in)), math.sin(constant * math.pi) / len(x_in))
                finalNum.append(multiple*nums[i])
            y_out.append(sum(finalNum))
        x_out = range(0,len(y_out),1)
        print(x_out)
        print(y_out)
        file_write = open('Written_signal','w')
        file_write.write('0\n0\n')
        file_write.write(f'{len(x_out)}\n')
        for i in range(0, len(x_out)):
            file_write.write(f'{x_out[i]},{y_out[i]}\n')
        file_write.close()



frequency_file = None


def choose_frequency_file():
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
    global frequency_file
    frequency_file = os.path.split(filenames)[0] + "/" + os.path.split(filenames)[1]
    frequency_file_directory.insert(1, frequency_file)
    if open(frequency_file, 'r').readlines()[1].split('\n')[0] == '1':
        label1.pack_forget()
        sampling_frequency.pack_forget()


def apply_DFT():
    file = open(frequency_file, 'r')
    file = file.readlines()
    x_vals = []
    y_vals = []

    if file[1].split('\n')[0] == '0':
        for i in range(3, len(file)):
            x_vals.append(float(file[i].split(' ')[0]))
            y_vals.append(float(file[i].split(' ')[1].split('\t')[0]))
        convert_time_to_freq(x_vals, y_vals, float(sampling_frequency.get()), 0)
    else:
        for i in range(3, len(file)):
            x_vals.append(float(file[i].split(',')[0].split('f')[0]))
            y_vals.append(float(file[i].split(',')[1].split('f')[0]))
        convert_time_to_freq(x_vals, y_vals, 0, 1)
dctvals = []
def apply_DCT():
    file = open(frequency_file, 'r')
    file = file.readlines()
    x_vals = []
    y_vals = []
    for i in range(3, len(file)):
        x_vals.append(float(file[i].split(' ')[0].split('f')[0]))
        y_vals.append(float(file[i].split(' ')[1].split('f')[0]))
    global dctvals
    dctvals = dct_for_m(x_vals, y_vals)
    print(dctvals)
    comparesignal2.SignalSamplesAreEqual('D:\signalApp\DCT\DCT_output.txt',dctvals)
    values_win = tkinter.Tk()
    values_win.title("DCT values")
    values_win.geometry("1000x500")
    values_window = tksheet.Sheet(values_win, height=400, width=900)
    values_window.pack()
    # values_window.grid()
    values_window.set_sheet_data([dctvals])
    values_window.enable_bindings(("single_select",
                       "row_select",
                       "column_width_resize",
                       "arrowkeys",
                       "right_click_popup_menu",
                       "rc_select",
                       "rc_insert_row",
                       "rc_delete_row",
                       "copy",
                       "cut",
                       "paste",
                       "delete",
                       "undo",
                       "edit_cell"))
    values_win.mainloop()


def save_dct():
    if not m_coefficients.get().isdigit():
        messagebox.showerror(message="Please insert a number!", title="Error!")
        return
    if not dctvals:
        messagebox.showerror(message="Please choose signal file and apply DCT first!", title="Error!")
        return
    if int(m_coefficients.get()) > len(dctvals):
        messagebox.showerror(message=f"there's only {len(dctvals)} coefficients and you entered {m_coefficients.get()}!", title="Error!")
        return
    save_file(0, 1, [0]*len(dctvals[0:int(m_coefficients.get())-1]), dctvals[0:int(m_coefficients.get())-1], 'SavedDct.txt')
def removeDC():
    file = open(frequency_file, 'r')
    file = file.readlines()
    x_vals = []
    y_vals = []
    for i in range(3, len(file)):
        x_vals.append(int(file[i].split(' ')[0].split('f')[0]))
        y_vals.append(float(file[i].split(' ')[1].split('f')[0]))
    avg = sum(y_vals)/len(y_vals)
    for i in range(len(y_vals)):    #y[i]-average(y)
        y_vals[i]-=avg
    comparesignal2.SignalSamplesAreEqual('D:\signalApp\Remove DC component\DC_component_output.txt', y_vals)
    values_win = tkinter.Tk()
    values_win.title("Signal after removing DC")
    values_win.geometry("1000x500")
    values_window = tksheet.Sheet(values_win, height=400, width=900)
    values_window.pack()
    # values_window.grid()
    values_window.set_sheet_data([y_vals])
    values_window.enable_bindings(("single_select",
                                   "row_select",
                                   "column_width_resize",
                                   "arrowkeys",
                                   "right_click_popup_menu",
                                   "rc_select",
                                   "rc_insert_row",
                                   "rc_delete_row",
                                   "copy",
                                   "cut",
                                   "paste",
                                   "delete",
                                   "undo",
                                   "edit_cell"))
    values_win.mainloop()
    save_file(0, 0, x_vals, y_vals, "removed DC signal.txt")




tkinter.Label(frequencyDomain, text="Signal Directory:").pack()
frequency_file_directory = tkinter.Entry(frequencyDomain, width=100)
select_frequency_file_button = tkinter.Button(frequencyDomain, text="Choose Signal", command=choose_frequency_file)

frequency_file_directory.pack()
select_frequency_file_button.pack()
label1 = tkinter.Label(frequencyDomain, text="Sampling Frequency")
label1.pack()
sampling_frequency = tkinter.Entry(frequencyDomain)
sampling_frequency.pack()
applyDFTbtn = tkinter.Button(frequencyDomain, text='Apply DFT', command=apply_DFT)
applyDFTbtn.pack()
applyDCTbtn = tkinter.Button(frequencyDomain, text='Apply DCT',command=apply_DCT)
tkinter.Label(frequencyDomain, text='number of coefficients to be saved').pack()
m_coefficients = tkinter.Entry(frequencyDomain)
saveDct = tkinter.Button(frequencyDomain, text='Save DCT', command=save_dct)
removeDCbtn = tkinter.Button(frequencyDomain, text="Remove DC Component", command=removeDC)
m_coefficients.pack()
applyDCTbtn.pack()
saveDct.pack()
removeDCbtn.pack()
# ---------------------------------Frequency Domain End------------------

# ---------------------------------Time domain---------------------------
time_domain_selected = tkinter.StringVar(value='Smoothing')
time_domain_options = tkinter.OptionMenu(time_domain_tab,time_domain_selected, 'Smoothing', 'Sharpening', 'Delay or Advance', 'Fold Signal', 'Remove DC')
tkinter.Label(time_domain_tab,text='Options: ').pack()
time_domain_options.pack()
# ---------------------------------Time domain end-----------------------
mainWindow.mainloop()
