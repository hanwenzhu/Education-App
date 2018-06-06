# Education app
# Made by Andy, Thomas

# imports
import tkinter as Tk
from time import sleep
from os import path
from sys import exit
from random import randint
from pickle import load
from winsound import PlaySound, SND_FILENAME, SND_ASYNC

# Constants
countries = (
'America',
'Argentina',
'Australia',
'Brazil',
'Canada',
'China',
'France',
'Germany',
'India',
'Indonesia',
'Italy',
'Japan',
'Mexico',
'Netherlands',
'Russia',
'South Korea',
'Spain',
'Sweden',
'Switzerland',
'Thailand',
'Turkey')
vocab_file = open('rsc\\vocabs', 'rb')
v = load(vocab_file)
vocab_file.close()
vocabs = {}
vocab_words = []
for vo in sorted(v):
	vocabs[vo.capitalize()] = v[vo]
	vocab_words += [vo.capitalize()]
def click_async():
	PlaySound(None, SND_FILENAME)
	PlaySound('rsc\\click.wav', SND_ASYNC)
def click_sync():
	PlaySound(None, SND_FILENAME)
	PlaySound('rsc\\click.wav', SND_FILENAME)

# main window
tk = Tk.Tk()
tk.wm_attributes('-fullscreen', True)
tk.resizable(False, False)
tk.title('Education app')
tk.update()
main_menu = Tk.Canvas(tk, width=tk.winfo_width(), height=tk.winfo_height(), bd=0, highlightthickness=0, cursor='dotbox')
main_menu.grid(row=0, column=0)
flag_win = Tk.Canvas(tk, width=tk.winfo_width(), height=tk.winfo_height(), bd=0, highlightthickness=0, cursor='dotbox')
flag_win.grid(row=0, column=0)
timestable_win = Tk.Canvas(tk, width=tk.winfo_width(), height=tk.winfo_height(), bd=0, highlightthickness=0, cursor='dotbox')
timestable_win.grid(row=0, column=0)
vocab_win = Tk.Canvas(tk, width=tk.winfo_width(), height=tk.winfo_height(), bd=0, highlightthickness=0, cursor='dotbox')
vocab_win.grid(row=0, column=0)

# main menu
def flag(*args):
	Tk.Misc.lift(flag_win)
	flag_win.focus_set()
	click_async()
def timestable(*args):
	Tk.Misc.lift(timestable_win)
	timestable_win.focus_set()
	click_async()
def vocab(*args):
	Tk.Misc.lift(vocab_win)
	vocab_win.focus_set()
	click_async()
def back(*args):
	Tk.Misc.lift(main_menu)
	main_menu.focus_set()
	click_async()
Tk.Misc.lift(main_menu)
main_menu.focus_set()
def ex(*args):
	click_sync()
	exit(0)
exit_button = main_menu.create_rectangle(10,10,130,70,fill='#FF0000',tags='exit_button')
exit_text = main_menu.create_text(30,20,text='Exit',font=('Helvetica',32),anchor='nw',tags='exit_button')
main_menu.tag_bind("exit_button","<Button-1>",ex)
flag_button = main_menu.create_rectangle(500,150,800,220,fill='#00FF00',tags='flag_button')
flag_text = main_menu.create_text(510,160,text='National Flags',font=('Helvetica',32),anchor='nw',tags='flag_button')
main_menu.tag_bind("flag_button",'<Button-1>',flag)
timestable_button = main_menu.create_rectangle(500,240,800,310,fill='#00FF00',tags='timestable_button')
timestable_text = main_menu.create_text(530,250,text='Times table',font=('Helvetica',32),anchor='nw',tags='timestable_button')
main_menu.tag_bind("timestable_button",'<Button-1>',timestable)
vocab_button = main_menu.create_rectangle(500,330,800,400,fill='#00FF00',tags='vocab_button')
vocab_text = main_menu.create_text(540,340,text='Vocabulary',font=('Helvetica',32),anchor='nw',tags='vocab_button')
main_menu.tag_bind("vocab_button",'<Button-1>',vocab)

# flag window
back_button1 = flag_win.create_rectangle(10,10,130,70,fill='#AAAAAA',tags='back_button')
back_text1 = flag_win.create_text(20,20,text='Back',font=('Helvetica',32),anchor='nw',tags='back_button')
flag_win.tag_bind('back_button', '<Button-1>', back)
flag_title = flag_win.create_text(530, 20, text='National Flags', font=('Helvetica', 32),anchor='nw')
flags = {}
for c in countries:
	flags[c] = Tk.PhotoImage(file="rsc\\flags\\{0}.gif".format(c))
	while flags[c].width() > tk.winfo_width() - 240 or flags[c].height() > tk.winfo_height()-150 or flags[c].width()*2 < tk.winfo_width() - 240 and 2*flags[c].height() < tk.winfo_height()-150:
		if flags[c].width() > tk.winfo_width() - 240 or flags[c].height() > tk.winfo_height()-150:
			flags[c] = flags[c].subsample(2,2)
		elif flags[c].width()*2 < tk.winfo_width() - 240 and 2*flags[c].height() < tk.winfo_height()-150:
			flags[c] = flags[c].zoom(2,2)
flag_current = countries[randint(0,len(countries)-1)]
flag_image = flag_win.create_image(240,80,image=flags[flag_current],anchor='nw')
flag_str = ''
flag_in_text = flag_win.create_text(240,tk.winfo_height()-40,text='',font=('Helvetica', 32),anchor="sw")
flag_bank = flag_win.create_text(20, 90, text='\n'.join(countries), font=('Helvetica', 16), anchor='nw')
def flag_check(*args):
	global flag_str, flag_current
	if flag_str == flag_current:
		flag_current = countries[randint(0,len(countries)-1)]
		flag_win.itemconfig(flag_image, image=flags[flag_current],anchor='nw')
		flag_str = ''
		flag_win.itemconfig(flag_in_text, text=flag_str)
def flag_input(event):
	global flag_str
	flag_str += event.char
	flag_str = ' '.join(map(str.capitalize, flag_str.split(' ')))
	flag_win.itemconfig(flag_in_text, text=flag_str)
def flag_backspace(*args):
	global flag_str
	flag_str = flag_str[:-1]
	flag_win.itemconfig(flag_in_text, text=flag_str)
flag_win.bind('<Key>', flag_input)
flag_win.bind('<Return>', flag_check)
flag_win.bind('<BackSpace>', flag_backspace)

# timestable window
back_button2 = timestable_win.create_rectangle(10,10,130,70,fill='#AAAAAA',tags='back_button')
back_text2 = timestable_win.create_text(20,20,text='Back',font=('Helvetica',32),anchor='nw',tags='back_button')
timestable_win.tag_bind('back_button', '<Button-1>', back)
timestable_title = timestable_win.create_text(tk.winfo_width()/2, 50, text='Times table', font = ('Helvetica', 32))
timestable_current = [randint(1,9),randint(1,9)]
timestable_product = timestable_win.create_text(tk.winfo_width()/2,200,text='%d * %d' % (timestable_current[0],timestable_current[1]),font=('Helvetica', 64))
timestable_str = ''
timestable_in_text = timestable_win.create_text(tk.winfo_width()/2,tk.winfo_height()-80,text='',font=('Helvetica', 64))
def timestable_check(*args):
	global timestable_str, timestable_product, timestable_current
	if timestable_str == str(timestable_current[0]*timestable_current[1]):
		timestable_current = [randint(1,9),randint(1,9)]
		timestable_win.itemconfig(timestable_product, text='%d * %d' % (timestable_current[0],timestable_current[1]))
		timestable_str = ''
		timestable_win.itemconfig(timestable_in_text, text=timestable_str)
def timestable_input(event):
	global timestable_str
	timestable_str += event.char
	timestable_win.itemconfig(timestable_in_text, text=timestable_str)
def timestable_backspace(*args):
	global timestable_str
	timestable_str = timestable_str[:-1]
	timestable_win.itemconfig(timestable_in_text, text=timestable_str)
timestable_win.bind('<Key>', timestable_input)
timestable_win.bind('<Return>', timestable_check)
timestable_win.bind('<BackSpace>', timestable_backspace)



# vocab window
back_button3 = vocab_win.create_rectangle(10,10,130,70,fill='#AAAAAA',tags='back_button')
back_text3 = vocab_win.create_text(20,20,text='Back',font=('Helvetica',32),anchor='nw',tags='back_button')
vocab_win.tag_bind('back_button', '<Button-1>', back)
vocab_current = vocab_words[randint(0, len(vocab_words)-1)]
vocab_def = vocab_win.create_text(180,80,text=vocabs[vocab_current].capitalize(),font=('Helvetica', 32), anchor='nw')
vocab_str = ''
vocab_in_text = vocab_win.create_text(240,tk.winfo_height()-40,text='',font=('Helvetica', 32),anchor="sw")
vocab_bank = vocab_win.create_text(tk.winfo_width() - 20, 200, text='\n'.join(vocab_words), font=('Helvetica', 16), anchor='ne')
def vocab_check(*args):
	global vocab_str, vocab_current
	if vocab_str == vocab_current:
		vocab_current = vocab_words[randint(0,len(vocab_words)-1)]
		vocab_win.itemconfig(vocab_def, text=vocabs[vocab_current].capitalize())
		vocab_str = ''
		vocab_win.itemconfig(vocab_in_text, text=vocab_str)
def vocab_input(event):
	global vocab_str
	vocab_str += event.char
	vocab_str = vocab_str.capitalize()
	vocab_win.itemconfig(vocab_in_text, text=vocab_str)
def vocab_backspace(*args):
	global vocab_str
	vocab_str = vocab_str[:-1]
	vocab_win.itemconfig(vocab_in_text, text=vocab_str)
vocab_win.bind('<Key>', vocab_input)
vocab_win.bind('<Return>', vocab_check)
vocab_win.bind('<BackSpace>', vocab_backspace)

# main loop
tk.mainloop()