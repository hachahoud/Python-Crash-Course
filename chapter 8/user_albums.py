def make_album(artist, title, tracks=0):
    info = {"artist":artist,"title":title}
    if tracks:
        info['tracks'] = tracks
    return info
while True:
    print("")
    print("Enter 'q' to exit at any time!")
    
    artist = input("Enter name of the artist: ")
    if artist.lower() == 'q':
        break

    title = input("Enter title of the album: ")
    if title.lower() == 'q':
        break

    album = make_album(artist,title)
    print(album)
