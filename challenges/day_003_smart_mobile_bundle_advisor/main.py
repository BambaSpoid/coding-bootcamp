print("Welcome to the Smart Mobile Bundle Advisor!")
budget = float(input("What is your budget for a mobile bundle? (in FCFA)\n"))
data_usage = float(input("What is your average monthly data usage? (in GB)\n"))
calls = input("Do you make a lot of phone calls? (yes/no)\n").strip().lower()
is_student = input("Are you a student? (yes/no)\n").strip().lower()


if budget < 1000:
    print("Sorry! No bundle is available for your budget.")
elif budget < 2000:
    bundle_name = "Mini"
    bundle_price = 1000
    bundle_data = 2
elif budget < 3000:
    if data_usage > 2:
        bundle_name = "Data"
        bundle_price = 2000
        bundle_data = 10
    else:
        bundle_name = "Mini"
        bundle_price = 1000
        bundle_data = 2     
elif budget < 5000:
    if calls == "yes":
        bundle_name = "Mix"
        bundle_price = 3000
        bundle_data = 8
    else:
        bundle_name = "Data"
        bundle_price = 2000
        bundle_data = 10
else:
    if data_usage > 10:
        bundle_name = "Max"
        bundle_price = 5000
        bundle_data = 25
    elif calls == "yes":
        bundle_name = "Mix"
        bundle_price = 3000
        bundle_data = 8
    else:
        bundle_name = "Data"
        bundle_price = 2000
        bundle_data = 10
if budget >= 1000:

    student_bonus = is_student == "yes" and budget >= 2000

    if student_bonus:
        bundle_data *= 1.2

    print("--- Recommendation ---")
    print("Recommended bundle:", bundle_name)
    print("Price:", bundle_price, "FCFA")
    print("Data:", bundle_data, "GB")
    print("Student bonus:", student_bonus)
    
    
choose_number = int(input("Enter an integer: "))
if choose_number % 2 == 0:
    print(choose_number, "is an even number.")
else:
    print(choose_number, "is an odd number.")