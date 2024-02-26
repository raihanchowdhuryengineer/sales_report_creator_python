sales_record={  'person':input("Enter your name:"),
                'item':input("Enter Item Name:"),
                'price':int(input("Enter Your price:")),
                'quantity':int(input("Enter quantity:")),
                
            }
sales_statement='{} brought {} item {} quantity of price {} Taka and total is {} Taka'

print(sales_statement.format(sales_record['person'],
                            sales_record['item'],
                            sales_record['quantity'],
                            sales_record['price'],
                            sales_record['quantity']*sales_record['price'])
    
      
      )