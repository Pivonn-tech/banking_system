print("Welcome to Pivon-Tech Services. Grateful to have you.") 
print("THE NO.1 TECH SOLUTIONS COMPANY WORLDWIDE")


Services = ["1. App development" , "2. Software development" , "3. Training and workshops", "4. Security services", "5. Database Management", "6. Ai and Machine learning", "7. Maintenance and support", "8. API development"]

#Services.insert()

name = input("Enter your name please \n")

print(f"Welcome {name} .We are grad to have you today"
) 
print(f"Below are our services:\n {Services} ")

Order = input(f"what services can we offer to you please {name}? (1-8)\n")

#print(f"Our services are charged at hourly rates {name}. Welcome.")

if Order == "1":
  rate = 10
  print(f"{Services[0]} has an hourly rate of {rate}/hr")
elif Order == "2":
  rate = 9
  print(f"{Services[1]} has an hourly rate of {rate}/hr")
elif Order == "3":
  rate = 8
  print(f"{Services[2]} has an hourly rate of {rate}/hr")
elif Order == "4":
  rate = 7
  print(f"{Services[3]} has an hourly rate of {rate}/hr")
elif Order == "5":
  rate =8
  print(f"{Services[4]} has an hourly rate of {rate}/hr")
elif Order == "6":
  rate = 9
  print(f"{Services[5]} has an hourly rate of {rate}/hr")
elif Order == "7":
  rate = 5
  print(f"{Services[6]} has an hourly rate of {rate}/hr")
elif Order == "8":
  rate = 4
  print(f"{Services[7]} has an hourly rate of {rate}/hr")
else:
  print("Enter valid selection (1-8)")
  


hrs = int(input("How long can you require our services?(hrs)(1-10)\n"))
if hrs < 1 or hrs >10:
  print(f"Enter valid hours please {name} ")
else:
  print(hrs)
  
print("©PIVON-TECH")
  
  