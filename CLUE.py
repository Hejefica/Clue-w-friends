import cv2 
import random
from tkinter import *
import tkinter as tk

characters = {1: "Jorge",
              2: "Johan",
              3: "Alex",
              4: "Paulo",
              5: "Hector"}

places = {1: "Ocotlan",
          2: "Oblatos",
          3: "Tlajomulco",
          4: "Arcos de Zapopan",
          5: "Cd. Granja"}

weapons = {1: "Caja de Atun",
           2: "Cosplay de Mona China",
           3: "Mototaxi",
           4: "Mochila Scout",
           5: "Bolsa de Tamales"}

root = Tk()
root.title("CLUE - CETI")
root.resizable(0, 0)

frame = Frame()
frame.pack()
frame.config(bg = "white", width = "800", height = "400")

canvas = tk.Canvas(frame, width = 800, height = 400)
canvas.pack()
img= tk.PhotoImage(file = "./Resources/Menu.png")
canvas.background = img
bg = canvas.create_image(0, 0, anchor = tk.NW, image = img)

ending = random.randint(1, 5)
print(f"Generated ending: {ending}")

def image_resize(image, width = None, Height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and Height is None:
        return image
    if width is None:
        r = Height / float(h)
        dim = (int(w * r), Height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

def Choice():
    for widgets in frame.winfo_children(): widgets.destroy()
    
    canvas = tk.Canvas(frame, width = 800, height = 400)
    canvas.pack()
    img= tk.PhotoImage(file="./Resources/Choice.png")
    canvas.background = img
    bg = canvas.create_image(0, 0, anchor = tk.NW, image = img)

    quit_button=tk.Button(frame, text = "Quit", command = Quit)
    quit_button.place(x = 725, y = 340)
    quit_button.config(fg = "white", bg = "red", font = ('helvetica', 15, "bold"))
      
    character_choice, place_choice, weapon_choice = IntVar(), IntVar(), IntVar()

    col1, col2, col3 = 100, 300, 500
    row1, row2, row3, row4, row5 = 230, 260, 290, 320, 350
    
    tk.Radiobutton(root, text = characters[1], value = 1, variable = character_choice).place (x = col1, y = row1)
    tk.Radiobutton(root, text = characters[2], value = 2, variable = character_choice).place (x = col1, y = row2)
    tk.Radiobutton(root, text = characters[3], value = 3, variable = character_choice).place (x = col1, y = row3)
    tk.Radiobutton(root, text = characters[4], value = 4, variable = character_choice).place (x = col1, y = row4)
    tk.Radiobutton(root, text = characters[5], value = 5, variable = character_choice).place (x = col1, y = row5)
    
    tk.Radiobutton(frame, text = places[1], value = 1, variable = place_choice).place (x = col2, y = row1)
    tk.Radiobutton(frame, text = places[2], value = 2, variable = place_choice).place (x = col2, y = row2)
    tk.Radiobutton(frame, text = places[3], value = 3, variable = place_choice).place (x = col2, y = row3)
    tk.Radiobutton(frame, text = places[4], value = 4, variable = place_choice).place (x = col2, y = row4)
    tk.Radiobutton(frame, text = places[5], value = 5, variable = place_choice).place (x = col2, y = row5)
    
    tk.Radiobutton(frame, text = weapons[1], value = 1, variable = weapon_choice).place (x = col3, y = row1)
    tk.Radiobutton(frame, text = weapons[2], value = 2, variable = weapon_choice).place (x = col3, y = row2)
    tk.Radiobutton(frame, text = weapons[3], value = 3, variable = weapon_choice).place (x = col3, y = row3)
    tk.Radiobutton(frame, text = weapons[4], value = 4, variable = weapon_choice).place (x = col3, y = row4)
    tk.Radiobutton(frame, text = weapons[5], value = 5, variable = weapon_choice).place (x = col3, y = row5)
    
    def Verify():
        b_ver.destroy()
        get_character, get_place, get_weapon =  character_choice.get(), place_choice.get(), weapon_choice.get()
    
        if character == get_character and place == get_place and weapon == get_weapon:
            print("Game won.")
            label_c = tk.Label(frame, text = "Game Over! You won.", fg = "green", bg = None, font = ('helvetica', 15, "bold" )).place (x = 150, y = 150) 
           
        else:
            print("Game lost.")
            label_c = (tk.Label(frame, text = "Game Over! You lost.", fg = "red", bg = "white", font = ('helvetica', 15,"bold" )).place(x = 150, y = 150),
                       tk.Label(frame, text = f"El culpable fue {characters[ending]}. Robó la gema del infinito en {places[ending]} con su {weapons[ending]}.",
                                fg = "black", bg = "white", font=('helvetica', 9)).place (x=100, y=180))
            
    b_ver = tk.Button(frame, text = "Verify", command = Verify)
    b_ver.place(x = 725, y = 300)
    b_ver.config(fg = "white", bg = "blue",font = ('helvetica', 12, "bold"))

    return (character_choice.get(), place_choice.get(), weapon_choice.get())
        
def Quit(): root.destroy()

def StoryPlace(place, final):
    cv2.imshow(f"{place}", image_resize(cv2.imread(f"./Resources/{place}{final}.png"), Height = 500))

character, weapon, place = ending, ending, ending
    
print(f"El culpable fue {characters[ending]}. Robó las caguamas en {places[ending]} con su {weapons[ending]}.")

b_wakanda = Button(frame, text = "Ocotlan", command = lambda : StoryPlace("Ocotlan", ending))
b_wakanda.place(x = 45, y = 330)
b_wakanda.config(fg = "white", bg = "black", font = ('helvetica', 12, "bold"))

b_xmen = Button(frame, text = "Oblatos", command = lambda : StoryPlace("Oblatos", ending))
b_xmen.place(x = 200, y = 330)
b_xmen.config(fg = "white", bg = "black", font = ('helvetica', 12, "bold"))

b_asgard = Button(frame, text = "Tlajomulco", command = lambda : StoryPlace("Tlajomulco", ending))
b_asgard.place(x = 350, y = 330)
b_asgard.config(fg = "white", bg = "black", font = ('helvetica', 12, "bold"))

b_tstark = Button(frame, text = "Arcos de Zapopan", command = lambda : StoryPlace("Arcos", ending))
b_tstark.place(x = 475, y = 330)
b_tstark.config(fg = "white", bg = "black", font = ('helvetica', 12, "bold"))

b_shield = Button(frame, text = "Cd. Granja", command = lambda : StoryPlace("Granja", ending))
b_shield.place(x = 670, y = 330)
b_shield.config(fg = "white", bg = "black", font = ('helvetica', 12, "bold"))

b_terminar = Button(frame, text = "Continue", command = Choice)
b_terminar.place(x = 500, y = 150)
b_terminar.config(fg = "white", bg = "red", font = ('helvetica', 15,"bold" ))

root.mainloop()