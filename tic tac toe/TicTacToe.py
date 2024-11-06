
import tkinter as tk


win = tk.Tk()
win.title('Крестики-Нолики')
win.geometry('330x480')
win.resizable(False, False)

maintext = '''Счёт:'''

first_count = 0
second_count = 0
turns = {0:'X',1:'O'}
colors = {0: 'red', 1: 'blue'}
turn = 0
def who():
    global turn, label3, turns, colors
    if turn == 0:
        turn += 1
    else:
        turn -= 1
    label3['text'] = turns[turn]
    label3['fg'] = colors[turn]
label = tk.Label(win, text = maintext,
bg = 'white',#свет фона
anchor='center',#закрепляет текст c лева
relief=tk.RAISED, # создаёт границу
bd = 2,font = ('Gothic', 12, 'bold') ,width= 9)
label.grid(row=0,column=0)

maintext1 = '''Ход:'''

label1 = tk.Label(win, text = maintext1,
bg = 'white',#свет фона
anchor='center',#закрепляет текст c лева
relief=tk.RAISED, # создаёт границу
bd = 2,font = ('Gothic', 12, 'bold') ,width= 9, #Ширина и высота
)
label1.grid(row=0,column=1)

maintext2 = '''0/0'''

label2 = tk.Label(win, text = maintext2,
bg = 'white',#свет фона
anchor='center',#закрепляет текст c лева
relief=tk.RAISED, # создаёт границу
bd = 2,font = ('Gothic', 12, 'bold') )
label2.grid(row=1,column=0)

maintext3 = '''X'''

label3 = tk.Label(win, text = maintext3,fg ='red',
bg = 'white',#свет фона
anchor='center',#закрепляет текст c лева
relief=tk.RAISED, # создаёт границу
bd = 2,font = ('Gothic', 12, 'bold') )
label3.grid(row=1,column=1)
def new_gameF():
    one['command']=one1
    two['command']=two2
    three['command']=three3
    four['command']=four4
    five['command']=five5
    six['command']=six6
    seven['command']=seven7
    eight['command']=eight8
    nine['command']=nine9

    first['command'] = firstF

    one['text'] = 'ㅤ'
    two['text'] = 'ㅤ'
    three['text'] = 'ㅤ'
    four['text'] = 'ㅤ'
    five['text'] = 'ㅤ'
    six['text'] = 'ㅤ'
    seven['text'] = 'ㅤ'
    eight['text'] = 'ㅤ'
    nine['text'] = 'ㅤ'
    who()

new_game = tk.Button(win, text = 'Новая игра', command=new_gameF, font = ('Gothic', 10, 'bold'))
new_game.grid(row=0,stick='we',column=2)
def firstF():
    global who
    who()
first = tk.Button(win, text = 'Первый ход:', command=firstF, font = ('Gothic', 10, 'bold'))
first.grid(row=1,stick='we',column=2)



def check_win():
    global one, two, three, four, five, six, seven, eight, nine, turn, turns, label2, first_count, second_count,  maintext3, who
    the_thing = False
    if one['text'] == turns[turn] and two['text'] == turns[turn] and three['text'] == turns[turn]:
        the_thing = True
        one['fg'] = 'gold'
        two['fg'] = 'gold'
        three['fg'] = 'gold'
    elif five['text'] == turns[turn] and six['text'] == turns[turn] and four['text'] == turns[turn]:
        the_thing = True
        four['fg'] = 'gold'
        five['fg'] = 'gold'
        six['fg'] = 'gold'
    elif seven['text'] == turns[turn] and eight['text'] == turns[turn] and nine['text'] == turns[turn]:
        the_thing = True
        seven['fg'] = 'gold'
        eight['fg'] = 'gold'
        nine['fg'] = 'gold'
    elif one['text'] == turns[turn] and five['text'] == turns[turn] and nine['text'] == turns[turn]:
        the_thing = True
        one['fg'] = 'gold'
        
        five['fg'] = 'gold'
        
        nine['fg'] = 'gold'
    elif seven['text'] == turns[turn] and five['text'] == turns[turn] and three['text'] == turns[turn]:
        the_thing = True
        
        
        three['fg'] = 'gold'
        
        five['fg'] = 'gold'
        
        seven['fg'] = 'gold'
        
    elif seven['text'] == turns[turn] and four['text'] == turns[turn] and one['text'] == turns[turn]:
        the_thing = True
        one['fg'] = 'gold'
        
        four['fg'] = 'gold'
        
        seven['fg'] = 'gold'
        
    elif nine['text'] == turns[turn] and six['text'] == turns[turn] and three['text'] == turns[turn]:
        the_thing = True
        
        three['fg'] = 'gold'
        
        six['fg'] = 'gold'
        
        nine['fg'] = 'gold'
    elif two['text'] == turns[turn] and five['text'] == turns[turn] and eight['text'] == turns[turn]:
        the_thing = True
        
        two['fg'] = 'gold'
        
        five['fg'] = 'gold'
        
        eight['fg'] = 'gold'
        



    if the_thing == True:
        one['command']=0
        two['command']=0
        three['command']=0
        four['command']=0
        five['command']=0
        six['command']=0
        seven['command']=0
        eight['command']=0
        nine['command']=0
        if turn == 0:
            first_count += 1
        else: second_count += 1
        


        maintext2 = f'{first_count}/{second_count}'
        print(maintext3)
        label2["text"] = maintext2
        
        
        label3['fg'] = 'gold'
    else: who()


def one1():
    global turn, turns, who, one, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    one['text'] = turns[turn]
    one['fg'] = colors[turn]
    one['command']=0
    check_win()
    
def two2():
    global turn, turns, who, two, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    two['text'] = turns[turn]
    two['fg'] = colors[turn]
    two['command']=0
    check_win()
    
def three3():
    global turn, turns, who, three, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    three['text'] = turns[turn]
    three['fg'] = colors[turn]
    three['command']=0
    check_win()
    
def four4():
    global turn, turns, who, four, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    four['text'] = turns[turn]
    four['fg'] = colors[turn]
    four['command']=0
    check_win()
    
def five5():
    global turn, turns, who, five, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    five['text'] = turns[turn]
    five['fg'] = colors[turn]
    five['command']=0
    check_win()
    
def six6():
    global turn, turns, who, six, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    six['text'] = turns[turn]
    six['fg'] = colors[turn]
    six['command']=0
    check_win()
    
def seven7():
    global turn, turns, who, seven, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    seven['text'] = turns[turn]
    seven['fg'] = colors[turn]
    seven['command']=0
    check_win()
    
def eight8():
    global turn, turns, who, eight, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    eight['text'] = turns[turn]
    eight['fg'] = colors[turn]
    eight['command']=0
    check_win()
    
def nine9():
    global turn, turns, who, nine, colors, check_win, label3, maintext3, first, firstF
    first['command'] = 0
    nine['text'] = turns[turn]
    nine['fg'] = colors[turn]
    nine['command']=0
    check_win()
    



one = tk.Button(win, text = 'ㅤ', command=one1, font = ('Gothic', 35, 'bold'))
one.grid(row=2,stick='we',column=0)

two = tk.Button(win, text = 'ㅤ', command=two2, font = ('Gothic', 35, 'bold'))
two.grid(row=2,stick='we',column=1)
three = tk.Button(win, text = 'ㅤ', command=three3, font = ('Gothic', 35, 'bold'),width= 3)
three.grid(row=2,column=2,stick='w')
four = tk.Button(win, text = 'ㅤ', command=four4, font = ('Gothic', 35, 'bold'))
four.grid(row=3,column=0,stick='we')
five = tk.Button(win, text = 'ㅤ', command=five5, font = ('Gothic', 35, 'bold'))
five.grid(row=3,column=1,stick='we')
six = tk.Button(win, text = 'ㅤ', command=six6, font = ('Gothic', 35, 'bold'),width= 3)
six.grid(row=3,column=2,stick='w')
seven = tk.Button(win, text = 'ㅤ', command=seven7, font = ('Gothic', 35, 'bold'))
seven.grid(row=4,column=0,stick='we')
eight = tk.Button(win, text = 'ㅤ', command=eight8, font = ('Gothic', 35, 'bold'))
eight.grid(row=4,column=1,stick='we')
nine = tk.Button(win, text = 'ㅤ', command=nine9, font = ('Gothic', 35, 'bold'),width= 3)
nine.grid(row=4,column=2,stick='w')




win.config(bg='skyblue')
win.mainloop()