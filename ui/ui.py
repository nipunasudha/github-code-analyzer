from tkinter import *

# window
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title('GitHub User Performance Analyzer')
window.configure(bg='white')
window.minsize(0, 500)
window.resizable(0, 0)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
# top frame
top_frame = Frame(window, bg='white')
top_frame.grid(row=0, column=0, sticky='we')
top_frame.grid_columnconfigure(0, weight=1)
# banner
banner_img = PhotoImage(file="../img/banner.png")
banner = Label(top_frame, image=banner_img, bg='white')
banner.grid(row=0, column=0)
# body frame
body_frame = Frame(window, bg='yellow')
body_frame.grid(row=1, column=0, sticky='news')
body_frame.grid_columnconfigure(0, weight=1)
body_frame.grid_rowconfigure(1, weight=1)
# analyze frame
analyze_frame = Frame(body_frame, bg='white', padx=20, pady=20)
analyze_frame.grid(row=0, column=0, sticky='we')
analyze_frame.grid_columnconfigure(0, weight=100)
analyze_frame.grid_columnconfigure(1, weight=1)
analyze_frame.grid_columnconfigure(2, weight=1)
analyze_frame.grid_columnconfigure(3, weight=1)
analyze_frame.grid_columnconfigure(4, weight=1)
analyze_frame.grid_columnconfigure(5, weight=100)
# analyze box
analyze_label = Label(analyze_frame, text="Enter GitHub username : ", bg=analyze_frame['bg'])
analyze_label.grid(row=0, column=0, sticky='e')
analyze_entry = Entry(analyze_frame)
analyze_entry.focus()
analyze_entry.grid(row=0, column=1, sticky='we')
clone_button = Button(analyze_frame, text='Clone all', bg='white', padx=10)
clone_button.grid(row=0, column=2, sticky='we', padx=4)
analyze_button = Button(analyze_frame, text='Analyze', bg='white', padx=10)
analyze_button.grid(row=0, column=3, sticky='w', padx=4)
report_button = Button(analyze_frame, text='Report', bg='white', padx=10)
report_button.grid(row=0, column=4, sticky='w', padx=4)
# list frame
list_frame = Frame(body_frame)
list_frame.grid(row=1, column=0, sticky='wens')
list_frame.grid_columnconfigure(0, weight=1)
list_frame.grid_rowconfigure(0, weight=1)
# report text
report_text = ScrolledText(list_frame, bg='white', relief=GROOVE, font='TkFixedFont')
report_text.grid(row=0, column=0, sticky='news')
# status bar
status_frame = Frame(list_frame, bg='#4CAF50')
status_frame.grid(row=1, column=0, sticky='news')
status_frame.grid_columnconfigure(0, weight=1)
status_frame.grid_rowconfigure(0, weight=1)
# status text
status_label = Label(status_frame, text="Waiting for user ", bg=status_frame['bg'], fg='white', font=('bold', 14))
status_label.grid(row=0, column=0, sticky='news', pady=5)
# MAIN LOOP
window.mainloop()
