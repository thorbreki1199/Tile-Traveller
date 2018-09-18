'''
https://github.com/thorbreki1199/Tile-Traveller/commits/master

Byrja að setja breytu x og y sem 1 sem táknar staðsetningu á kortinu

Á meðan spilari er ekki á reit 3,1:
	Ná hvaða leiðum spilarinn má fara (með if og elif)
	Skrifa út mögulegar leiðir
	Fá inntak frá spilara
	Ef spilarinn slær inn svar sem er gilt:
		Breyta x og y gildum
	Annars:
		Prenta út villumeldingu

Prenta út “Victory!”
'''

x, y = 1, 1

while x != 3 or y != 1:
    if x == 1 and y == 1:
        answer_string = "n"
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        answer_string = "sen"
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        answer_string = "es"
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1:
        answer_string = "n"
        print("You can travel: (N)orth.")
    elif x == 2 and y == 2:
        answer_string = "sw"
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3:
        answer_string = "we"
        print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 3:
        answer_string = "ws"
        print("You can travel: (S)outh or (W)est.")
    elif x == 3 and y == 2:
        answer_string = "sn"
        print("You can travel: (N)orth or (S)outh.")
    else:
        break
    
    while True:
        the_input = input("Direction: ").lower()

        if the_input in answer_string:
            if the_input == "n":
                y += 1
            elif the_input == "s":
                y -= 1
            elif the_input == "w":
                x -= 1
            else:
                x += 1
            break
        else:
            print("Not a valid direction!")

print("Victory!")