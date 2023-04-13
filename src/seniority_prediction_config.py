# If title includes one of the substrings (per management level) we will mark it as "in management level
relevant_title_parts_per_management_level = {
    'c_level': [
        'chief', 'ceo', 'cto', 'cpo', 'cso', 'coo', 'cfo', 'cmo', 'cio', 'cao', 'chro',
        'president', 'global head'
    ],
    'vp_level': ['vp', 'vice president', 'vice-president'],
    'director_level': ['director', 'dir.', 'directeur'],
    'manager_level': ['manager', 'team lead', 'team-lead'],
}

# If title includes one of the substrings (per management level) we will mark it as "not in management level-
# will be applied after the logic from above
substrings_to_exclude_per_management_level = {
    'c_level': ['coordin', 'director', 'vice'],
    'vp_level': [],
    'director_level': [],
    'manager_level': [],
}
