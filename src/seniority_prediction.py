import src.config as config


def check_if_title_contains_keyword(title, list_of_keywords):
    for keyword in list_of_keywords:
        if keyword in title.lower():
            return 1
    return 0


def get_title_parts_info(title):
    has_title_parts = {
        'c_level': 0,
        'vp_level': 0,
        'director_level': 0,
        'manager_level': 0,
    }

    for level, list_of_keywords in config.relevant_title_parts_per_management_level.items():
        has_title_parts[level] = check_if_title_contains_keyword(title, list_of_keywords)

    for level, substrings_to_exclude in config.substrings_to_exclude_per_management_level.items():
        for sub_s in substrings_to_exclude:
            if has_title_parts[level] == 1 and sub_s in title:
                has_title_parts[level] = 0

    return has_title_parts


def get_prediction(title_parts_info):
    if title_parts_info['c_level'] == 1:
        return 'C-Level'
    if title_parts_info['vp_level'] == 1:
        return 'VP-Level'
    if title_parts_info['director_level'] == 1:
        return 'Director-Level'
    if title_parts_info['manager_level'] == 1:
        return 'Manager-Level'
    return 'Other'


def predict_seniority(title):
    if title is None:
        return 'Other'

    title_parts_info = get_title_parts_info(title=title)
    pred = get_prediction(title_parts_info=title_parts_info)
    return pred
