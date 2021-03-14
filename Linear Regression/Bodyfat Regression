# Name: Minseok Gang
# HW8
# 9074016560 / gang3

import csv
import numpy as np
import math
import random


def get_dataset(filename):
    with open(filename, newline='') as f:
        dataset = list(csv.reader(f))
        del dataset[0]
        for i in dataset:
            del i[0]
            for ele in range(len(i)):
                i[ele] = float(i[ele])

    output = np.array(dataset)
    return output


def print_stats(dataset, col):
    num_datapoints = 0
    total = 0
    sd = 0
    for row in dataset:
        num_datapoints += 1
        total += row[col]

    mean = total/num_datapoints

    for row in dataset:
        sd += (row[col] - mean)**2
    sd = math.sqrt((1/(num_datapoints-1)) * sd)
    print(num_datapoints)
    print('{:.2f}'.format(mean))
    print('{:.2f}'.format(sd))


def regression(dataset, cols, betas):
    size = len(dataset)
    mse = 0
    for row in dataset:
        sum = 0
        for i in range(len(cols)):
            sum += row[cols[i]] * betas[i+1]
        mse += (betas[0] + sum - row[0])**2

    mse = mse / size

    return mse


def gradient_descent(dataset, cols, betas):
    size = len(dataset)
    grads = []

    for i in range(len(betas)):
        output = 0
        for row in dataset:
            sum = 0
            if i == 0:
                for j in range(len(cols)):
                    sum += row[cols[j]] * betas[j+1]
                output += sum + betas[0] - row[0]
            else:
                for j in range(len(cols)):
                    sum += row[cols[j]] * betas[j+1]
                output += (sum + betas[0] - row[0]) * row[cols[i-1]]

        grads.append(2*output/size)

    return grads


def iterate_gradient(dataset, cols, betas, T, eta):
    result = []
    t = 1

    while t != T+1:

        temp = gradient_descent(dataset, cols, betas)
        output = []
        track = []
        idx = 0

        for i in betas:
            i = i - temp[idx]*eta
            track.append(i)
            idx += 1

        betas = track
        output.append(t)
        output.append('{:.2f}'.format(regression(dataset, cols, betas)))

        for i in betas:
            output.append('{:.2f}'.format(i))

        result.append(output)
        t += 1

    for s in result:
        print(*s)


def compute_betas(dataset, cols):
    x = []
    y = []
    for row in dataset:
        y.append(row[0])
        features = []
        features.append(1)
        for i in cols:
            features.append(row[i])
        x.append(features)
    x_matrix = np.matrix(x)
    x_transposed = np.transpose(np.matrix(x))
    betas = np.dot(np.dot(np.linalg.inv(
        np.dot(x_transposed, x_matrix)), x_transposed), y)
    betas = np.array(betas)
    mse = regression(dataset, cols, betas[0])
    betas = np.squeeze(betas)

    return (mse, *betas)


def predict(dataset, cols, features):
    items = compute_betas(dataset, cols)
    result = 0
    for i in range(len(items)):
        if i == 0:
            continue
        elif i == 1:
            result += items[i]
        else:
            result += features[i-2]*items[i]

    return result


def random_index_generator(min_val, max_val, seed=42):
    """
    DO NOT MODIFY THIS FUNCTION.
    DO NOT CHANGE THE SEED.
    This generator picks a random value between min_val and max_val,
    seeded by 42.
    """
    random.seed(seed)
    while True:
        yield random.randrange(min_val, max_val)


def sgd(dataset, cols, betas, T, eta):
    size = len(dataset)
    rand_row = random_index_generator(0, size)

    result = []
    t = 1

    while t != T+1:
        temp = gradient_descent([dataset[next(rand_row)]], cols, betas)
        output = []
        track = []
        idx = 0

        for i in betas:
            i = i - temp[idx]*eta
            track.append(i)
            idx += 1

        betas = track
        output.append(t)
        output.append('{:.2f}'.format(regression(dataset, cols, betas)))

        for i in betas:
            output.append('{:.2f}'.format(i))

        result.append(output)
        t += 1

    for s in result:
        print(*s)


if __name__ == '__main__':
    # Your debugging code goes here.
    pass
