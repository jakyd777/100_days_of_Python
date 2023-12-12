import pandas as pd

data = pd.read_csv("squirrel_data.csv")

list_of_colors = []
primary_color = data['Primary Fur Color'].to_list()

for each_color in primary_color:
    if each_color not in list_of_colors:
        list_of_colors.append(each_color)

colors_dict = {}
color_name = []
color_count = []

for color in list_of_colors:           
    number = 0
    for each_color in primary_color:
        if each_color == color:
            number += 1
    if number != 0:
        color_name.append(color.lower())
        color_count.append(number)

colors_dict["Fur Color"] = color_name
colors_dict["Count"] = color_count

squirrel_count = pd.DataFrame(colors_dict)
squirrel_count.to_csv("squirrel_count.csv")



#
# data_list = data['temp']
# print(data_list)
#
# print(data_list.mean())
# print(data_list.max())

# monday = data[data.day == "Monday"]
# temp_to_convert = (monday.temp * 1.8) + 32
# print(temp_to_convert)