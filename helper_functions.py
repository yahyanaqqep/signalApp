import math
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
