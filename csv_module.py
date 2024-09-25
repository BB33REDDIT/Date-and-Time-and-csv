import csv
#
#with open('stock_data.csv','r') as file:
    #reader = csv.DictReader(file)
    #for row in reader:
       #print(row)




with open("output.csv", 'w') as file:
    writer = csv.writer(file, delimiter=':')
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Dinku', 40, 'Kannur'])
    writer.writerow(['Pranav', 18, 'Kasargod'])


with open("dictoutput.csv", 'w') as file:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Dinku', 'age': 40, 'city': 'Kannur'})
    writer.writerow({'name': 'Pranav', 'age': 18, 'city': 'Kasargod'})


try:
    with open('stock_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except csv.Error as e:
    print(f'Error reading CSV file: {e}')
