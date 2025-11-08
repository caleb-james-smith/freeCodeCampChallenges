
def can_post(message):
    length = len(message)
    if length <= 40:
        return "short post"
    if length <= 80:
        return "long post"
    return "invalid post"



