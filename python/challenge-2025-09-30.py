
def format_number(number):
    country_code    = number[:1]
    area_code       = number[1:4]
    part_1          = number[4:7]
    part_2          = number[7:]
    result = f"+{country_code} ({area_code}) {part_1}-{part_2}"
    return result



