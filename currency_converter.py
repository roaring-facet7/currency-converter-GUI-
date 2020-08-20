import time

def data_to_dict():
    data = open('data.csv', 'r')
    data.readline()
    curr_dict = {}
    for row in data:
        cntry, val = row.split(',')
        curr_dict[cntry] = float(val)
    return curr_dict


def f_to_INR(code,val):
    # print("Foreign to INR")
    # code = input("Enter the 3 digit code of your country: ")
    # val = float(input("Enter the amount of money in foreign currency: "))
    curr = data_to_dict()
    conv_fac = curr['IND']/curr[code]
    res = val * conv_fac
    return res


def INR_to_f(code,res):
    curr = data_to_dict()
    conv_fac = curr['IND'] / curr[code]
    val = res/conv_fac
    return val

'''
def main():
    print("Choose one of the following options:-")
    print("1. Convert foreign currency to INR")
    print("2. Convert INR to foreign currency")
    opt = int(input())

    if opt == 1:
        f_to_INR()
    elif opt == 2:
        INR_to_f()
    else:
        print("Dummy choose 1 or 2")
'''
