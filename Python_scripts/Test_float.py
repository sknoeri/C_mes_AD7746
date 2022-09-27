import matplotlib.pyplot as plt

string = "23aasad039"

print("The entered string : " + str(string))

r = string.replace('.', '', 1).isnumeric()

print("Is string a float number ? : " + str(r))