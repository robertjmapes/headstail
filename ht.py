coins = []

def flip(x):
    if x == 0:
        x = 1
    else:
        x = 0
    return x


# Appending Coins
for  i in range(0,10):
    coins.append(0)
print(coins)

for a in range(len(coins)):

    for i in range(len(coins)):
        if (i+1) % (a+2) == 0:
            coins[i] = flip(coins[i])
            print(f"\n{coins} :: {i}")

print(f"\n{coins}")

