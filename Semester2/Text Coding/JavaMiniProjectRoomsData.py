from random import randint
def write():
    data=['Cushion Wifi_5G coffee Morning',"End table Tea set Fireplace Floor lamp Tableet Blinds",\
            "Tea set Fireplace coffee_Morning","Cushion Television Speaker End_table Tea_set"\
            "coffee Morning Wifi_5G Cushion Television Speaker End table Tea set Fireplace Floor lamp Tableet Blinds"\
            "End table Tea set Fireplace Floor lamp Tableet Blinds","Wifi_5G"]
    with open("file.sql", "w") as file:
        for i in range(500):
            file.write("insert into rooms values ("+str(i+9)+","+str(randint(1, 4))+","+str(randint(1, 4))+","+str(randint(1, 5))+","+str(randint(100, 10000))+",'"+data[randint(1,10)%len(data)]+"');\n")
write()