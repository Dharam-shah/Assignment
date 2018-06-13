
first_age = int(input("Enter first age:"))
second_age = int(input("Enter second  age:"))
Third_age = int(input("Enter third age:"))

if first_age > second_age and first_age > Third_age:
    print("Person One is the Oldest Person")

elif first_age < second_age and first_age < Third_age:
    print("Person One is the Youngest Person")

elif second_age > first_age and second_age > Third_age:
    print("Person two is the Oldest Person")

elif second_age < first_age and second_age < Third_age:
    print("Person Two is the Youngest Person")

elif Third_age < first_age and Third_age < second_age:
    print("Person Three is the Youngest Person")

elif Third_age > first_age and Third_age >  second_age:
    print("Person Three is the Oldest Person")
