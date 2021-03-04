
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
#
# average_temp = data["temp"].mean()
#
# max_temp = data["temp"].max()
#
# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * 1.8 + 32
# print(monday_temp_f)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon_color_count, gray_color_count, black_color_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("final_color_counts.csv")






