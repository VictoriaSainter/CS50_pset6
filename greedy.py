import cs50

print("O hai! How much change is owed?")

change = cs50.get_float()

while change<0:
    print("How much change is owed?")
    change = cs50.get_float()


changeInCents = round(change*100)
numQuarters = int(changeInCents / 25)
quarterRemainder = changeInCents % 25
numDimes =  int(quarterRemainder / 10)
dimeRemainder = quarterRemainder % 10
numNickels = int(dimeRemainder / 5)
nickelRemainder = dimeRemainder % 5
numPennies =  nickelRemainder
totalNumCoins = numQuarters + numDimes + numNickels + numPennies

print("{}".format(totalNumCoins))
