import numpy as np

#this code is about Lottery winning chances (Thai lott)
print("lottery test")
try :
    quantity = int(input("quantity : ")) #Number of tickets purchased
except :
    quantity = 1
    print("if there's error, the system will define to 1")

#actually digits
_1prize = [np.random.randint(1,10) for o in range(6)]
_2prize = [[np.random.randint(1, 10) for o in range(6)] for y in range(2)]
_3prize = [[np.random.randint(1, 10) for o in range(6)] for y in range(10)]
_4prize = [[np.random.randint(1, 10) for o in range(6)] for y in range(50)]
_5prize = [[np.random.randint(1, 10) for o in range(6)] for y in range(100)]
prefix3 = [[np.random.randint(1, 10) for o in range(3)] for y in range(2)]
suffix3 = [[np.random.randint(1, 10) for o in range(3)] for y in range(2)]
suffix2 = [np.random.randint(1, 10) for o in range(2)]


#check
money = 0
_1prizeTrue = 0
_1prizeNeiTrue = 0
_2prizeTrue = 0
_3prizeTrue = 0
_4prizeTrue = 0
_5prizeTrue = 0
prefix3True = 0
suffix3True = 0
suffix2True = 0
none = 0


for i in range(quantity): 
    our = []
    print(" ")
    print("lottery ticket number", i+1,":")
    for b in range(6):
        ourrandom = np.random.randint(1, 9)
        print(ourrandom, end="")
        our.append(ourrandom) #our lottery number random is here

    if _1prize == our:
        _1prizeTrue += 1
        money += 6_000_000
    elif our[:5] == _1prize[:5]:
        if our[5] == _1prize[5]-1 or our[5] == _1prize[5]+1:
            _1prizeNeiTrue += 1
            money += 100_000
    elif our in _2prize:
        _2prizeTrue += 1
        money += 200_000
    elif our in _3prize:
        _3prizeTrue += 1
        money += 80_000
    elif our in _4prize:
        _4prizeTrue += 1
        money += 40_000
    elif our in _5prize:
        _5prizeTrue += 1
        money += 20_000
    elif our[:3] in prefix3:
        prefix3True += 1
        money += 4_000
    elif our[:3] in suffix3:
        suffix3True += 1
        money += 4_000
    elif our[:2] == suffix2:
        money += 2_000
        suffix2True += 1
    else :
        none += 1

def add_commas(number):
    if number > 999 or number < -999 :
        number_str = str(number)[::-1]
        result = ",".join(number_str[i:i+3] for i in range(0, len(number_str), 3))
        result = result[::-1]
    else :
        result = number
    return result

print(" ")
print("1st prize won :", _1prizeTrue)
print("1st prize neighbors won : ", _1prizeNeiTrue)
print("2nd prize won :", _2prizeTrue)
print("3rd prize won :", _3prizeTrue)
print("4th prize won :", _4prizeTrue)
print("5th prize won :", _5prizeTrue)
print("3-digit prefix won :", prefix3True)
print("3-digit suffix won :", suffix3True)
print("2-digit suffix won :", suffix2True)
print("Didn't win any prize : ", none)

moneyFromLott = add_commas(money)
moneySpent = add_commas(quantity*100)
profit = add_commas(money - (quantity*100))
print("money spent (100baht per 1 lottery) :", moneySpent)
print("money won from the lottery : ", moneyFromLott)
print("profit :", profit)
