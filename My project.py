'''
Begin
'''

from tkinter import *

########################################################################

##############
#Window's Area
##############

james09 = Tk()
james09.title("Order's Manager")
james09.geometry('700x600+200+10')
james09.resizable(0,0)
james09.configure(bg = '#1d2951')
james09.state('iconic')


###############
#Top level Area
###############
james = Toplevel(bg = '#1d2951')
james.title("Order's Manager")
james.geometry('700x600+150+50')
james.resizable(0,0)
james.state('iconic')

zero = Toplevel(bg = '#1d2951')
zero.title("MANGER")
zero.geometry('100x600+60+10')
zero.resizable(0,0)
zero.state('iconic')
##################################3

zahir = Toplevel(bg = 'powder blue')
zahir.title("Order's Manager")
zahir.geometry('700x600+200+10')
zahir.resizable(0,0)

z = Toplevel(bg = '#1d2951')
z.title("MANGER")
z.geometry('100x600+60+10')
z.resizable(0,0)

#######################################################################

#################
#Programming Area
#################

#icons

##
zeroo = PhotoImage(file ='zero.png')
##
icon = PhotoImage(file ='flash.png')
##
message = PhotoImage(file ='sms.png')
##
total = PhotoImage(file ='run.png')
##
reset = PhotoImage(file ='delete.png')
##
play = PhotoImage(file ='on.png')
##
close = PhotoImage(file ='clo.png')
##
night = PhotoImage(file ='sce.png')
##
meal = PhotoImage(file ='meal.png')
##
sweets = PhotoImage(file ='sweet.png')
##
don = PhotoImage(file ='don.png')
##
besst = PhotoImage(file ='best1.png')
##
totall = PhotoImage(file ='total.png')



#########
#Methods
#########
serial = StringVar()
erorr = StringVar()
##
piz = IntVar()
fpiz = IntVar()
ber = IntVar()
xber = IntVar()
aga = IntVar()
hot = IntVar()
sha = IntVar()
shi = IntVar()
lem = IntVar()
car = IntVar()
wat = IntVar()
donat = IntVar()
cup = IntVar()
jato = IntVar()
totalll = IntVar()
##


def click1():
    if james09.state() == 'iconic' :
        butotal.config(state='disabled')
        bureset.config(state='disabled')
        bunight.config(state='disabled')
        buclose.config(state='disabled')
        zahir.destroy()
        z.destroy()
        zero.state('iconic')
        james.state('normal')

###
def serialkey():
    
    if serial.get() == 'orders311' :
        james.destroy()
        james09.state('normal')
        zero.state('normal')
        
    else :
        erorr.set("Invaild Serial Number")

    if james09.state() == 'normal' :
        butotal.config(state='normal')
        bureset.config(state='normal')
        bunight.config(state='normal')
        buclose.config(state='normal')

        
    
    

def nightmood():
    james09.configure(bg = '#ffb6c1')
    zero.config(bg='#ffb6c1')
    butotal.config(bg = '#ffb6c1')
    bureset.config(bg = '#ffb6c1')
    bunight.config(bg = '#ffb6c1')
    buclose.config(bg = '#ffb6c1')



def click3():
    if totalll.get() == 0 :
        a = (piz.get()*120) + (fpiz.get()*600)
        b = (ber.get()*100) + (xber.get()*200)
        c = (aga.get()*150) + (hot.get()*80)
        d = (sha.get()*80) + (shi.get()*60)
        e = (lem.get()*50) + (car.get()*50)
        f = (wat.get()*50) + (donat.get()*50)
        g = (cup.get()*100) + (jato.get()*1000)
        totalll.set(a+b+c+d+e+f+g)


def click4():
    piz.set(0)
    fpiz.set(0)
    ber.set(0)
    xber.set(0)
    aga.set(0)
    hot.set(0)
    sha.set(0)
    shi.set(0)
    lem.set(0)
    car.set(0)
    wat.set(0)
    donat.set(0)
    cup.set(0)
    jato.set(0)
    totalll.set(0)

def click5():
    james09.destroy()
    
    



#########################################################################



############
#Design Area
############

###############################
can = Canvas(zahir,width = 700 , height = 700 , bg = 'navy')
can.create_image(360,110,image=zeroo)
can.pack()
###############################

bunext = Button(z, image = icon , bg = "#1d2951",
                width= 60,
                height = 50,
                command = click1
                )
bunext.place(x = 20 ,rely = 0.2 )
#####################################

lbserial = Label(james,bg='#1d2951',
                 text="Inter The serial key",
                 fg = '#588bae' ,
                 font=('verdana',30,'bold')
                 )
lbserial.place(x = 150, y = 220)

##

entserial = Entry(james,bg = '#003152',
                  width = 30,
                  font=('Arial',15,'bold'),
                  show = '*',
                  textvariable = serial
                  )
entserial.place(x=180,y = 300)
##
buplay = Button(james,bg='#1d2951',
               image = play,
               width = 70,
               height = 50,
               command = serialkey
               )
buplay.place(x = 310 , y = 360)
##
lberorr = Label(james,bg='#1d2951',
                font=('verdana',15,'bold'),
                fg = 'red',
                textvariable = erorr
                )
lberorr.place(x = 220 , y = 440)

##

lbsend = Label(james,text="zahir.tarig@mail.ru",
               font=('courier',12,),
               fg = '#588bae',
               bg='#1d2951'
               )
lbsend.place(relx = 0.7 , rely = 0.9)
##
lbmes = Label(james,image = message,
              bg='#1d2951'
              )
lbmes.place(x =450 , rely = 0.9)

##############################################
# MANAGER



butotal = Button(zero,bg='#1d2951',
                 width = 50,
                 height = 50,
                 image = total,
                 command=click3
                 )
butotal.place(relx = 0.3 , y = 50)
##
bureset = Button(zero,bg='#1d2951',
                 width = 50,
                 height = 50,
                 image = reset,
                 command = click4
                 )
bureset.place(relx = 0.3 , y = 150)
##
bunight = Button(zero,bg='#1d2951',
                 width = 50,
                 height = 50,
                 image = night,
                 command = nightmood
                 )
bunight.place(relx = 0.3 , y = 260)
##
buclose = Button(zero,bg='#1d2951',
                 width = 50,
                 height = 50,
                 image = close,
                 command = click5
                 )
buclose.place(relx = 0.3 , y = 370)
##

###################################################################


#################
mnu = Menu(james09)

####
mnu_piz = Menu(james09)
mnu.add_cascade(label="Pizza",menu = mnu_piz)
mnu_piz.add_command(label = "pizza for one ps = 120")
mnu_piz.add_command(label = "Family pizza = 600")
###
mnu_bur = Menu(james09)
mnu.add_cascade(label="Berger",menu = mnu_bur)
mnu_bur.add_command(label = "Normal Berger = 100")
mnu_bur.add_command(label = "XXL Berger + ships = 200")
###
mnu_aga = Menu(james09)
mnu.add_cascade(label="Agashii" , menu = mnu_aga)
mnu_aga.add_command(label="Full Agashii meal = 150")
###
mnu_san = Menu(james09)
mnu.add_cascade(label="Sandwich", menu = mnu_san)
mnu_san.add_command(label="Hot dog = 80")
mnu_san.add_command(label="Shawrmaa = 80")
mnu_san.add_command(label="ships = 60")
###
mnu_swe = Menu(james09)
mnu.add_cascade(label = "sweets", menu = mnu_swe)
mnu_swe.add_command(label="Donat's = 50")
mnu_swe.add_command(label="Cup Cake= 100")
mnu_swe.add_command(label="Full Birth day jato = 1000")
###
mnu_ju = Menu(james09)
mnu.add_cascade(label="Juice", menu = mnu_ju)
mnu_ju.add_command(label="lemon = 50")
mnu_ju.add_command(label="Carrots = 50")
mnu_ju.add_command(label="WaterMelon = 50")
###
mnu_water = Menu(james09)
mnu.add_cascade(label="Water", menu = mnu_water)
mnu_water.add_command(label="Water is F R E E")



james09.config(menu = mnu)
################

canl = Canvas(james09,width=0.5,height=600)
canl.pack()

cn = Canvas(james09,width=350,height=0.5)
cn.place(relx=0.5 , y = 480)

################
#iconss

lbmeal = Label(james09,bg='#1d2951',image = meal)
lbmeal.place(x = 100 , y = 30)

lbsweets = Label(james09,bg = '#1d2951' , image = sweets)
lbsweets.place(x = 380 , y = 30)

lbsweets2 = Label(james09,bg = '#1d2951' , image = don)
lbsweets2.place(x = 530 , y = 30)

#######

lbpiz = Label(james09,text="PIZZA",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbpiz.place(x = 30, y = 200)

lbfpiz = Label(james09,text="FAMILY PIZZA",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbfpiz.place(x = 20, y = 250)

lbber = Label(james09,text="BERGER",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbber.place(x = 30, y = 300)

lbxber = Label(james09,text="XXXL BERGER",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbxber.place(x = 20, y = 350)

lbaga = Label(james09,text="AGASHI",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbaga.place(x = 30, y = 400)

lbhot = Label(james09,text="SAND-HOTDOG",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbhot.place(x = 20, y = 450)

lbsha = Label(james09,text="SHAWORMA",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbsha.place(x = 20, y = 500)

lbshi = Label(james09,text="SAND-SHIPS",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbshi.place(x = 20, y = 550)
######
lblem = Label(james09,text="LEMON",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lblem.place(x = 380, y = 200)

lbcar = Label(james09,text="CARROTS",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbcar.place(x = 370, y = 250)

lbwat = Label(james09,text="WATERMELON",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbwat.place(x = 360, y = 300)

lbdon = Label(james09,text="DONAT'S",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbdon.place(x = 360, y = 350)

lbcup = Label(james09,text="CUP-CAKE",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbcup.place(x = 360, y = 400)

lbjato = Label(james09,text="Jato",
              font = ('vardana',15,'bold'),
              bg = '#1d2951',
              fg='#8a2be2'
              )
lbjato.place(x = 360, y = 450)
#########################################################
entpiz = Entry(james09,bg = '#003152',
               width = 10,
               font=('Arial',15,'bold')
               ,textvariable = piz
               )
entpiz.place(x=190,y = 200)

entfpiz = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = fpiz
                )
entfpiz.place(x=190,y = 250)

entber = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = ber
               )
entber.place(x=190,y = 300)

entxber = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = xber
                )
entxber.place(x=190,y = 350)

entaga = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = aga
               )
entaga.place(x=190,y = 400)

enthot = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = hot
               )
enthot.place(x=190,y = 450)

entsha = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = sha
               )
entsha.place(x=190,y = 500)

entshi = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = shi
               )
entshi.place(x=190,y = 550)
###########################
entlem = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = lem
               )
entlem.place(x=550,y = 200)

entcar = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = car
               )
entcar.place(x=550,y = 250)

entwat = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = wat
               )
entwat.place(x=550,y = 300)

entdon = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = donat
               )
entdon.place(x=550,y = 350)

entcup = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'),textvariable = cup
               )
entcup.place(x=550,y = 400)

entjato = Entry(james09,bg = '#003152',
                  width = 10,
                  font=('Arial',15,'bold'), textvariable = jato
                )
entjato.place(x=550,y = 450)


#########################################################
##Total

enttotal = Button(james09,state='disabled',
                  bg = '#003152',
                  font=('Arial',15,'bold'),
                  width = 10,textvariable = totalll
                  )
enttotal.place(x = 550, y = 520)

best = Label(zero,image = besst
             )
best.place(x = -10 , y = 460)

#############################
lbtotal = Label(james09,image=totall,
                width = 128,
                height = 100,
                bd=6,
                relief = 'groove',
                #bg = '#8a2be2'
                )
lbtotal.place(x = 380, y = 490)



























########################################################################

'''
 End
'''
if __name__ == 'main' :
    zahir.mainloop()
