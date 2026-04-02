# --- User Information Gathering ---
Name = input("Please enter your name")
print(f"Welcome to the Loan Approval system, {Name}. ")

# --- Financial Data Inputs ---
Income = float(input("What is your monthly income? "))
Credit_Score = int(input("What is your credit score?"))
Debts = float(input("Enter your total monthly debt payments (rent, cards, etc.): $"))

# --- Debt-to-Income (DTI) Calculation ---
# Formula: (Total Monthly Debts / Monthly Income) * 100
DTI = Debts / Income * 100

# --- DTI Risk Level Assessment ---
if DTI <= 20:
    print("Exceptional - Minimal Risk")

elif DTI <= 35:
    print("Very Good - Ideal Balance. This is the ideal range for most loans.")

elif DTI <= 43:
    print("Good / Acceptable - Standard Limit. You are still eligible but have less flexibility.")

elif  DTI <= 50:
    print("Fair / Risky - Borderline. You might need a higher credit score to compensate.")

else:
    print("Poor / Critical - Overextended. High probability of rejection as more than half your income is committed.")

# --- Credit Score Eligibility Check ---
if Credit_Score < 300 or Credit_Score > 850:
    print("Error: Invalid Credit Score. Please enter a value between 300 and 850. ")

elif Credit_Score >= 800:
    print("You qualify for our 'Elite Tier' with the best interest rates due to your credit score.")

elif Credit_Score >= 740:
    print("You are a reliable borrower and qualify for competitive rates due to your credit score.")

elif Credit_Score >= 670:
    print("Most lenders will approve your application under our 'Standard Program'.")

# Nested logic to allow lower scores if income is high
elif Credit_Score >= 580:
    if Income >= 4000:
        print("Your score is Fair. Approved due to high monthly income.")
    else:
        print("Your score is Fair, but your income is too low for this risk level. Denied.")


# --- Final Loan Verdict ---
# Approval requires a solid income and a valid credit score
if Income >= 4000 and Credit_Score >= 650:
    print(f"Congratulations, {Name}, Your Loan Is Approved")

last = input("\nPress Enter to exit...")
