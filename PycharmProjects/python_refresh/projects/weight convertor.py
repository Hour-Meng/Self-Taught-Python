choice = input("Which would you like to choose? Kilogram or Pound? (K/L): ").lower()
# The rule of thumb
# Use "and" When you want to reject everything that's not one of the valid option
# Use "or" When you want to accept anything that matches at least one valid option
while choice != "k" and choice != "l":
    print("Input is invalid!!")
    choice = input("Which would you like to choose? Kilogram or Pound? (K/L): ").lower()


if choice == "k":
    print("This will convert kilogram to pound")
    weight = float(input("How many kilogram?: "))
    main_unit = "kg"
    convert_unit = "lbs"
    result = weight*2.204

elif choice == "l":
    print("This will convert from pound to kilogram")
    weight = float(input("How many pound?: "))
    main_unit = "lbs"
    convert_unit = "kg"
    result = weight*0.45

print(f"Here is the result {weight}{main_unit} is equal to {result}{convert_unit}")