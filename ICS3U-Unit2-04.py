# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: September 2022
# ICS3U-Unit2-04.py File, learning pseudo-code in python.

import constants


def main():

    # input
    diameter = int(input("Type in the diameter of your pizza in inches: "))

    # process
    pizza_cost = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = pizza_cost * constants.HST

    # output
    print("\nThe cost of the pizza for {0} inches is ${1:,.2f} mm².".format(diameter, total))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
