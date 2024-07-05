import csv
import pandas

# with open('./weather_data.csv') as file:
#     contents = csv.reader(file)
#     next(contents)
#     temperature = []
#     for row in contents:
#         temp = int(row[1])
#         temperature.append(temp)

# print(temperature)
# new = []
# for content in contents:
#     new_content = content.strip('\n')
#     new.append(new_content)

# print(new)
        
data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()
# data_dict = data.to_dict()

# maximum = data['temp'].max()
# minimum = data['temp'].min()

# print(f"{maximum},{minimum}")

monday = data[data.day == 'Monday']
temp_in_farenheit = monday.temp * 1.8 + 32
print(temp_in_farenheit)





