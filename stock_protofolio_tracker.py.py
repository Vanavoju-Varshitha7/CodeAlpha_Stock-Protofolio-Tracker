stock_list={"AAPL":180,"TSLA":250,"GOOG":700,"YOUT":2700}
print("<<<<<<<<<<<<<<<<<< Stock Protofolio Tracker >>>>>>>>>>>>>>>>>>>>>>>")
num_input=int(input("How many stocks you want to add in the stock_list:"))
sum=0
lst=[]
lst1=[]
for _ in range(num_input):
    stock_name=input("Enter your stock name:").upper()
    
    quantity=int(input(f"enter quantity of {stock_name} stock_name: "))
    if stock_name in stock_list:
        lst.append(stock_name)
        lst1.append(quantity)
        sum+=quantity*(stock_list[stock_name])
              
    else:
        print("The stock name you entered is incorrect.Can you check once.")
    
print("\n------------your protofolio-----------")
if(sum==0):
    print("\n------------------Your total investment value:$0--------------------------")
else:
    for i in range(len(lst)):
        res=stock_list[lst[i]]*lst1[i]
        print(f">{lst[i]}: {lst1[i]} shares@ ${lst1[i]}each = ${res}")
    print(f"\n--------------Total investment value:${sum}------------------")       

save_file=input("Do you want to save this file(yes/no):").lower()
if save_file=="yes":
    file_name=input("enter your filename with .txt or .csv :")
    with open(file_name,"w") as file:
        file.write("Stock,Quantity,Price,Total investment($):\n")
        for i in range(0,len(lst)):
            stock1=lst[i]
            quantity_list=lst1[i]
            calculate_separately= stock_list[lst[i]]*lst1[i]
            file.write(f"{stock1},{quantity_list},{stock_list[lst[i]]},{calculate_separately}\n")
        file.write(f"\n------------Total investment = ${sum}-----------------\n")
        print(f"Your protofolio succesfully saved in {file_name}.")
            

  

