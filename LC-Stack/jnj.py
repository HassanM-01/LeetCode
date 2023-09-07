# Import regex module
import re

# Constants
INPUT_STRING = "5.0,15,4.0,25,3.0,10:L10;5.0,18,4.0,42,3.0,12:L20;"
LOCK_REGEX = r"[L]\d+"
RATE_REGEX = r"\d+[.]\d+"


# Functions
def extract_labels(input_str, regex):
    matches = re.findall(regex, input_str)
    return "".join(matches).split("L")


def get_unique_labels(input_str, regex):
    return sorted(set(re.findall(regex, input_str)), key=float)


def preprocess(input_str):
    return ",".join(input_str.replace(":", ",").split(", ")).split(",")


def extract_data(input_list):
    values = []
    for value in input_list:
        if value.isdigit():
            values.append(value)
    return values


# Main program
lock_labels = extract_labels(INPUT_STRING, LOCK_REGEX)
row_labels = get_unique_labels(INPUT_STRING, RATE_REGEX)
processed_data = preprocess(INPUT_STRING)
data_values = extract_data(processed_data)

matrix = [lock_labels]
for i in range(len(lock_labels)):
    row = ["" for _ in range(len(lock_labels))]
    row[0] = row_labels[i]
    matrix.append(row)

num = 0
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[i])):
        matrix[i][j] = data_values[num]
        num += 1

for row in matrix:
    print(row)
