
def image_search(images, term):
    result = []
    for image in images:
        if term.lower() in image.lower():
            result.append(image)
    return result



