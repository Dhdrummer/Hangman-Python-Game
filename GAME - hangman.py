lives = 10
count = 0
already_used = []
already_used_flag = False
end_flag = False
word = list("pipistrel")
print("Dolžina besede: ", len(word))
display = ["_"] * (len(word))
print("".join(display))

def branje():
    global letter
    global already_used_flag
    global end_flag
    if word != display:
        letter = input()
    elif word == display:
        end_flag = True
    if letter in already_used and end_flag == False:
        print("Črka že uporabljena! Poizkusi z drugo črko.")
        already_used_flag = True
    else:
        if end_flag == False:
            already_used.append(letter)
            already_used_flag = False

def preverjanje():
    global lives
    global count
    if letter in word and already_used_flag == False and end_flag == False:
        print("Pravilna črka.   Življenja: ", lives)
        count += 1
        izpis(letter)
    elif end_flag == False:
        lives -= 1
        print("Napačna črka.   Življenja: ", lives)

def izpis(letter):
    indices = [i for i, c in enumerate(word) if c == letter]

    for j in range(len(indices)):
        display[indices[j]] = letter
        print("".join(display))

def konec():
    if word == display:
        print("Iskana beseda: " + "".join(word))
        print("Točke: ", lives)
        print("Zmaga!")
        

while lives > 0:
    branje()
    preverjanje()
    if end_flag == True:
        konec()
        lives = 0
        break

if lives == 0:
    print("Konec igre.")
    already_used.clear()
