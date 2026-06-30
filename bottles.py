def bottle_word(count):
    if count == 1:
      return "bottle"
    return "bottles"

def verse(count):
    if count == 0:
      return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
    
    if count == 1:
      return (
				f"1 {bottle_word(count)} of beer on the wall, "
        f"1 {bottle_word(count)} of beer.\n"
        f"Take one down and pass it around, no more bottles of beer on the wall."
			)
    
    return (
			f"{count} {bottle_word(count)} of beer on the wall, "
      f"{count} {bottle_word(count)} of beer.\n"
      f"Take one down and pass it around, {count - 1} {bottle_word(count - 1)} of beer on the wall."
		)
    
def bottle_song(start=99):
    lyrics = []
    for count in range (start, -1, -1):
        lyrics.append(verse(count))
    return "\n".join(lyrics)
if __name__ == "__main__":
    print(bottle_song(100))