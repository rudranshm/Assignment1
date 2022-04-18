dueamount=int(input("Amount borrowed, in rupees : ")) #Taking input of principal amount in rupees

interest=int(input("Interest at which amount is borrowed, in percent : ")) #Taking input of interest in %

pay1=int(input("Amount paid at the end of the first year, in rupees : ")) #Taking input of principal amount in rupees
              
pay2=int(input("Amount paid at the end of the second year, in rupees : ")) #Taking input of principal amount in rupees             
             
dueamount=dueamount+((dueamount*interest)/100) # Amount due at end of first year after adding interest

dueamount=dueamount - pay1 #First payment

dueamount=dueamount+ ((dueamount*interest)/100) # Amount due at end of second year, after making first payment and subsequently adding interest

dueamount=dueamount - pay2 #Second payment

print("The amount of loan outstanding at the end of year two is ", dueamount," rupees." )
