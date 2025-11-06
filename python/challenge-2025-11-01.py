
def verify(message, key, signature):
    message_value = getValueOfString(message)
    key_value = getValueOfString(key)
    total_value = message_value + key_value
    if total_value == signature:
        return True
    else:
        return False

def getValueOfString(string):
    result = 0
    for x in string:
        value = getValueOfChar(x)
        result += value
    return result

def getValueOfChar(x):
    result = 0
    x_ord = ord(x)
    if ord('a') <= x_ord <= ord('z'):
        result = x_ord - ord('a') + 1
    if ord('A') <= x_ord <= ord('Z'):
        result = x_ord - ord('A') + 27
    return result



