import time
import keyboard
from tkinter import *
import string

root = Tk()

root.geometry("600x800")
root.config(padx=20, pady=20, bg="light cyan")
root.title("Writer's Block")

allowed_characters = string.ascii_lowercase + string.digits + string.punctuation + " "
start_time = time.time()
end_time = time.time()
elapsed_time = end_time - start_time


def is_typing():
    # returns True if a key is pressed
    for char in allowed_characters:
        if keyboard.is_pressed(char):
            return True
    return False


def clear_screen():
    my_text.delete(1.0, END)

# function to save text
def save_text():
    text_file = open("the_next_great_american_novel.txt", "w")
    text_file.write(my_text.get(1.0, END))
    text_file.close()


#Create start function
def start_writing():
    start_typing_time = time.time()
    start_time = time.time()
    while True:
        time.sleep(0.1)
        my_text.update()
        if is_typing():
            start_time = time.time()
            if time.time() > start_typing_time + 300:
                print("saving text")
                save_text()
                exit()
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 5:
                clear_screen()

my_text = Text(root, width=60, height=20, font="Calibri, 14", bg="light yellow")
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

start_button = Button(button_frame, text="Get Writing!", command=start_writing)
start_button.grid(row=1, column=0)


root.mainloop()