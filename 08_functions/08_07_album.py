# Gives some artists and their albums with the number of songs

def make_album(artist, album, tracks= 0):
    """Returns a dictionary of an artist and their album"""
    info = {'name': artist, 'album': album}
    if tracks:
        info['tracks'] = tracks
    return info
musician = make_album('The Beatles', 'Abbey Road', tracks= 17)
print(musician)
musician = make_album('Michael Jackson', 'Thriller')
print(musician)
musician = make_album('Blonde', 'Frank Ocean')
print(musician)