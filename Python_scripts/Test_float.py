import pandas as pd
string = "23aasad039"
a = [1,2,3,4,454,65]
data=pd.DataFrame(a)
data.to_csv('test.csv')
print("The entered string : " + str(string))

r = string.replace('.', '', 1).isnumeric()

print("Is string a float number ? : " + str(r))