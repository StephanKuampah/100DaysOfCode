import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_squirel = len(data[data["Primary Fur Color"] == "Gray"])

red_squirel = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [f"{grey_squirel}", f"{red_squirel}", f"{black_squirel}"]
}

new = pandas.DataFrame(data_dict)

squirel_data = new.to_csv()

print(squirel_data)