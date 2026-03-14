import json
from checks import *


def run_checks(nutrition_set):

    result = {
        "errors": [],
        "warnings": []
    }

    check_value_over_105(nutrition_set, result)
    check_saturated_fat_greater_than_fat(nutrition_set, result)

    return result


def main():

    with open("dataset.json", "r") as f:
        dataset = json.load(f)

    for i, nutrition_set in enumerate(dataset):

        result = run_checks(nutrition_set)

        print("Example", i + 1)
        print("Input:", nutrition_set)
        print("Output:", result)
        print("-" * 40)


if __name__ == "__main__":
    main()
