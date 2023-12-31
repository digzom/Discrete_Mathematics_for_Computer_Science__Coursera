import random

# try to generate dinamically
random_numbers = [
    91,
    128,
    170,
    614,
    849,
    1482,
    1522,
    1761,
    1819,
    1940,
    2136,
    2176,
    2283,
    2386,
    2624,
    2725,
    2907,
    2973,
    3195,
    3304,
    3391,
    3439,
    3453,
    3495,
    3620,
    3653,
    3755,
    3836,
    3974,
    3994,
    4081,
    4246,
    4436,
    4604,
    4624,
    4781,
    4796,
    4801,
    4950,
    5164,
    5331,
    5462,
    5577,
    5637,
    5790,
    5872,
    5933,
    5999,
    6099,
    6231,
    6269,
    6312,
    6350,
    6363,
    6382,
    6477,
    6513,
    6647,
    6811,
    6981,
    7106,
    7137,
    7229,
    7331,
    7394,
    7465,
    7525,
    7584,
    7697,
    7801,
    7811,
    7836,
    7921,
    8043,
    8119,
    8145,
    8180,
    8255,
    8397,
    8502,
    8523,
    8577,
    8687,
    8751,
    8853,
    8909,
    8963,
    8977,
    8981,
    8994,
    9025,
    9070,
    9139,
    9148,
    9224,
    9254,
    9364,
    9380,
    9490,
    9546,
    9675,
    9741,
    9757,
]


def binary_search(number_list, x):
    print(f"Searching {x} in {number_list}...")

    if len(number_list) == 0:
        print(f"The number {x} is not in the list.")
        return False

    if number_list[len(number_list) // 2] == x:
        print("Found!")
        return True
    elif number_list[len(number_list) // 2] < x:
        # it is +1 because we are discarting the previous checking
        return binary_search(number_list[len(number_list) // 2 + 1 :], x)
    else:
        return binary_search(number_list[: len(number_list) // 2], x)


binary_search(random_numbers, 7811)
