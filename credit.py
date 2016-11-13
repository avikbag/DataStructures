#!usr/bin/python


def check(val):
    val = str(val)
    i = -1
    ex = -2
    store = []
    total = 0
    total_rem = 0
    while i >= -len(val):
        total += int(val[i])
        store.append(int(val[ex]))
        i -= 2
        ex -= 2
    #print total
    store = [x*2 for x in store]
    #print store
    for i in store:
        total_rem += (i/10) + (i%10)
    #print total_rem
    check_sum = total + total_rem
    if check_sum%10 == 0:
        return True
    else:
        return False

def main():
    test_vect =[43589795,
                5979853433394390,
                4561325629913234,
                234912912347,
                321932313999,
                4092611758114081,
                75917413300961746711946909974528,
                3432111232230921]
    for value in test_vect:
        if check(value) == True:
            print "%i is a VALID Credit Card Number" %value
        else: 
            print "%i is a NOT VALID Credit Card Number" %value
            
if __name__ == "__main__":
    main()
