'''
https://github.com/thorbreki1199/Tile-Traveller/commits/master

1. Which implementation was easier and why?
    Mér fannst mun auðveldara að setja upp kóðann með functions vegna þess að ég þurfti ekki að skrifa sama kóðann aftur og aftur.
    Einnig var bara auðveldara að setja upp kóðann svona þar sem þegar ég var búinn að setja upp the functions rétt þá þurfti ég 
    ekkert að pæla í þeim lengur.

2. Which implementation is more readable and why?
    Implementation 2 er mun læsilegri þar sem þú þarft ekki að pæla í hvað gerist í the functions, en ef þú vilt þá máttu það. Einnig er
    the structure á kóðanum betri.

3. Which problems in the first implementations were you able to solve with the latter
implementation?
    The only problems that we fixed were the readability of the code. The code in the first implementation was not good but using
    functions made it much more readable right of the bat.

'''
'''
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

def check_where_you_can_go(x, y):
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
        answer_string = ""
    return answer_string

def input_and_change(x, y, answer_string):
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
        else:
            print("Not a valid direction!")
        return x, y

x, y = 1, 1

while x != 3 or y != 1:
    answer_string = check_where_you_can_go(x, y)
    x, y = input_and_change(x, y, answer_string)
    

print("Victory!")