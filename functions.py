from datetime import datetime, timedelta
DOB = datetime(2005,12, 4 ) # Date of Birth
a= datetime.strftime(DOB, "%d/%m/%Y") 
print(a) # Date of Birth in the form of dd/mm/yy
e= int(datetime.strftime(DOB, "%Y"))  # only the year
CD= datetime(2022,11,13) # Current date
b= datetime.strftime(CD, "%d/%m/%Y") 
print(b) # Current Date in the form of dd//mm/yy
f= int(datetime.strftime(CD, "%Y")) # only the year
g= f- e 
j=g//4  
e=CD-DOB
print("Total Days Lived in Earth till the current Date:" , e-timedelta(j)) # including Leap year 