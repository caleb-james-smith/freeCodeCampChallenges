
def format(duration_seconds):
    hours = duration_seconds // (60 * 60)
    remainder = duration_seconds % (60 * 60)
    minutes = remainder // 60
    seconds = remainder % 60
    if hours > 0:
        result = "{0}:{1:02d}:{2:02d}".format(hours, minutes, seconds)
    else:
        result = "{0}:{1:02d}".format(minutes, seconds)
    return result



