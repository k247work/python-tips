
def conv_change(change_price):
    dict_money = { 'PENNY': .01, 'NICKEL': .05, 'DIME': .10,'QUARTER': .25, \
             'HALF DOLLAR': .50, 'ONE': 1.00, 'TWO': 2.00, 'FIVE': 5.00, \
             'TEN': 10.00, 'TWENTY': 20.00, 'FIFTY': 50.00, \
             'ONE HUNDRED': 100.00 }
    list_key = list(dict_money.keys())
    list_val = list(dict_money.values())
    nmax     = len(list_val)
    list_num = [0] * nmax
    list_ret = []
    c_change = change_price
    for i in range(nmax):
        if c_change >= list_val[nmax-1-i]:
            list_num[nmax-1-i] = 1
            c_change -= list_val[nmax-1-i]
            list_ret.append(list_key[nmax-1-i])
    return ",".join(sorted(list_ret))


print(conv_change(11.0))