keys = {
    'year' : int,
    'genre' : str,
    'album' : str,
    'song title' : str,
    'artist' : str
}

info = {}
for key, datatype in keys.items():
    value = input(f"Enter the {key}: ")
    info[key] = datatype(value)

print("--------------------------")
print("SONG DETAILS")
print("--------------------------")

print(f"Year Released: {info['year']}")
print(f"Genre: {info['genre']}")
print(f"Album: {info['album']}")
print(f"Title: \"{info['song title']}\"")
print(f"Artist: {info['artist']}")