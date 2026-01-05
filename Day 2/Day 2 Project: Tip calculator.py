#Day 2 project: calculadora de propinas

print ("Welcome to the tip calculator!")

#Captura de valores

Bill = float(input("What was the total bill? $"))
tip_input = int(input("How much tip would you like to give? " + " " + "10," + " " + "12," + " " + "or" + " " " 15?"))
people_split = int(input("How many people to split the bill?"))

#Calculo del pago de propinas y cantidad personas

tip =(tip_input/100)*Bill
pay = (Bill+tip)/people_split

#para que el pago final sea un aproximado de decimales de 2 despues del punto

final_pay = round(pay,2)

#Resultado final de lo que pagaria cada quien de tip

print(f"Each person should pay: ${final_pay} ")

