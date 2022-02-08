import random

#karaktere in variablen packen
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1294567890._(),/"
konsonanten = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vocale = "aeiouAEIOU"
nubers = "1234567890"
special = "._(),/"

#passort lange abfragen und passwort variable vorbereiten
pw_len = input("Passwort länge!!: ")
pw = ""

#erste passwort version generieren
for i in range(0, int(pw_len)):
    pw += chars[random.randint(0, len(chars) - 1)]

#passwort anpassen zum besser merken
for i in range(0, 15):
    for i in range(0, int(pw_len)-1):
        window = [pw[i], pw[i+1]]
        print(window)
        if window[0] == window[1]:
            print("wiederholung gefunden")
            pw = list(pw)
            pw[i] = chars[random.randint(0, len(chars) - 1)]
            pw = "".join(pw)
        elif window[0] in list(konsonanten) and window[1] in list(konsonanten):
            print("doppel konsonanten gefunden")
            pw = list(pw)
            pw[i] = chars[random.randint(0, len(chars) - 1)]
            pw = "".join(pw)
        elif window[0] in list(vocale) and window[1] in list(vocale):
            print("doppel vocal gefunden")
            pw = list(pw)
            pw[i] = chars[random.randint(0, len(chars) - 1)]
            pw = "".join(pw)
        elif window[0] in list(special) and window[1] in list(special):
            print("doppel special gefunden")
            pw = list(pw)
            pw[i] = chars[random.randint(0, len(chars) - 1)]
            pw = "".join(pw)
        elif window[0] in list(nubers) and window[1] in list(nubers):
            print("doppel numer gefunden")
            if random.randint(0, 1) == 1:
                pw = list(pw)
                pw[i] = chars[random.randint(0, len(chars) - 1)]
                pw = "".join(pw)

#paswort ausgeben
print(pw)