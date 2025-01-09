def min_coins(coins, S):
    denomination = [float('inf')] * (S + 1)
    denomination[0] = 0  

    # Iterate it throigh each denomination
    for coin in coins:
        for amount in range(coin, S + 1):
            denomination[amount] = min(denomination[amount], denomination[amount - coin] + 1)

    return denomination[S] if denomination[S] != float('inf') else -1

def main():
    coins = list(map(int, input().split()))
    S = int(input())
    print(min_coins(coins, S))

if __name__ == "__main__":
    main()
