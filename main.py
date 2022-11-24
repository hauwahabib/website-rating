print("🌟Website Rating🌟")
print()
website = input("Input the website name: ")
print()
url = input("Input the URL: ")
print()
description1 = input("Input your description: ")
print()
star = input("Input the star rating out of 5: ")
print()
myUser = {"name":website,"URL":url,"description":description1,"rating":star}
for name,value in myUser.items():
  print(f"{name} :{value}")
