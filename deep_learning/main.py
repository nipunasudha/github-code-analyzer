import csv
from tkinter import *
from tkinter import messagebox

from titlecase import titlecase

from deep_learning.core import  get_prediction
from deep_learning.core import  train_model

window = Tk()
window.configure(background="#9980FA")
window.title("GIithub User Level Detector")
window.geometry('500x300')

lb5 = Label(window, text='', wraplength=300, background="#0652DD", fg='#40407a')
lb5.pack(fill=BOTH, expand=1)
lbl = Label(window, text="Predict Expertise", wraplength=300, background="#2c2c54")
lbl.pack(fill=BOTH, expand=1)


def train():
    train_model()


with open('./generated_csv/direct_predict.csv', encoding="utf8") as f:
    users_array = [{k: v for k, v in row.items()}
                   for row in csv.DictReader(f, skipinitialspace=True)]
dic_predict = {}
for row in users_array:
    key = row['Id']
    dic_predict[key] = row


def predict():
    number = (entry.get())
    i = 0
    if str(number) in dic_predict.keys():
        i = 0
        for key in dic_predict.keys():
            i = i + 1
            if str(key) == str(number):
                answer = get_prediction(i)
                messagebox.showinfo('Predicted Answer', titlecase(answer))


btn1 = Button(window, text="Train", command=train, background="#706fd3")
btn1.pack(fill=BOTH, padx=40, pady=20)
entry = Entry(window, bg='white')
entry.pack(fill=BOTH, padx=150, pady=20)
lb2 = Label(window, text="Enter User Name", wraplength=300, background="#474787")
lb2.pack(fill=BOTH, padx=80, pady=0)
btn = Button(window, text="Predict", command=predict, background="#ff793f")
btn.pack(fill=BOTH, padx=40, pady=20)

window.mainloop()
