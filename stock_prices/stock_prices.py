import argparse


def find_max_profit(prices):
    """
    prices - [list] - received as input in the form of integers seperated by a space
    

    - We have to buy a stock first, before selling it (duh)
    - Start with buy price at index 0
    - Iterate thru list and calculate highest profit by selling at each index
    - Capture max profit
    - Move buy cursor to next index, repeat iteration
    - Return max profit


    """

    max_profit = float("-inf")

    for buy_index in range(0, len(prices)):
        for sell_index in range(buy_index + 1, len(prices)):
            profit = prices[sell_index] - prices[buy_index]
            if max_profit < profit:
                max_profit = profit

    return max_profit


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

