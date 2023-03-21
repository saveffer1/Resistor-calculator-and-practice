import tkinter.messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from sympy import pretty_print as pp, latex
from sympy.abc import a, b, n
from random import*
from time import*
from practice import*
import sqlite3

conn = sqlite3.connect('bgcolor.db')
cursor = conn.execute("SELECT NAME from SAVEONE")
rows = cursor.fetchone()[0]
conn.close()

titlefsize = 41
widthsize = 10

def background(back):
    back = rows
    return back

def maxbg():
    mbg = rows
    return mbg

bgset = rows

def grid_hide(widget):
    widget._grid_info = widget.grid_info()
    widget.grid_remove()

def grid_show(widget):
    widget.grid(**widget._grid_info)

def sfformat(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

class Treath:
    def __init__(self,app):
        self.app = app
        bgset = "indianred"
        self.app.title("saveffer resistor Training")
        self.app.iconbitmap("icon.ico")
        self.app.geometry("965x500+0+0")
        self.app.configure(background =bgset)
        #self.app.wm_attributes('-transparentcolor','cyan4')
        #photo1 = PhotoImage(file="resbody.png")
        photo1 = PhotoImage(file="resbody - Copy.v1.png")
        photo1 = photo1.subsample(2)
        #photo1 = photo1.zoom(2)

        th = 1
        clsp = 40
        clspan = 14

        var1 = DoubleVar()
        var2 = DoubleVar()
        var3 = DoubleVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = StringVar()
        var7 = DoubleVar()
        var8 = StringVar()

        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        var6.set("")
        var7.set("")
        var8.set("")

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()

        colorresval = ["black","brown","red","orange","yellow","green","blue","purple","grey","white"]
        colorresvaldict = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"purple":7,"grey":8,"white":9}
        colorresmult = ["black","brown","red","orange","yellow","green","blue","purple","grey","white","gold","silver"]
        colorrestolorance = ["black","brown","red","green","blue","purple","grey","gold","silver","white"]

        colorresppm = ["black","brown","red","orange","yellow","green","blue","purple","grey"]

        translateval = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","orange":"ส้ม","yellow":"เหลือง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา","white":"ขาว"," ":" "}
        translatemult = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","orange":"ส้ม","yellow":"เหลือง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา","white":"ขาว","gold":"ทอง","silver":"เงิน"," ":" "}
        translatetoloro = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา","gold":"ทอง","silver":"เงิน","white":"ขาว"," ":" "}
        translateppm = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","orange":"ส้ม","yellow":"เหลือง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา"," ":" "}

        ranval1 = choice(colorresval)
        ranval2 = choice(colorresval)
        ranval3 = choice(colorresval)
        ranmult = choice(colorresmult)
        rantolorance = choice(colorrestolorance)
        ranppm = choice(colorresppm)

        def grid_hide(widget):
            widget._grid_info = widget.grid_info()
            widget.grid_remove()

        def grid_show(widget):
            widget.grid(**widget._grid_info)

        def reset1():
            reset1 = tkinter.messagebox.askyesno("โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี","คุณต้องการรีเซ็ตหรือไม่?")
            if reset1 > 0:
                var1.set("")
                var2.set("")
                var3.set("")
                var4.set("")
                var5.set("")
                var6.set("")
                var7.set("")
                var8.set("")
                return

        def exit1():
            exit1 = tkinter.messagebox.askyesno("โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี","คุณต้องการออกหรือไม่?")
            if exit1 > 0:
                app.destroy()
                return
        def f4b():
            clspan = 15
            self.rescol1 = Label(rsframe,width = 2,height = 5,bg = "white")
            self.rescol1.grid(row=3,column = 4)

            self.rescol2 = Label(rsframe,width = 2,height = 4,bg = "white")
            self.rescol2.grid(row=3,column = 5)

            self.rescol3 = Label(rsframe,width = 2,height = 4,bg = "white")
            self.rescol3.grid(row=3,column = 7)

            self.rescol3 = Label(rsframe,width = 2,height = 4,bg = "white")
            self.rescol3.grid(row=3,column = 8)

        def f5b():
            clspan = 14
            self.rescol1 = Label(rsframe,width = 2,height = 5,bg = "brown")
            self.rescol1.grid(row=3,column = 4)

            self.rescol5 = Label(rsframe,width = 2,height = 4,bg = "black")
            self.rescol5.grid(row=3,column = 6)

            self.rescol2 = Label(rsframe,width = 2,height = 4,bg = "black")
            self.rescol2.grid(row=3,column = 5)

            self.rescol3 = Label(rsframe,width = 2,height = 4,bg = "red")
            self.rescol3.grid(row=3,column = 7)

            self.rescol4 = Label(rsframe,width = 2,height = 4,bg = "gold")
            self.rescol4.grid(row=3,column = 8)

        def f6b():
            clspan = 14
            self.rescol1 = Label(rsframe,width = 2,height = 5,bg = "brown")
            self.rescol1.grid(row=3,column = 4)

            self.rescol5 = Label(rsframe,width = 2,height = 4,bg = "black")
            self.rescol5.grid(row=3,column = 6)

            self.rescol2 = Label(rsframe,width = 2,height = 4,bg = "black")
            self.rescol2.grid(row=3,column = 5)

            self.rescol3 = Label(rsframe,width = 2,height = 4,bg = "red")
            self.rescol3.grid(row=3,column = 7)

            self.rescol4 = Label(rsframe,width = 2,height = 4,bg = "gold")
            self.rescol4.grid(row=3,column = 8)

            self.rescol6 = Label(rsframe,width = 2,height = 5,bg = "brown")
            self.rescol6.grid(row=3,column = 9)

        def colosh(val1,val2,mult,tolo,val3,ppm):
            colorshow = CheckVar2.get()
            print("colorshow = ",colorshow)
            boxset = 12
            val11 = translateval[val1]
            val22 = translateval[val2]
            valmt = translatemult[mult]
            valtolo = translatetoloro[tolo]
            val33 = translateval[val3]
            valpp = translateppm[ppm]
            x1 = 6
            x2 =7
            x3 = 9
            x4 = 10
            x5 = 8
            x6 = 11

            if th == 1:
                if colorshow == 0:
                
                    self.show0 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "                      ",fg = "black",bg = bgset)
                    self.show0.grid(row=0,column = 0)
                    
                    self.show1 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "            ",fg = "black",bg = bgset)
                    self.show1.grid(row=0,column = x1)

                    self.show2 = Label(txtcolr,font = ('arial',boxset,'bold'),text= "             ",fg = "black",bg = bgset)
                    self.show2.grid(row=0,column = x2)

                    self.show3 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "            ",fg = "black",bg = bgset)
                    self.show3.grid(row=0,column = x3)

                    self.show4 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "            ",fg = "black",bg = bgset)
                    self.show4.grid(row=0,column = x4)

                    self.show5 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show5.grid(row=0,column = x5)

                    self.show6 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show6.grid(row=0,column = x6)


                    self.show1 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show1.grid(row=1,column = x1)
                    self.show1 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show1.grid(row=1,column = x1)

                    self.show2 = Label(txtcolr,font = ('arial',boxset,'bold'),text= "              ",fg = "black",bg = bgset)
                    self.show2.grid(row=1,column = x2)

                    self.show3 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show3.grid(row=1,column = x3)

                    self.show4 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show4.grid(row=1,column = x4)

                    self.show5 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show5.grid(row=1,column = x5)

                    self.show6 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "             ",fg = "black",bg = bgset)
                    self.show6.grid(row=1,column = x6)



                    self.show1 = Label(txtcolr,font = ('arial',boxset,'bold'),text = val11,fg = "black",bg = bgset)
                    self.show1.grid(row=1,column = x1)

                    self.show2 = Label(txtcolr,font = ('arial',boxset,'bold'),text = val22,fg = "black",bg = bgset)
                    self.show2.grid(row=1,column = x2)

                    self.show3 = Label(txtcolr,font = ('arial',boxset,'bold'),text = valmt,fg = "black",bg = bgset)
                    self.show3.grid(row=1,column = x3)

                    self.show4 = Label(txtcolr,font = ('arial',boxset,'bold'),text = valtolo,fg = "black",bg = bgset)
                    self.show4.grid(row=1,column = x4)

                    self.show5 = Label(txtcolr,font = ('arial',boxset,'bold'),text = val33,fg = "black",bg = bgset)
                    self.show5.grid(row=1,column = x5)

                    self.show6 = Label(txtcolr,font = ('arial',boxset,'bold'),text = valpp,fg = "black",bg = bgset)
                    self.show6.grid(row=1,column = x6)
            else:
                if colorshow == 0:
                    self.show1 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "                    ",fg = "black",bg = bgset)
                    self.show1.grid(row=0,column = x1)

                    self.show2 = Label(txtcolr,font = ('arial',boxset,'bold'),text= "                    ",fg = "black",bg = bgset)
                    self.show2.grid(row=0,column = x2)

                    self.show3 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "                    ",fg = "black",bg = bgset)
                    self.show3.grid(row=0,column = x3)

                    self.show4 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "                    ",fg = "black",bg = bgset)
                    self.show4.grid(row=0,column = x4)

                    self.show5 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "                    ",fg = "black",bg = bgset)
                    self.show5.grid(row=0,column = x5)

                    self.show6 = Label(txtcolr,font = ('arial',boxset,'bold'),text = "                    ",fg = "black",bg = bgset)
                    self.show6.grid(row=0,column = x6)


                    self.show1 = Label(txtcolr,font = ('arial',boxset,'bold'),text = val1,fg = "black",bg = bgset)
                    self.show1.grid(row=0,column = x1)

                    self.show2 = Label(txtcolr,font = ('arial',boxset,'bold'),text = val2,fg = "black",bg = bgset)
                    self.show2.grid(row=0,column = x2)

                    self.show3 = Label(txtcolr,font = ('arial',boxset,'bold'),text = mult,fg = "black",bg = bgset)
                    self.show3.grid(row=0,column = x3)

                    self.show4 = Label(txtcolr,font = ('arial',boxset,'bold'),text = tolo,fg = "black",bg = bgset)
                    self.show4.grid(row=0,column = x4)

                    self.show5 = Label(txtcolr,font = ('arial',boxset,'bold'),text = val3,fg = "black",bg = bgset)
                    self.show5.grid(row=0,column = x5)

                    self.show6 = Label(txtcolr,font = ('arial',boxset,'bold'),text = ppm,fg = "black",bg = bgset)
                    self.show6.grid(row=0,column = x6)

        def thebands():
            vala = CheckVar1.get()
            print("vala = ",vala)
            ranval1 = choice(colorresval)
            ranval2 = choice(colorresval)
            ranval3 = choice(colorresval)
            ranmult = choice(colorresmult)
            rantolorance = choice(colorrestolorance)
            ranppm = choice(colorresppm)
            x1 = " "
            x2 = " "
            x3 = " "
            x4 = " "
            x5 = " "
            x6 = " "

            self.rescol5 = Label(rsframe,width = 2,height = 6,bg = ranval2)
            self.rescol5.grid(row=3,column = 4)

            self.rescol6 = Label(rsframe,width = 2,height = 7,bg = ranppm)
            self.rescol6.grid(row=3,column = 7)


            if vala == 0:
                clspan = 14
                x1 = str(ranval1)
                x2 = str(ranval2)
                x3 = str(ranmult)
                x4 = str(rantolorance)
                x5 = " "
                x6 = " "

                resimfdg = Label(rsframe, text="1", bg=bgset, width=550,height = 400,image=photo1)
                resimfdg.image = photo1
                resimfdg.grid(row=1, column=0,rowspan = 5,columnspan = 11,sticky="news")
                
                self.rescol1 = Label(rsframe,width = 2,height = 7,bg = ranval1)
                self.rescol1.grid(row=3,column = 2)

                self.rescol2 = Label(rsframe,width = 2,height = 6,bg = ranval2)
                self.rescol2.grid(row=3,column = 3)

                self.rescol3 = Label(rsframe,width = 2,height = 6,bg = ranmult)
                self.rescol3.grid(row=3,column = 5)

                self.rescol4 = Label(rsframe,width = 2,height = 6,bg = rantolorance)
                self.rescol4.grid(row=3,column = 6)

                self.rescol5 = Label(rsframe,width = 2,height = 6,bg = ranval2)
                self.rescol5.grid(row=3,column = 4)

                grid_hide(self.rescol5)
                grid_hide(self.rescol6)
                
                colosh(ranval1,ranval2,ranmult,rantolorance," "," ")



            elif vala == 1:
                clspan = 14
                x1 = str(ranval1)
                x2 = str(ranval2)
                x3 = str(ranmult)
                x4 = str(rantolorance)
                x5 = str(ranval3)
                x6 = " "

                
                self.rescol1 = Label(rsframe,width = 2,height = 7,bg = ranval1)
                self.rescol1.grid(row=3,column = 2)

                self.rescol5 = Label(rsframe,width = 2,height = 6,bg = ranval3)
                self.rescol5.grid(row=3,column = 4)

                self.rescol2 = Label(rsframe,width = 2,height = 6,bg = ranval2)
                self.rescol2.grid(row=3,column = 3)

                self.rescol3 = Label(rsframe,width = 2,height = 6,bg = ranmult)
                self.rescol3.grid(row=3,column = 5)

                self.rescol4 = Label(rsframe,width = 2,height = 6,bg = rantolorance)
                self.rescol4.grid(row=3,column = 6)
               
                grid_hide(self.rescol6)

                colosh(ranval1,ranval2,ranmult,rantolorance,ranval3," ")

            elif vala == 2:
                clspan = 14
                x1 = str(ranval1)
                x2 = str(ranval2)
                x3 = str(ranmult)
                x4 = str(rantolorance)
                x5 = str(ranval3)
                x6 = str(ranppm)
                
                self.rescol1 = Label(rsframe,width = 2,height = 7,bg = ranval1)
                self.rescol1.grid(row=3,column = 2)

                self.rescol5 = Label(rsframe,width = 2,height = 6,bg = ranval2)
                self.rescol5.grid(row=3,column = 4)

                self.rescol2 = Label(rsframe,width = 2,height = 6,bg = ranval3)
                self.rescol2.grid(row=3,column = 3)

                self.rescol3 = Label(rsframe,width = 2,height = 6,bg = ranmult)
                self.rescol3.grid(row=3,column = 5)

                self.rescol4 = Label(rsframe,width = 2,height = 6,bg = rantolorance)
                self.rescol4.grid(row=3,column = 6)

                self.rescol6 = Label(rsframe,width = 2,height = 7,bg = ranppm)
                self.rescol6.grid(row=3,column = 7)

                colosh(ranval1,ranval2,ranmult,rantolorance,ranval3,ranppm)

            else:
                grid_hide(self.rescol1)
                grid_hide(self.rescol2)
                grid_hide(self.rescol3)
                grid_hide(self.rescol4)
                grid_hide(self.rescol5)
                grid_hide(self.rescol6)
            
            return str(x1),str(x2),str(x3),str(x4),str(x5),str(x6);

        def ban():
            gotplan = thebands()
            colosh(gotplan[0],gotplan[1],gotplan[2],gotplan[3],gotplan[4],gotplan[5])

        frame1 = Frame(self.app,width = 800,height = 400,bg = bgset)
        frame1.grid(row=0,column=0)

        frame2 = Frame(self.app,width = 250,height = 400,bg = bgset)
        frame2.grid(row=0,column=1,sticky = "nse")

        frame3 = Frame(self.app,width = 250,height = 400,bg = bgset)
        frame3.grid(row=1,column=0,columnspan = 2)
        

        menubar=Menu(app)
        mmnnuu=Menu(menubar,tearoff=0)
        mmnnuu.add_command(label="รีเซ็ต",command = reset1)
        mmnnuu.add_command(label="ออก",command = exit1)
        menubar.add_cascade(label="เมนู",menu=mmnnuu)
        app.config(menu=menubar)
        
        rsframe = Frame(frame1,width = 550,bd = 10,bg = bgset,padx = 15,pady = 3,relief = RIDGE)
        rsframe.grid(sticky="nsw")

        resimfdg = Label(rsframe, text="1", bg=bgset, width=550,height = 400,image=photo1)
        resimfdg.image = photo1
        resimfdg.grid(row=1, column=0,rowspan = 5,columnspan = 10,sticky="news")

        txtcolr = Frame(rsframe, bg=bgset,padx = 15,pady = 3,relief = RIDGE)
        txtcolr.grid(row=0, column=0,columnspan = clsp,sticky="news")


        self.rescol1 = Label(rsframe,width = 2,height = 7,bg = ranval1)
        self.rescol1.grid(row=3,column = 2)

        self.rescol2 = Label(rsframe,width = 2,height = 6,bg = ranval2)
        self.rescol2.grid(row=3,column = 3)

        self.rescol3 = Label(rsframe,width = 2,height = 6,bg = ranmult)
        self.rescol3.grid(row=3,column = 5)

        self.rescol4 = Label(rsframe,width = 2,height = 6,bg = rantolorance)
        self.rescol4.grid(row=3,column = 6)


        indicatorframe =  Frame(frame2,width = 250,height = 400,bd = 10,bg = bgset,padx = 42,pady = 8,relief = RIDGE)
        indicatorframe.grid(row=0,column=0, sticky="nswe")

        checkframe = Frame(indicatorframe,bg = bgset)
        checkframe.grid(row=0,column=0,rowspan = 2,columnspan = 3)

        colsllabel = Label(checkframe,font = ('arial',14,'bold'),text = "เลือกแถบสี",bg = bgset)
        colsllabel.grid(row = 0,column = 0,columnspan = 3)
        
        gotplan = thebands()
        onetime = CheckVar2.get()

        self.C4 = Checkbutton(checkframe, text = "4",bg = bgset, variable = CheckVar1,onvalue = 0,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 0, sticky="nswe")

        self.C4 = Checkbutton(checkframe, text = "5",bg = bgset, variable = CheckVar1,onvalue = 1,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 1, sticky="nswe")

        self.C4 = Checkbutton(checkframe, text = "6",bg = bgset, variable = CheckVar1,onvalue = 2,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 2, sticky="nswe")

        CheckVar2.get()+1
        
        
        self.chekshow = Checkbutton(checkframe, text = "แสดงข้อความสี",bg = bgset, variable = CheckVar2,onvalue = 0,offvalue = 1,command = ban, height=1,width = 2)
        self.chekshow.grid(row = 2,column = 0,columnspan = 3, sticky="nswe")
        grid_hide(self.chekshow)
        
        self.labelask = Label(checkframe,font = ('arial',10,'bold'),text = "คำตอบ",bg = bgset)
        self.labelask.grid(row=3,column=0,sticky = W,pady = 10)
        self.txtask = Entry(checkframe,font = ('arial',10,'bold'),width = 10)
        self.txtask.grid(row=3,column=1,pady = 10)

        calculatebt = Button(checkframe,font = ('arial',12,'bold'),text = "ส่งคำตอบ",bg = "black",fg = "white")
        calculatebt.grid(row=4,column=0,pady = 25)

        rsbt = Button(checkframe,font = ('arial',12,'bold'),text = "สุ่มค่าใหม่",bg = "black",command = thebands,fg = "white")
        rsbt.grid(row=4,column=1,pady = 25)

        self.labeladj = Label(checkframe,font = ('arial',10,'bold'),text = "* สุ่มใหม่คะแนนจะรีเซ็ต",bg = bgset)
        self.labeladj.grid(row=5,column=1,sticky = W,pady = 10)


class Resistor:
    #===========GUI==============#
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap("icon.ico")
        self.root.title("saveffer resistor calculate")
        #self.root.geometry("1454x675+0+0")
        self.root.configure(background =bgset)
#==========================================#
        var1 = DoubleVar()
        var2 = DoubleVar()
        var3 = DoubleVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = StringVar()
        var7 = DoubleVar()
        var8 = StringVar()

        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        var6.set("")
        var7.set("")
        var8.set("")

        def Band1_Black():
            var1.set(0)
        def Band1_Brown():
            var1.set(1)
        def Band1_Red():
            var1.set(2)
        def Band1_Orange():
            var1.set(3)
        def Band1_Yellow():
            var1.set(4)
        def Band1_Green():
            var1.set(5)
        def Band1_Blue():
            var1.set(6)
        def Band1_Violet():
            var1.set(7)
        def Band1_Grey():
            var1.set(8)
        def Band1_White():
            var1.set(9)
#==========================#

        def Band2_Black():
            var2.set(0)
        def Band2_Brown():
            var2.set(1)
        def Band2_Red():
            var2.set(2)
        def Band2_Orange():
            var2.set(3)
        def Band2_Yellow():
            var2.set(4)
        def Band2_Green():
            var2.set(5)
        def Band2_Blue():
            var2.set(6)
        def Band2_Violet():
            var2.set(7)
        def Band2_Grey():
            var2.set(8)
        def Band2_White():
            var2.set(9)
#==================================#
        def Band3_Black():
            var7.set(0)
        def Band3_Brown():
            var7.set(1)
        def Band3_Red():
            var7.set(2)
        def Band3_Orange():
            var7.set(3)
        def Band3_Yellow():
            var7.set(4)
        def Band3_Green():
            var7.set(5)
        def Band3_Blue():
            var7.set(6)
        def Band3_Violet():
            var7.set(7)
        def Band3_Grey():
            var7.set(8)
        def Band3_White():
            var7.set(9)
#==================================#

        def multi_Black():
            var3.set(1)
        def multi_Brown():
            var3.set(10)
        def multi_Red():
            var3.set(100)
        def multi_Orange():
            var3.set(1000)
        def multi_Yellow():
            var3.set(10000)
        def multi_Green():
            var3.set(100000)
        def multi_Blue():
            var3.set(1000000)
        def multi_Violet():
            var3.set(10000000)
        def multi_Grey():
            var3.set(100000000)
        def multi_White():
            var3.set(1000000000)
        def multi_Gold():
            var3.set(0.1)
        def multi_Silver():
            var3.set(0.01)
#======================================#
        def torelance_Brown():
            var4.set(0.01)
            var6.set(u"\u00B1 1%")
        def torelance_Red():
            var4.set(0.02)
            var6.set(u"\u00B1 2%")
        def torelance_Green():
            var4.set(0.005)
            var6.set(u"\u00B1 0.5%")
        def torelance_Blue():
            var4.set(0.0025)
            var6.set(u"\u00B1 0.25%")
        def torelance_Violet():
            var4.set(0.001)
            var6.set(u"\u00B1 0.01%")
        def torelance_Grey():
            var4.set(0.0005)
            var6.set(u"\u00B1 0.05%")
        def torelance_Gold():
            var4.set(0.05)
            var6.set(u"\u00B1 5%")
        def torelance_Silver():
            var4.set(0.1)
            var6.set(u"\u00B1 10%")
        def torelance_None():
            var4.set(0.2)
            var6.set(u"\u00B1 20%")
#=================================================#

        def ppm1_Black():
            var8.set("250 ppm")
        def ppm1_Brown():
            var8.set("100 ppm")
        def ppm1_Red():
            var8.set("50 ppm")
        def ppm1_Orange():
            var8.set("15 ppm")
        def ppm1_Yellow():
            var8.set("25 ppm")
        def ppm1_Green():
            var8.set("20 ppm")
        def ppm1_Blue():
            var8.set("10 ppm")
        def ppm1_Violet():
            var8.set("5 ppm")
        def ppm1_Grey():
            var8.set("1 ppm")
        def ppm1_White():
            var8.set("N/A ppm")
        def ppm1_Gold():
            var8.set("N/A ppm")
        def ppm1_Silver():
            var8.set("N/A ppm")
#=================================================#
        def exit1():
            exit1 = tkinter.messagebox.askyesno("โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี","คุณต้องการออกหรือไม่?")
            if exit1 > 0:
                root.destroy()
                return
        def exit2():
            exit2 = tkinter.messagebox.askyesno("โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี","คุณต้องการออกหรือไม่?")
            if exit1 > 0:
                Practice.destroy()
                return
        def reset1():
            reset1 = tkinter.messagebox.askyesno("โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี","คุณต้องการรีเซ็ตหรือไม่?")
            if reset1 > 0:
                var1.set("")
                var2.set("")
                var3.set("")
                var4.set("")
                var5.set("")
                var6.set("")
                var7.set("")
                var8.set("")
                return

        def res1():
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            var6.set("")
            var7.set("")
            var8.set("")

        def calculate():
            rst = float("%d%d" %((var1.get(),var2.get())))
            rst *= var3.get()
            saveffer = sfformat(rst)
            #total = float(var5)
            tolance = str(var6.get())
            if rst >= 1000:
                var5.set(str(saveffer)+"\u03A9"+"("+str(rst)+"\u03A9"+")"+" "+str(tolance))
            else:
                var5.set(str(rst)+"\u03A9"+" "+str(tolance))
        def calculate2():
            rst = float("%d%d%d" %((var1.get(),var2.get(),var7.get())))
            rst *= var3.get()
            saveffer = sfformat(rst)
            #total = float(var5)
            tolance = str(var6.get())
            if rst >= 1000:
                var5.set(str(saveffer)+"\u03A9"+"("+str(rst)+"\u03A9"+")"+" "+str(tolance))
            else:
                var5.set(str(rst)+"\u03A9"+" "+str(tolance))

        def calculate3():
            ppg = var8.get()
            rst = float("%d%d%d" %((var1.get(),var2.get(),var7.get())))
            rst *= var3.get()
            saveffer = sfformat(rst)
            x = rst
            if x%10 == 0:
                rst = int(x)
                saveffer = sfformat(x)
            #total = float(var5)
            tolance = str(var6.get())
            if rst >= 1000:
                var5.set(str(saveffer)+"\u03A9"+"("+str(rst)+"\u03A9"+")"+" "+str(tolance)+" "+str(ppg))
            else:
                var5.set(str(rst)+"\u03A9"+" "+str(tolance)+" "+str(ppg))
            
        def train():
            app = Toplevel()
            dat = Training(app)
            app.attributes('-topmost', 'true')
            app.mainloop()

        """main bands"""
        def fourb():
            connn = sqlite3.connect('bgcolor.db')
            cursor = connn.execute("SELECT NAME from SAVEONE")
            rows = cursor.fetchone()[0]
            dos = rows

            bg(dos)
            conn.close()
            res1()
            self.labeltitle = Label(titleframe,font = ('arial',titlefsize,'bold'),text = "โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี",bg = rows,padx = 100)
            self.labeltitle.grid(row=0,rowspan = 2)
            indicateframe.grid(row=1,column=0, sticky="nse")
            """ forgot this!!! """

            self.blacktorelance.grid(row=1,column=3)
            self.browntorelance.grid(row=2,column=3)
            self.redtorelance.grid(row=3,column=3)
            self.orangetorelance.grid(row=4,column=3)
            self.yellowtorelance.grid(row=5,column=3)
            self.greentorelance.grid(row=6,column=3)
            self.bluetorelance.grid(row=7,column=3)
            self.purpletorelance.grid(row=8,column=3)
            self.greytorelance.grid(row=9,column=3)
            self.whitetorelance.grid(row=10,column=3)
            self.goldtorelance.grid(row=11,column=3)
            self.silvertorelance.grid(row=12,column=3)

            #self.ptb.grid(row=0,column=2)
            self.blackppm.grid(row=1,column=2)
            self.Brownppm.grid(row=2,column=2)
            self.Redppm.grid(row=3,column=2)
            self.Orangeppm.grid(row=4,column=2)
            self.Yellowppm.grid(row=5,column=2)
            self.Greenppm.grid(row=6,column=2)
            self.Blueppm.grid(row=7,column=2)
            self.Violetppm.grid(row=8,column=2)
            self.Greyppm.grid(row=9,column=2)
            self.Whiteppm.grid(row=10,column=2)
            self.Goldppm.grid(row=11,column=2)
            self.Silverppm.grid(row=12,column=2)

            self.xtb1 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
            self.xtb1.grid(row=0,column=4)

            self.xtb2 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
            self.xtb2.grid(row=0,column=5)

            self.xtb3 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
            self.xtb3.grid(row=0,column=6)

            self.blackppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="250",fg = "white",command = ppm1_Black,bg="black")
            self.blackppm.grid(row=1,column=0)
            self.Brownppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="100",fg = "white",command = ppm1_Brown,bg="brown")
            self.Brownppm.grid(row=2,column=0)
            self.Redppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="50",fg = "white",command = ppm1_Red,bg="red")
            self.Redppm.grid(row=3,column=0)
            self.Orangeppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="15",fg = "black",command =ppm1_Orange,bg="orange")
            self.Orangeppm.grid(row=4,column=0)
            self.Yellowppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="25",fg = "black",command = ppm1_Yellow,bg="yellow")
            self.Yellowppm.grid(row=5,column=0)
            self.Greenppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="20",fg = "white",command =ppm1_Green,bg="green")
            self.Greenppm.grid(row=6,column=0)
            self.Blueppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="10",fg = "white",command =ppm1_Blue,bg="blue")
            self.Blueppm.grid(row=7,column=0)
            self.Violetppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command =ppm1_Violet,bg="purple")
            self.Violetppm.grid(row=8,column=0)
            self.Greyppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "black",command =ppm1_Grey,bg="grey")
            self.Greyppm.grid(row=9,column=0)
            self.Whiteppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_White,bg="white")
            self.Whiteppm.grid(row=10,column=0)
            self.Goldppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_Gold,bg="gold")
            self.Goldppm.grid(row=11,column=0)
            self.Silverppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_Silver,bg="silver")
            self.Silverppm.grid(row=12,column=0)

            """resistans color"""
        
            self.blackcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ดำ",fg = "white",command = Band1_Black,bg="black")
            self.blackcolor.grid(row=1,column=0)

            self.browncolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="น้ำตาล",fg = "white",command = Band1_Brown,bg="brown")
            self.browncolor.grid(row=2,column=0)

            self.redcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แดง",fg = "white",command = Band1_Red,bg="red")
            self.redcolor.grid(row=3,column=0)

            self.orangecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ส้ม",fg = "black",command = Band1_Orange,bg="orange")
            self.orangecolor.grid(row=4,column=0)

            self.yellowcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เหลือง",fg = "black",command = Band1_Yellow,bg="yellow")
            self.yellowcolor.grid(row=5,column=0)

            self.greencolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เขียว",fg = "white",command = Band1_Green,bg="green")
            self.greencolor.grid(row=6,column=0)

            self.bluecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="น้ำเงิน",fg = "white",command = Band1_Blue,bg="blue")
            self.bluecolor.grid(row=7,column=0)

            #violet
            self.purplecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ม่วง",fg = "white",command = Band1_Violet,bg="purple")
            self.purplecolor.grid(row=8,column=0)
            
            self.greycolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เทา",fg = "black",command = Band1_Grey,bg="grey")
            self.greycolor.grid(row=9,column=0)

            self.whitecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ขาว",fg = "black",command = Band1_White,bg="white")
            self.whitecolor.grid(row=10,column=0)

            self.goldcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ทอง",fg = "black",bg="gold")
            self.goldcolor.grid(row=11,column=0)

            self.silvercolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เงิน",fg = "black",bg="silver")
            self.silvercolor.grid(row=12,column=0)

            """resistans value2"""
        
            self.blackval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="0",fg = "white",command = Band3_Black,bg="black")
            self.blackval2.grid(row=1,column=1)

            self.brownval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "white",command = Band3_Brown,bg="brown")
            self.brownval2.grid(row=2,column=1)

            self.redval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="2",fg = "white",command = Band3_Red,bg="red")
            self.redval2.grid(row=3,column=1)

            self.orangeval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="3",fg = "black",command = Band3_Orange,bg="orange")
            self.orangeval2.grid(row=4,column=1)

            self.yellowval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="4",fg = "black",command = Band3_Yellow,bg="yellow")
            self.yellowval2.grid(row=5,column=1)

            self.greenval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command = Band3_Green,bg="green")
            self.greenval2.grid(row=6,column=1)

            self.blueval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="6",fg = "white",command = Band3_Blue,bg="blue")
            self.blueval2.grid(row=7,column=1)

            #violet
            self.purpleval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="7",fg = "white",command = Band3_Violet,bg="purple")
            self.purpleval2.grid(row=8,column=1)
            
            self.greyval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="8",fg = "black",command = Band3_Grey,bg="grey")
            self.greyval2.grid(row=9,column=1)

            self.whiteval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="9",fg = "black",command = Band3_White,bg="white")
            self.whiteval2.grid(row=10,column=1)

            self.goldval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="gold")
            self.goldval2.grid(row=11,column=1)

            self.silverval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="silver")
            self.silverval2.grid(row=12,column=1)

            """resistans value"""
        
            self.blackval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="0",fg = "white",command = Band2_Black,bg="black")
            self.blackval.grid(row=1,column=1)

            self.brownval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "white",command = Band2_Brown,bg="brown")
            self.brownval.grid(row=2,column=1)

            self.redval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="2",fg = "white",command = Band2_Red,bg="red")
            self.redval.grid(row=3,column=1)

            self.orangeval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="3",fg = "black",command = Band2_Orange,bg="orange")
            self.orangeval.grid(row=4,column=1)

            self.yellowval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="4",fg = "black",command = Band2_Yellow,bg="yellow")
            self.yellowval.grid(row=5,column=1)

            self.greenval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command = Band2_Green,bg="green")
            self.greenval.grid(row=6,column=1)

            self.blueval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="6",fg = "white",command = Band2_Blue,bg="blue")
            self.blueval.grid(row=7,column=1)

            #violet
            self.purpleval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="7",fg = "white",command = Band2_Violet,bg="purple")
            self.purpleval.grid(row=8,column=1)
            
            self.greyval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="8",fg = "black",command = Band2_Grey,bg="grey")
            self.greyval.grid(row=9,column=1)

            self.whiteval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="9",fg = "black",command = Band2_White,bg="white")
            self.whiteval.grid(row=10,column=1)

            self.goldval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="gold")
            self.goldval.grid(row=11,column=1)

            self.silverval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="silver")
            self.silverval.grid(row=12,column=1)


            """resistans multiply"""
            self.multip = [10**0,10**1,10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**(-1),10**(-2)]

            self.blackmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^0",fg = "white",command = multi_Black,bg="black")
            self.blackmult.grid(row=1,column=2)

            self.brownmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^1",fg = "white",command = multi_Brown,bg="brown")
            self.brownmult.grid(row=2,column=2)

            self.redmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^2",fg = "white",command = multi_Red,bg="red")
            self.redmult.grid(row=3,column=2)

            self.orangemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^3",fg = "black",command = multi_Orange,bg="orange")
            self.orangemult.grid(row=4,column=2)

            self.yellowmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^4",fg = "black",command = multi_Yellow,bg="yellow")
            self.yellowmult.grid(row=5,column=2)

            self.greenmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^5",fg = "white",command = multi_Green,bg="green")
            self.greenmult.grid(row=6,column=2)

            self.bluemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^6",fg = "white",command = multi_Blue,bg="blue")
            self.bluemult.grid(row=7,column=2)

            #violet
            self.purplemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^7",fg = "white",command = multi_Violet,bg="purple")
            self.purplemult.grid(row=8,column=2)
            
            self.greymult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^8",fg = "black",command = multi_Grey,bg="grey")
            self.greymult.grid(row=9,column=2)

            self.whitemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^9",fg = "black",command = multi_White,bg="white")
            self.whitemult.grid(row=10,column=2)

            self.goldmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^-1",fg = "black",command = multi_Gold,bg="gold")
            self.goldmult.grid(row=11,column=2)

            self.silvermult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "x10^-2",fg = "black",command = multi_Silver,bg="silver")
            self.silvermult.grid(row=12,column=2)
            
            """resistans torelance"""
            self.blacktorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "white",command = torelance_None,bg="black")
            self.blacktorelance.grid(row=1,column=3)

            self.browntorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 1%",fg = "white",command = torelance_Brown,bg="brown")
            self.browntorelance.grid(row=2,column=3)

            self.redtorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 2%",fg = "white",command = torelance_Red,bg="red")
            self.redtorelance.grid(row=3,column=3)

            self.orangetorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "black",command = torelance_None,bg="orange")
            self.orangetorelance.grid(row=4,column=3)

            self.yellowtorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "black",command = torelance_None,bg="yellow")
            self.yellowtorelance.grid(row=5,column=3)

            self.greentorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.5%",fg = "white",command = torelance_Green,bg="green")
            self.greentorelance.grid(row=6,column=3)

            self.bluetorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.25%",fg = "white",command = torelance_Blue,bg="blue")
            self.bluetorelance.grid(row=7,column=3)

            #violet
            self.purpletorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.1%",fg = "white",command = torelance_Violet,bg="purple")
            self.purpletorelance.grid(row=8,column=3)
            
            self.greytorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.05%",fg = "black",command = torelance_Grey,bg="grey")
            self.greytorelance.grid(row=9,column=3)

            self.whitetorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "black",command = torelance_None,bg="white")
            self.whitetorelance.grid(row=10,column=3)

            self.goldtorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 5%",fg = "black",command = torelance_Gold,bg="gold")
            self.goldtorelance.grid(row=11,column=3)

            self.silvertorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 10%",fg = "black",command = torelance_Silver,bg="silver")
            self.silvertorelance.grid(row=12,column=3)

            """base"""
            self.onetb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่า 1",fg = "black",bg = rows)
            self.onetb.grid(row=0,column=0)

            self.thrtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่า 3",fg = "black",bg = rows)
            self.thrtb.grid(row=0,column=1)

            self.twotb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่า 2",fg = "black",bg = rows)
            self.twotb.grid(row=0,column=1)

            self.mtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ตัวคูณ",fg = "black",bg = rows)
            self.mtb.grid(row=0,column=2)

            self.stb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่าผิดพลาด",fg = "black",bg = rows)
            self.stb.grid(row=0,column=3)
            
            

            "indicate"
            self.labelone = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 1",bg = rows)
            self.labelone.grid(row=0,column=0,sticky = W,pady = 10)
            self.txtone = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var1)
            self.txtone.grid(row=0,column=1,pady = 10)

            self.labelthree = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 3",bg = rows)
            self.labelthree.grid(row=2,column=0,sticky = W,pady = 10)
            self.txtthree = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var7)
            self.txtthree.grid(row=2,column=1,pady = 10)

            self.labeltwo = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 2",bg = rows)
            self.labeltwo.grid(row=1,column=0,sticky = W,pady = 10)
            self.txttwo = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var2)
            self.txttwo.grid(row=1,column=1,pady = 10)

            self.labelmult = Label(intframe,font = ('arial',12,'bold'),text = "ตัวคูณ",bg = rows)
            self.labelmult.grid(row=3,column=0,sticky = W,pady = 10)
            self.txtmult = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var3)
            self.txtmult.grid(row=3,column=1,pady = 10)

            self.labeltol = Label(intframe,font = ('arial',12,'bold'),text = "ค่าผิดพลาด",bg = rows)
            self.labeltol.grid(row=4,column=0,sticky = W,pady = 10)
            self.txttol = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var4)
            self.txttol.grid(row=4,column=1,pady = 10)

            self.labelppm = Label(intframe,font = ('arial',12,'bold'),text = "สัมประสิทธิ์อุณหภูมิ",bg = rows)
            self.labelppm.grid(row=5,column=0,sticky = W,pady = 10)
            self.txtppm = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var8)
            self.txtppm.grid(row=5,column=1,pady = 10)

            self.labelres = Label(intframe,font = ('arial',12,'bold'),text = "ค่าต้านทาน",bg = rows)
            self.labelres.grid(row=6,column=0,sticky = W,pady = 10)
            self.txtres = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var5)
            self.txtres.grid(row=6,column=1,pady = 10)

            calculatebt = Button(callingframe,font = ('arial',12,'bold'),text = "คำนวณ",bg = "black",command = calculate,fg = "white")
            calculatebt.grid(row=7,column=0,pady = 25)

        def fiveb():     
            connn = sqlite3.connect('bgcolor.db')
            cursor = connn.execute("SELECT NAME from SAVEONE")
            rows = cursor.fetchone()[0]
            dos = rows
            bg(dos)
            conn.close()
            res1()
            self.labeltitle = Label(titleframe,font = ('arial',titlefsize,'bold'),text = "โปรแกรมคำนวณรหัสสี Resistor 5 แถบสี",bg = rows,padx = 100)
            self.labeltitle.grid(row=0,rowspan = 2)
            indicateframe.grid(row=1,column=0, sticky="nse") 

            self.xtb1 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
            self.xtb1.grid(row=0,column=5)

            self.blackppm.grid(row=1,column=3)
            self.Brownppm.grid(row=2,column=3)
            self.Redppm.grid(row=3,column=2)
            self.Orangeppm.grid(row=4,column=3)
            self.Yellowppm.grid(row=5,column=3)
            self.Greenppm.grid(row=6,column=3)
            self.Blueppm.grid(row=7,column=3)
            self.Violetppm.grid(row=8,column=3)
            self.Greyppm.grid(row=9,column=3)
            self.Whiteppm.grid(row=10,column=3)
            self.Goldppm.grid(row=11,column=3)
            self.Silverppm.grid(row=12,column=3)

            self.blackval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="0",fg = "white",command = Band3_Black,bg="black")
            self.blackval2.grid(row=1,column=2)

            self.brownval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "white",command = Band3_Brown,bg="brown")
            self.brownval2.grid(row=2,column=2)

            self.redval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="2",fg = "white",command = Band3_Red,bg="red")
            self.redval2.grid(row=3,column=2)

            self.orangeval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="3",fg = "black",command = Band3_Orange,bg="orange")
            self.orangeval2.grid(row=4,column=2)

            self.yellowval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="4",fg = "black",command = Band3_Yellow,bg="yellow")
            self.yellowval2.grid(row=5,column=2)

            self.greenval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command = Band3_Green,bg="green")
            self.greenval2.grid(row=6,column=2)

            self.blueval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="6",fg = "white",command = Band3_Blue,bg="blue")
            self.blueval2.grid(row=7,column=2)

            #violet
            self.purpleval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="7",fg = "white",command = Band3_Violet,bg="purple")
            self.purpleval2.grid(row=8,column=2)
            
            self.greyval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="8",fg = "black",command = Band3_Grey,bg="grey")
            self.greyval2.grid(row=9,column=2)

            self.whiteval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="9",fg = "black",command = Band3_White,bg="white")
            self.whiteval2.grid(row=10,column=2)

            self.goldval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="gold")
            self.goldval2.grid(row=11,column=2)

            self.silverval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="silver")
            self.silverval2.grid(row=12,column=2)


            self.blackmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^0",fg = "white",command = multi_Black,bg="black")
            self.blackmult.grid(row=1,column=3)

            self.brownmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^1",fg = "white",command = multi_Brown,bg="brown")
            self.brownmult.grid(row=2,column=3)

            self.redmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^2",fg = "white",command = multi_Red,bg="red")
            self.redmult.grid(row=3,column=3)

            self.orangemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^3",fg = "black",command = multi_Orange,bg="orange")
            self.orangemult.grid(row=4,column=3)

            self.yellowmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^4",fg = "black",command = multi_Yellow,bg="yellow")
            self.yellowmult.grid(row=5,column=3)

            self.greenmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^5",fg = "white",command = multi_Green,bg="green")
            self.greenmult.grid(row=6,column=3)

            self.bluemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^6",fg = "white",command = multi_Blue,bg="blue")
            self.bluemult.grid(row=7,column=3)

            #violet
            self.purplemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^7",fg = "white",command = multi_Violet,bg="purple")
            self.purplemult.grid(row=8,column=3)
            
            self.greymult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^8",fg = "black",command = multi_Grey,bg="grey")
            self.greymult.grid(row=9,column=3)

            self.whitemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^9",fg = "black",command = multi_White,bg="white")
            self.whitemult.grid(row=10,column=3)

            self.goldmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^-1",fg = "black",command = multi_Gold,bg="gold")
            self.goldmult.grid(row=11,column=3)

            self.silvermult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "x10^-2",fg = "black",command = multi_Silver,bg="silver")
            self.silvermult.grid(row=12,column=3)

            self.blacktorelance.grid(row=1,column=4)
            self.browntorelance.grid(row=2,column=4)
            self.redtorelance.grid(row=3,column=4)
            self.orangetorelance.grid(row=4,column=4)
            self.yellowtorelance.grid(row=5,column=4)
            self.greentorelance.grid(row=6,column=4)
            self.bluetorelance.grid(row=7,column=4)
            self.purpletorelance.grid(row=8,column=4)
            self.greytorelance.grid(row=9,column=4)
            self.whitetorelance.grid(row=10,column=4)
            self.goldtorelance.grid(row=11,column=4)
            self.silvertorelance.grid(row=12,column=4)

            calculatebt2 = Button(callingframe,font = ('arial',12,'bold'),text = "คำนวณ",bg = "black",command = calculate2,fg = "white")
            calculatebt2.grid(row=7,column=0,pady = 25)

            self.thrtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 3",fg = "black",bg = rows)
            self.thrtb.grid(row=0,column=2)

            self.mtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ตัวคูณ",fg = "black",bg = rows)
            self.mtb.grid(row=0,column=3)

            self.stb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่าผิดพลาด",fg = "black",bg = rows)
            self.stb.grid(row=0,column=4)

            self.labelone = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 1",bg = rows)
            self.labelone.grid(row=0,column=0,sticky = W,pady = 10)
            self.txtone = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var1)
            self.txtone.grid(row=0,column=1,pady = 10)

            self.labeltwo = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 2",bg = rows)
            self.labeltwo.grid(row=1,column=0,sticky = W,pady = 10)
            self.txttwo = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var2)
            self.txttwo.grid(row=1,column=1,pady = 10)

            self.labelthree = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 3",bg = rows)
            self.labelthree.grid(row=2,column=0,sticky = W,pady = 10)
            self.txtthree = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var7)
            self.txtthree.grid(row=2,column=1,pady = 10)

            self.labelmult = Label(intframe,font = ('arial',12,'bold'),text = "ตัวคูณ",bg = rows)
            self.labelmult.grid(row=3,column=0,sticky = W,pady = 10)
            self.txtmult = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var3)
            self.txtmult.grid(row=3,column=1,pady = 10)

            self.labeltol = Label(intframe,font = ('arial',12,'bold'),text = "ค่าผิดพลาด",bg = rows)
            self.labeltol.grid(row=4,column=0,sticky = W,pady = 10)
            self.txttol = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var4)
            self.txttol.grid(row=4,column=1,pady = 10)

            self.labelres = Label(intframe,font = ('arial',12,'bold'),text = "ค่าต้านทาน",bg = rows)
            self.labelres.grid(row=6,column=0,sticky = W,pady = 10)
            self.txtres = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var5)
            self.txtres.grid(row=6,column=1,pady = 10)

        def sixb():
            connn = sqlite3.connect('bgcolor.db')
            cursor = connn.execute("SELECT NAME from SAVEONE")
            rows = cursor.fetchone()[0]
            dos = rows
            bg(dos)
            conn.close()
            res1()

            self.labeltitle = Label(titleframe,font = ('arial',titlefsize,'bold'),text = "โปรแกรมคำนวณรหัสสี Resistor 6 แถบสี",bg = rows,padx = 100)
            self.labeltitle.grid(row=0,rowspan = 2)
            indicateframe.grid(row=1,column=0, sticky="nse")

            self.blackval2.grid(row=1,column=2)
            self.brownval2.grid(row=2,column=2)
            self.redval2.grid(row=3,column=2)
            self.orangeval2.grid(row=4,column=2)
            self.yellowval2.grid(row=5,column=2)
            self.greenval2.grid(row=6,column=2)
            self.blueval2.grid(row=7,column=2)
            self.purpleval2.grid(row=8,column=2)
            self.greyval2.grid(row=9,column=2)
            self.whiteval2.grid(row=10,column=2)
            self.goldval2.grid(row=11,column=2)
            self.silverval2.grid(row=12,column=2)

            self.blackmult.grid(row=1,column=3)
            self.brownmult.grid(row=2,column=3)
            self.redmult.grid(row=3,column=3)
            self.orangemult.grid(row=4,column=3)
            self.yellowmult.grid(row=5,column=3)
            self.greenmult.grid(row=6,column=3)
            self.bluemult.grid(row=7,column=3)
            self.purplemult.grid(row=8,column=3)
            self.greymult.grid(row=9,column=3)
            self.whitemult.grid(row=10,column=3)
            self.goldmult.grid(row=11,column=3)
            self.silvermult.grid(row=12,column=3)

            self.blacktorelance.grid(row=1,column=4)
            self.browntorelance.grid(row=2,column=4)
            self.redtorelance.grid(row=3,column=4)
            self.orangetorelance.grid(row=4,column=4)
            self.yellowtorelance.grid(row=5,column=4)
            self.greentorelance.grid(row=6,column=4)
            self.bluetorelance.grid(row=7,column=4)
            self.purpletorelance.grid(row=8,column=4)
            self.greytorelance.grid(row=9,column=4)
            self.whitetorelance.grid(row=10,column=4)
            self.goldtorelance.grid(row=11,column=4)
            self.silvertorelance.grid(row=12,column=4)

            self.blackppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="250",fg = "white",command = ppm1_Black,bg="black")
            self.blackppm.grid(row=1,column=5)
            self.Brownppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="100",fg = "white",command = ppm1_Brown,bg="brown")
            self.Brownppm.grid(row=2,column=5)
            self.Redppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="50",fg = "white",command = ppm1_Red,bg="red")
            self.Redppm.grid(row=3,column=5)
            self.Orangeppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="15",fg = "black",command =ppm1_Orange,bg="orange")
            self.Orangeppm.grid(row=4,column=5)
            self.Yellowppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="25",fg = "black",command = ppm1_Yellow,bg="yellow")
            self.Yellowppm.grid(row=5,column=5)
            self.Greenppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="20",fg = "white",command =ppm1_Green,bg="green")
            self.Greenppm.grid(row=6,column=5)
            self.Blueppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="10",fg = "white",command =ppm1_Blue,bg="blue")
            self.Blueppm.grid(row=7,column=5)
            self.Violetppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command =ppm1_Violet,bg="purple")
            self.Violetppm.grid(row=8,column=5)
            self.Greyppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "black",command =ppm1_Grey,bg="grey")
            self.Greyppm.grid(row=9,column=5)
            self.Whiteppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_White,bg="white")
            self.Whiteppm.grid(row=10,column=5)
            self.Goldppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_Gold,bg="gold")
            self.Goldppm.grid(row=11,column=5)
            self.Silverppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_Silver,bg="silver")
            self.Silverppm.grid(row=12,column=5)
           
            self.onetb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 1",fg = "black",bg = rows)
            self.onetb.grid(row=0,column=0)

            self.twotb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 2",fg = "black",bg = rows)
            self.twotb.grid(row=0,column=1)

            self.thrtb= Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 3",fg = "black",bg = rows)
            self.thrtb.grid(row=0,column=2)

            self.mtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ตัวคูณ",fg = "black",bg = rows)
            self.mtb.grid(row=0,column=3)

            self.stb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่าผิดพลาด",fg = "black",bg = rows)
            self.stb.grid(row=0,column=4)

            self.xtb2 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ทนอุณหภูมิ",fg = "black",bg = rows)
            self.xtb2.grid(row=0,column=5)


            self.labelone = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 1",bg = rows)
            self.labelone.grid(row=0,column=0,sticky = W,pady = 10)
            self.txtone = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var1)
            self.txtone.grid(row=0,column=1,pady = 10)

            self.labeltwo = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 2",bg = rows)
            self.labeltwo.grid(row=1,column=0,sticky = W,pady = 10)
            self.txttwo = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var2)
            self.txttwo.grid(row=1,column=1,pady = 10)

            self.labelthree = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 3",bg = rows)
            self.labelthree.grid(row=2,column=0,sticky = W,pady = 10)
            self.txtthree = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var7)
            self.txtthree.grid(row=2,column=1,pady = 10)

            self.labelmult = Label(intframe,font = ('arial',12,'bold'),text = "ตัวคูณ",bg = rows)
            self.labelmult.grid(row=3,column=0,sticky = W,pady = 10)
            self.txtmult = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var3)
            self.txtmult.grid(row=3,column=1,pady = 10)

            self.labeltol = Label(intframe,font = ('arial',12,'bold'),text = "ค่าผิดพลาด",bg = rows)
            self.labeltol.grid(row=4,column=0,sticky = W,pady = 10)
            self.txttol = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var4)
            self.txttol.grid(row=4,column=1,pady = 10)

            self.labelres = Label(intframe,font = ('arial',12,'bold'),text = "ค่าต้านทาน",bg = rows)
            self.labelres.grid(row=6,column=0,sticky = W,pady = 10)
            self.txtres = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var5)
            self.txtres.grid(row=6,column=1,pady = 10)

            calculatebt3 = Button(callingframe,font = ('arial',12,'bold'),text = "คำนวณ",bg = "black",command = calculate3,fg = "white")
            calculatebt3.grid(row=7,column=0,pady = 25)
        
        def bg(color):
            conn = sqlite3.connect('bgcolor.db')
            cursor = conn.execute("SELECT NAME from SAVEONE")
            rowling = cursor.fetchone()[0]
            print(rowling)
            print(bgset)
            conn.execute("UPDATE SAVEONE set NAME = ? where NAME = ?",(color,rowling))
            print(rowling)
            conn.commit()
            conn.close()
            self.root.config(bg=color)
            frame1.config(bg=color)
            self.labeltitle.config(bg=color)
            indicateframe.config(bg=color)
            rsframe.config(bg=color)
            callingframe.config(bg=color)
            titleframe.config(bg=color)
            self.labelmult.config(bg=color)
            self.labelres.config(bg=color)
            self.labelppm.config(bg=color)
            self.labeltol.config(bg=color)
            self.labelthree.config(bg=color)
            self.labeltwo.config(bg=color)
            self.labelone.config(bg=color)
            intframe.config(bg=color)
            self.onetb.config(bg=color)
            self.thrtb.config(bg=color)
            self.twotb.config(bg=color)
            self.twotb.config(bg=color)
            self.mtb.config(bg=color)
            self.stb.config(bg=color)
            self.xtb1.config(bg=color)
            self.xtb2.config(bg=color)
            self.xtb3.config(bg=color)
            background(color)

            return color

        def restart_program():
            exit1 = tkinter.messagebox.askyesno("โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี","คุณต้องการออกหรือไม่?")
            if exit1 > 0:
                python = sys.executable
                os.execl(python, python, * sys.argv)
#========================================ready================================================================================================================#            
        frame1 = Frame(self.root,bg = bgset)
        frame1.grid()

        titleframe = Frame(frame1,width = 1550,bd = 10,bg = bgset,padx = 20,pady = 8,relief = RIDGE)
        titleframe.grid(row=0,column=0)
        self.labeltitle = Label(titleframe,font = ('arial',titlefsize,'bold'),text = "โปรแกรมคำนวณรหัสสี Resistor 4 แถบสี",bg = bgset,padx = 100)
        self.labeltitle.grid(row=0,rowspan = 2)

        menubar=Menu(root)
        fileMenu=Menu(menubar,tearoff=0)
        fileMenu.add_command(label="4 แถบสี",command = fourb)
        fileMenu.add_command(label="5 แถบสี",command = fiveb)
        fileMenu.add_command(label="6 แถบสี",command = sixb)

        menubar.add_cascade(label="เลือกแถบสี",menu=fileMenu)
        mmnnuu=Menu(menubar,tearoff=0)
        mmnnuu.add_command(label="ฝึก",command = train)
        mmnnuu.add_command(label="รีเซ็ต",command = reset1)
        mmnnuu.add_command(label="ออก",command = exit1)
        menubar.add_cascade(label="เมนู",menu=mmnnuu)
        bgmenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="สีพื้นหลัง",menu=bgmenu)
        bgmenu.add_command(label="Tomato",command = lambda: bg('tomato4'))
        bgmenu.add_command(label="Medium Purple",command = lambda: bg('mediumpurple1'))
        bgmenu.add_command(label="Salmon",command = lambda: bg('salmon'))
        bgmenu.add_command(label="Indian red",command = lambda: bg('indianred'))
        bgmenu.add_command(label="Powder blue",command = lambda: bg('powderblue'))
        bgmenu.add_command(label="Grey",command = lambda: bg('grey'))
        bgmenu.add_command(label="wheat",command = lambda: bg('wheat4'))
        root.config(menu=menubar)

        rsframe = Frame(frame1,width = 1550,bd = 10,bg = bgset,padx = 15,pady = 8,relief = RIDGE)
        rsframe.grid(row=1,column=0, sticky="nsw")

        indicateframe = Frame(frame1,width = 1550,bd = 10,bg = bgset,padx = 15,pady = 8,relief = RIDGE)
        indicateframe.grid(row=1,column=0, sticky="nse")
        intframe = Frame(indicateframe,bg = bgset,pady = 6)
        intframe.grid(row=1,column=0, sticky="n")
        callingframe = Frame(indicateframe,bg = bgset,pady = 6)
        callingframe.grid(row=2,column=0, sticky="s")
        """PPM Value"""

        self.blackppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="250",fg = "white",command = ppm1_Black,bg="black")
        self.blackppm.grid(row=1,column=0)
        self.Brownppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="100",fg = "white",command = ppm1_Brown,bg="brown")
        self.Brownppm.grid(row=2,column=0)
        self.Redppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="50",fg = "white",command = ppm1_Red,bg="red")
        self.Redppm.grid(row=3,column=0)
        self.Orangeppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="15",fg = "black",command =ppm1_Orange,bg="orange")
        self.Orangeppm.grid(row=4,column=0)
        self.Yellowppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="25",fg = "black",command = ppm1_Yellow,bg="yellow")
        self.Yellowppm.grid(row=5,column=0)
        self.Greenppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="20",fg = "white",command =ppm1_Green,bg="green")
        self.Greenppm.grid(row=6,column=0)
        self.Blueppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="10",fg = "white",command =ppm1_Blue,bg="blue")
        self.Blueppm.grid(row=7,column=0)
        self.Violetppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command =ppm1_Violet,bg="purple")
        self.Violetppm.grid(row=8,column=0)
        self.Greyppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "black",command =ppm1_Grey,bg="grey")
        self.Greyppm.grid(row=9,column=0)
        self.Whiteppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_White,bg="white")
        self.Whiteppm.grid(row=10,column=0)
        self.Goldppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_Gold,bg="gold")
        self.Goldppm.grid(row=11,column=0)
        self.Silverppm = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",command =ppm1_Silver,bg="silver")
        self.Silverppm.grid(row=12,column=0)

        """resistans color"""
    
        self.blackcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ดำ",fg = "white",command = Band1_Black,bg="black")
        self.blackcolor.grid(row=1,column=0)

        self.browncolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="น้ำตาล",fg = "white",command = Band1_Brown,bg="brown")
        self.browncolor.grid(row=2,column=0)

        self.redcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แดง",fg = "white",command = Band1_Red,bg="red")
        self.redcolor.grid(row=3,column=0)

        self.orangecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ส้ม",fg = "black",command = Band1_Orange,bg="orange")
        self.orangecolor.grid(row=4,column=0)

        self.yellowcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เหลือง",fg = "black",command = Band1_Yellow,bg="yellow")
        self.yellowcolor.grid(row=5,column=0)

        self.greencolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เขียว",fg = "white",command = Band1_Green,bg="green")
        self.greencolor.grid(row=6,column=0)

        self.bluecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="น้ำเงิน",fg = "white",command = Band1_Blue,bg="blue")
        self.bluecolor.grid(row=7,column=0)

        #violet
        self.purplecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ม่วง",fg = "white",command = Band1_Violet,bg="purple")
        self.purplecolor.grid(row=8,column=0)
        
        self.greycolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เทา",fg = "black",command = Band1_Grey,bg="grey")
        self.greycolor.grid(row=9,column=0)

        self.whitecolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ขาว",fg = "black",command = Band1_White,bg="white")
        self.whitecolor.grid(row=10,column=0)

        self.goldcolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ทอง",fg = "black",bg="gold")
        self.goldcolor.grid(row=11,column=0)

        self.silvercolor = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="เงิน",fg = "black",bg="silver")
        self.silvercolor.grid(row=12,column=0)

        """resistans value2"""
    
        self.blackval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="0",fg = "white",command = Band3_Black,bg="black")
        self.blackval2.grid(row=1,column=1)

        self.brownval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "white",command = Band3_Brown,bg="brown")
        self.brownval2.grid(row=2,column=1)

        self.redval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="2",fg = "white",command = Band3_Red,bg="red")
        self.redval2.grid(row=3,column=1)

        self.orangeval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="3",fg = "black",command = Band3_Orange,bg="orange")
        self.orangeval2.grid(row=4,column=1)

        self.yellowval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="4",fg = "black",command = Band3_Yellow,bg="yellow")
        self.yellowval2.grid(row=5,column=1)

        self.greenval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command = Band3_Green,bg="green")
        self.greenval2.grid(row=6,column=1)

        self.blueval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="6",fg = "white",command = Band3_Blue,bg="blue")
        self.blueval2.grid(row=7,column=1)

        #violet
        self.purpleval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="7",fg = "white",command = Band3_Violet,bg="purple")
        self.purpleval2.grid(row=8,column=1)
        
        self.greyval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="8",fg = "black",command = Band3_Grey,bg="grey")
        self.greyval2.grid(row=9,column=1)

        self.whiteval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="9",fg = "black",command = Band3_White,bg="white")
        self.whiteval2.grid(row=10,column=1)

        self.goldval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="gold")
        self.goldval2.grid(row=11,column=1)

        self.silverval2 = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="silver")
        self.silverval2.grid(row=12,column=1)

        """resistans value"""
    
        self.blackval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="0",fg = "white",command = Band2_Black,bg="black")
        self.blackval.grid(row=1,column=1)

        self.brownval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="1",fg = "white",command = Band2_Brown,bg="brown")
        self.brownval.grid(row=2,column=1)

        self.redval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="2",fg = "white",command = Band2_Red,bg="red")
        self.redval.grid(row=3,column=1)

        self.orangeval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="3",fg = "black",command = Band2_Orange,bg="orange")
        self.orangeval.grid(row=4,column=1)

        self.yellowval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="4",fg = "black",command = Band2_Yellow,bg="yellow")
        self.yellowval.grid(row=5,column=1)

        self.greenval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="5",fg = "white",command = Band2_Green,bg="green")
        self.greenval.grid(row=6,column=1)

        self.blueval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="6",fg = "white",command = Band2_Blue,bg="blue")
        self.blueval.grid(row=7,column=1)

        #violet
        self.purpleval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="7",fg = "white",command = Band2_Violet,bg="purple")
        self.purpleval.grid(row=8,column=1)
        
        self.greyval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="8",fg = "black",command = Band2_Grey,bg="grey")
        self.greyval.grid(row=9,column=1)

        self.whiteval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="9",fg = "black",command = Band2_White,bg="white")
        self.whiteval.grid(row=10,column=1)

        self.goldval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="gold")
        self.goldval.grid(row=11,column=1)

        self.silverval = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="N/A",fg = "black",bg="silver")
        self.silverval.grid(row=12,column=1)


        """resistans multiply"""
        self.multip = [10**0,10**1,10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**(-1),10**(-2)]

        self.blackmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^0",fg = "white",command = multi_Black,bg="black")
        self.blackmult.grid(row=1,column=2)

        self.brownmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^1",fg = "white",command = multi_Brown,bg="brown")
        self.brownmult.grid(row=2,column=2)

        self.redmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^2",fg = "white",command = multi_Red,bg="red")
        self.redmult.grid(row=3,column=2)

        self.orangemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^3",fg = "black",command = multi_Orange,bg="orange")
        self.orangemult.grid(row=4,column=2)

        self.yellowmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^4",fg = "black",command = multi_Yellow,bg="yellow")
        self.yellowmult.grid(row=5,column=2)

        self.greenmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^5",fg = "white",command = multi_Green,bg="green")
        self.greenmult.grid(row=6,column=2)

        self.bluemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^6",fg = "white",command = multi_Blue,bg="blue")
        self.bluemult.grid(row=7,column=2)

        #violet
        self.purplemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^7",fg = "white",command = multi_Violet,bg="purple")
        self.purplemult.grid(row=8,column=2)
        
        self.greymult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^8",fg = "black",command = multi_Grey,bg="grey")
        self.greymult.grid(row=9,column=2)

        self.whitemult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^9",fg = "black",command = multi_White,bg="white")
        self.whitemult.grid(row=10,column=2)

        self.goldmult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text="x10^-1",fg = "black",command = multi_Gold,bg="gold")
        self.goldmult.grid(row=11,column=2)

        self.silvermult = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "x10^-2",fg = "black",command = multi_Silver,bg="silver")
        self.silvermult.grid(row=12,column=2)
        
        """resistans torelance"""
        self.blacktorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "white",command = torelance_None,bg="black")
        self.blacktorelance.grid(row=1,column=3)

        self.browntorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 1%",fg = "white",command = torelance_Brown,bg="brown")
        self.browntorelance.grid(row=2,column=3)

        self.redtorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 2%",fg = "white",command = torelance_Red,bg="red")
        self.redtorelance.grid(row=3,column=3)

        self.orangetorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "black",command = torelance_None,bg="orange")
        self.orangetorelance.grid(row=4,column=3)

        self.yellowtorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "black",command = torelance_None,bg="yellow")
        self.yellowtorelance.grid(row=5,column=3)

        self.greentorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.5%",fg = "white",command = torelance_Green,bg="green")
        self.greentorelance.grid(row=6,column=3)

        self.bluetorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.25%",fg = "white",command = torelance_Blue,bg="blue")
        self.bluetorelance.grid(row=7,column=3)

        #violet
        self.purpletorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.1%",fg = "white",command = torelance_Violet,bg="purple")
        self.purpletorelance.grid(row=8,column=3)
        
        self.greytorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 0.05%",fg = "black",command = torelance_Grey,bg="grey")
        self.greytorelance.grid(row=9,column=3)

        self.whitetorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= "N/A",fg = "black",command = torelance_None,bg="white")
        self.whitetorelance.grid(row=10,column=3)

        self.goldtorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 5%",fg = "black",command = torelance_Gold,bg="gold")
        self.goldtorelance.grid(row=11,column=3)

        self.silvertorelance = Button(rsframe,width = widthsize,font = ('arial',14,'bold'),text= u"\u00B1 10%",fg = "black",command = torelance_Silver,bg="silver")
        self.silvertorelance.grid(row=12,column=3)

        """base"""
        self.onetb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 1",fg = "black",bg = bgset)
        self.onetb.grid(row=0,column=0)

        self.thrtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 3",fg = "black",bg = bgset)
        self.thrtb.grid(row=0,column=1)

        self.twotb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="แถบสี 2",fg = "black",bg = bgset)
        self.twotb.grid(row=0,column=1)

        self.mtb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ตัวคูณ",fg = "black",bg = bgset)
        self.mtb.grid(row=0,column=2)

        self.ptb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ทนอุณหภูมิ",fg = "black",bg = bgset)
        self.ptb.grid(row=0,column=3)

        self.stb = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="ค่าผิดพลาด",fg = "black",bg = bgset)
        self.stb.grid(row=0,column=3)
        
        self.xtb1 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
        self.xtb1.grid(row=0,column=4)

        self.xtb2 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
        self.xtb2.grid(row=0,column=5)

        self.xtb3 = Label(rsframe,width = widthsize,font = ('arial',14,'bold'),text="                 ",fg = "black",bg = rows)
        self.xtb3.grid(row=0,column=6)
        

        "indicate"
        self.labelone = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 1",bg = bgset)
        self.labelone.grid(row=0,column=0,sticky = W,pady = 10)
        self.txtone = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var1)
        self.txtone.grid(row=0,column=1,pady = 10)

        self.labelthree = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 3",bg = bgset)
        self.labelthree.grid(row=2,column=0,sticky = W,pady = 10)
        self.txtthree = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var7)
        self.txtthree.grid(row=2,column=1,pady = 10)

        self.labeltwo = Label(intframe,font = ('arial',12,'bold'),text = "แถบสี 2",bg = bgset)
        self.labeltwo.grid(row=1,column=0,sticky = W,pady = 10)
        self.txttwo = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var2)
        self.txttwo.grid(row=1,column=1,pady = 10)

        self.labelmult = Label(intframe,font = ('arial',12,'bold'),text = "ตัวคูณ",bg = bgset)
        self.labelmult.grid(row=3,column=0,sticky = W,pady = 10)
        self.txtmult = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var3)
        self.txtmult.grid(row=3,column=1,pady = 10)

        self.labeltol = Label(intframe,font = ('arial',12,'bold'),text = "ค่าผิดพลาด",bg = bgset)
        self.labeltol.grid(row=4,column=0,sticky = W,pady = 10)
        self.txttol = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var4)
        self.txttol.grid(row=4,column=1,pady = 10)

        self.labelppm = Label(intframe,font = ('arial',12,'bold'),text = "สัมประสิทธิ์อุณหภูมิ",bg = bgset)
        self.labelppm.grid(row=5,column=0,sticky = W,pady = 10)
        self.txtppm = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var8)
        self.txtppm.grid(row=5,column=1,pady = 10)

        self.labelres = Label(intframe,font = ('arial',12,'bold'),text = "ค่าต้านทาน",bg = bgset)
        self.labelres.grid(row=6,column=0,sticky = W,pady = 10)
        self.txtres = Entry(intframe,font = ('arial',12,'bold'),width = 25,textvariable = var5)
        self.txtres.grid(row=6,column=1,pady = 10)

        calculatebt3 = Button(callingframe,font = ('arial',12,'bold'),text = "คำนวณ",bg = "black",command = calculate3,fg = "white")
        calculatebt3.grid(row=7,column=0,pady = 25)

        calculatebt2 = Button(callingframe,font = ('arial',12,'bold'),text = "คำนวณ",bg = "black",command = calculate2,fg = "white")
        calculatebt2.grid(row=7,column=0,pady = 25)

        calculatebt = Button(callingframe,font = ('arial',12,'bold'),text = "คำนวณ",bg = "black",command = calculate,fg = "white")
        calculatebt.grid(row=7,column=0,pady = 25)

        resetbt = Button(callingframe,font = ('arial',12,'bold'),text = "รีเซ็ต",bg = "black",command = reset1,fg = "white")
        resetbt.grid(row=7,column=1,pady = 25)

        exitbt = Button(callingframe,font = ('arial',12,'bold'),text = "ออก",bg = "black",command = exit1,fg = "white")
        exitbt.grid(row=7,column=2,pady = 25)
        
        trainbt = Button(callingframe,font = ('arial',12,'bold'),text = "ฝึกอ่าน",bg = "black",command = train,fg = "white")
        trainbt.grid(row=8,column=1,pady = 25)
       


if __name__ == "__main__":
    root = Tk()
    napp = Resistor(root)
    root.mainloop()

