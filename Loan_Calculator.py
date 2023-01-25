import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="display a square of a given number")
parser.add_argument("--principal", type=int, help="Annuity payment")
parser.add_argument("--periods", type=int, help="Number of periods")
parser.add_argument("--interest", type=float, help="Loan interest")
parser.add_argument("--payment", type=int, help="Monthly payment amount")

args = parser.parse_args()

loan_principal = args.principal
number_of_periods = args.periods
loan_interest = args.interest
payment = args.payment
type = args.type

tab = [loan_principal, number_of_periods, loan_interest, payment, type]

if tab.count(None) >= 2:
    print('Incorrect parameters')
    exit()
elif args.interest == None or args.type == None:
    print('Incorrect parameters')
    exit()
elif args.type != "diff" and args.type != "annuity":
    print('Incorrect parameters')
    exit()
elif args.type == "diff" and payment != None:
    print('Incorrect parameters')
    exit()


if args.type == "diff" and payment == None:
    i = loan_interest / (12 * 100)
    all_payment = 0
    for m in range(1, number_of_periods + 1):
        d = (loan_principal / number_of_periods) + i * (loan_principal - ((loan_principal * (m - 1)) / number_of_periods))
        d = math.ceil(d)
        print(f'Month {m}: payment is {d}')
        all_payment = all_payment + d
    Overpayment = all_payment - loan_principal
    print(f'Overpayment = {Overpayment}')

elif args.type == "annuity" and payment == None:
    i = loan_interest / (12 * 100)
    licz = loan_principal * i * (math.pow(1 + i, number_of_periods))
    mian = math.pow(1 + i, number_of_periods) - 1
    a = licz / mian
    a = math.ceil(a)
    Overpayment = (a * number_of_periods) - loan_principal
    print(f'Your monthly payment = {a}!')
    print(f'Overpayment = {Overpayment}')

elif args.type == "annuity" and loan_principal == None:
    i = loan_interest / (12 * 100)
    mian = (i * (math.pow(1 + i, number_of_periods))) / ((math.pow(1 + i, number_of_periods)) - 1)
    p = payment / mian
    p = int(p)
    Overpayment = (payment * number_of_periods) - p 
    print(f'Your loan principal = {p}!')
    print(f'Overpayment ={Overpayment}')

elif args.type == "annuity" and number_of_periods == None:
    i = loan_interest / (12 * 100)
    n = math.log(payment / (payment - i * loan_principal), 1 + i)
    n = math.floor(n) + 1
    if n % 12 == 0:
        n = n / 12
        n = int(n)
        print(f'It will take {n} years to repay this loan!')
    else:
        r = n % 12
        r = math.ceil(r)
        n = n / 12
        n = math.floor(n)
        print(f'It will take {n} years and {r} months to repay this loan!')
    Overpayment = (n * 12 * payment) - loan_principal
    print(f'Overpayment = {Overpayment}')
