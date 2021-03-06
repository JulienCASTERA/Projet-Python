import tkinter as tk
from player import *
from ball import *
from bonus import *
import time

class Frames(tk.Tk):
    """Initialise les données liées à toutes les fenetres"""
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Menu)
        self.resizable(False, False)
        self.title("Pong")


    def switch_frame(self, frame_class):
        """Detruit la frame actuelle avant de la remplacer par la frame demandée (actuelle)."""
        new_frame = frame_class(self)
        if self._frame is not None:
            #self._frame.destroy()
            self._frame.grid_forget()
        self._frame = new_frame
        self._frame.rowconfigure(0, weight=1)
        self._frame.columnconfigure(0, weight=1)
        self._frame.grid(row=0, column=0, columnspan=4, padx=0, pady=0)


class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='PONG - Accueil').grid(row=0,ipadx=450)
        tk.Label(self, text="Entrez la vitesse de la balle : ").grid(row=1)
        tk.Label(self, text="Entrez le score max : ").grid(row=5)
        Menu.scoremax = tk.IntVar()
        Menu.scoremax.set(2)
        Menu.v = tk.IntVar()
        Menu.v.set(5)
        tk.Checkbutton(self, text="Balle lente", variable=Menu.v, onvalue="5", offvalue="5", state='active').grid(row=2)
        tk.Checkbutton(self, text="Balle moyenne", variable=Menu.v, onvalue="7", offvalue="5").grid(row=3)
        tk.Checkbutton(self, text="Balle rapide", variable=Menu.v, onvalue="10", offvalue="5").grid(row=4)

        tk.Checkbutton(self, text="5", variable=self.scoremax, onvalue="5", offvalue="2", state='active').grid()
        tk.Checkbutton(self, text="10", variable=self.scoremax, onvalue="10", offvalue="2").grid()
        tk.Checkbutton(self, text="20", variable=self.scoremax, onvalue="20", offvalue="2").grid()

        tk.Button(self, text='Jouer', command=lambda: master.switch_frame(Jeu)).grid()
        tk.Button(self, text="Quitter", command=master.destroy).grid()


class Jeu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # INIT Canvas
        Jeu.last = tk.IntVar()
        Jeu.last.set(0)
        width = 1000
        height = 500
        canvas = tk.Canvas(self, width=width, height=height, background="black")
        canvas.grid(column=0, row=1, columnspan=4, sticky="news")

        # INIT Ball
        Jeu.bon = None
        ball = Ball(canvas, 15, int(Menu.v.get()))

        # INIT Player
        player = Player("Joueur 1", canvas, 20, 100, 0)
        player2 = Player("Joueur 2", canvas, 20, 100, 1)
        Jeu.p1s = tk.IntVar()
        Jeu.p2s = tk.IntVar()
        tk.Label(self, textvariable=Jeu.p1s, width=10).grid(column=0, row=0, sticky='w')
        tk.Label(self, textvariable=Jeu.p2s, width=10).grid(column=2, row=0, sticky='e')

        # INIT Messages
        print('###############################################################')
        print("Vitesse définie sur cette partie :", Menu.v.get())
        print("Score défini sur cette partie :", Menu.scoremax.get())

        # Movement P1
        canvas.bind_all('<Up>', player.up)
        canvas.bind_all('<Down>', player.down)
        # Movement P2
        canvas.bind_all('<z>', player2.up)
        canvas.bind_all('<s>', player2.down)
        Jeu.start_time = time.time()
        Jeu.oui = True
        def checkpoint():  # Check point
            coords = canvas.coords(ball.ball)
            cp1 = canvas.coords(player.player)
            cp2 = canvas.coords(player2.player)
            # Collision mur
            if Jeu.oui == True:
                canvas.after(34, checkpoint)
                bonus()
                if coords[3] < 0 or coords[1] > int(canvas['height']) - 40:
                    ball.y_speed = -ball.y_speed
                # Collision joueur
                collision = canvas.find_overlapping(
                    coords[0], coords[1], coords[2], coords[3])
                c_p1 = canvas.find_overlapping(
                    cp1[0], cp1[1], cp1[2], cp1[3])
                c_p2 = canvas.find_overlapping(
                    cp2[0], cp2[1], cp2[2], cp2[3])
                if collision != (1,):
                    if collision == c_p1 or collision == c_p2:
                        ball.x_speed = -ball.x_speed
                    if collision == c_p1:
                        Jeu.last.set(1)
                    if collision == c_p2:
                        Jeu.last.set(2)
                # J1 Gagne 1 pts
                if coords[0] > int(canvas['width']):
                    if Jeu.p1s.get() < Menu.scoremax.get() - 1:
                        Jeu.p1s.set(Jeu.p1s.get()+1)
                        print("Joueur 1 : ", Jeu.p1s.get())
                        canvas.move(ball.ball, -500, 0)
                        ball.x_speed = -ball.x_speed
                        ball.y_speed = -ball.y_speed
                        player.resize(0)
                        player2.resize(0)
                        player.speed()
                        player2.speed()
                        canvas.unbind_all('<s>')
                        canvas.unbind_all('<z>')
                        canvas.bind_all('<z>', player2.up)
                        canvas.bind_all('<s>', player2.down)
                        canvas.unbind_all('<Down>')
                        canvas.unbind_all('<Up>')
                        canvas.bind_all('<Up>', player.up)
                        canvas.bind_all('<Down>', player.down)
                    else:
                        Jeu.oui = False
                        print('Game is running:', Jeu.oui)
                        Jeu.p1s.set(Jeu.p1s.get()+1)
                        canvas.unbind_all('<s>')
                        canvas.unbind_all('<z>')
                        canvas.unbind_all('<Down>')
                        canvas.unbind_all('<Up>')
                        canvas.delete(ball.ball)
                        canvas.after_cancel(checkpoint)
                        master.switch_frame(EndScreen)
                # J2 Gagne 1pts
                if coords[2] < 0:
                    if Jeu.p2s.get() < Menu.scoremax.get() - 1:
                        Jeu.p2s.set(Jeu.p2s.get()+1)
                        print("Joueur 2 : ", Jeu.p2s.get())
                        canvas.move(ball.ball, 500, 0)
                        ball.x_speed = -ball.x_speed
                        ball.y_speed = -ball.y_speed
                        player.resize(0)
                        player2.resize(0)
                        player.speed()
                        player2.speed()
                        canvas.unbind_all('<s>')
                        canvas.unbind_all('<z>')
                        canvas.bind_all('<z>', player2.up)
                        canvas.bind_all('<s>', player2.down)
                        canvas.unbind_all('<Down>')
                        canvas.unbind_all('<Up>')
                        canvas.bind_all('<Up>', player.up)
                        canvas.bind_all('<Down>', player.down)
                    else:
                        Jeu.oui = False
                        print('Game is running:', Jeu.oui)
                        Jeu.p2s.set(Jeu.p2s.get()+1)
                        canvas.unbind_all('<s>')
                        canvas.unbind_all('<z>')
                        canvas.unbind_all('<Down>')
                        canvas.unbind_all('<Up>')
                        canvas.delete(ball.ball)
                        canvas.after_cancel(checkpoint)
                        master.switch_frame(EndScreen)
        def bonus():
            canvas.after(3000, bonus)
            if Jeu.bon == None:
                Jeu.bon = Bonus(canvas, player, player2, ball.ball)
            if Jeu.bon.checkCol(player,player2,ball.ball) != None:
                col = Jeu.bon.checkCol(player,player2,ball.ball)
                Jeu.bon = None
                print("Couleur du bonus : ", col, "pour le joueur : ", Jeu.last.get())
                if col == 'red' and Jeu.last.get() == 1:
                    print('P1 Move')
                    player.speed(60)
                if col == 'red' and Jeu.last.get() == 2:
                    print('P2 Move')
                    player2.speed(60)
                if col == 'blue' and Jeu.last.get() == 1:
                    print('P1 Resize')
                    player.resize(1.2)
                if col == 'blue' and Jeu.last.get() == 2:
                    print('P2 Resize')
                    player2.resize(1.2)
                if col == 'green':
                    print('Les deux joueurs sont resize en plus grand')
                    player.resize(1.2)
                    player2.resize(1.2)
                if col == 'yellow':
                    print('Les deux joueurs vont plus vite')
                    player.speed(60)
                    player2.speed(60)
                if col =='purple':
                    if Jeu.last.get() == 1:
                        print('Le joueur 2 a un malus de vitesse !')
                        player2.speed(10)
                    else:
                        print('Le joueur 1 a un malus de vitesse !')
                        player.speed(10)
                if col =='pink':
                    if Jeu.last.get() == 1:
                        print('Le joueur 2 a les controles inversés !')
                        canvas.unbind_all('<s>')
                        canvas.unbind_all('<z>')
                        canvas.bind_all('<z>', player2.down)
                        canvas.bind_all('<s>', player2.up)
                    else:
                        print('Le joueur 1 a les controles inversés !')
                        canvas.unbind_all('<Down>')
                        canvas.unbind_all('<Up>')
                        canvas.bind_all('<Up>', player.down)
                        canvas.bind_all('<Down>', player.up)
                        



        checkpoint()
        

class EndScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Score final : ").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Joueur 1 : ").pack(side="top", fill="x", pady=10)
        tk.Label(self, text=Jeu.p1s.get(), width=10).pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Joueur 2 : ").pack(side="top", fill="x", pady=10)
        tk.Label(self, text=Jeu.p2s.get(), width=10).pack(side="top", fill="x", pady=20)
        if Jeu.p1s.get() == Menu.scoremax.get():
            tk.Label(self, text="Joueur 1 gagne ! ").pack(side="top", fill="x", pady=10)
        else:
            tk.Label(self, text="Joueur 2 gagne ! ").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Retour à l'écran principal", command=lambda: master.switch_frame(Menu)).pack()
        e = time.time() - Jeu.start_time
        tk.Label(self, text="Temps écoulé : {:.0f}:{:.0f}:{:02f}".format(e // 3600, (e % 3600 // 60), e % 60)).pack(side="top", fill="x", pady=10)
        print('Temps écoulé : {:.0f}:{:.0f}:{:02f}'.format(e // 3600, (e % 3600 // 60), e % 60))
        print('###############################################################')


if __name__ == "__main__":
    app = Frames()
    app.mainloop()