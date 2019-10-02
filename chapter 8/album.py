def make_album(artist, title, tracks=0):
    info = {"artist":artist,"title":title}
    if tracks:
        info['tracks'] = tracks
    return info

print(make_album("The Black Keys","Brothers"))
print(make_album("Led Zeppelin","Led Zeppelin", 10))