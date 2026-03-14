# ---------- trace amounts ----------

trace_amounts = {
    "fat": 0.5,
    "carbohydrates": 0.5,
    "carbohydrates-total": 0.5,
    "sugars": 0.5,
    "proteins": 0.5,
    "saturated-fat": 0.1,
    "salt": 0.0125
}


# ---------- helpers ----------

def modifier_is_ignored(nutrient_data):
    modifier = nutrient_data.get("modifier", "")
    return modifier in ["<", "~", "≤"]


def min_nutrient_value(nutrients, nutrient_name):
    nutrient_data = nutrients.get(nutrient_name, {})

    if modifier_is_ignored(nutrient_data):
        return 0

    return nutrient_data.get("value", 0)


def nutrient_total_less_than_parts(nutrients, total_name, part_names):

    total_data = nutrients.get(total_name, {})

    if modifier_is_ignored(total_data):
        return False

    total = total_data.get("value")

    if total is None:
        return False

    if total == 0:
        total = trace_amounts.get(total_name, 0)

    parts_sum = 0

    for part in part_names:
        parts_sum += min_nutrient_value(nutrients, part)

    tolerance = 0.01
    if total >= 10:
        tolerance = 0.1

    if round(parts_sum, 2) > round(total + tolerance, 2):
        return True

    return False


# ---------- checks ----------

def check_value_over_105(nutrition_set, result):

    per = nutrition_set["per"]
    nutrients = nutrition_set["nutrients"]
    set_id = nutrition_set["set_id"]

    for nutrient_name, nutrient_data in nutrients.items():

        value = nutrient_data.get("value")

        if value is None:
            continue

        if (per == "100g" or per == "100ml"):

            if ("energy" not in nutrient_name) and ("footprint" not in nutrient_name) and (value > 105):

                tag = f"en:{set_id}-value-over-105-{nutrient_name}"
                result["errors"].append(tag)


def check_saturated_fat_greater_than_fat(nutrition_set, result):

    nutrients = nutrition_set["nutrients"]
    set_id = nutrition_set["set_id"]

    if nutrient_total_less_than_parts(nutrients, "fat", ["saturated-fat"]):

        tag = f"en:{set_id}-saturated-fat-greater-than-fat"
        result["errors"].append(tag)
