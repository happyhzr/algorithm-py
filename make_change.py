from typing import List


def make_change_1(coin_denoms: List[int], change: int) -> int:
    if change in coin_denoms:
        return 1
    min_coins = float("inf")
    for i in [c for c in coin_denoms if c <= change]:
        num_coins = 1 + make_change_1(coin_denoms, change - i)
        min_coins = min(num_coins, min_coins)
    return min_coins


def make_change_2(
    coin_value_list: List[int], change: int, known_results: List[int]
) -> int:
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    if known_results[change] > 0:
        return known_results[change]
    min_coins = change
    for i in [c for c in coin_value_list if c <= change]:
        num_coins = 1 + make_change_2(coin_value_list, change - i, known_results)
        min_coins = min(min_coins, num_coins)
        known_results[change] = min_coins
    return min_coins


def make_change_3(coin_value_list: List[int], change: int, min_coins: List[int]) -> int:
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


def make_change_4(
    coin_value_list: List[int], change: int, min_coins: List[int], coins_used: List[int]
) -> int:
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used: List[int], change: int) -> None:
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


def main() -> None:
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)

    print(f"Making change for {amnt}")
    print(
        f"Requires the following {make_change_4(clist,amnt,coin_count,coins_used)} coins"
    )
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)


if __name__ == "__main__":
    main()
