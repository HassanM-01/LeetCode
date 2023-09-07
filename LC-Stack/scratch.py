# Import regex module
import re
# Define input string
input_string = "5.0,15,4.0,25,3.0,10:L10;5.0,18,4.0,42,3.0,12:L20;"
# Regex patterns
lock_pattern = r"[L]\d+"
rate_pattern = r"\d+[.]\d+"
# Extract lock labels
lock_labels = "".join(re.findall(lock_pattern, input_string)).split("L")
# Extract unique row labels 
row_labels = sorted(set(re.findall(rate_pattern, input_string)), key=float)
# Preprocess string 
processed_str = ",".join(input_string.replace(":", ",").split(", ")).split(",")
# Extract data values
data_values = []
for value in processed_str:
    if value.isdigit():
        data_values.append(value)
# Initialize matrix
matrix = [lock_labels]
# Add rows 
for i in range(len(lock_labels)):
    row = ["" for l in range(len(lock_labels))]
    row[0] = row_labels[i]
    matrix.append(row)
# Populate matrix
for i in range(1, len(matrix)):
    num = i - 1
    for j in range(1, len(matrix[i])):
        matrix[i][j] = data_values[num]
        num += len(row_labels)
# Print matrix
for row in matrix:
    print(row)