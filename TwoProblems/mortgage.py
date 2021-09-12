# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
mnthly_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
total_num_of_instlmnt_paid=0

while principal > 0:
    if principal < mnthly_payment:
        total_paid = total_paid + round(principal, 2)
        principal = int(principal - round(principal, 2))
        total_num_of_instlmnt_paid=total_num_of_instlmnt_paid+1
        
    elif total_num_of_instlmnt_paid >= extra_payment_start_month-1 and total_num_of_instlmnt_paid < extra_payment_end_month:
        principal = principal * (1+rate/12) - (mnthly_payment+extra_payment)
        total_paid = total_paid + (mnthly_payment+extra_payment)
        total_num_of_instlmnt_paid=total_num_of_instlmnt_paid+1

    else:
        principal = principal * (1+rate/12) - mnthly_payment
        total_paid = total_paid + mnthly_payment
        total_num_of_instlmnt_paid=total_num_of_instlmnt_paid+1

##    #print... total number of instlmnt paid so far or the numer of months
##    print(total_num_of_instlmnt_paid, end=' ')
##    #print... total amount paid so far
##    print(total_paid, end=' ')
##    #print... remaining principal
##    print(principal)
    print(f'{total_num_of_instlmnt_paid:3d} {total_paid:12.5f} {principal:12.5f}')
