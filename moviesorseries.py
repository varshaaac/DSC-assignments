thriller= ["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy = ["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]
movieorseries = input()
movieorseries = movieorseries.lower()
thriller = map(str.lower,thriller)
comedy = map(str.lower,comedy)
if movieorseries in thriller:
    print("It is a thriller")
elif movieorseries in comedy:
    print("It is a comedy")
else:
    print("It is neither thriller nor comedy")
