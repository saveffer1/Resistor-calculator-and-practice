from tkinter import simpledialog
import tkinter.messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import askstring
from sympy import pretty_print as pp, latex
from sympy.abc import a, b, n
from random import*
from time import*
from main import*
import sqlite3

class StringDialog(simpledialog._QueryString):
    def body(self, master):
        super().body(master)
        self.iconbitmap('icon.ico')

    def ask_string(title, prompt, **kargs):
        d = StringDialog(title, prompt, **kargs)
        return d.result

def sfformat(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

class Training:
    def __init__(self,app):
        self.app = app
        conn = sqlite3.connect('bgcolor.db')
        print("เปิดฐานข้อมูลสำเร็จ")
        cursor = conn.execute("SELECT NAME from SAVEONE")
        rows = cursor.fetchone()[0]
        bgset = rows
        self.app.title("saveffer resistor Training")
        self.app.iconbitmap("icon.ico")
        self.app.geometry("1078x485+0+0")
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
        var3 = StringVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = StringVar()
        var7 = DoubleVar()
        var8 = StringVar()
        gotthis = ""
        varsc = IntVar()
        varname = StringVar()
        hofsc = IntVar()
        hofname = StringVar()

        var1.set("")
        var2.set("")
        var3.set(" ")
        var4.set("")
        var5.set("")
        var6.set("")
        var7.set("")
        var8.set("")

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()

        colorresval = ["black","brown","red","orange","yellow","green","blue","purple","grey","white"]
        resval = ["brown","red","orange","yellow","green","blue","purple","grey","white"]
        colorresvaldict = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"purple":7,"grey":8,"white":9}
        colorresmult = ["black","brown","red","orange","yellow","green","blue","purple","grey","white","gold","silver"]
        #colorrestolorance = ["black","brown","red","green","blue","purple","grey","gold","silver","white"]
        colorrestolorance = ["brown","red","green","blue","purple","grey","gold","silver","white"]

        colorresppm = ["black","brown","red","orange","yellow","green","blue","purple","grey"]

        translateval = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","orange":"ส้ม","yellow":"เหลือง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา","white":"ขาว"," ":" "}
        translatemult = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","orange":"ส้ม","yellow":"เหลือง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา","white":"ขาว","gold":"ทอง","silver":"เงิน"," ":" "}
        translatetoloro = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา","gold":"ทอง","silver":"เงิน","white":"N/A"," ":" "}
        translateppm = {"black":"ดำ","brown":"น้ำตาล","red":"แดง","orange":"ส้ม","yellow":"เหลือง","green":"เขียว","blue":"น้ำเงิน","purple":"ม่วง","grey":"เทา"," ":" "}

        ranval1 = choice(colorresval)
        ranval2 = choice(colorresval)
        ranval3 = choice(colorresval)
        ranmult = choice(colorresmult)
        rantolorance = choice(colorrestolorance)
        ranppm = choice(colorresppm)

        hoff = sqlite3.connect('bgcolor.db')
        print("เปิดฐานข้อมูลสำเร็จ")
        cor = hoff.execute("SELECT NAME from SAVESC")
        hname = cor.fetchone()[0]
        hofname.set(str(hname))
        
        cor2 = hoff.execute("SELECT SCORE from SAVESC") 
        hsc = cor2.fetchone()[0]
        hofsc.set(str(hsc))

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
            ranval1 = choice(resval)
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
            
            print(str(x1),str(x2),str(x3),str(x4),str(x5),str(x6))

            conn = sqlite3.connect('bgcolor.db')
            print("เปิดฐานข้อมูลสำเร็จ")
            cursor1 = conn.execute("SELECT VAL1 from SAVETWO")
            rowling1 = cursor1.fetchone()[0]

            cursor2 = conn.execute("SELECT VAL2 from SAVETWO")
            rowling2 = cursor2.fetchone()[0]

            cursor3 = conn.execute("SELECT MULT from SAVETWO")
            rowling3 = cursor3.fetchone()[0]

            cursor4 = conn.execute("SELECT TORO from SAVETWO")
            rowling4 = cursor4.fetchone()[0]

            cursor5 = conn.execute("SELECT VAL3 from SAVETWO")
            rowling5 = cursor5.fetchone()[0]

            cursor6 = conn.execute("SELECT PPM from SAVETWO")
            rowling6 = cursor6.fetchone()[0]

            conn.execute("UPDATE SAVETWO set VAL1 = ? where VAL1 = ?",(x1,rowling1))
            conn.execute("UPDATE SAVETWO set VAL2 = ? where VAL2 = ?",(x2,rowling2))
            conn.execute("UPDATE SAVETWO set MULT = ? where MULT = ?",(x3,rowling3))
            conn.execute("UPDATE SAVETWO set TORO = ? where TORO = ?",(x4,rowling4))
            conn.execute("UPDATE SAVETWO set VAL3 = ? where VAL3 = ?",(x5,rowling5))
            conn.execute("UPDATE SAVETWO set PPM = ? where PPM = ?",(x6,rowling6))
            conn.commit()
            print("แถวที่อัปเดรตข้อมูลใหม่ :", conn.total_changes)
            print("ค่าเก่า")
            print("VAL1 = ", rowling1)
            print("VAL2 = ", rowling2)
            print("MULT = ", rowling3)
            print("TORO = ", rowling4)
            print("VAL3 = ", rowling5)
            print("PPM = ", rowling6)
            print("ค่าใหม่")
            print("VAL1 = ", x1)
            print("VAL2 = ", x1)
            print("MULT = ", x3)
            print("TORO = ", x4)
            print("VAL3 = ", x5)
            print("PPM = ", x6)
            print("ดำเนินการเสร็จสิ้น")
            conn.close()
            print(gotthis)
            var1.set("")
            var2.set("")
            var3.set(" ")
            return str(x1),str(x2),str(x3),str(x4),str(x5),str(x6);

        def ban():
            gotplan = thebands()
            x1 = gotplan[0]
            x2 = gotplan[1]
            x3 = gotplan[2]
            x4 = gotplan[3]
            x5 = gotplan[4]
            x6 = gotplan[5]

            print("ban = ",gotplan)
            return str(x1),str(x2),str(x3),str(x4),str(x5),str(x6);

        def anscheck(resis,tole,pp):
            print(gotthis)

            conn = sqlite3.connect('bgcolor.db')
            print("เปิดฐานข้อมูลสำเร็จ")
            cs1 = conn.execute("SELECT VAL1 from SAVETWO")
            ro1 = cs1.fetchone()[0]

            cs2 = conn.execute("SELECT VAL2 from SAVETWO")
            ro2 = cs2.fetchone()[0]

            cs3 = conn.execute("SELECT MULT from SAVETWO")
            ro3 = cs3.fetchone()[0]

            cs4 = conn.execute("SELECT TORO from SAVETWO")
            ro4 = cs4.fetchone()[0]

            cs5 = conn.execute("SELECT VAL3 from SAVETWO")
            ro5 = cs5.fetchone()[0]

            cs6 = conn.execute("SELECT PPM from SAVETWO")
            ro6 = cs6.fetchone()[0]

            answer = [ro1,ro2,ro3,ro4,ro5,ro6]

            print("askcheck")
            print("VAL1 = ", ro1)
            print("VAL2 = ", ro2)
            print("MULT = ", ro3)
            print("TORO = ", ro4)
            print("VAL3 = ", ro5)
            print("PPM = ", ro6)
            print("ดำเนินการเสร็จสิ้น")

            conn.close()

            #answer = ["red","red","black","gold"," "," "] #ค่า R ที่ เช็ค
            print(answer)
            dicval = {" ":" ","black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"purple":7,"grey":8,"white":9}
            dicmult = {"black":1,"brown":10,"red":100,"orange":1000,"yellow":10000,"green":100000,"blue":1000000,"purple":10000000,"grey":100000000,"white":1000000000,"gold":0.1,"silver":0.01}
            dictoro = {" ":" ","black":20,"brown":1,"red":2,"orange":20,"yellow":20,"green":0.5,"blue":0.25,"purple":0.1,"grey":0.05,"white":20,"gold":5,"silver":10}
            dicppm = {" ":" ","black":250,"brown":100,"red":50,"orange":15,"yellow":25,"green":20,"blue":10,"purple":5,"grey":1}
            ans = ""
            ansor = ""
            ask = ""
            ans2 = ""
            ask2 = ""
            pm = ""
            
            if answer[4] == " " and answer[5] == " ":
                print("4 bands")
                rst = float("%d%d" %((dicval[answer[0]],dicval[answer[1]])))
                rst *= dicmult[answer[2]]
                rstfor = sfformat(rst)
                rstint = int(rst)
                pm = dicppm[answer[5]]     
                if pp == " " or pp == None or pp == ""or pp == "-":
                    pp = "N/A"
                if pm == " ":
                    pm = "N/A"   
                                
                tolance = dictoro[answer[3]]
                block = float(resis)

                ressaveformat = sfformat(float(resis))

                if rst > rstint:
                    print("float")
                    ansor = str("{:.1f}"+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm").format(rst)
                    ans = str("{:.2f}"+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm").format(rst)
                    ask = str(str(block)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")
                elif rst == rstint:
                    print("int")
                    ans = str(str(rstint)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm")
                    ask = str(str(int(resis))+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")

                if rst >= 1000:
                    ans2 = str(str(rstfor)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm")
                    ask2 = str(str(ressaveformat)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")
                else:
                    ans2 = "*noformat"
                    ask2 = "/noformat"
                
            elif answer[5] == " ":
                print("5 bands")
                rst = float("%d%d%d" %((dicval[answer[0]],dicval[answer[1]],dicval[answer[4]])))
                rst *= dicmult[answer[2]]
                rstfor = sfformat(rst)
                rstint = int(rst)
                pm = dicppm[answer[5]]      
                if pp == " "or pp == None or pp == ""or pp == "-":
                    pp = "N/A"
                if pm == " ":
                    pm = "N/A"         
                tolance = dictoro[answer[3]]
                block = float(resis)

                ressaveformat = sfformat(float(resis))

                if rst > rstint:
                    ansor = str("{:.1f}"+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm").format(rst)
                    ans = str("{:.2f}"+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm").format(rst)
                    ask = str(str(block)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")
                elif rst == rstint:
                    ans = str(str(rstint)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm")
                    ask = str(str(int(resis))+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")

                if rst >= 1000:
                    ans2 = str(str(rstfor)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm")
                    ask2 = str(str(ressaveformat)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")
                else:
                    ans2 = "*noformat"
                    ask2 = "/noformat"
                    
            elif answer[0] != None and answer[1] != None and answer[2] != None and answer[3] != None and answer[4] != None and answer[5] != None:
                print("6 bands")
                rst = float("%d%d%d" %((dicval[answer[0]],dicval[answer[1]],dicval[answer[4]])))
                rst *= dicmult[answer[2]]
                rstfor = sfformat(rst)
                rstint = int(rst)
                pm = dicppm[answer[5]]        
                tolance = dictoro[answer[3]]
                block = float(resis)

                ressaveformat = sfformat(float(resis))

                if rst > rstint:
                    print("int")
                    ansor = str("{:.1f}"+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm").format(rst)
                    ans = str("{:.2f}"+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm").format(rst)
                    ask = str(str(block)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")
                elif rst == rstint:
                    print("float")
                    ans = str(str(rstint)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm")
                    ask = str(str(int(resis))+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")

                if rst >= 1000:
                    ans2 = str(str(rstfor)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pm)+" ppm")
                    ask2 = str(str(ressaveformat)+" "+"\u03A9"+" "+u"\u00B1 "+(str(tolance))+"%"+" "+str(pp)+" ppm")
                else:
                    ans2 = "*noformat"
                    ask2 = "/noformat"

            else:
                ans = "+"
                ask = "-"
                ans2 = "*"
                ask2 = "/"

            print(ans,end=" ")
            print(" || ",end=" ")
            print(ans2,end=" ")
            print(" || ",end=" ")
            print(ask,end=" ")
            print(" || ",end=" ")
            print(ask2)
            
            if  ansor or ans == ask or ans2 == ask2:
                print("true")
                add = varsc.get()+1
                varsc.set(add)
                self.labelsc.config(textvariable = varsc)
                maxcheck = sqlite3.connect('bgcolor.db')
                indexname = maxcheck.execute("SELECT NAME from SAVESC")
                indexscore = maxcheck.execute("SELECT SCORE from SAVESC")
                bashname = indexname.fetchone()[0]
                bashsc = indexscore.fetchone()[0]
                doc = int(bashsc)
                gadd = str(add)
                ipname = varname.get()
                maxcheck.close()
                if add > doc:
                    maxcheck = sqlite3.connect('bgcolor.db')
                    maxcheck.execute("UPDATE SAVESC set SCORE = ? where SCORE = ?",(gadd,bashsc))
                    maxcheck.execute("UPDATE SAVESC set NAME = ? where NAME = ?",(ipname,bashname))
                    maxcheck.commit()
                    print("Hall of Frame has change")
                    gotname = maxcheck.execute("SELECT NAME from SAVESC")
                    gotscore = maxcheck.execute("SELECT SCORE from SAVESC")
                    gname = gotname.fetchone()[0]
                    gsc = gotscore.fetchone()[0]
                    hofsc.set(gsc)
                    hofname.set(gname)
                    #self.labelhsc.config(textvariable = varsc)
                    #self.labelname.config(textvariable = varname)
                maxcheck.close()
                thebands()
            else:
                print("false")
                varsc.set(0)

        def cal(event=None):
            resist = var1.get()
            tolet = var2.get()
            ppmt = var3.get()
            anscheck(resist,tolet,ppmt)
            var1.set("")
            var2.set("")
            var3.set(" ")
        
        
        prompt = StringDialog.ask_string("กรอกชื่อ", "ป้อนชื่อของคุณ")
        print(prompt)

        varname.set(prompt)
        frame1 = Frame(self.app,width = 800,height = 400,bg = bgset)
        frame1.grid(row=0,column=0)

        frame2 = Frame(self.app,width = 250,height = 400,bg = bgset)
        frame2.grid(row=0,column=1,sticky = "nse")

        frame3 = Frame(self.app,width = 250,height = 400,bg = bgset)
        frame3.grid(row=1,column=0,columnspan = 2)
        
        """
        self.labeltitle1 = Label(frame1,font = ('arial',47,'bold'),text = "1",bg = bgset,padx = 5)
        self.labeltitle1.grid(row=0,column=0,columnspan = 3)

        self.labeltitle2 = Label(frame1,font = ('arial',47,'bold'),text = "2",bg = bgset,padx = 5)
        self.labeltitle2.grid(row=0,column=3,columnspan = 6)

        self.labeltitle3 = Label(frame1,font = ('arial',47,'bold'),text = "3",bg = bgset,padx = 5)
        self.labeltitle3.grid(row=1,column=0,columnspan = 6)
        """
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
        
        """check button bands"""
        """
        self.C4 = Checkbutton(checkframe, text = "0",bg = bgset, variable = CheckVar1,onvalue = 0,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 0, sticky="nswe")
        grid_hide(self.C4)
        """
        gotplan = thebands()
        onetime = CheckVar2.get()

        self.C4 = Checkbutton(checkframe, text = "4",bg = bgset, variable = CheckVar1,onvalue = 0,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 0, sticky="nswe")

        self.C4 = Checkbutton(checkframe, text = "5",bg = bgset, variable = CheckVar1,onvalue = 1,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 1, sticky="nswe")

        self.C4 = Checkbutton(checkframe, text = "6",bg = bgset, variable = CheckVar1,onvalue = 2,command = thebands, height=1,width = 2)
        self.C4.grid(row = 1,column = 2, sticky="nswe")

        CheckVar2.get()+1
        
        
        self.chekshow = Checkbutton(checkframe, text = "แสดงข้อความสี",bg = bgset, variable = CheckVar2,onvalue = 0,offvalue = 1,command = thebands, height=1,width = 2)
        self.chekshow.grid(row = 2,column = 0,columnspan = 3, sticky="nswe")
        grid_hide(self.chekshow)

        self.labelask = Label(checkframe,font = ('arial',14,'bold'),text = "คำตอบ",bg = bgset)
        self.labelask.grid(row=3,column=0,columnspan = 3,sticky = "nswe",pady = 10)
        
        self.labelask = Label(checkframe,font = ('arial',10,'bold'),text = "ค่าต้านทาน",bg = bgset)
        self.labelask.grid(row=4,column=0,sticky = "nswe",pady = 10)

        self.labelask = Label(checkframe,font = ('arial',10,'bold'),text = "ค่าผิดพลาด",bg = bgset)
        self.labelask.grid(row=4,column=1,sticky = "nswe",pady = 10)

        self.labelask = Label(checkframe,font = ('arial',10,'bold'),text = "สัมประสิทธิ์อุณหภูมิ",bg = bgset)
        self.labelask.grid(row=4,column=2,sticky = "nswe",pady = 10)

        self.txtask1 = Entry(checkframe,font = ('arial',8,'bold'),width = 10,textvariable = var1)
        self.txtask1.grid(row=5,column=0,pady = 10)

        self.txtask2 = Entry(checkframe,font = ('arial',8,'bold'),width = 10,textvariable = var2)
        self.txtask2.grid(row=5,column=1,pady = 10)

        self.txtask3 = Entry(checkframe,font = ('arial',8,'bold'),width = 10,textvariable = var3)
        self.txtask3.grid(row=5,column=2,pady = 10)

        calculatebt = Button(checkframe,font = ('arial',12,'bold'),text = "ส่งคำตอบ",bg = "black",fg = "white",command = cal)
        calculatebt.grid(row=6,column=1,pady = 25)

        rsbt = Button(checkframe,font = ('arial',12,'bold'),text = "สุ่มค่าใหม่",bg = "black",command = thebands,fg = "white")
        rsbt.grid(row=6,column=2,pady = 25)

        self.labeladj = Label(checkframe,font = ('arial',10,'bold'),text = "* ไม่ต้องใส่หน่วย",bg = bgset)
        self.labeladj.grid(row=7,column=0,sticky = W,pady = 10)

        self.labeladj = Label(checkframe,font = ('arial',10,'bold'),text = "* ถ้าไม่มีค่าให้เว้นไว้",bg = bgset)
        self.labeladj.grid(row=7,column=1,sticky = W,pady = 10)

        self.labeladj = Label(checkframe,font = ('arial',10,'bold'),text = "* ค่าผิดพลาดสีขาว = N/A",bg = bgset)
        self.labeladj.grid(row=7,column=2,sticky = W,pady = 10)

        self.labeladj = Label(checkframe,font = ('arial',15,'bold'),text = "คะแนน:",bg = bgset)
        self.labeladj.grid(row=8,column=0,sticky = 'news',pady = 28)

        self.labelsc = Label(checkframe,font = ('arial',15,'bold'),textvariable = varsc,bg = bgset)
        self.labelsc.grid(row=8,column=1,columnspan = 2,sticky = 'news',pady = 28)

        self.labeladj = Label(checkframe,font = ('arial',15,'bold'),text = "คะแนนสูงสุด:",bg = bgset)
        self.labeladj.grid(row=9,column=0,sticky = 'news',pady = 14)

        self.labelname = Label(checkframe,font = ('arial',15,'bold'),textvariable = hofname,bg = bgset)
        self.labelname.grid(row=9,column=1,sticky = 'news',pady = 14)

        self.labelhsc = Label(checkframe,font = ('arial',15,'bold'),textvariable = hofsc,bg = bgset)
        self.labelhsc.grid(row=9,column=2,sticky = 'news',pady = 14)

        self.app.bind('<Return>', cal)

        thebands()


        
if __name__ == "__main__":   
    app = Tk()
    dat = Training(app)
    app.mainloop() 
