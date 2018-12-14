from tkinter import *
from functools import partial
from player import *
from ball import *


def jouer():
    global menu
    menu.destroy()


    # INIT TK
    tk = Tk()
    tk.title("[Pong]")
    # INIT Canvas
    WIDTH = 1000
    HEIGHT = 500
    vitesse = 0
    mainmenu = Menu(tk)
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT, background="black")
    canvas.pack()


    first_menu = Menu(mainmenu)
    first_menu.add_command(label="Balle lente", command=5)
    first_menu.add_command(label="Balle moyenne", command=7)
    first_menu.add_command(label="Balle rapide", command=10)

    second_menu = Menu(mainmenu)
    second_menu.add_command(label="Quitter", command=tk.destroy)
    second_menu.add_command(label="Commande 2", command=jouer)

    mainmenu.add_cascade(label="Jeu", menu=first_menu)
    mainmenu.add_cascade(label="Options", menu=second_menu)



    # INIT Ball
    vitesse = v.get()
    print("Vitesse définie sur cette partie :", vitesse)
    ball = Ball(canvas, 15, int(vitesse))

    # INIT Player
    player = Player("Joueur 1", canvas, 20, 100, 0)
    player2 = Player("Joueur 2", canvas, 20, 100, 1)


    # Movement P1
    canvas.bind_all('<Up>', player.up)
    canvas.bind_all('<Down>', player.down)
    # Movement P2
    canvas.bind_all('<z>', player2.up)
    canvas.bind_all('<s>', player2.down)


    def checkpoint():  # Check point
        coords = canvas.coords(ball.ball)

        # Collision mur
        if coords[3] < 0 or coords[1] > int(canvas['height']):
            ball.y_speed = -ball.y_speed
        # Collision joueur
        collision = canvas.find_overlapping(
            coords[0], coords[1], coords[2], coords[3])
        if collision != (1,):
            ball.x_speed = -ball.x_speed
        # J2 Gagne 1pts
        if coords[2] < 0:
            player2.addscore(1)
            ball.x_speed = -ball.x_speed

        # J1 Gagne 1 pts
        if coords[0] > int(canvas['width']):
            player.addscore(1)
            ball.x_speed = -ball.x_speed
        canvas.after(34, checkpoint)


    checkpoint()
    tk.config(menu=mainmenu)
    tk.mainloop()


menu = Tk()
menu.title("[Pong]")
menu.geometry("480x320")



textvitesse = Label(menu, text="Entrez la vitesse de la balle : ").place(x=10, y=100)
textscore = Label(menu, text="Entrez le score max : ").place(x=10, y=200)

v = IntVar()
scoremax = IntVar()

lent = Checkbutton(menu, text="Balle lente", variable=v, onvalue="5", offvalue="0").place(x=195, y=100)
moyenne = Checkbutton(menu, text="Balle moyenne", variable=v, onvalue="7", offvalue="0").place(x=195, y=120)
rapide = Checkbutton(menu, text="Balle rapide", variable=v, onvalue="10", offvalue="0").place(x=195, y=140)


score_5 = Checkbutton(menu, text="5", variable=scoremax, onvalue="5", offvalue="5").place(x=195, y=200)
score_10 = Checkbutton(menu, text="10", variable=scoremax, onvalue="10", offvalue="0").place(x=195, y=220)
score_20 = Checkbutton(menu, text="20", variable=scoremax, onvalue="20", offvalue="0").place(x=195, y=240)


ButtonJouer = Button(menu, text="Jouer", command=jouer)
ButtonJouer.pack(padx=5, pady=5)




ButtonQuitter = Button(menu, text="Quitter", command=menu.destroy)
ButtonQuitter.pack(padx=5, pady=5)

menu.mainloop()
