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


if __name__ == "__main__":
    print(make_change_2([1, 5, 10, 25], 62, [0] * 64))
