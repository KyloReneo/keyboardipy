import tkinter as tk
from tkinter import ttk

key = tk.Tk()  # key window name
key.title('vKeyboard By SaEeD :)')  # title Name

# key.iconbitmap('add icon link And Directory name')    # icon add

# function coding start 


exp = " "          # global variable 
# showing all data in display 

def press(num):
    global exp
    exp=exp + str(num)
    equation.set(exp)
# end 


# function clear button

def clear():
    global exp
    exp = " "
    equation.set(exp)

# end 


# Enter Button Work Next line Function

def action():
  exp = " Next Line : "
  equation.set(exp)

# end function coding


# Tab Button Function 


def Tab():
  exp = " TAB : "
  equation.set(exp)

# END Tab Button Fucntion

#Copy function

def copy_text ():
    txt = Dis_entry.get ()
    print (txt)
    key.clipboard_append (txt)



# Size window size
key.geometry('1330x430')         # normal size
key.maxsize(width=1330, height=430)      # maximum size
key.minsize(width= 1330 , height = 430)     # minimum size
# end window size

key.configure(bg = 'black')    #  add background color

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)
# end entry box

# add all button line wise 

# First Line Button

q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
q.grid(row = 2, column = 0, ipadx = 20 , ipady = 10)

w = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
w.grid(row = 2, column = 1, ipadx = 20 , ipady = 10)

E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 2 , column = 2, ipadx = 20 , ipady = 10)

R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 2, column = 3, ipadx = 20 , ipady = 10)

T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 2, column = 4, ipadx = 20 , ipady = 10)

Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 2, column = 5, ipadx = 20 , ipady = 10)

U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 2, column = 6, ipadx = 20 , ipady = 10)

I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 2, column = 7, ipadx = 20 , ipady = 10)

O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 2, column = 8, ipadx = 20 , ipady = 10)

P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 2, column = 9, ipadx = 20 , ipady = 10)

cur = ttk.Button(key,text = '{' , width = 6, command = lambda : press('{'))
cur.grid(row = 2, column = 10 , ipadx = 20 , ipady = 10)

cur_c = ttk.Button(key,text = '}' , width = 6, command = lambda : press('}'))
cur_c.grid(row = 2, column = 11, ipadx = 20 , ipady = 10)

back_slash = ttk.Button(key,text = '\\' , width = 6, command = lambda : press('\\'))
back_slash.grid(row = 2, column = 12, ipadx = 20 , ipady = 10)


clear = ttk.Button(key,text = 'Clear' , width = 11, command = clear)
clear.grid(row = 8 , column = 11 , ipadx = 6 , ipady = 10)

# Second Line Button



A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 3, column = 0, ipadx = 20 , ipady = 10)



S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 3, column = 1, ipadx = 20 , ipady = 10)

D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 3, column = 2, ipadx = 20 , ipady = 10)

F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 3, column = 3, ipadx = 20 , ipady = 10)


G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 3, column = 4, ipadx = 20 , ipady = 10)


H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 3, column = 5, ipadx = 20 , ipady = 10)


J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 3, column = 6, ipadx = 20 , ipady = 10)


K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 3 , column = 7, ipadx = 20 , ipady = 10)

L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 3 , column = 8, ipadx = 20 , ipady = 10)


semi_co = ttk.Button(key,text = '"' , width = 6, command = lambda : press('"'))
semi_co.grid(row = 3 , column = 9, ipadx = 20 , ipady = 10)


# d_colon = ttk.Button(key,text = '"' , width = 6, command = lambda : press('"'))
# d_colon.grid(row = 3 , column = 10, ipadx = 20 , ipady = 10)


enter = ttk.Button(key,text = 'Enter' , width = 6, command = action)
enter.grid(row = 3 , column = 10, ipadx = 20 , ipady = 10)

# third line Button

Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 4 , column = 0, ipadx = 20 , ipady = 10)


X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 4, column = 1, ipadx = 20 , ipady = 10)


C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 4 , column = 2, ipadx = 20 , ipady = 10)


V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 4 , column = 3, ipadx = 20 , ipady = 10)

B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 4, column = 4 , ipadx = 20 ,ipady = 10)


N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 4, column = 5, ipadx = 20 , ipady = 10)


M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 4 , column = 6, ipadx = 20 , ipady = 10)


left = ttk.Button(key,text = '<' , width = 6, command = lambda : press('<'))
left.grid(row = 4 , column = 7, ipadx = 20 , ipady = 10)


right = ttk.Button(key,text = '>' , width = 6, command = lambda : press('>'))
right.grid(row = 4 , column = 8, ipadx = 20 , ipady = 10)


slas = ttk.Button(key,text = '/' , width = 6, command = lambda : press('/'))
slas.grid(row = 4 , column = 9, ipadx = 20 , ipady = 10)


q_mark = ttk.Button(key,text = '?' , width = 6, command = lambda : press('?'))
q_mark.grid(row = 4 , column = 10, ipadx = 20 , ipady = 10)


coma = ttk.Button(key,text = ',' , width = 6, command = lambda : press(','))
coma.grid(row = 4 , column = 11, ipadx = 20 , ipady = 10)

dot = ttk.Button(key,text = '.' , width = 6, command = lambda : press('.'))
dot.grid(row = 4 , column = 12, ipadx = 20 , ipady = 10)

Copy = ttk.Button(key,text = 'Copy!' , width = 11, command = copy_text)
Copy.grid(row = 8 , column = 10 , ipadx = 6 , ipady = 10)



#Fourth Line Button

one = ttk.Button(key,text = '1' , width = 6, command = lambda : press('1'))
one.grid(row = 1 , column = 0, ipadx = 20 , ipady = 10)


two = ttk.Button(key,text = '2' , width = 6, command = lambda : press('2'))
two.grid(row = 1 , column = 1, ipadx = 20 , ipady = 10)


three = ttk.Button(key,text = '3' , width = 6, command = lambda : press('3'))
three.grid(row = 1 , column = 2, ipadx = 20 , ipady = 10)


four = ttk.Button(key,text = '4' , width = 6, command = lambda : press('4'))
four.grid(row = 1 , column = 3, ipadx = 20 , ipady = 10)

five = ttk.Button(key, text= '5' , width = 6 , command = lambda : press('5'))
five.grid(row = 1 , column = 4 , ipadx = 20 ,ipady = 10)


six = ttk.Button(key,text = '6' , width = 6, command = lambda : press('6'))
six.grid(row = 1 , column = 5, ipadx = 20 , ipady = 10)


seven = ttk.Button(key,text = '7' , width = 6, command = lambda : press('7'))
seven.grid(row = 1 , column = 6, ipadx = 20 , ipady = 10)


eight = ttk.Button(key,text = '8' , width = 6, command = lambda : press('8'))
eight.grid(row = 1 , column = 7, ipadx = 20 , ipady = 10)


nine = ttk.Button(key,text = '9' , width = 6, command = lambda : press('9'))
nine.grid(row = 1 , column = 8, ipadx = 20 , ipady = 10)


zero = ttk.Button(key,text = '0' , width = 6, command = lambda : press('0'))
zero.grid(row = 1 , column = 9, ipadx = 20 , ipady = 10)


p1 = ttk.Button(key,text = '(' , width = 6, command = lambda : press('('))
p1.grid(row = 1 , column = 10, ipadx = 20 , ipady = 10)


p2 = ttk.Button(key,text = ')' , width = 6, command = lambda : press(')'))
p2.grid(row = 1 , column = 11, ipadx = 20 , ipady = 10)

star = ttk.Button(key,text = '*' , width = 6, command = lambda : press('*'))
star.grid(row = 1 , column = 12, ipadx = 20 , ipady = 10)

#Fifth Line

z1 = ttk.Button(key,text = 'ض' , width = 6, command = lambda : press('ض'))
z1.grid(row = 5 , column = 0, ipadx = 20 , ipady = 10)


s1 = ttk.Button(key,text = 'ص' , width = 6, command = lambda : press('ص'))
s1.grid(row = 5 , column = 1, ipadx = 20 , ipady = 10)


s2 = ttk.Button(key,text = 'ث' , width = 6, command = lambda : press('ث'))
s2.grid(row = 5 , column = 2, ipadx = 20 , ipady = 10)


gh1 = ttk.Button(key,text = 'ق' , width = 6, command = lambda : press('ق'))
gh1.grid(row = 5 , column = 3, ipadx = 20 , ipady = 10)

feh = ttk.Button(key, text= 'ف' , width = 6 , command = lambda : press('ف'))
feh.grid(row = 5 , column = 4 , ipadx = 20 ,ipady = 10)


gh2 = ttk.Button(key,text = 'غ' , width = 6, command = lambda : press('غ'))
gh2.grid(row = 5 , column = 5, ipadx = 20 , ipady = 10)


eyn = ttk.Button(key,text = 'ع' , width = 6, command = lambda : press('ع'))
eyn.grid(row = 5 , column = 6, ipadx = 20 , ipady = 10)


heh = ttk.Button(key,text = 'ه' , width = 6, command = lambda : press('ه'))
heh.grid(row = 5 , column = 7, ipadx = 20 , ipady = 10)


kh = ttk.Button(key,text = 'خ' , width = 6, command = lambda : press('خ'))
kh.grid(row = 5 , column = 8, ipadx = 20 , ipady = 10)


heh2 = ttk.Button(key,text = 'ح' , width = 6, command = lambda : press('ح'))
heh2.grid(row = 5 , column = 9, ipadx = 20 , ipady = 10)


ge = ttk.Button(key,text = 'ج' , width = 6, command = lambda : press('ج'))
ge.grid(row = 5 , column = 10, ipadx = 20 , ipady = 10)


che = ttk.Button(key,text = 'چ' , width = 6, command = lambda : press('چ'))
che.grid(row = 5 , column = 11, ipadx = 20 , ipady = 10)

pe = ttk.Button(key,text = 'پ' , width = 6, command = lambda : press('پ'))
pe.grid(row = 5 , column = 12, ipadx = 20 , ipady = 10)


#6

z1x = ttk.Button(key,text = 'ش' , width = 6, command = lambda : press('ش'))
z1x.grid(row = 6 , column = 0, ipadx = 20 , ipady = 10)


s1d = ttk.Button(key,text = 'س' , width = 6, command = lambda : press('س'))
s1d.grid(row = 6 , column = 1, ipadx = 20 , ipady = 10)


s2d = ttk.Button(key,text = 'ی' , width = 6, command = lambda : press('ی'))
s2d.grid(row = 6 , column = 2, ipadx = 20 , ipady = 10)


gh1m = ttk.Button(key,text = 'ب' , width = 6, command = lambda : press('ب'))
gh1m.grid(row = 6 , column = 3, ipadx = 20 , ipady = 10)

fehn = ttk.Button(key, text= 'ل' , width = 6 , command = lambda : press('ل'))
fehn.grid(row = 6 , column = 4 , ipadx = 20 ,ipady = 10)


gh2b = ttk.Button(key,text = 'ا' , width = 6, command = lambda : press('ا'))
gh2b.grid(row = 6 , column = 5, ipadx = 20 , ipady = 10)


eyna = ttk.Button(key,text = 'ت' , width = 6, command = lambda : press('ت'))
eyna.grid(row = 6 , column = 6, ipadx = 20 , ipady = 10)


hehs = ttk.Button(key,text = 'ن' , width = 6, command = lambda : press('ن'))
hehs.grid(row = 6 , column = 7, ipadx = 20 , ipady = 10)


khd = ttk.Button(key,text = 'م' , width = 6, command = lambda : press('م'))
khd.grid(row = 6 , column = 8, ipadx = 20 , ipady = 10)


heh2b = ttk.Button(key,text = 'ک' , width = 6, command = lambda : press('ک'))
heh2b.grid(row = 6 , column = 9, ipadx = 20 , ipady = 10)


geh = ttk.Button(key,text = 'گ' , width = 6, command = lambda : press('گ'))
geh.grid(row = 6 , column = 10, ipadx = 20 , ipady = 10)


pp = ttk.Button(key,text = '+' , width = 6, command = lambda : press('+'))
pp.grid(row = 6 , column = 11, ipadx = 20 , ipady = 10)

ii = ttk.Button(key,text = '=' , width = 6, command = lambda : press('='))
ii.grid(row = 6 , column = 12, ipadx = 20 , ipady = 10)


#7


z1 = ttk.Button(key,text = 'ظ' , width = 6, command = lambda : press('ظ'))
z1.grid(row = 7 , column = 0, ipadx = 20 , ipady = 10)


s1 = ttk.Button(key,text = 'ط' , width = 6, command = lambda : press('ط'))
s1.grid(row = 7 , column = 1, ipadx = 20 , ipady = 10)


s2 = ttk.Button(key,text = 'ز' , width = 6, command = lambda : press('ز'))
s2.grid(row = 7 , column = 2, ipadx = 20 , ipady = 10)


gh1 = ttk.Button(key,text = 'ر' , width = 6, command = lambda : press('ر'))
gh1.grid(row = 7 , column = 3, ipadx = 20 , ipady = 10)

feh = ttk.Button(key, text= 'ذ' , width = 6 , command = lambda : press('ذ'))
feh.grid(row = 7 , column = 4 , ipadx = 20 ,ipady = 10)


gh2 = ttk.Button(key,text = 'د' , width = 6, command = lambda : press('د'))
gh2.grid(row = 7 , column = 5, ipadx = 20 , ipady = 10)


eyn = ttk.Button(key,text = 'ئ' , width = 6, command = lambda : press('ئ'))
eyn.grid(row = 7 , column = 6, ipadx = 20 , ipady = 10)


heh = ttk.Button(key,text = 'و' , width = 6, command = lambda : press('و'))
heh.grid(row = 7 , column = 7, ipadx = 20 , ipady = 10)


kh = ttk.Button(key,text = '.' , width = 6, command = lambda : press('.'))
kh.grid(row = 7 , column = 8, ipadx = 20 , ipady = 10)


heh2 = ttk.Button(key,text = ';' , width = 6, command = lambda : press(';'))
heh2.grid(row = 7 , column = 9, ipadx = 20 , ipady = 10)


ge = ttk.Button(key,text = ':' , width = 6, command = lambda : press(':'))
ge.grid(row = 7 , column = 10, ipadx = 20 , ipady = 10)


che = ttk.Button(key,text = '-' , width = 6, command = lambda : press('-'))
che.grid(row = 7 , column = 11, ipadx = 20 , ipady = 10)

pe = ttk.Button(key,text = '_' , width = 6, command = lambda : press('_'))
pe.grid(row = 7 , column = 12, ipadx = 20 , ipady = 10)


#8

ctrl = ttk.Button(key,text = 'Ctrl' , width = 15, command = lambda : press('Ctrl'))
ctrl.grid(row = 8 , column = 0, ipadx = 6 , ipady = 10)


Fn = ttk.Button(key,text = 'Fn' , width = 16, command = lambda : press('Fn'))
Fn.grid(row = 8 , column = 1, ipadx = 6 , ipady = 10)


window = ttk.Button(key,text = 'Window' , width = 12, command = lambda : press('Window'))
window.grid(row = 8 , column = 2 , ipadx = 6 , ipady = 10)

Alt = ttk.Button(key,text = 'Alt' , width = 12, command = lambda : press('Alt'))
Alt.grid(row = 8 , column = 3 , ipadx = 6 , ipady = 10)

space = ttk.Button(key,text = 'Space' , width = 25, command = lambda : press(' '))
space.grid(row = 8 , columnspan = 14 , ipadx = 160 , ipady = 10)

# Alt_gr = ttk.Button(key,text = 'Alt Gr' , width = 6, command = lambda : press('Alt Gr'))
# Alt_gr.grid(row = 8 , column = 10 , ipadx = 6 , ipady = 10)

# open_b = ttk.Button(key,text = '(' , width = 6, command = lambda : press('('))
# open_b.grid(row = 8 , column = 11 , ipadx = 6 , ipady = 10)

# close_b = ttk.Button(key,text = ')' , width = 6, command = lambda : press(')'))
# close_b.grid(row = 8 , column = 12 , ipadx = 6 , ipady = 10)


# tap = ttk.Button(key,text = 'Tab' , width = 6, command = Tab)
# tap.grid(row = 8 , column = 13 , ipadx = 20 , ipady = 10)



key.mainloop()  # using ending point
