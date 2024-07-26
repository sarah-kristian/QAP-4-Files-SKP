# QAP4: Python - Online Auto Insurance Portal for One Stop Insurance
# Author: Sarah Perry
# Date(s): Jul 19 - Jul 26, 2024


# Define required libraries.
from datetime import datetime
import time
from display_handler import dollar_dsp, phone_num_dsp, pc_add_dsp
from input_handler import get_user_contact, get_user_info, get_year_between, get_user_int, get_plate_number, get_list_option, get_user_yesno, get_user_float
from utility_module import clear_screen, get_last_id, progress_dots, check_password


# Define program constants and global variables
const_file = 'Const.dat' # This file will store the default values
data_file = 'Data.dat'   # This file will store the policy details
cust_file = 'Cust.dat'   # This file will store the customer details
car_file = 'Car.dat'     # This file will store the car details
claims_file = 'Claims.dat' # This file will store the claims details


TRY_AGAIN_MSG = "\nPlease enter your information again."
TODAY = datetime.now()
NUM_MONTHLY_PAYMENTS = 8

# Get default values from the constants file
file = open(const_file, 'r')
const = file.readlines()     
NEXT_ID_NUM = int(const[0])
BASIC_PREMIUM = float(const[1])
DISC_RATE = float(const[2])
EXTRA_LIABILITY_FEE = float(const[3])
GLASS_FEE = float(const[4])
LONER_FEE = float(const[5])
HST_RATE = float(const[6])
PROCESSING_FEE = float(const[7])
file.close()


# initialize variables
long_line = "-"
short_line = "-"


########################################################################################
# Define utility functions
########################################################################################

def get_new_id(file_path, default_id):
    # Get the next available ID from a file
    # If the file does not exist, return the default ID

    last_id = get_last_id(file_path, default_id)
    return last_id + 1



def update_policy_number(file_path, next_id):
    # Update the next available ID in the file
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

        lines[0] = str(next_id) + "\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)


def print_row(rows):
    # Print the rows of a CSV table (or a list with comma delimited values)
    for row in rows:
        print(row)


def get_extra_cost(detail, fee): 
    # Get the cost of an extra insurance option
    if detail == "Y":
        cost = fee
        cost_dsp = dollar_dsp(fee)
    else:
        cost = 0.00
        cost_dsp = ""
    return cost, cost_dsp



########################################################################################
# Define introduction display
########################################################################################

def print_QAP_intro():
    clear_screen()
    print("""\n************************************************************
          
       Welcome to Sarah's final Python QAP project!
          
************************************************************""")
    
    print("\nAs we near the end of the semester, I've made this project a bit more complex.")    
    print("\nFor ease of testing and grading, I've added some default values to avoid inputting multiple values.") 
    print("You can use these responses to trigger default values:")
    print("\n1. For customer ID, enter: 1001")
    print("2. For customer password, enter: test")
    print("3. For car make, enter: test")
    print("\nThis will retrieve a customer with three claims and create mock values for a car description.")
    input("\nPress ENTER when ready to continue...")
    clear_screen()


def print_intro():
    # Header: Welcome to Our Online Auto Insurance Portal!
    clear_screen()
    print("\n************   WELCOME TO ONE STOP AUTO INSURANCE!   ************ \n")

    print("Our online platform is designed to make purchasing auto insurance convenient for you.")
    print("We offer tailored coverage, competitive rates, and a quick and easy process.")
    print()
    print("Get started today and enjoy peace of mind on the road!")
    print("")

    print("\nSteps to Get Started:")
    print("-----------------------------------------------------------------------------------")
    print("1) NEW CUSTOMER: Create an account to access our services.")
    print("2) RETURNING CUSTOMER: Sign in using your account number and password.")
    print("3) PROVIDE VEHICLE DETAILS: Enter details about your car for accurate quotes.")
    print("4) CUSTOMIZE YOUR COVERAGE: Choose the coverage options that suit you best.")
    print("5) GET A QUOTE: Receive an instant quote based on your inputs.")
    print("6) PURCHASE YOUR POLICY: Complete the payment to finalize your insurance.")
    print()
    print()



########################################################################################
# define customer functions
########################################################################################

# Create customer account
def create_customer_account():
    # Display user preamble
    print("Welcome! Let's create your account.\n")

    # Get user ID & password
    customer_id = get_new_id(cust_file, 35)
    print(f"Your customer ID is: {customer_id}")
    password = input("Create a password: ")
    while True:
        password_check = input("Re-enter your password: ")
        if password == password_check:
            break
        else:
            print("Passwords do not match. Please try again.")

    # Get user contact information
    print("\nTo set up your account, we need some information about you.\n")
    user_contact = get_user_contact()
    fname, lname = user_contact["first_name"], user_contact["last_name"]
    str_address, city, province, postal_code = user_contact["street_add"], user_contact["city_add"], user_contact["prov_add"], pc_add_dsp(user_contact["pc_add"])
    phone_number = phone_num_dsp(user_contact["phone_num"])

    customer_info = [customer_id, fname, lname, str_address, city, province, postal_code, phone_number]

    # Save the customer information to the file
    with open(cust_file, 'a') as file:
        file.write(f"{customer_id}, {fname}, {lname}, {str_address}, {city}, {province}, {postal_code}, {phone_number}, {password}\n")
    return customer_info


# Get the customer information from existing customer file
def get_existing_customer():

    # Display user preamble
    print("Welcome back! Please enter your 4 digit customer ID and password to access your account.\n")
    print("If you are testing the program and want default values:")
    print("    Customer ID: 1001")
    print("    Password: test\n")

    # Get user contact ID
    while True:
        customer_id = get_user_info("Customer ID: ")
        if len(customer_id) == 4:
            break
        else:
            print("Invalid customer ID. Please try again.\n")

    # Read the customer details from the file
    with open(cust_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if str(customer_id) in line:
                customer_info = line.split(',')
                fname = customer_info[1]
                lname = customer_info[2]
                str_address = customer_info[3]
                city = customer_info[4]
                province = customer_info[5]
                postal_code = customer_info[6]
                phone_number = customer_info[7]
                password = customer_info[8].strip()
                break
            else:
                print("Customer ID not found. Please try again.")
                customer_id = get_user_info("Customer ID: ")

    # Check the password
    check_password(password)

    customer_info = [customer_id, fname, lname, str_address, city, province, postal_code, phone_number]
    return customer_info


# Create new customer account or retrieves existing customer information
def get_customer_info():

    customer_status = get_list_option("Are you a new (N) or returning (R) customer?: ", ["N", "R"]).upper() 
    clear_screen()
    print("\n************   CUSTOMER INFORMATION   ************ \n")
    
    if customer_status == "N":
        customer_info = create_customer_account()
    
    if customer_status == "R":
        customer_info = get_existing_customer()

    return customer_info


########################################################################################
# Define vehicle functions
########################################################################################

def get_vehicle_info():
    clear_screen()
    # Get vehicle information from the user

    # Initialize the vehicle information list
    vehicle_info = []

    # Display user preamble
    print("\n************   VEHICLE INFORMATION   ************ \n")
    num_cars = get_user_int("How many vehicles would you like to insure? ")

    # Get vehicle information for each car
    for car_num in range (1, num_cars +1):
        if num_cars == 1:
            car_msg = "\nPlease provide the following details about your vehicle. \n   If you are testing the program, for MAKE, enter: test\n"
        else:
            car_msg = f"\nPlease provide the following details about Vehicle {car_num}. \n   If you are testing the program, for MAKE, enter: test\n"

        print(car_msg)
        make =  get_user_info("Make: ").title()
        if make == "Test":
            model = "Test"
            year = 2022
            value = 30000.00
            plate_num = "ABC12" + str(car_num)

        else:
            model = get_user_info("Model: ").title()
            year =  get_year_between("Year: ", '1900', 'current')
            value = get_user_float("Estimated Value: $")
            value = f'${value:,.2f}'
            plate_num = get_plate_number("License Plate Number: ")
            plate_num = plate_num[0:3] + " " + plate_num[3:6]
                
    # Get user insurance options for each car
        print("\nWould you like to include any of the following optional insurance options?")
        extra_liability = get_user_yesno("    Extra liability coverage? (Y/N): ")[0].upper()
        glass_coverage =  get_user_yesno("    Glass coverage? (Y/N): ")[0].upper()
        loner_coverage =  get_user_yesno("    Loner car coverage? (Y/N): ")[0].upper()

    # Add the vehicle information to the list
        car = [plate_num, make, model, year, value, extra_liability, glass_coverage, loner_coverage]
        vehicle_info.append(car)
        clear_screen()
        
    return vehicle_info


########################################################################################
# Define insurance functions
########################################################################################

# Get the extra insurance costs (including discounts and extra options) for each car
def get_insurance_costs(vehicle_info):
    # Get the extra insurance costs for the car

    # initialize the list to store the insurance costs
    insurance_costs = []

    for car in vehicle_info:
        extra_liability = car[5]
        glass_coverage = car[6]
        loner_coverage = car[7]

        # Calculate the insurance premiums of car
        if car == vehicle_info[0]:
            insurance_premiums = BASIC_PREMIUM 
        else: 
            insurance_premiums = BASIC_PREMIUM * (1 - DISC_RATE)

        liability_cost, liability_dsp = get_extra_cost(extra_liability, EXTRA_LIABILITY_FEE)
        glass_cost, glass_dsp = get_extra_cost(glass_coverage, GLASS_FEE)
        loner_cost, loner_dsp = get_extra_cost(loner_coverage, LONER_FEE)

        extra_costs = liability_cost + glass_cost + loner_cost
        total_premiums = insurance_premiums + extra_costs

        car_costs = [insurance_premiums, liability_cost, glass_cost, loner_cost, extra_costs, total_premiums, liability_dsp, glass_dsp, loner_dsp]
        insurance_costs.append(car_costs)

    return insurance_costs


# Create a policy quote for the customer
def create_policy_quote(policy_num, insurance_costs):

    print("\n************   POLICY QUOTE   ************ \n") 

    # Calculate the total cost of the insurance policy
    sum_premiums = sum([detail[0] for detail in insurance_costs])
    sum_extra_cost = sum([detail[-5] for detail in insurance_costs])
    subtotal = sum_premiums + sum_extra_cost
    hst = subtotal * HST_RATE
    policy_quote = subtotal + hst

    quote_info = [policy_num, sum_premiums, sum_extra_cost, subtotal, hst, policy_quote]

    # Display the quote for review
    print(f"{'Total Premiums:':<20s} {dollar_dsp(sum_premiums):>10}")
    print(f"{'Total Extra Cost:':<20s} {dollar_dsp(sum_extra_cost):>10}")
    print(f"{'HST:':<20s} {dollar_dsp(hst):>10}")
    print(f"{'Total Cost:':<20s} {dollar_dsp(policy_quote):>10}")
    print(f"* note that this does not include a processing fee of ${PROCESSING_FEE:,.2f} for monthly payments.")
    print()

    return quote_info


# Get the payment details from the user
def get_payment_details():
    print("\n************   PAYMENT DETAILS   ************ \n")

    # Get the payment options from the user and calculate the payment details
    pay_option = get_list_option("How would you like to pay? Full (F), Monthly (M), or with Down Payment (D): ", ["F", "M", "D"]).strip().upper()[0]
    if pay_option == "D":
        downpayment = get_user_float("Enter the down payment amount: ")
    else:
        downpayment = 0.00

    # Calculate the first payment date
    first_payment_month = TODAY.month + 1
    if first_payment_month > 12:
        first_payment_month = 1
        first_payment_year = TODAY.year + 1
    else:
        first_payment_year = TODAY.year

    first_payment_date = datetime(first_payment_year, first_payment_month, 1)
    first_payment_date_dsp = datetime.strftime(first_payment_date, "%Y-%m-%d")

    # Calculate the last payment date
    last_payment_month = first_payment_month + NUM_MONTHLY_PAYMENTS - 1
    last_payment_year = first_payment_year
    if last_payment_month > 12:
        last_payment_month -= 12
        last_payment_year += 1
    last_payment_date = datetime(last_payment_year, last_payment_month, 1)
    last_payment_date_dsp = datetime.strftime(last_payment_date, "%Y-%m-%d")
    payment_method = input("\nHow would you like to pay for your policy, credit or cash? ") # not needed for this version
    print()

    payment_details = [pay_option, downpayment, first_payment_date_dsp, last_payment_date_dsp]

    return payment_details



########################################################################################
# Define receipt functions
########################################################################################

def generate_top_rows(customer_info, policy_costs):

    # Process record: unpack and ID and customer information & create relevant rows for top of receipt
    policy_num = policy_costs[0]
    customer_id = customer_info[0]
    fname = customer_info[1]
    lname = customer_info[2]
    str_address = customer_info[3]
    city = customer_info[4]
    province = customer_info[5]
    postal_code = customer_info[6]
    postal_code = pc_add_dsp(postal_code)
    phone_number = customer_info[7]
    phone_number = phone_num_dsp(phone_number)

    # Format record: format the rows for the top of the receipt
    ID_rows = [ f"Policy Number: {policy_num}"
            ,f"Customer ID:   {customer_id}"
            ,""
            ,f"Inv Date:    {TODAY.strftime("%Y-%m-%d")}"
            ,""]

    cust_info_rows =[fname + " " + lname
                    , str_address
                    , city + ", " + province
                    , postal_code
                    , phone_number]

    # create a list of the top rows
    top_rows = zip(ID_rows, cust_info_rows)

    return top_rows



def generate_line_items(vehicle_info, insurance_costs):
    
    # Initialize an empty list to store the car details
    detail_rows = []    #create an empty list to store the car details

    # Process records
    # Merge information for each vehicle into one list (details)

    details = [item1 + item2 for item1, item2 in zip(vehicle_info, insurance_costs)]   

    # Process each car in the details list
    for detail in details:
        # extract information from car_details
        make = detail[1]
        model = detail[2]
        year = detail[3]
        extra_liability = detail[5]
        glass_coverage = detail[6]
        loner_coverage = detail[7]
        insurance_premiums = detail[8]
        liability_dsp = detail[-3]
        glass_dsp = detail[-2]
        loner_dsp = detail[-1]


    # Format records: Create the detail rows for each car and append to the detail_rows list
        row1 = [f"{make} {model} {year}", "Insurance Premimus", " ", dollar_dsp(insurance_premiums)]
        row2 = ["", "Extra Liability", extra_liability, liability_dsp]
        row3 = ["", "Glass Coverage", glass_coverage, glass_dsp]
        row4 = ["", "Loner Coverage", loner_coverage, loner_dsp]

        for row in [row1, row2, row3, row4]:
            detail_rows.append(row)
    
    return detail_rows



def generate_total_rows(policy_costs, payment_details):

    # Process data: Unpack policy costs and create payment rows

    subtotal = policy_costs[3]
    hst = policy_costs[4]
    payment_amt = policy_costs[5]

    
    pay_option = payment_details[0]
    downpayment = payment_details[1]
    payment_amt = dollar_dsp(payment_amt)

    total_cost = subtotal + hst + PROCESSING_FEE - downpayment

    # Create items for each total rows

    total_row0 = ["", "Subtotal", "", dollar_dsp(subtotal)]
    total_row1 = ["", "HST", "", dollar_dsp(hst)]
    total_row2 = ["", "Processing Fee", "", dollar_dsp(PROCESSING_FEE)]
    total_row3 = ["", "Downpayment", "", "-"+dollar_dsp(downpayment)]
    total_row4 = ["", "Total", "", dollar_dsp(total_cost)]

    # Create list of total rows
    total_rows = [total_row0, total_row1, total_row2, total_row3, total_row4]


    if pay_option == "F":
        total_rows.remove(total_row2)

    if downpayment == 0:
        total_rows.remove(total_row3)

    return total_rows


def generate_payment_row(payment_details, policy_costs):

    # process data: unpack payment details and policy costs

    payment_amt = policy_costs[5]
    pay_option = payment_details[0]
    first_payment_date = payment_details[2]
    last_payment_date = payment_details[3]
    payment_amt = dollar_dsp(payment_amt)

    # Format record: Unpack payment options and create payment rows
    if pay_option == "F":
        payment_row = f"""
Full payment amount, {payment_amt}, due on {first_payment_date}.
        """
    else:
        payment_row = f"""
Monthly payment amount: {payment_amt}
First payment due {first_payment_date}  Last payment due {last_payment_date}
"""
    return payment_row



def generate_claim_table(customer_id):

    # definte local variables
    width = [10, 10, 9]
    full_width = width[0] + width[1] + width[2] + 3
    long_line = "-" * full_width


    # Initialize the claim table
    claim_table = []

    # Generate report headings

    title = f"{'PREVIOUS CLAIMS':^{full_width}}"
    header_rows = [title
                   ,long_line
                   ,f"{'Claim #':<{width[0]}} {' Claim Date':<{width[1]}} {'Amount':>{width[2]}}"
                   ,long_line]


    # Append the header rows to the claim table
    for row in header_rows:
        claim_table.append(row)


    # Read the claims file and get the claims information for the customer
    # and append to the claim table, formatting where applicable

    with open(claims_file, "r") as file:
        # Open the data file.
        lines = file.readlines()
        for line in lines:
            if f"{customer_id}" in line:
                field = line.split(',')
                claim_num = field[0]
                claim_date = field[1]
                claim_amt = '$' + field[2]
                customer_id = field[4]
                claims_info = f"{claim_num:<{width[0]}} {claim_date:<{width[1]}} {claim_amt:>{width[2]}}"
                claim_table.append(claims_info)

    return claim_table


# Generate policy report
def print_receipt(customer_info, vehicle_info, insurance_costs, policy_costs, payment_details):
    # Define table formatting
    width = [20, 20, 3, 12]
    full_width = width[0] + width[1] + width[2] + width[3] + 3
    long_line = '-' * full_width
    short_line = '-' * 10
    half_line = f"{'':<{width[0]}} {'-' * width[1]} {'':<{width[2]}} {short_line:>{width[3]}}"

    customer_id = customer_info[0]

    # Generate header rows
    title = "One Stop Auto Insurance Receipt"
    main_title = [long_line, f"{title:^{full_width}}".upper(), long_line]
    details_col_titles = [long_line
    ,f"{'Car details':<{width[0]}} {'Item':<{width[1]}} {'Y/N':<{width[2]}} {'Cost':^{width[3]}}"
    ,long_line]
    

    # Generate the rows for the receipt
    top_rows = generate_top_rows(customer_info, policy_costs)
    detail_rows = generate_line_items(vehicle_info, insurance_costs)
    total_rows = generate_total_rows(policy_costs, payment_details)
    long_line
    payment_row = generate_payment_row(payment_details, policy_costs)
    long_line
    claim_table = generate_claim_table(customer_id)


    # Create the footer
    footer = [long_line, f"{'Thank you for choosing One Stop Auto Insurance!':^{full_width}}", long_line]

    # Print the receipt
    print_row(main_title)
    print()

    for ID, cust in top_rows:
        print(f"{ID:<30} {cust:<30}")
    print()

    print_row(details_col_titles)
    for row in detail_rows:
        print(f"{row[0]:<{width[0]}s} {row[1]:<{width[1]}s} {row[2]:<{width[2]}} {row[3]:>{width[3]}}")
    print(half_line)
    for row in total_rows[:-1]:
        print(f"{row[0]:<{width[0]}s} {row[1]:>{width[1]}s} {row[2]:<{width[2]}} {row[3]:>{width[3]}}")
    print(half_line)
    for row in total_rows[-1:]:
        print(f"{row[0]:<{width[0]}s} {row[1]:>{width[1]}s} {row[2]:<{width[2]}} {row[3]:>{width[3]}s}")

    print(long_line)
    print(payment_row)
    print(long_line)

    print_row(claim_table)

    print_row(footer)


########################################################################################
# Define main function
########################################################################################

def main():
    # Define program variables
    default_id = NEXT_ID_NUM
    policy_num = get_new_id(data_file, default_id)

    # Display the introduction
    print_QAP_intro()

    # Display the welcome message
    print_intro()

    # Start the main loop
    while True:

        # Get customer personal information
        customer_info = get_customer_info()
        customer_id = customer_info[0]

        # Get vehicle information
        time.sleep(2)
        clear_screen()
        vehicle_info = get_vehicle_info()
        num_cars = len(vehicle_info)

        # Get insurance costs for each car
        insurance_costs = get_insurance_costs(vehicle_info)

        # Create quote for the policy
        clear_screen()
        quote_info = create_policy_quote(policy_num, insurance_costs)

        # Ask the user if they want to continue with the policy
        go_on = get_user_yesno("Do you want to continue with this policy (Y/N)?: ")
        if go_on == "N":
        # End the program
            break

        if go_on == "Y":
            policy_costs = quote_info
            sum_premiums = policy_costs[1]
            sum_extra_cost = policy_costs[2]
            subtotal = policy_costs[3]
            hst = policy_costs[4]

        # Get payment details
            clear_screen()
            payment_details = get_payment_details()
            pay_option = payment_details[0]
            downpayment = payment_details[1]
            first_payment_date = payment_details[2]

        # Calculate the payment options
            if pay_option == "F":
                processing_fee = 0.00
                num_payments = 1
            else:
                processing_fee = PROCESSING_FEE
                num_payments = NUM_MONTHLY_PAYMENTS

            payment_amt = (subtotal - downpayment + processing_fee) / num_payments

        # Revise policy costs

            policy_costs.pop()
            policy_costs.append(payment_amt)

        # Display the receipt
            progress_dots("Generating Receipt...")
            time.sleep(2)

            clear_screen()
            print_receipt(customer_info, vehicle_info, insurance_costs, policy_costs, payment_details)

        # Save the policy details to relevant files
            with open(car_file, "a") as file:
                for detail in vehicle_info:
                    file.write(f"{detail[0]}, {detail[1]}, {detail[2]}, {detail[3]}, {detail[4]}, {customer_id}, {policy_num}, {detail[5]}, {detail[6]}, {detail[7]}\n")
                    
            with open(data_file, "a") as file:
                file.write(f"{policy_num}, {num_cars}, {sum_premiums}, {sum_extra_cost}, {hst}, {pay_option}, {downpayment}, {payment_amt}, {num_payments}, {first_payment_date}, {customer_id}\n")

        # Update the policy number
            next_id = policy_num + 1
            update_policy_number(const_file, next_id)

        # Provide option to continue for another customer
            go_on = get_user_yesno("\nWould you like to continue for another customer (Y/N)?: ")

            if go_on == "Y":
            # Loop back to start a new policy
                print("\nLet's start a new policy!\n")
                time.sleep(2)
                clear_screen()

            else:
        # End the program
                print("\nExiting the program...")
                break

    # Housekeeping
    print("\nThank you for using our program. Have a great day!\n")

if __name__ == "__main__":
    main()