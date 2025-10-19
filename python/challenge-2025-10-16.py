
def containsExactlyOne(string, character):
    n_matches = 0
    for x in string:
        if x == character:
            n_matches += 1
    if n_matches == 1:
        return True
    else:
        return False

def containsOnly(string, characters):
    for x in string:
        if x not in characters:
            return False
    
    return True

def validate(email):
    contains_exactly_one_at = containsExactlyOne(email, "@")
    if not contains_exactly_one_at:
        return False

    email_split = email.split("@")
    local   = email_split[0]
    domain  = email_split[1]

    letters = "abcdefghijklmnopqrstuvwxyz"
    digits  = "0123456789"
    symbols = "._-"
    letters_upper = letters.upper()
    letters_lower = letters.lower()
    
    # local

    local_allowed_characters = letters_lower + letters_upper + digits + symbols

    local_contains_allowed_characters = containsOnly(local, local_allowed_characters)

    if not local_contains_allowed_characters:
        return False

    if local.startswith("."):
        return False

    if local.endswith("."):
        return False

    if ".." in local:
        return False

    # domain

    domain_end_allowed_charatcters = letters_lower + letters_upper

    if "." not in domain:
        return False

    if ".." in domain:
        return False

    domain_split = domain.split(".")
    domain_end = domain_split[-1]

    domain_end_contains_allowed_characters = containsOnly(domain_end, domain_end_allowed_charatcters)

    if not domain_end_contains_allowed_characters:
        return False

    if len(domain_end) < 2:
        return False

    return True



