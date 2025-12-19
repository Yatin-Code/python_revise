
# import csv
# with open("002 weather-data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         try:
#             temperature = (int(row[1]))
#             temp.append(temperature)
#         except ValueError:
#             continue
# print(temp)
import pandas

data = pandas.read_csv("002 weather-data.csv")
# data_list = data["temp"].to_list()
# print(data_list)

## FINDING mean:

# METHOD 1


# total_sum = 0
# total_num = 0
# for i in data_list:
#     total_num += 1
#     total_sum +=  i


# avg = total_sum/total_num
# print(round(avg))

# Method 2

# total_sum = sum(data_list)
# total_num = len(data_list)
# print(total_sum/total_num)

# Method 3

# print(data["temp"].max())

# print((data[data.temp == data.temp.max()]))
monday = data[data.day == "Monday"]
print(int(monday.temp) * 9/5 + 32)