relevant_title_parts_per_management_level = {
    'c_level': [
        'chief', 'ceo', 'cto', 'cpo', 'cso', 'coo', 'cfo', 'cmo', 'cio', 'cao', 'chro',
        'president', 'global head'
    ],
    'vp_level': ['vp', 'vice president', 'vice-president'],
    'director_level': ['director', 'dir.', 'directeur'],
    'manager_level': ['manager', 'team lead', 'team-lead'],
}

substrings_to_exclude_per_management_level = {
    'c_level': ['coordin', 'director', 'vice'],
    'vp_level': [],
    'director_level': [],
    'manager_level': [],
}