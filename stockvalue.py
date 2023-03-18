#Define the table header
table = [
  ["item1", 200, 150], 
  ["item2", 50, 300],
  ["item3",  90, 550],
  ["item4",  100, 350], 
  ["item5", 50, 300], 
  ["item6", 50, 600], 
  ["item7", 100, 14.5],
  ["item8", 100, 6.6], 
  ["item9", 20, 1000]
  ]
  # Calculate the amount for each row and add it as a new column
for row in table:
    quantity = row[1]
    unit_price = row[2]
    amount = quantity * unit_price
    row.append(amount)

# Calculate the total amount by summing up the amounts in the last column
total_amount = sum(row[3] for row in table)

# Print the table and the total amount
print("{:<10} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Unit Price", "Amount"))
for row in table:
  print("{:<10} {:<10} {:<10.2f} {:<10.2f}".format(row[0], row[1], row[2], row[3]))
print("Total amount:", total_amount)
