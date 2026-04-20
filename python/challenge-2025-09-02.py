def rgb_to_hex(rgb):
    value_string = rgb[4:-1]
    values = value_string.split(',')
    values = [int(x.strip()) for x in values]
    values_hex = [f"{x:02x}" for x in values]
    
    result = "".join(values_hex)
    result = "#" + result
    print(result)
    return result
