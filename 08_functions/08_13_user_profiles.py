# Prints some information about me

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('anthony', 'frederick',
location='king of prussia',
field='computer science',
language='english')
print(user_profile)