
def spookify(boo):
    boo = boo.replace("_", "~")
    boo = boo.replace("-", "~")
    
    result = ""
    letter_counter = 0
    for i in range(len(boo)):
        if boo[i] == "~":
            result += boo[i]
        else:
            if letter_counter % 2 == 0:
                result += boo[i].upper()
            else:
                result += boo[i].lower()
            letter_counter += 1
    
    return result



