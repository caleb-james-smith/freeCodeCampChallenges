
def favorite_songs(playlist):
    most_plays = -999
    second_most_plays = -999
    most_played_song = ""
    second_most_played_song = ""
    for song in playlist:
        if song["plays"] > most_plays:
            most_plays = song["plays"]
            most_played_song = song["title"]

    for song in playlist:
        if song["plays"] > second_most_plays and song["plays"] < most_plays:
            second_most_plays = song["plays"]
            second_most_played_song = song["title"]

    result = [most_played_song, second_most_played_song]
    return result



