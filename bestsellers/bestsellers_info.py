import csv 

csv_file_path = 'Bestseller - Sheet1.csv'

best_seller = None
max_sales = 0

with open(csv_file_path, mode='r', encoding = 'utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    csv_file.readline()

    for row in csv_reader:
        current_sales = float(row[4])

    if current_sales > max_sales:
        max_sales = current_sales
        best_seller = row

output_file_path = 'bestseller_info.csv'

with open(output_file_path, mode='w', newline = '') as output_file:  
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['Title', 'Author', 'Genre', 'Publisher', 'Sales'])
    csv_writer.writerow([best_seller[0], best_seller[1], best_seller[2], best_seller[3], best_seller[4]])


print("The best-selling book is", output_file_path)





