def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)  # średnia temperatur suma / liczba
    return average_local


average = get_average()
print(average)