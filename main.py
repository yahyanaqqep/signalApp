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

mainWindow = tkinter.Tk()
mainWindow.title("Wave App")
mainWindow.geometry("800x500")
tabControl = ttk.Notebook(mainWindow)
readSignalTab = ttk.Frame(tabControl)
createSignalTab = ttk.Frame(tabControl)
arithmeticTab = ttk.Frame(tabControl)
tabControl.add(readSignalTab, text="Read Signal")
tabControl.add(createSignalTab, text="Create Signal")
tabControl.add(arithmeticTab, text="Arithmetic Operation")
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


# ---------------------------------Arithmetic Operation-------------
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
        for i in range(3, 2+int(file[2])):
            text = file[i]
            text = text.split(" ")
            x_arithmetic.append(float(text[0]))
            y_arithmetic.append(float(text[1]))
        for i in range(1, len(signals_directory)):
            file = open(signals_directory[i], 'r')
            file = file.readlines()
            for j in range(3, 2+int(file[2])):
                text = file[j]
                text = text.split(" ")
                y_arithmetic[j-3] += float(text[1])
        plt.plot(x_arithmetic, y_arithmetic)
        plt.show()
    elif operation_radio_var.get() ==2:
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
        plt.plot(x_arithmetic,y_arithmetic)
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
            y_arithmetic[i] = math.pow(y_arithmetic[i],2)
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
        shift = float(multiply_signal_const.get(1.0,'end-1c'))
        for i in range(0, len(x_arithmetic)):
            if x_arithmetic[i]<0:
                x_arithmetic[i] -= shift
            elif x_arithmetic[i]>0:
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
        for i in range(0,len(y_arithmetic)):
            y_arithmetic[i] = ((y_arithmetic[i]-left_min)/(left_max-left_min))*right_span + right_min
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
        for i in range(1,len(y_arithmetic)):
            y_arithmetic[i] += y_arithmetic[i-1]
        plt.plot(x_arithmetic,y_arithmetic)
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
        choose_multiply.place(x=500,y=15)
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
addition_radio_button = tkinter.Radiobutton(arithmeticTab, text="Addition", variable=operation_radio_var, value=1, command=show_hide_arithmetic)
subtraction_radio_button = tkinter.Radiobutton(arithmeticTab, text="Subtraction", variable=operation_radio_var, value=2, command=show_hide_arithmetic)
multiplication_radio_button = tkinter.Radiobutton(arithmeticTab, text="Multiplication", variable=operation_radio_var, value=3, command=show_hide_arithmetic)
squaring_radio_button = tkinter.Radiobutton(arithmeticTab, text="Squaring", variable=operation_radio_var, value=4, command=show_hide_arithmetic)
shifting_radio_button = tkinter.Radiobutton(arithmeticTab, text="Shift Signal", variable=operation_radio_var, value=5, command=show_hide_arithmetic)
normalization_radio_button = tkinter.Radiobutton(arithmeticTab, text="Normalize", variable=operation_radio_var, value=6, command=show_hide_arithmetic)
accumulation_radio_button = tkinter.Radiobutton(arithmeticTab, text="Accumulate", variable=operation_radio_var, value=7, command=show_hide_arithmetic)
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
normalization_radio_one = tkinter.Radiobutton(arithmeticTab, text="0 to 1", variable=normalization_radio_variable, value=1)
normalization_radio_two = tkinter.Radiobutton(arithmeticTab, text="-1 to 1", variable=normalization_radio_variable, value=2)

# ---------------------------------Arithmetic Operation End---------

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
        comparesignals.SignalSamplesAreEqual("SinOutput.txt", x, y)


draw_signal_button = tkinter.Button(createSignalTab, text="Draw Signal", command=draw_signal)
draw_signal_button.place(x=80, y=190)

mainWindow.mainloop()
