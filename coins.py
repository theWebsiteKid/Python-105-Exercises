coins = 0

print "You have %.0f coin(s)." % coins
add_coin = raw_input("Do you want another? \n('yes' or 'no'): ")

while add_coin == "yes":
    coins += 1
    print "You have %.0f coin(s)." % coins
    add_coin = raw_input("Do you want another? \n('yes' or 'no'): ")
else:
    print "Bye!"