import csv
import validators

with open('cafe-data2.csv', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
    # for row in list_of_rows:
    #     for item in row:
    #         # if item[0:4] == "http":
    #         #     print(item)
    print(list_of_rows)


name = "Hallo"
location = "https://google.com"
time_open = "08:30AM"
time_close = "21:00PM"
cafe = "3star"
wifi = "3star"
power = "3star"
data_to_append = [name, location, time_open, time_close, cafe, wifi, power]
with open('cafe-data2.csv', "a", newline='', encoding='utf-8') as csv_file:
    csv_data = csv.writer(csv_file)
    csv_data.writerow(data_to_append)
