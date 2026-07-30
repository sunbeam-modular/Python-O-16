# requirements for menu driven application
# - get account holder information for a bank 
#   - name, intial deposit, address, phone, email
# - add the account holder data to the list of bank accounts
# - perform bank transactions: deposit, withdrawl
# - print all the account holders information
# - get the list of transactions performed by a customer

# since the customers will get added dynamically
# define the customers collection as a list
customers = []

def add_customer():
    # get customer information from user
    name = input("enter your name: ")
    address = input("enter your address: ")
    phone = input("enter your phone: ")
    email = input("enter your email: ")
    initial_deposit = int(input("enter your initial deposit: "))

    # create a dictionary of all these values and store it in the customers list
    customers.append({
        'account_no': len(customers) + 1,
        'name': name,
        'address': address,
        'phone': phone,
        'email': email,
        'balance': initial_deposit,
        'transactions': []
    })

def deposit(account_no: int, amount: int):
    # find the customer with the account number
    for customer in customers:
        # check if the account number is matching
        if customer['account_no'] == account_no:

            # keep the information about the traction
            customer['transactions'].append({
                'type': 'deposit',
                'amount': amount,
                'balance_before_update': customer['balance'],
                'balance_after_update': customer['balance'] + amount
            })
            
            # update the balance
            customer['balance'] += amount
            
            break

def withdrawl(account_no: int, amount: int):
    # find the customer with the account number
    for customer in customers:
        # check if the account number is matching
        if customer['account_no'] == account_no:

            # check if the customer has valid balance for withdrawl
            if customer['balance'] < amount:
                print("error: invalid balance")
                break

            # keep the information about the traction
            customer['transactions'].append({
                'type': 'withdrwal',
                'amount': amount,
                'balance_before_update': customer['balance'],
                'balance_after_update': customer['balance'] - amount
            })
            
            # update the balance
            customer['balance'] -= amount
            
            break

def print_customer_information(account_no: int):
    # find the customer with the account number
        for customer in customers:
            # check if the account number is matching
            if customer['account_no'] == account_no:
                print(f"name    = {customer['name']}")
                print(f"phone   = {customer['phone']}")
                print(f"email   = {customer['email']}")
                print(f"address = {customer['address']}")
                print(f"balance = {customer['balance']}")
                break

def print_all_transactions(account_no: int):
    # find the customer with the account number
    for customer in customers:
        # check if the account number is matching
        if customer['account_no'] == account_no:

            # print all the tractions
            for transaction in customer['transactions']:
                print(f"{transaction['type']} - {transaction['amount']} - {transaction['balance_before_update']} - {transaction['balance_after_update']}")

            break

while True:
    # print the menu
    print(f"your options are: ")
    print(f"1. register a new account")
    print(f"2. deposit")
    print(f"3. withdrawl")
    print(f"4. print your information")
    print(f"5. print your transactions")
    print(f"6. exit")

    # get the input from user
    choice = int(input("enter your choice: "))

    if choice == 1:
        add_customer()
    elif choice == 2:
        account_no = int(input("enter your account no: "))
        amount = int(input("enter amount to deposit: "))
        deposit(account_no, amount)
    elif choice == 3:
        account_no = int(input("enter your account no: "))
        amount = int(input("enter amount to withdrawl: "))
        withdrawl(account_no, amount)
    elif choice == 4:
        account_no = int(input("enter your account no: "))
        print_customer_information(account_no)
    elif choice == 5:
        account_no = int(input("enter your account no: "))
        print_all_transactions(account_no)
    elif choice == 6:
        print("bye bye, have a nice day")
        break
    else:
        print("invalid option, try again")
    print('-' * 80)