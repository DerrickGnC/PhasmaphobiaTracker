import tkinter  as tk
from tkinter.constants import S 
my_w = tk.Tk()

my_w.title("Phasmaphobia Tracker")
my_w.iconbitmap('F:\Python Programs\Phasmo Tracker\Logo.ico')

def Evi1Upd():
    global e1
    e1=0
    #if Evidence 1 EMF is on Evidence 2 & 3 are off
    if (EVI1EMF_v.get()==1):e1=e1+1
    if (EVI1EMF_v.get()==1):EVI2EMF.config(state='disabled')
    if (EVI1EMF_v.get()==1):EVI3EMF.config(state='disabled')
    #if Evidence 1 Fingerprints is on Evidence 2 & 3 are off
    if (EVI1Fin_v.get()==1):e1=e1+1
    if (EVI1Fin_v.get()==1):EVI2Fin.config(state='disabled')
    if (EVI1Fin_v.get()==1):EVI3Fin.config(state='disabled')
    #if Evidence 1 Temperature is on Evidence 2 & 3 are off
    if (EVI1Temp_v.get()==1):e1=e1+1
    if (EVI1Temp_v.get()==1):EVI2Temp.config(state='disabled')
    if (EVI1Temp_v.get()==1):EVI3Temp.config(state='disabled')
    #if Evidence 1 Ghost Orb is on Evidence 2 & 3 are off
    if (EVI1Orb_v.get()==1):e1=e1+1
    if (EVI1Orb_v.get()==1):EVI2Orb.config(state='disabled')
    if (EVI1Orb_v.get()==1):EVI3Orb.config(state='disabled')
    #if Evidence 1 Ghost Writing is on Evidence 2 & 3 are off
    if (EVI1Write_v.get()==1):e1=e1+1
    if (EVI1Write_v.get()==1):EVI2Write.config(state='disabled')
    if (EVI1Write_v.get()==1):EVI3Write.config(state='disabled')
    #if Evidence 1 Spirit Box is on Evidence 2 & 3 are off
    if (EVI1Box_v.get()==1):e1=e1+1
    if (EVI1Box_v.get()==1):EVI2Box.config(state='disabled')
    if (EVI1Box_v.get()==1):EVI3Box.config(state='disabled')
    if  (e1>0):
        if (EVI1EMF_v.get()!=1):EVI1EMF.config(state='disabled')
        if (EVI1Fin_v.get()!=1):EVI1Fin.config(state="disabled")
        if (EVI1Temp_v.get()!=1):EVI1Temp.config(state="disabled")
        if (EVI1Orb_v.get()!=1):EVI1Orb.config(state="disabled")
        if (EVI1Write_v.get()!=1):EVI1Write.config(state="disabled")
        if (EVI1Box_v.get()!=1):EVI1Box.config(state="disabled")
    else:
        EVI1EMF.config(state='normal')
        EVI2EMF.config(state='normal')
        EVI3EMF.config(state='normal')
        EVI1Fin.config(state='normal')
        EVI2Fin.config(state='normal')
        EVI3Fin.config(state='normal')
        EVI1Temp.config(state='normal')
        EVI2Temp.config(state='normal')
        EVI3Temp.config(state='normal')
        EVI1Orb.config(state='normal')
        EVI2Orb.config(state='normal')
        EVI3Orb.config(state='normal')
        EVI1Write.config(state='normal')
        EVI2Write.config(state='normal')
        EVI3Write.config(state='normal')
        EVI1Box.config(state='normal')
        EVI2Box.config(state='normal')
        EVI3Box.config(state='normal')

def Evi2Upd():
        e2=0
        #if Evidence 2 EMF is on Evidence 3 is off
        if (EVI2EMF_v.get()==1):e2=e2+1
        if (EVI2EMF_v.get()==1):EVI3EMF.config(state='disabled')
        #if Evidence 2 Fingerprint is on Evidence 3 is off
        if (EVI2Fin_v.get()==1):e2=e2+1
        if (EVI2Fin_v.get()==1):EVI3Fin.config(state='disabled')
        #if Evidence 2 Temperature is on Evidence 3 is off
        if (EVI2Temp_v.get()==1):e2=e2+1
        if (EVI2Temp_v.get()==1):EVI3Temp.config(state='disabled')
        #if Evidence 2 Ghost Orb is on Evidence 3 is off
        if (EVI2Orb_v.get()==1):e2=e2+1
        if (EVI2Orb_v.get()==1):EVI3Orb.config(state='disabled')
        #if Evidence 2 Ghost Orb is on Evidence 3 is off
        if (EVI2Write_v.get()==1):e2=e2+1
        if (EVI2Write_v.get()==1):EVI3Write.config(state='disabled')
        #if Evidence 2 Ghost Box is on Evidence 3 is off
        if (EVI2Box_v.get()==1):e2=e2+1
        if (EVI2Box_v.get()==1):EVI3Box.config(state='disabled')
        if  (e2>0):
            if (EVI2EMF_v.get()!=1):EVI2EMF.config(state='disabled')
            if (EVI2Fin_v.get()!=1):EVI2Fin.config(state="disabled")
            if (EVI2Temp_v.get()!=1):EVI2Temp.config(state="disabled")
            if (EVI2Orb_v.get()!=1):EVI2Orb.config(state="disabled")
            if (EVI2Write_v.get()!=1):EVI2Write.config(state="disabled")
            if (EVI2Box_v.get()!=1):EVI2Box.config(state="disabled")
            
        else:
            EVI2EMF.config(state='normal')
            EVI3EMF.config(state='normal')
            EVI2Fin.config(state='normal')
            EVI3Fin.config(state='normal')
            EVI2Temp.config(state='normal')
            EVI3Temp.config(state='normal')
            EVI2Orb.config(state='normal')
            EVI3Orb.config(state='normal')
            EVI2Write.config(state='normal')
            EVI3Write.config(state='normal')
            EVI2Box.config(state='normal')
            EVI3Box.config(state='normal')

def Evi3Upd():
    e3=0
    if (EVI3EMF_v.get()==1):e3=e3+1
    if (EVI3Fin_v.get()==1):e3=e3+1
    if (EVI3Temp_v.get()==1):e3=e3+1
    if (EVI3Orb_v.get()==1):e3=e3+1
    if (EVI3Write_v.get()==1):e3=e3+1
    if (EVI3Box_v.get()==1):e3=e3+1
    if  (e3>0):
        if (EVI3EMF_v.get()!=1):EVI3EMF.config(state='disabled')
        if (EVI3Fin_v.get()!=1):EVI3Fin.config(state="disabled")
        if (EVI3Temp_v.get()!=1):EVI3Temp.config(state="disabled")
        if (EVI3Orb_v.get()!=1):EVI3Orb.config(state="disabled")
        if (EVI3Write_v.get()!=1):EVI3Write.config(state="disabled")
        if (EVI3Box_v.get()!=1):EVI3Box.config(state="disabled")
    else:
        EVI3EMF.config(state='normal')
        EVI3Fin.config(state='normal')
        EVI3Temp.config(state='normal')
        EVI3Orb.config(state='normal')
        EVI3Write.config(state='normal')
        EVI3Box.config(state='normal')        

def GhostTypeEmf():
    if EVI1EMF_v.get()==1:
        Poltergeist.config(state='disabled')
        Spirit.config(state='disabled')
        Wraith.config(state='disabled')
        Hantu.config(state='disabled')
        Demon.config(state='disabled')
        Mare.config(state='disabled')
        Yurei.config(state='disabled')
        Yokai.config(state='disabled')
    else:
        Poltergeist.config(state='normal')
        Spirit.config(state='normal')
        Wraith.config(state='normal')
        Hantu.config(state='normal')
        Demon.config(state='normal')
        Mare.config(state='normal')
        Yurei.config(state='normal')
        Yokai.config(state='normal')
    if EVI2EMF_v.get()==1:
        Poltergeist.config(state='disabled')
        Spirit.config(state='disabled')
        Wraith.config(state='disabled')
        Hantu.config(state='disabled')
        Demon.config(state='disabled')
        Mare.config(state='disabled')
        Yurei.config(state='disabled')
        Yokai.config(state='disabled')
    if EVI3EMF_v.get()==1:
        Poltergeist.config(state='disabled')
        Spirit.config(state='disabled')
        Wraith.config(state='disabled')
        Hantu.config(state='disabled')
        Demon.config(state='disabled')
        Mare.config(state='disabled')
        Yurei.config(state='disabled')
        Yokai.config(state='disabled')

def GhostTypePrint():
    if EVI1Fin_v.get()==1:
        Jinn.config(state='disabled')
        Oni.config(state='disabled')
        Phantom.config(state='disabled')
        Shade.config(state='disabled')
        Demon.config(state='disabled')
        Yurei.config(state='disabled')
        Yokai.config(state='disabled')
        Mare.config(state='disabled')
    else:
        Jinn.config(state='normal')
        Oni.config(state='normal')
        Phantom.config(state='normal')
        Shade.config(state='normal')
        Demon.config(state='normal')
        Yurei.config(state='normal')
        Yokai.config(state='normal')
        Mare.config(state='normal')
    if EVI2Fin_v.get()==1:
        Jinn.config(state='disabled')
        Oni.config(state='disabled')
        Phantom.config(state='disabled')
        Shade.config(state='disabled')
        Demon.config(state='disabled')
        Yurei.config(state='disabled')
        Yokai.config(state='disabled')
        Mare.config(state='disabled')
    if EVI3Fin_v.get()==1:
        Jinn.config(state='disabled')
        Oni.config(state='disabled')
        Phantom.config(state='disabled')
        Shade.config(state='disabled')
        Demon.config(state='disabled')
        Yurei.config(state='disabled')
        Yokai.config(state='disabled')
        Mare.config(state='disabled')

def GhostTypeTemp():
    if EVI1Temp_v.get()==1:
        Revenant.config(state='disabled')
        Spirit.config(state='disabled')
        Oni.config(state='disabled')
        Poltergeist.config(state='disabled')
        Hantu.config(state='disabled')
        Jinn.config(state='disabled')
        Shade.config(state='disabled')
        Yokai.config(state='disabled')
    else:
        Revenant.config(state='normal')
        Spirit.config(state='normal')
        Oni.config(state='normal')
        Poltergeist.config(state='normal')
        Hantu.config(state='normal')
        Jinn.config(state='normal')
        Shade.config(state='normal')
        Yokai.config(state='normal')
    if EVI2Temp_v.get()==1:
        Revenant.config(state='disabled')
        Spirit.config(state='disabled')
        Oni.config(state='disabled')
        Poltergeist.config(state='disabled')
        Hantu.config(state='disabled')
        Jinn.config(state='disabled')
        Shade.config(state='disabled')
        Yokai.config(state='disabled')
    if EVI3Temp_v.get()==1:
        Revenant.config(state='disabled')
        Spirit.config(state='disabled')
        Oni.config(state='disabled')
        Poltergeist.config(state='disabled')
        Hantu.config(state='disabled')
        Jinn.config(state='disabled')
        Shade.config(state='disabled')
        Yokai.config(state='disabled')

def GhostTypeOrb():
    if EVI1Orb_v.get()==1:
        Banshee.config(state='disabled')
        Demon.config(state='disabled')
        Wraith.config(state='disabled')
        Oni.config(state='disabled')
        Revenant.config(state='disabled')
        Spirit.config(state='disabled')
    else:
        Banshee.config(state='normal')
        Demon.config(state='normal')
        Wraith.config(state='normal')
        Oni.config(state='normal')
        Revenant.config(state='normal')
        Spirit.config(state='normal')
    if EVI2Orb_v.get()==1:
        Banshee.config(state='disabled')
        Demon.config(state='disabled')
        Wraith.config(state='disabled')
        Oni.config(state='disabled')
        Revenant.config(state='disabled')
        Spirit.config(state='disabled')
    if EVI3Orb_v.get()==1:
        Banshee.config(state='disabled')
        Demon.config(state='disabled')
        Wraith.config(state='disabled')
        Oni.config(state='disabled')
        Revenant.config(state='disabled')
        Spirit.config(state='disabled')

def GhostTypeWrite():
    if EVI1Write_v.get()==1:
        Banshee.config(state='disabled')
        Jinn.config(state='disabled')
        Mare.config(state='disabled')
        Phantom.config(state='disabled')
        Poltergeist.config(state='disabled')
        Wraith.config(state='disabled')
    else:
        Banshee.config(state='normal')
        Jinn.config(state='normal')
        Mare.config(state='normal')
        Phantom.config(state='normal')
        Poltergeist.config(state='normal')
        Wraith.config(state='normal')
    if EVI2Write_v.get()==1:
        Banshee.config(state='disabled')
        Jinn.config(state='disabled')
        Mare.config(state='disabled')
        Phantom.config(state='disabled')
        Poltergeist.config(state='disabled')
        Wraith.config(state='disabled')
    if EVI3Write_v.get()==1:
        Banshee.config(state='disabled')
        Jinn.config(state='disabled')
        Mare.config(state='disabled')
        Phantom.config(state='disabled')
        Poltergeist.config(state='disabled')
        Wraith.config(state='disabled')

def GhostTypeBox():
    if EVI1Box_v.get()==1:
        Banshee.config(state='disabled')
        Hantu.config(state='disabled')
        Phantom.config(state='disabled')
        Revenant.config(state='disabled')
        Shade.config(state='disabled')
        Yurei.config(state='disabled')
    else:
        Banshee.config(state='normal')
        Hantu.config(state='normal')
        Phantom.config(state='normal')
        Revenant.config(state='normal')
        Shade.config(state='normal')
        Yurei.config(state='normal')
    if EVI2Box_v.get()==1:
        Banshee.config(state='disabled')
        Hantu.config(state='disabled')
        Phantom.config(state='disabled')
        Revenant.config(state='disabled')
        Shade.config(state='disabled')
        Yurei.config(state='disabled')
    if EVI3Box_v.get()==1:
        Banshee.config(state='disabled')
        Hantu.config(state='disabled')
        Phantom.config(state='disabled')
        Revenant.config(state='disabled')
        Shade.config(state='disabled')
        Yurei.config(state='disabled')
    
    

    #if EVI2EMF_v.get()==1:Poltergeist.config(state='disabled')
    #if EVI2EMF_v.get()==1:Spirit.config(state='disabled')
    #if EVI2EMF_v.get()==1:Wraith.config(state='disabled')
    #if EVI2EMF_v.get()==1:Hantu.config(state='disabled')
    #if EVI2EMF_v.get()==1:Demon.config(state='disabled')
    #if EVI2EMF_v.get()==1:Mare.config(state='disabled')
    #if EVI2EMF_v.get()==1:Yurei.config(state='disabled')
    #if EVI2EMF_v.get()==1:Yokai.config(state='disabled')
    #if EVI3EMF_v.get()==1:Poltergeist.config(state='disabled')
    #if EVI3EMF_v.get()==1:Spirit.config(state='disabled')
    #if EVI3EMF_v.get()==1:Wraith.config(state='disabled')
    #if EVI3EMF_v.get()==1:Hantu.config(state='disabled')
    #if EVI3EMF_v.get()==1:Demon.config(state='disabled')
    #if EVI3EMF_v.get()==1:Mare.config(state='disabled')
    #if EVI3EMF_v.get()==1:Yurei.config(state='disabled')
    #if EVI3EMF_v.get()==1:Yokai.config(state='disabled')
    


#Evidence 1
Evidence1 = tk.Label(text="Evidence 1")
Evidence1.grid(row=0,column=1,sticky="nsew")

EVI1EMF_v = tk.IntVar(my_w)
EVI1EMF =tk.Checkbutton(my_w,text= "EMF LVL 5",command=lambda:[Evi1Upd(),GhostTypeEmf()], variable=EVI1EMF_v)
EVI1EMF.grid(row=1,column=0,sticky="nsew")


EVI1Fin_v = tk.IntVar(my_w)
EVI1Fin = tk.Checkbutton(my_w,text= "Fingerprints",command=lambda:[Evi1Upd(),GhostTypePrint()], variable=EVI1Fin_v)
EVI1Fin.grid(row=1,column=1,sticky="nsew")

EVI1Temp_v = tk.IntVar(my_w)
EVI1Temp= tk.Checkbutton(my_w,text= "Freezing Temp",command=lambda:[Evi1Upd(),GhostTypeTemp()], variable=EVI1Temp_v)
EVI1Temp.grid(row=1,column=2,sticky="nsew")

EVI1Orb_v = tk.IntVar(my_w)
EVI1Orb = tk.Checkbutton(my_w,text= "Ghost Orb",command=lambda:[Evi1Upd(),GhostTypeOrb()], variable=EVI1Orb_v)
EVI1Orb.grid(row=2,column=0,sticky="nsew")

EVI1Write_v = tk.IntVar(my_w)
EVI1Write= tk.Checkbutton(my_w,text= "Ghost Writing",command=lambda:[Evi1Upd(),GhostTypeWrite()], variable=EVI1Write_v)
EVI1Write.grid(row=2,column=1,sticky="nsew")

EVI1Box_v = tk.IntVar(my_w)
EVI1Box= tk.Checkbutton(my_w,text= "Spirit Box",command=lambda:[Evi1Upd(),GhostTypeBox()], variable=EVI1Box_v)
EVI1Box.grid(row=2,column=2,sticky="nsew")

#Evidence 2
Evidence2 = tk.Label(text="Evidence 2")
Evidence2.grid(row=3,column=1,sticky="nsew")

EVI2EMF_v = tk.IntVar(my_w)
EVI2EMF =tk.Checkbutton(my_w,text= "EMF LVL 5",command=lambda:[Evi2Upd(),GhostTypeEmf()], variable=EVI2EMF_v)
EVI2EMF.grid(row=4,column=0,sticky="nsew")


EVI2Fin_v = tk.IntVar(my_w)
EVI2Fin = tk.Checkbutton(my_w,text= "Fingerprints",command=lambda:[Evi2Upd(),GhostTypePrint()], variable=EVI2Fin_v)
EVI2Fin.grid(row=4,column=1,sticky="nsew")

EVI2Temp_v = tk.IntVar(my_w)
EVI2Temp= tk.Checkbutton(my_w,text= "Freezing Temp",command=lambda:[Evi2Upd(),GhostTypeTemp()], variable=EVI2Temp_v)
EVI2Temp.grid(row=4,column=2,sticky="nsew")

EVI2Orb_v = tk.IntVar(my_w)
EVI2Orb = tk.Checkbutton(my_w,text= "Ghost Orb",command=lambda:[Evi2Upd(),GhostTypeOrb()], variable=EVI2Orb_v)
EVI2Orb.grid(row=5,column=0,sticky="nsew")

EVI2Write_v = tk.IntVar(my_w)
EVI2Write= tk.Checkbutton(my_w,text= "Ghost Writing",command=lambda:[Evi2Upd(),GhostTypeWrite()], variable=EVI2Write_v)
EVI2Write.grid(row=5,column=1,sticky="nsew")

EVI2Box_v = tk.IntVar(my_w)
EVI2Box= tk.Checkbutton(my_w,text= "Spirit Box",command=lambda:[Evi2Upd(),GhostTypeBox()], variable=EVI2Box_v)
EVI2Box.grid(row=5,column=2,sticky="nsew")

#Evidence 3
Evidence3 = tk.Label(text="Evidence 3")
Evidence3.grid(row=6,column=1,sticky="nsew")

EVI3EMF_v = tk.IntVar(my_w)
EVI3EMF =tk.Checkbutton(my_w,text= "EMF LVL 5",command=lambda:[Evi3Upd(),GhostTypeEmf()], variable=EVI3EMF_v)
EVI3EMF.grid(row=7,column=0,sticky="nsew")


EVI3Fin_v = tk.IntVar(my_w)
EVI3Fin = tk.Checkbutton(my_w,text= "Fingerprints",command=lambda:[Evi3Upd(),GhostTypePrint()], variable=EVI3Fin_v)
EVI3Fin.grid(row=7,column=1,sticky="nsew")

EVI3Temp_v = tk.IntVar(my_w)
EVI3Temp= tk.Checkbutton(my_w,text= "Freezing Temp",command=lambda:[Evi3Upd(),GhostTypeTemp()], variable=EVI3Temp_v)
EVI3Temp.grid(row=7,column=2,sticky="nsew")

EVI3Orb_v = tk.IntVar(my_w)
EVI3Orb = tk.Checkbutton(my_w,text= "Ghost Orb",command=lambda:[Evi3Upd(),GhostTypeOrb()], variable=EVI3Orb_v)
EVI3Orb.grid(row=8,column=0,sticky="nsew")

EVI3Write_v = tk.IntVar(my_w)
EVI3Write= tk.Checkbutton(my_w,text= "Ghost Writing",command=lambda:[Evi3Upd(),GhostTypeWrite()], variable=EVI3Write_v)
EVI3Write.grid(row=8,column=1,sticky="nsew")

EVI3Box_v = tk.IntVar(my_w)
EVI3Box= tk.Checkbutton(my_w,text= "Spirit Box",command=lambda:[Evi3Upd(),GhostTypeBox()], variable=EVI3Box_v)
EVI3Box.grid(row=8,column=2,sticky="nsew")

GhostSelection = tk.Label(text="Your Ghost Type is")
GhostSelection.grid(row=9,column=1,sticky="nsew")

Banshee = tk.Label(text="Banshee")
Banshee.grid(row=10,column=0,sticky="nsew")

Demon = tk.Label(text="Demon")
Demon.grid(row=10,column=1,sticky="nsew")

Hantu = tk.Label(text="Hantu")
Hantu.grid(row=10,column=2,sticky="nsew")

Jinn = tk.Label(text="Jinn")
Jinn.grid(row=11,column=0,sticky="nsew")

Mare = tk.Label(text="Mare")
Mare.grid(row=11,column=1,sticky="nsew")

Oni = tk.Label(text="Oni")
Oni.grid(row=11,column=2,sticky="nsew")

Phantom = tk.Label(text="Phantom")
Phantom.grid(row=12,column=0,sticky="nsew")

Poltergeist = tk.Label(text="Poltergeist")
Poltergeist.grid(row=12,column=1,sticky="nsew")

Revenant = tk.Label(text="Revenant")
Revenant.grid(row=12,column=2,sticky="nsew")

Shade = tk.Label(text="Shade")
Shade.grid(row=13,column=0,sticky="nsew")

Spirit = tk.Label(text="Spirit")
Spirit.grid(row=13,column=1,sticky="nsew")

Wraith = tk.Label(text="Wraith")
Wraith.grid(row=13,column=2,sticky="nsew")

Yokai = tk.Label(text="Yokai")
Yokai.grid(row=14,column=0,sticky="nsew")

Yurei = tk.Label(text="Yurei")
Yurei.grid(row=14,column=2,sticky="nsew")


my_w.mainloop()
