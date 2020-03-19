#!/usr/bin/env python

import sys


def rock_paper_scissors(r):
    """
    - Identify base cases
        - 0 - append round choices list to master result list
        - Equation is n^r where n is choices and r is plays
            - Each index must have 3 ** n / 3 of each choice 
        - rock_paper_scissors needs to hold choices and master result list
        - Helper func will run actual recursive functionality
    """

    choices = [
        "rock",
        "paper",
        "scissors",
    ]

    choices_len = len(choices)

    # n^r where n is choices and r is plays
    outer_len = choices_len ** r

    # Outer cursor for appending choice lists
    outer_cursor = 0

    # Prebuild array with calculated length from equation above
    result = [[]] * outer_len

    def getCombinations(rounds, roundChoice=[]):
        nonlocal outer_cursor
        # Base case - No more work to be done so append resulting round of choices to final result list
        if rounds == 0:

            # Append round choices
            result[outer_cursor] = roundChoice

            # Move to next index
            outer_cursor += 1
            return

        # n rounds, 3 choices, n^r where n is choices and r is plays
        for i in range(0, choices_len):
            getCombinations(rounds - 1, roundChoice + [choices[i]])

    # Call to start recursion chain
    getCombinations(r)

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

