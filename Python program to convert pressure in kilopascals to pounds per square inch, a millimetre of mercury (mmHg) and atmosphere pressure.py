# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimetre of mercury (mmHg) and atmosphere pressure.

def convert_pressure():
    kpa = float(input("Enter pressure in kilopascals (kPa): "))

    if kpa < 0:
        print("Pressure cannot be negative.")
        return

    psi = kpa * 0.145038
    mmhg = kpa * 7.50062
    atm = kpa / 101.325

    print("\nConverted Pressure Values:")
    print(f"PSI   : {psi:.4f} pounds per square inch")
    print(f"mmHg  : {mmhg:.2f} millimetres of mercury")
    print(f"ATM   : {atm:.4f} atmosphere")

convert_pressure()