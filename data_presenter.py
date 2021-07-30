

# from matplotlib import pyplot as plt

open_file = open("CupcakeInvoices.csv")

for row in open_file:
    print(row)

for row in open_file:
    row = row.rstrip('\n').split(',')
    for value in row:
        if (value == "Chocolate") or (value == "Vanilla") or (value == "Strawberry"):
            print(value)
total = 0
for row in open_file:
    row = row.rstrip('\n').split(',')
    invoice_total = float(row[3]) * float(row[4])
    total += invoice_total
    print(f"invoice total = ${invoice_total}")
print(f"complete total = ${total}")

open_file.close()
# # Jayden's help

# # arr_x = [1,2,3,4,5]
# # arr_y = [10,20,30,40,50]
# # plt.plot(arr_x, arr_y)
# # plt.show()