import re
str1 = "i'm prince kumawat"
matches1 = re.findall("prince",str1)
print(matches1)
matches2 = re.findall("i'm",str1)
print(matches2)
matches3 = re.findall("Pri",str1)
print(matches3)
matches4 = re.findall("kumawat",str1)
print(matches4)