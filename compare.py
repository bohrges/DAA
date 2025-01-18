import csv

def compare_csv(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = list(csv.reader(f1))
        reader2 = list(csv.reader(f2))

        if reader1 == reader2:
            print("The CSV files are equal.")
        else:
            print("The CSV files are not equal.")

# Usage
file1 = "test_predictions_ann.csv"
file2 = "ann_best.csv"

compare_csv(file1, file2)
