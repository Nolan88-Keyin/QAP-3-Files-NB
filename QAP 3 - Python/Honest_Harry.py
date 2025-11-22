# Description: Car sales tracking program for Honest Harry's used car lot
# Author: Nolan Butt
# Date(s): 2025-11-19


# Define required libraries.
import datetime
import FormatValues as FV

# Define program constants.
LICENSE_FEE_LOW = 75.00
LICENSE_FEE_HIGH = 165.00
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
HST_RATE = 0.15
FINANCING_FEE_PER_YEAR = 39.99
INVOICE_DATE = datetime.datetime.today()


# Define program functions.
def valid_phone():
    while True:
        phone = input("Enter the phone number (999-999-9999): ")
        if phone[0:3].isdigit() and phone[4:7].isdigit() and phone[8:12].isdigit() and len(phone) == 12 and phone[3] == '-' and phone[7] == '-':
            return phone
        else:
            print("** Data Entry Error ** Invalid phone number. Please enter exactly 12 characters in the format 999-999-9999.")


def valid_plate():
    while True:
        plate = input("Enter the plate number (XXX999): ").upper()
        if len(plate) == 6 and plate[0:3].isalpha() and plate[3:6].isdigit():
            return plate
        else:
            print("** Data Entry Error ** Invalid plate number. Please enter exactly 6 characters.")


def generate_receipt_id(first_name, last_name, plate, phone):
    initials = first_name[0].upper() + last_name[0].upper()
    plate_last_chars = plate[-3:].upper()
    phone_last_digits = phone[-4:]
    return f"{initials}-{plate_last_chars}-{phone_last_digits}"

# Main program starts here.
while True:
    
    # Gather user inputs.
    first_name = input("Enter customer first name (END to quit): ").title()
    if first_name == "End":
        break
    
    last_name = input("Enter customer last name: ").title()
    phone = valid_phone()
    plate = valid_plate()
    car_make = input("Enter car make: ").title()
    car_model = input("Enter car model: ").title()
    caryear = input("Enter car year: ")

    while True:
        selling_price = float(input("Enter car price (Less than or equal to $50,000): $"))
        if 0 < selling_price <= 50000:
            break
        else:
            print("** Data Entry Error ** Price must be less than or equal to $50,000.")
            
    while True:
        Trade_in_Amt = float(input("Enter trade-in amount(Must be less than or equal to selling price): $"))
        if Trade_in_Amt <= selling_price:
            break
        else:
            print("** Data Entry Error ** Trade-in amount cannot be greater than selling price.")

    Salesperson = input("Enter salesperson name: ").title()

    # Perform required calculations.
    Customer_Name = first_name[0] + "." + last_name
    Format_phone = f"({phone[0:3]}) {phone[4:7]}-{phone[8:12]}"

    price_after_trade = selling_price - Trade_in_Amt

    if selling_price <= 15000:
        license_fee = LICENSE_FEE_LOW
    else:
        license_fee = LICENSE_FEE_HIGH


    if selling_price <= 20000:
        transfer_fee = selling_price * TRANSFER_FEE_RATE
    else:
        transfer_fee = selling_price * TRANSFER_FEE_RATE
        luxury_tax = transfer_fee * LUXURY_TAX_RATE
        transfer_fee += luxury_tax

    subtotal = price_after_trade + license_fee + transfer_fee

    hst = subtotal * HST_RATE

    total_sales_price = subtotal + hst


    # Display results
    print()
    print(f"Honest Harry Car Sales                     Invoice Date:", INVOICE_DATE.strftime("%Y-%m-%d"))
    print(f"Used Car Sale and Receipt                  Receipt No:  ", generate_receipt_id(first_name, last_name, plate, phone))
    print()
    print(f"                                           Sale price:            {FV.FDollar2(selling_price)}")
    print(f"Sold to:                                   Trade Allowance:       {FV.FDollar2(Trade_in_Amt)}")
    print(f"{'':8s}                                   -----------------------------------")
    print(f"    {Customer_Name:<15s}{'':13s}           Price after Trade:     {FV.FDollar2(price_after_trade)}")
    print(f"    {Format_phone:<15s}{'':12s}            License Fee:           {FV.FDollar2(license_fee)}")
    print(f"                                           Transfer Fee:          {FV.FDollar2(transfer_fee)}")
    print(f"{'':8s}                                   -----------------------------------")
    print(f"Car Details:                               Subtotal:              {FV.FDollar2(subtotal)}")
    print(f"                                           HST:                   {FV.FDollar2(hst)}")
    print(f"{f'    {caryear} {car_make} {car_model}':<43}-----------------------------------")
    print(f"                                           Total sales price:     {FV.FDollar2(total_sales_price)}")
    print("------------------------------------------------------------------------------")

    # First payment date
    current_date = INVOICE_DATE
    if current_date.day >= 25:
        if current_date.month == 12:
            first_payment_date = datetime.date(current_date.year + 1, 2, 1)
        else:
            first_payment_date = datetime.date(current_date.year, current_date.month + 2, 1)
    else:
        if current_date.month == 12:
            first_payment_date = datetime.date(current_date.year + 1, 1, 1)
        else:
            first_payment_date = datetime.date(current_date.year, current_date.month + 1, 1)

    print(f"                           Financing     Total        Monthly")
    print(f" # Years    # Payments        Fee        Price        Payment")
    print(f" ------------------------------------------------------------")
    
    # Payment schedule loop
    for years in range(1, 5):
        monthly_payments = years * 12
        financing_fee = FINANCING_FEE_PER_YEAR * years
        total_price = total_sales_price + financing_fee
        monthly_payment = total_price / monthly_payments
        
        print(f"     {years}           {monthly_payments:2d}         {FV.FDollar2(financing_fee):>8s}   {FV.FDollar2(total_price):>10s}   {FV.FDollar2(monthly_payment):>9s}")
    
    print(f" ------------------------------------------------------------")
    print(f" First payment date: {first_payment_date.strftime('%Y-%m-%d')}")
    print(f"--------------------------------------------------------------")
    print(f"                 Best used cars at the best prices! ")
    
    
    break




