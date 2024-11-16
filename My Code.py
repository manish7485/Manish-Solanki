#Title Case
a = input("Enter: ")
b = a.title()
c = a.upper()
d = a.lower()

print(" Choose Case!")
print("Title")
print("Upper")
print("Lower")

e = input("Enter Case: ")

if e == "Title":
	print(f"{b}\n")
elif e == "Upper":
	print(f"{c}\n")
elif e == "Lower":
	print(f"{d}\n")
	
else:
	print("invalid")
	
print(f"Thanks For Using!");