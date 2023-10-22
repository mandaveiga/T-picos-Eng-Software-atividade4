import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            avgAge(data)
            avgAgeCountry(data, "BR")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def returnSameValue(value):
    return value

def avgAgeCountry(users, country, transform = returnSameValue):
    if hasattr(users, "__len__"):
        avg_age_by_country = {}

        for user in users:
            if user.get("country"):
                if avg_age_by_country.get(user["country"]):
                    if user.get("age"):
                        avg_age_by_country[user["country"]]["avg"] = ((avg_age_by_country[user["country"]]["avg"] * avg_age_by_country[user["country"]]["entries"]) + transform(user["age"])) / (avg_age_by_country[user["country"]]["entries"] + 1)
                        avg_age_by_country[user["country"]]["entries"] += 1
                else:
                    avg_age_by_country[user["country"]] = {
                        "avg": transform(user["age"]),
                        "entries": 1
                    }

        country_avg = avg_age_by_country.get(country)
        return float("{:.2f}".format(country_avg["avg"])) if country_avg else None
    return None

def avgAge(users):
    if hasattr(users, "__len__"):
        counter_valid_users = 0
        ages_sum = 0
        for user in users:
            if user.get("age"):
                counter_valid_users += 1
                ages_sum += user["age"]

        if counter_valid_users == 0:
            return None
        else:
            return float("{:.2f}".format(ages_sum / counter_valid_users))
    return None

def transformToMonths(y):
    if (isinstance(y, int) or isinstance(y, float)) and y > 0:
        return y * 12
    return None

if __name__ == "__main__":
    read_json_file('./users.json')
