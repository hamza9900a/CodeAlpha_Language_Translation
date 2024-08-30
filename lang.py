from tkinter import *
from tkinter import ttk, messagebox

# Initialize the main window
root = Tk()
root.title("Translator App")
root.geometry("1080x500")
root.resizable(False, False)
root.configure(background="#1c1c1c")

# Function to update labels based on selected languages
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c.upper())
    label2.configure(text=c1.upper())
    root.after(1000, label_change)

# Simple built-in translation dictionary
translation_dict = {
    'hello': {'spanish': 'hola', 'french': 'bonjour', 'german': 'hallo'},
    'goodbye': {'spanish': 'adios', 'french': 'au revoir', 'german': 'tschüss'},
    'please': {'spanish': 'por favor', 'french': 's\'il vous plaît', 'german': 'bitte'},
    'thank you': {'spanish': 'gracias', 'french': 'merci', 'german': 'danke'},
    'yes': {'spanish': 'sí', 'french': 'oui', 'german': 'ja'},
    'no': {'spanish': 'no', 'french': 'non', 'german': 'nein'}
}

# Function to translate text
def translate_now():
    text_ = text1.get(1.0, END).strip().lower()
    if not text_:
        messagebox.showinfo("Info", "Please enter text to translate.")
        return

    source_lang = combo1.get().lower()
    target_lang = combo2.get().lower()

    if source_lang == target_lang:
        trans_text = text_
    else:
        trans_text = translation_dict.get(text_, {}).get(target_lang, "Translation not found")

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# Dictionary of languages
languages = ['english', 'spanish', 'french', 'german']

# ComboBox for selecting the source language
combo1 = ttk.Combobox(root, values=languages, font="Roboto 14", state="normal")
combo1.place(x=110, y=20)
combo1.set("english")

# Label for source language
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="#2b2b2b", fg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Frame for the text input section
f = Frame(root, bg="#3b3b3b", bd=5)
f.place(x=10, y=118, width=440, height=210)

# Text widget for entering text to be translated
text1 = Text(f, font="Roboto 20", bg="#4b4b4b", fg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# ComboBox for selecting the target language
combo2 = ttk.Combobox(root, values=languages, font="Roboto 14", state="normal")
combo2.place(x=730, y=20)
combo2.set("select language")

# Label for target language
label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="#2b2b2b", fg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Frame for the translated text output section
f1 = Frame(root, bg="#3b3b3b", bd=5)
f1.place(x=620, y=118, width=440, height=210)

# Text widget for displaying the translated text
text2 = Text(f1, font="Roboto 20", bg="#4b4b4b", fg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="#f39c12", cursor="hand2", bd=5,
                   bg='#e67e22', fg="white", command=translate_now)
translate.place(x=480, y=400, width=120, height=50)

# Clear button
clear = Button(root, text="Clear", font="Roboto 15 bold italic", activebackground="#f39c12", cursor="hand2", bd=5,
               bg='#e67e22', fg="white", command=lambda: text1.delete(1.0, END))
clear.place(x=620, y=400, width=120, height=50)

# Exit button
exit_button = Button(root, text="Exit", font="Roboto 15 bold italic", activebackground="#e74c3c", cursor="hand2", bd=5,
                     bg='#c0392b', fg="white", command=root.quit)
exit_button.place(x=760, y=400, width=120, height=50)

label_change()
root.mainloop()
