import csv
import os


data_list = []
data_dict = {}


def enter_filename():
    filename = input("\nPlease enter the filename.csv to be opened: ")
    if os.path.exists(filename):
        with open(filename, mode='r')as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if line == []:  # to handle empty lines
                    continue
                else:
                    data_list.append(line)
    else:
        print("File not found.")
        enter_filename()




def total_spending():
    total = 0.0
    for amount in data_dict.values():
        total += float(amount)
    print(f"The total spending is {total}")



def sorting(data_dict):
    data_dict = dict(sorted(data_dict.items(),key = lambda x: x[1],reverse = True))

    print(f"The highest spending category is {list(data_dict)[0]}")
    print(f"The sorted dictionary:\n{data_dict}")


enter_filename()
for item in data_list:
    data_dict[item[0]] = float(item[1])


print(data_dict)
total_spending()
sorting(data_dict)
