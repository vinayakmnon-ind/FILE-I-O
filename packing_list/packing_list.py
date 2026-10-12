import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
           print(row)

except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open('packing_list.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)

x = input("What would you like to add to the packing list? (Enter 'done' to finish):")
while x != 'done':
    quantity = input(f"How many {x} would you like to add? ")
    data.append([x, quantity])
    x = input("What would you like to add to the packing list? (Enter 'done' to finish):")

with open('packing_list.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)



    


