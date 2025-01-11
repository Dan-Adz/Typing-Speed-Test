# Typing Speed Test

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime

# Insert the text you want to try as the variable below
type_speed_text = """Proofreader applicants are tested primarily on their spelling speed and skill in finding errors in  
    the sample text Toward that end they may be given a list of ten or twenty classically difficult words and a 
    proofreading test both tightly timed The proofreading test will often have a maximum number of errors per 
    quantity of text and a minimum amount of time to find them The goal of this approach is to identify those with the 
    best skill set"""

misspelled_count = 0
type_speed_text_list = type_speed_text.split(" ")
type_speed_text_list_words = []
for item in type_speed_text_list:
    if item != '' and item != '\n':
        type_speed_text_list_words.append(item)
type_speed_text_list = type_speed_text_list_words
length = len(type_speed_text_list_words)
start_time = int(datetime.now().timestamp())


# To end the test early input END
def next_word(event=None):
    global length
    global misspelled_count
    word = word_entry.get()
    print(word)
    if word_count_entry.get() == "":
        count = 0
    else:
        count = int(word_count_entry.get())
    if word in type_speed_text_list:
        word_count_entry.delete(0, len(str(count)))
        word_count_entry.insert(0, str(count + 1))
    elif len(word) > 0:
        word_count_entry.delete(0, len(str(count)))
        word_count_entry.insert(0, str(count + 1))
        if word != 'END':
            misspelled_count += 1
    word_entry.delete(0, len(word))
    if count >= length or word == "END":
        stop_time = int(datetime.now().timestamp())
        spent_time = stop_time - start_time
        total_count = count + 1
        WPM = (total_count / spent_time) * 60
        messagebox.showinfo(title="WPM", message=f"Your WMP is: {WPM} Misspelled Words: {misspelled_count}")
        word_count_entry.delete(0, len(str(count)))


window = Tk()
window.title("Type Speed Test")
window.config(padx=50, pady=50)

# Labels
test_text = Label(text=type_speed_text)
test_text.grid(row=0, column=0, columnspan=3)
type_label = Label(text="Type Here:")
type_label.grid(row=1, column=0)
word_count_label = Label(text="Word Count:")
word_count_label.grid(row=2, column=0)
next_word_label = Label(text="Press Enter after each word", width=36)
next_word_label.grid(row=3, column=1, columnspan=2)

# Entries
word_entry = Entry(width=35)
word_entry.grid(row=1, column=1, columnspan=2)
word_count_entry = Entry(width=10)
word_count_entry.grid(row=2, column=1)

window.bind("<Return>", next_word)

window.mainloop()
