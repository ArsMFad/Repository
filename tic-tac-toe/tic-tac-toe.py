from tkinter import *

class MainApp:
    def __init__ (self):
        self.xpla = 0
        self.ypla = 0

        self.itmustbeusefull = 0

        self.xory = 0

        self.polework = "........."
        self.polework = list(self.polework)

        self.pole = "0.0, 1.0, 2.0, 0.1, 1.1, 2.1, 0.2, 1.2, 2.2"
        self.pole = self.pole.split(", ")

        self.button_list = []

        self.label_list = "0.0, 1.0, 2.0, 0.1, 1.1, 2.1, 0.2, 1.2, 2.2"
        self.label_list = self.label_list.split(", ")

        self.wincoords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        self.winlist = []

        self.winner = 0

        for i in range(0, 9):
            self.gamebutton = Button(root, width = 13, height = 6)
            self.gamebutton.place(x = self.xpla, y = self.ypla)

            if self.itmustbeusefull != 2:
                self.xpla += 100
                self.itmustbeusefull += 1
            else:
                self.xpla = 0
                self.ypla += 100
                self.itmustbeusefull = 0

            self.gamebutton.bind("<Button-1>", self.playchange)
            self.button_list.append(self.gamebutton)


    def playchange(self, event):
        if self.xory == 0:
            event.widget["text"] = "X"
            self.xory = 1

        else:
            event.widget["text"] = "O"
            self.xory = 0


        for but in self.button_list:
            self.checkenbut = but
            self.xposelab = self.checkenbut.winfo_x()
            self.yposelab = self.checkenbut.winfo_y()

            if self.checkenbut["text"]:
                self.gamelabel = Label(root, text = self.checkenbut["text"])
                self.gamelabel.place(x = self.xposelab + 45, y = self.yposelab + 45)
                MainApp.adder_to_list_lab(self, self.xposelab, self.yposelab, self.gamelabel)

                self.button_list.remove(self.checkenbut)
                MainApp.adder_to_pole(self, self.xposelab, self.yposelab, self.checkenbut['text'])
                self.checkenbut.destroy()

    def adder_to_list_lab(self, posx, posy, soblabel):
        self.polxlab_in_pole = posx//100
        self.polylab_in_pole = posy//100
        self.laberposition = str(self.polxlab_in_pole) + "." + str(self.polylab_in_pole)

        for labina in range(0, len(self.label_list)):
            if self.label_list[labina] == self.laberposition:
                self.label_list.remove(self.laberposition)
                self.label_list.insert(labina, soblabel)

    def adder_to_pole(self, posx, posy, znak):
        self.polx_in_pole = posx//100
        self.poly_in_pole = posy//100
        self.labposition = str(self.polx_in_pole) + "." + str(self.poly_in_pole)

        for poledina in range(0, len(self.pole)):
            if self.pole[poledina] == self.labposition:
                self.polework[poledina] = znak

        MainApp.whoiswin(self)

    def whoiswin(self):
        for winco in self.wincoords:
            if self.polework[winco[0]] == self.polework[winco[1]] == self.polework[winco[2]] == "X":
                self.winlist = [winco[0], winco[1], winco[2]]
                self.winner = "X"
                MainApp.winner_takes_all(self)

            elif self.polework[winco[0]] == self.polework[winco[1]] == self.polework[winco[2]] == "O":
                self.winlist = [winco[0], winco[1], winco[2]]
                self.winner = "O"
                MainApp.winner_takes_all(self)

            elif self.button_list == [] and self.winner == 0:
                MainApp.nobody_wins(self)

    def winner_takes_all(self):
        for pose in self.winlist:
            self.winlabnow = self.label_list[pose]
            self.winlabnow['fg'] = "#ff0000"

        for end in self.button_list:
            end.destroy()
        self.button_list.clear()

        self.winlabel = Label(root, text = self.winner + "\'s are win!'", bd = 15, font = 24, fg = "#ff0000")
        self.winlabel.place(x = 100, y = 300)

    def nobody_wins(self):
        self.winlabel = Label(root, text = "Nobody wins!", bd = 15, font = 24)
        self.winlabel.place(x = 100, y = 300)


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x350")

    MainApp()

    root.mainloop()
