import math
import cmath
import numpy as np
from tkinter import messagebox
from tkinter import filedialog as fd
import os.path
import numpy

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
        my_num = []
        for j in range(0, len(signal)):
            if i == 0 or j == 0:
                my_num.append(signal[j]+0j)
            else:
                num1 = cmath.cos((-2*cmath.pi*i*j)/len(signal))
                num2 = cmath.sin((-2*cmath.pi*i*j)/len(signal))
                my_num.append((signal[j]*(num1+num2*1j)))
        my_num = round(sum(my_num).real, 3)+round(sum(my_num).imag, 3)*1j
        out.append(my_num)
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


def is_periodic(path):
    file = open(path, 'r')
    file = file.readlines()
    if file[1].split('\n')[0] == '1':
        return True
    elif file[1].split('\n')[0] == '0':
        return False


def get_correlation(signal1, signal2, periodic):
    denominator = (1/len(signal1))*math.sqrt(sum([x**2 for x in signal1])*sum([x**2 for x in signal2]))
    corr_out = []
    for j in range(0, len(signal1)+1):
        nums = []
        for n in range(0, len(signal1)):
            index = None
            if n+j < len(signal2):
                index = signal2[n+j]
            elif n+j >= len(signal2) and periodic:
                index = signal2[(n+j)-len(signal2)]
            elif n+j >= len(signal2) and not periodic:
                index = 0

            nums.append(signal1[n]*index)
        corr_out.append((1/len(signal2))*sum(nums))
    corr_out = [x/denominator for x in corr_out]
    return corr_out


def conv_to_time(signal):
    out = []
    for n in range(0, len(signal)):
        current = 0+0j
        for k in range(0, len(signal)):
            current += signal[k] * (cmath.cos(2*cmath.pi*n*k/len(signal))+cmath.sin(2*cmath.pi*n*k/len(signal))*1j)

        current = current/len(signal)
        current = round(current.real, 3) + round(current.imag, 3)*1j
        to_be_appended = current.real + (current.imag * -1)
        out.append(to_be_appended)
    return out


def fast_convolution(signal1, signal2):
    len_zeroes_signal1 = (len(signal1) + len(signal2) -1)-len(signal1)
    len_zeroes_signal2 = (len(signal1) + len(signal2) - 1) - len(signal2)
    for i in range(0, len_zeroes_signal1):
        signal1.append(0)
    for i in range(0, len_zeroes_signal2):
        signal2.append(0)
    signal1_freq = numpy.array(conv_to_freq(signal1))
    signal2_freq = numpy.array(conv_to_freq(signal2))
    convolved_signal = numpy.multiply(signal1_freq, signal2_freq)
    return conv_to_time(convolved_signal)


def fast_auto_correlation(signal):
    signal_freq = conv_to_freq(signal)
    signal_freq_dash = [complex(i.real, -i.imag) for i in signal_freq]
    fd = []
    out = []
    for i in range(0, len(signal_freq)):
        num = signal_freq[i] * signal_freq_dash[i]
        num = num.real + (num.imag*-1)
        fd.append(num)
    for i in range(0, len(fd)):
        current = 0
        for j in range(0, len(fd)):
            current += fd[j]*complex(round(math.cos(2*math.pi*i*j/len(fd))), round(math.sin(2*math.pi*i*j/len(fd))))
        current = current/len(fd)
        out.append(current)
    return [x.real/len(fd) for x in out]


def fast_cross_correlation(signal1, signal2, is_periodic):
    signal1_freq = conv_to_freq(signal1)
    signal2_freq = conv_to_freq(signal2)
    signal1_conjugate = [i.real - i.imag*1j for i in signal1_freq]
    signal1_conjugate = np.array(signal1_conjugate)
    signal2_freq = np.array(signal2_freq)
    out = np.multiply(signal1_conjugate, signal2_freq)
    num_to_divide_by = cmath.sqrt(sum([x**2 for x in signal1])*sum([x**2 for x in signal2]))/len(signal1)
    out = [numpy.round((x/len(signal1)), 3) for x in out]
    return conv_to_time(out)


print(fast_cross_correlation([2, 1, 0, 0, 3], [3, 2, 1, 1, 5], True))
# print(fast_auto_correlation([1,0,0,1]))
