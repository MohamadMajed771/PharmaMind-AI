import json
from rapidfuzz import process


def load_drug_names():
    with open("data/drug_names.json", "r", encoding="utf-8") as file:
        return json.load(file)


drug_names = load_drug_names()


def find_drug_match(user_input):
    match = process.extractOne(
        user_input,
        drug_names,
        score_cutoff=70
    )

    if match:
        return match[0]

    return None