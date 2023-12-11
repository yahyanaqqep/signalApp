import math
import numpy as np
from tkinter import messagebox
from tkinter import filedialog as fd
import os.path

def dct(x, y, k):
    sum_arr = []
    for i in range(0, len(y)):
        sum_arr.append(y[i]*math.cos((math.pi/(4*len(y)))*((2*x[i])-1)*((2*k)-1)))
    return math.sqrt(2/len(y))*sum(sum_arr)


def dct_for_m(x, y):
    out = []
    for i in range(0, len(y)):
        out.append(dct(x, y, i))
    return out


def save_file(signal_type, periodic, x, y, file_name):
    file = open(file_name, 'w')
    file.write(f'{signal_type}\n{periodic}\n')
    file.write(f'{len(y)}\n')
    for i in range(0, len(x)):
        file.write(f'{x[i]} {y[i]}\n')
    file.close()


def moving_average(x, N):
    y = []
    for n in range(len(x)):
        if n < N - 1:
            # Not enough past samples for the first few points
            y.append(sum(x[:n+1]) / (n+1))
        else:
            # Compute the moving average using the window of size N
            y.append(sum(x[n-N+1:n+1]) / N)
    return y


def fold_signal(y):
    print(len(y))
    last_index = ((len(y)-1)/2)
    last_index = int(last_index)
    first_half_y = y[0:last_index]
    first_index = ((len(y) + 1) / 2)
    first_index = int(first_index)
    last_index = len(y)
    last_index = int(last_index)
    second_half_y = y[first_index:last_index]
    first_half_y.reverse()
    second_half_y.reverse()
    first_index = ((len(y)+1)/2)-1
    first_index = int(first_index)
    print(first_index)
    item = y[first_index]
    second_half_y.append(item)
    second_half_y.extend(first_half_y)
    return second_half_y


def shift_signal(x, shift):
    for i in range(0, len(x)):
        x[i] += shift
    return x


def remove_dc_freq(X):
    N = len(X)  # total number of samples
    k = np.arange(N)
    shift_factor = np.exp(-1j * 2 * np.pi * k / N)
    X_shifted = X * shift_factor
    return X_shifted


def browse_file():
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
    file = os.path.split(filenames)[0] + "/" + os.path.split(filenames)[1]
    return file


def get_signal(path):
    file = open(path, 'r')
    file = file.readlines()
    x_vals = []
    y_vals = []

    for i in range(3, len(file)):
        x_vals.append(float(file[i].split(' ')[0]))
        y_vals.append(float(file[i].split(' ')[1].split('\t')[0]))
    return x_vals, y_vals


def conv_to_freq(signal):
    out = []
    for i in range(0, len(signal)):
        num = complex(0, 0)
        for j in range(0, len(signal)):
            num += complex(math.cos((-2*math.pi*i*j)/len(signal)), math.sin((-2*math.pi*i*j)/len(signal)))
        out.append(num)
    return out


def convolve(x_signal1, x_signal2, y_signal1, y_signal2):
    convolved_signal = []
    n_minimum_limit = x_signal1[0] + x_signal2[0]
    n_max_limit = x_signal1[len(x_signal1)-1] + x_signal2[len(x_signal2)-1]
    for i in range(int(n_minimum_limit),int(n_max_limit + 1)):
        yi = 0
        k = x_signal1[0]
        while i-k > x_signal2[0]-1 and k < x_signal1[len(x_signal1)-1]+1:
            if i-k > x_signal2[len(x_signal2)-1] or k < x_signal1[0]:
                k += 1
                continue
            index_of_y_signal1 = x_signal1.index(k)
            index_of_y_signal2 = x_signal2.index(i-k)
            yi += y_signal1[index_of_y_signal1]*y_signal2[index_of_y_signal2]
            k += 1
        convolved_signal.append(yi)

    return list(range(int(n_minimum_limit),int(n_max_limit + 1) )), convolved_signal


def get_correlation(signal1, signal2):
    denominator = (1/len(signal1))*math.sqrt(sum([x**2 for x in signal1])*sum([x**2 for x in signal2]))
    corr_out = []
    for j in range(0, len(signal1)+1):
        nums = []
        for n in range(0, len(signal1)):
            index = n+j
            if n+j >= len(signal2):
                index = (n+j)-len(signal2)
            nums.append(signal1[n]*signal2[index])
        corr_out.append((1/len(signal2))*sum(nums))
    corr_out = [x/denominator for x in corr_out]
    return corr_out



