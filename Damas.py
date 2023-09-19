# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:47:19 2023




@author: JC
"""
# Dama 

from tkinter import *
from functools import *
#from redisenar_imagen import *
import tkinter.messagebox



from PIL import Image,ImageTk 
lista_botones=[]
turno=1
def ComerMas(boton):
   
    if  boton.getcassilla1() is not None  and boton.getcassilla1().getColor()is not None and boton.getcassilla1().getColor() != boton.getColor() and boton.getcassilla1().getcassilla1()is not None and  boton.getcassilla1().getcassilla1().getColor()== None    :
        
        if boton.getColor()=="Negras" :
            boton.getcassilla1().getboton().config(command=partial(ComerFicha,boton.getcassilla1(),boton,1))
        else :
            boton.getcassilla1().getboton().config(command=partial(ComerFichaInv,boton.getcassilla1(),boton,1))
        
    
    if  boton.getcassilla2() is not None  and boton.getcassilla2().getColor()is not None and boton.getcassilla2().getColor() != boton.getColor() and boton.getcassilla2().getcassilla2()is not None and  boton.getcassilla2().getcassilla1().getColor()== None    :
        if boton.getColor()=="Negras" :
            boton.getcassilla2().getboton().config(command=partial(ComerFicha,boton.getcassilla2(),boton,2))
        else:
            boton.getcassilla2().getboton().config(command=partial(ComerFichaInv,boton.getcassilla2(),boton,2))
        
    if  boton.getcassillaAnt1() is not None  and boton.getcassillaAnt1().getColor()is not None and boton.getcassillaAnt1().getColor() != boton.getColor() and boton.getcassillaAnt1().getcassillaAnt1()is not None and  boton.getcassillaAnt1().getcassillaAnt1().getColor()== None    :
        if boton.getColor()=="Blancas" :
            boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,1))
        else:
            boton.getcassillaAnt1().getboton().config(command=partial(ComerFichaInv,boton.getcassillaAnt1(),boton,1))


    if  boton.getcassillaAnt2() is not None  and boton.getcassillaAnt2().getColor()is not None and boton.getcassillaAnt1().getColor() != boton.getColor() and boton.getcassillaAnt2().getcassillaAnt2()is not None and  boton.getcassillaAnt2().getcassillaAnt2().getColor()== None    :
         
        if boton.getColor()=="Blancas" :
            boton.getcassillaAnt2().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt2(),boton,2))
        else:
            boton.getcassillaAnt2().getboton().config(command=partial(ComerFichaInv,boton.getcassillaAnt2(),boton,2))
       
    
    


def ComerFicha(boton,anterior,num):
    global turno
    if anterior.getColor()=="Negras":
        
        if num==1:
            if boton.getcassilla1() is not None :
                
                if boton.getcassilla1().getColor()==None :
                   
                    var=boton.getcassilla1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassilla1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassilla1().setColor(var2)
                    
                    
                    boton.getboton().config(command=partial(Mover,boton))
                    turno=1
                    ComerMas(boton.getcassilla1())
                else :
                    
                    boton.getboton().config(command=partial(Mover,boton))
            else:
                
                boton.getboton().config(command=partial(Mover,boton))
            
        if num==2:
             
              if boton.getcassilla2() is not None :
                 
                 if boton.getcassilla2().getColor()==None :
                    
                     var=boton.getcassilla2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassilla2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassilla2().setColor(var2)
                     
                     
                     boton.getboton().config(command=partial(Mover,boton))
                     turno=1
                     ComerMas(boton.getcassilla2())
                 else :
                     
                     boton.getboton().config(command=partial(Mover,boton))
        else:
                 
            boton.getboton().config(command=partial(Mover,boton))
    if anterior.getColor()=="Blancas":
        
        if num==1:
            
            
            if boton.getcassillaAnt1() is not None :
                
                if boton.getcassillaAnt1().getColor()==None :
                   
                    var=boton.getcassillaAnt1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassillaAnt1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassillaAnt1().setColor(var2)
                    
                    
                    boton.getboton().config(command=partial(Mover,boton))
                    turno=2
                    ComerMas(boton.getcassillaAnt1())
                else :
                    
                    boton.getboton().config(command=partial(Mover,boton))
            else:
                
                boton.getboton().config(command=partial(Mover,boton))
            
        if num==2:
              
             
              if boton.getcassillaAnt2() is not None :
                 
                 if boton.getcassillaAnt2().getColor()==None :
                    
                     var=boton.getcassillaAnt2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassillaAnt2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassillaAnt2().setColor(var2)
                     
                     
                     boton.getboton().config(command=partial(Mover,boton))
                     turno=2
                     ComerMas(boton.getcassillaAnt2())
                 else :
                     
                     boton.getboton().config(command=partial(Mover,boton))
        else:
                 
            boton.getboton().config(command=partial(Mover,boton))
            
def ComerFichaInv(boton,anterior,num):
    
    if anterior.getColor()=="Blancas":
        
        if num==1:
            if boton.getcassilla1() is not None :
                
                if boton.getcassilla1().getColor()==None :
                   
                    var=boton.getcassilla1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassilla1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassilla1().setColor(var2)
                    
                    
                    boton.getboton().config(command=partial(Mover,boton))
                    
                    ComerMas(boton.getcassilla1())
                else :
                    
                    boton.getboton().config(command=partial(Mover,boton))
            else:
                
                boton.getboton().config(command=partial(Mover,boton))
            
        if num==2:
             
              if boton.getcassilla2() is not None :
                 
                 if boton.getcassilla2().getColor()==None :
                    
                     var=boton.getcassilla2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassilla2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassilla2().setColor(var2)
                     
                     
                     boton.getboton().config(command=partial(Mover,boton))
                     
                     ComerMas(boton.getcassilla2())
                 else :
                     
                     boton.getboton().config(command=partial(Mover,boton))
        else:
                 
            boton.getboton().config(command=partial(Mover,boton))
    if anterior.getColor()=="Negras":
        
        if num==1:
            if boton.getcassillaAnt1() is not None :
                
                if boton.getcassillaAnt1().getColor()==None :
                   
                    var=boton.getcassillaAnt1().getImagen()
                    
                    var2= anterior.getColor()
                    
                    boton.getcassillaAnt1().setImagen(anterior.getImagen())
                    
                    boton.setImagen(var)
                    
                    anterior.setImagen(var)

                    boton.setColor(None)
                    
                    anterior.setColor(None)
                    
                    boton.getcassillaAnt1().setColor(var2)
                    
                    
                    boton.getboton().config(command=partial(Mover,boton))
                    
                    ComerMas(boton.getcassillaAnt1())
                else :
                    
                    boton.getboton().config(command=partial(Mover,boton))
            else:
                
                boton.getboton().config(command=partial(Mover,boton))
            
        if num==2:
              
             
              if boton.getcassillaAnt2() is not None :
                 
                 if boton.getcassillaAnt2().getColor()==None :
                    
                     var=boton.getcassillaAnt2().getImagen()
                     
                     var2= anterior.getColor()
                     
                     boton.getcassillaAnt2().setImagen(anterior.getImagen())
                     
                     boton.setImagen(var)
                     
                     anterior.setImagen(var)

                     boton.setColor(None)
                     
                     anterior.setColor(None)
                     
                     boton.getcassillaAnt2().setColor(var2)
                     
                     
                     boton.getboton().config(command=partial(Mover,boton))
                     
                     ComerMas(boton.getcassillaAnt2())
                 else :
                     
                     boton.getboton().config(command=partial(Mover,boton))
        else:
                 
            boton.getboton().config(command=partial(Mover,boton))


def Salir():
    salir = tkinter.messagebox.askquestion(title="Salir",message="Deseas salir de el programa ")
    if salir=="yes" :
        root.destroy()
    
def Liciencia():
    tkinter.messagebox.showinfo(title="Creado",message="Julio Cesar Batista Torres")

def NuevaPartida():
    frame.pack_forget()
    VentanaDeJuego.pack()

def Volver():
    VentanaDeJuego.pack_forget()
    frame.pack()

def Mover(boton):
    global lista_botones
    global turno
    
    for i in lista_botones :
        i.getboton().config(command=partial(Mover,i))

    
    if boton.getColor()=="Negras"  :
 
                     
        if turno==1:
           return
       
        if boton.getcassilla1()==None and boton.getcassilla2()==None :
            
            return
        
        
        if boton.getcassilla2()==None:
            
            
            
            if boton.getcassilla1().getColor()=="Negras":
                
    
                return
            
            elif boton.getcassilla1().getColor()== None  :
                

                boton.getcassilla1().getboton().config(command=partial(Cambiar,boton.getcassilla1(),boton))
            
            elif boton.getcassilla1().getColor()=="Blancas" :
                
              if boton.getdireccionA()=="D":
                boton.getcassilla1().getboton().config(command=partial(ComerFicha,boton.getcassilla1(),boton,1))
              else:
                 boton.getcassilla1().getboton().config(command=partial(ComerFicha,boton.getcassilla1(),boton,2))
                
                
   
    
        elif  boton.getcassilla1().getColor()=="Negras" or boton.getcassilla2().getColor()== "Negras":
            
            if boton.getcassilla1().getColor()=="Negras" and boton.getcassilla2().getColor()=="Negras" :
               
                return
   
            elif boton.getcassilla1().getColor()=="Negras":
                if  boton.getcassilla2().getColor()=="Blancas":
                    boton.getcassilla2().getboton().config(command=partial(ComerFicha,boton.getcassilla2(),boton,2))
                    return
           
                boton.getcassilla2().getboton().config(command=partial(Cambiar,boton.getcassilla2(),boton))
            
            elif boton.getcassilla2().getColor()=="Negras":
                
                if boton.getcassilla1().getColor()=="Blancas" :
                    boton.getcassilla1().getboton().config(command=partial(ComerFicha,boton.getcassilla1(),boton,1))
                    return
  
                boton.getcassilla1().getboton().config(command=partial(Cambiar,boton.getcassilla1(),boton))
        
       
        elif boton.getcassilla1().getColor()=="Blancas" or boton.getcassilla2().getColor()=="Blancas" :
            
            
                
            if boton.getcassilla1().getColor()=="Blancas" and boton.getcassilla2().getColor()=="Blancas":
                    
                boton.getcassilla1().getboton().config(command=partial(ComerFicha,boton.getcassilla1(),boton,1))
                    
                boton.getcassilla2().getboton().config(command=partial(ComerFicha,boton.getcassilla2(),boton,2))
                
            elif boton.getcassilla1().getColor()=="Blancas":
                boton.getcassilla1().getboton().config(command=partial(ComerFicha,boton.getcassilla1(),boton,1))
                boton.getcassilla2().getboton().config(command=partial(Cambiar,boton.getcassilla2(),boton,boton.getcassilla1()))
                
            elif boton.getcassilla2().getColor()=="Blancas":
                boton.getcassilla2().getboton().config(command=partial(ComerFicha,boton.getcassilla2(),boton,2))
                boton.getcassilla1().getboton().config(command=partial(Cambiar,boton.getcassilla1(),boton,boton.getcassilla2()))
                
                
                
  
        else:
            
            boton.getcassilla1().getboton().config(command=partial(Cambiar,boton.getcassilla1(),boton,boton.getcassilla2()))
            boton.getcassilla2().getboton().config(command=partial(Cambiar,boton.getcassilla2(),boton,boton.getcassilla1()))
        
       
    
    if boton.getColor()=="Blancas"  :
        
        
        if turno==2:
           return
        
            
        if boton.getcassillaAnt1()==None and boton.getcassillaAnt2()==None :
            
            return
        
        
        if boton.getcassillaAnt2()==None:
            
            
            
            if boton.getcassillaAnt1().getColor()=="Blancas":
                
                return
            
            elif boton.getcassillaAnt1().getColor()== None  :

                boton.getcassillaAnt1().getboton().config(command=partial(Cambiar,boton.getcassillaAnt1(),boton))
            
            elif boton.getcassillaAnt1().getColor()=="Negras" :
               
                if boton.getdireccionA()=="D":
                    
                    boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,1))
                    
                else:
                   
                   boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,2))
                

        elif  boton.getcassillaAnt1().getColor()=="Blancas" or boton.getcassillaAnt2().getColor()== "Blancas":
            
            if boton.getcassillaAnt1().getColor()=="Blancas" and boton.getcassillaAnt2().getColor()=="Blancas" :
               
                return
   
            elif boton.getcassillaAnt1().getColor()=="Blancas":
                if  boton.getcassillaAnt2().getColor()=="Negras":
                    boton.getcassillaAnt2().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt2(),boton,2))
                    return
           
                boton.getcassillaAnt2().getboton().config(command=partial(Cambiar,boton.getcassillaAnt2(),boton))
            
            elif boton.getcassillaAnt2().getColor()=="Blancas":
                
                if boton.getcassillaAnt1().getColor()=="Negras" :
                    boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,1))
                    return
  
                boton.getcassillaAnt1().getboton().config(command=partial(Cambiar,boton.getcassillaAnt1(),boton))
        
       
        elif boton.getcassillaAnt1().getColor()=="Negras" or boton.getcassillaAnt2().getColor()=="Negras" :
            
            
                
            if boton.getcassillaAnt1().getColor()=="Negras" and boton.getcassillaAnt2().getColor()=="Negras":
                    
                boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,1))
                    
                boton.getcassillaAnt2().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt2(),boton,2))
                
            elif boton.getcassillaAnt1().getColor()=="Negras":
                
               
                if  boton.getcassillaAnt1().getdireccionA()=="I" :
                    
                    boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,2))
                
                else:
                   
                    boton.getcassillaAnt1().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt1(),boton,1))
               
                boton.getcassillaAnt2().getboton().config(command=partial(Cambiar,boton.getcassillaAnt2(),boton,boton.getcassillaAnt1()))
                
            elif boton.getcassillaAnt2().getColor()=="Negras":
                
                boton.getcassillaAnt2().getboton().config(command=partial(ComerFicha,boton.getcassillaAnt2(),boton,2))
                boton.getcassillaAnt1().getboton().config(command=partial(Cambiar,boton.getcassillaAnt1(),boton,boton.getcassillaAnt2()))
                
                
                
  
        else:
            
            boton.getcassillaAnt1().getboton().config(command=partial(Cambiar,boton.getcassillaAnt1(),boton,boton.getcassillaAnt2()))
            boton.getcassillaAnt2().getboton().config(command=partial(Cambiar,boton.getcassillaAnt2(),boton,boton.getcassillaAnt1()))
        
        

def Cambiar(*Arg):
    global turno
    if Arg[1].getColor()=="Negras":
        turno-=1
    if Arg[1].getColor()=="Blancas":
        turno+=1
    if len(Arg)==2:
        
        
        var=Arg[0].getImagen()
        Arg[0].setImagen(Arg[1].getImagen())
        Arg[1].setImagen(var)
        Arg[0].setColor(Arg[1].getColor())
        Arg[1].setColor(None)
        Arg[0].getboton().config(command=partial(Mover,Arg[0]))
      
                                 
    else:
       
        var=Arg[0].getImagen()
        Arg[0].setImagen(Arg[1].getImagen())
        Arg[1].setImagen(var)
        Arg[0].setColor(Arg[1].getColor())
        Arg[1].setColor(None)
        Arg[0].getboton().config(command=partial(Mover,Arg[0]))
        Arg[2].getboton().config(command=partial(Mover,Arg[2]))
        
        
    

root=Tk()
root.title("Damas")

root.resizable(False,False)

frame=Frame()
frame.pack(fill="both",expand="true")
frame.config(width=1300,height=700)



Portada=Image.open("dama3.jpg")
resize_portada = Portada.resize((1300,700))
imagen=ImageTk.PhotoImage(resize_portada)
label=Label(frame,image=imagen)

label.place(x=0,y=0)


boton=Button(frame,text="Empezar Partida",width=13,command=NuevaPartida)
boton.place(x=1000,y=100)

licencia=Button(frame,text="Creador",width=13,command=Liciencia)
licencia.place(x=1000,y=150)

Cerrar=Button(frame,text="Salir",width=13,command=Salir)
Cerrar.place(x=1000,y=200)


VentanaDeJuego=Frame()
VentanaDeJuego.pack(fill="both",expand="true")
VentanaDeJuego.config(width=1300,height=700,bg="blue")
VentanaDeJuego.pack_forget()



tablero_=Image.open("tablero.jfif")
redimensionar_tablero_=tablero_.resize((1300,700))
tablero=ImageTk.PhotoImage(redimensionar_tablero_)
label_tablero=Label(VentanaDeJuego,image=tablero)
label_tablero.place(x=0,y=0)

volver=Button(VentanaDeJuego,text="volver",width=13,command=Volver)
volver.place(x=1100,y=30)

# imagen de los botones 

imagen_boton=Image.open("Negro.png")
redimensionar_imagen_boton=imagen_boton.resize((500,500))
imagen__boton=ImageTk.PhotoImage((redimensionar_imagen_boton))


imagen_fichaN=Image.open("fichaNegra.jpg")
redimensionar_imagen_fichaN=imagen_fichaN.resize((100,100))
imagen__fichaN=ImageTk.PhotoImage((redimensionar_imagen_fichaN))

imagen_fichaB=Image.open("fichablanca.jpg")
redimensionar_imagen_fichaB=imagen_fichaB.resize((100,100))
imagen__fichaB=ImageTk.PhotoImage((redimensionar_imagen_fichaB))

#imagen_fichaB=reziset_mio("fichablanca.jpg",100,100)


#clasess

class Boton():
    def __init__(self,imagen,posicionX,posicionY):
        self.imagen=imagen
        self.boton=Button(VentanaDeJuego,text="Prueva",height=70,width=120,image=imagen,command=partial(Mover,self))
        self.boton.place(x=posicionX,y=posicionY)
        self.cassilla1=None
        self.cassilla2=None
        self.cassillaAnt1=None
        self.cassillaAnt2=None
        self.direccionA=None
       
        
        if imagen==imagen__fichaN :
            
            self.Color="Negras"
            
        elif imagen==imagen__fichaB :
            
            self.Color="Blancas"
            
        else :
            self.Color=None
            
    def getdireccionA(self):
        return self.direccionA
  
    
    def getboton(self):
        return self.boton
    
    def getcassillaAnt1(self):
        return self.cassillaAnt1
    
    
    def getcassillaAnt2(self):
        return self.cassillaAnt2
    
    
    def getImagen(self):
        return self.imagen
    
    def getcassilla1(self):
        return self.cassilla1
    
    def getcassilla2(self):
        return self.cassilla2
    
    def getColor(self):
        return self.Color
    
    def setImagen (self,var):
        self.imagen=var
        self.boton.config(image=var)
    
    def setcassilla1 (self,var):
        self.cassilla1=var
        
    def setcassilla2 (self,var):
        self.cassilla2=var
        
    def setColor (self,var):
        self.Color=var
        
    def setcassillaAnt1 (self,var):
        self.cassillaAnt1=var
    
    def setcassillaAnt2 (self,var):
        self.cassillaAnt2=var
        
    def setdireccionA(self,var):
         self.direccionA=var
         
    def setdireccionB(self,var):
         self.direccionB=var

#botones de fichas 
# Fila 1
cassilla1=Boton(imagen__fichaN, 260, 65)

cassilla2=Boton(imagen__fichaN, 525, 65)

cassilla3=Boton(imagen__fichaN, 790, 65)

cassilla4=Boton(imagen__fichaN, 1055, 65)

# Fila 2

cassilla5=Boton(imagen__fichaN, 130, 140)

cassilla6=Boton(imagen__fichaN, 395, 140)



cassilla7=Boton(imagen__fichaN, 660, 140)

cassilla8=Boton(imagen__fichaN, 925, 140)

#fila 3
cassilla9=Boton(imagen__fichaN, 260, 210)

cassilla10=Boton(imagen__fichaN, 525, 210)

cassilla11=Boton(imagen__fichaN, 790, 210)

cassilla12=Boton(imagen__fichaN, 1055, 210)


# fila 4

cassilla13=Boton(imagen__boton, 130, 280)

cassilla14=Boton(imagen__boton, 395, 280)


cassilla15=Boton(imagen__boton, 660, 280)
                 
cassilla16=Boton(imagen__boton, 925, 280)


# fila 5

cassilla17=Boton(imagen__boton, 260, 350)

cassilla18=Boton(imagen__boton, 525, 350)

cassilla19=Boton(imagen__boton, 790, 350)

cassilla20=Boton(imagen__boton, 1055, 350)

# fila 6

cassilla21=Boton(imagen__fichaB, 130, 420)

cassilla22=Boton(imagen__fichaB, 395, 420)

cassilla23=Boton(imagen__fichaB, 660, 420)


cassilla24=Boton(imagen__fichaB, 925, 420)

# fila 7

cassilla25=Boton(imagen__fichaB, 260, 490)

cassilla26=Boton(imagen__fichaB, 525, 490)

cassilla27=Boton(imagen__fichaB, 790, 490)

cassilla28=Boton(imagen__fichaB, 1055, 490)


# fila 8

cassilla29=Boton(imagen__fichaB, 130, 565)

cassilla30=Boton(imagen__fichaB, 395, 565)

cassilla31=Boton(imagen__fichaB, 660, 565)

cassilla32=Boton(imagen__fichaB, 925, 565)
lista_botones=[]
lista_botones.append(cassilla1)
lista_botones.append(cassilla2)
lista_botones.append(cassilla3)
lista_botones.append(cassilla4)
lista_botones.append(cassilla5)
lista_botones.append(cassilla6)
lista_botones.append(cassilla7)
lista_botones.append(cassilla8)
lista_botones.append(cassilla9)
lista_botones.append(cassilla10)
lista_botones.append(cassilla11)
lista_botones.append(cassilla12)
lista_botones.append(cassilla13)
lista_botones.append(cassilla14)
lista_botones.append(cassilla15)
lista_botones.append(cassilla16)
lista_botones.append(cassilla17)
lista_botones.append(cassilla18)
lista_botones.append(cassilla9)
lista_botones.append(cassilla20)
lista_botones.append(cassilla21)
lista_botones.append(cassilla22)
lista_botones.append(cassilla23)
lista_botones.append(cassilla24)
lista_botones.append(cassilla25)
lista_botones.append(cassilla26)
lista_botones.append(cassilla27)
lista_botones.append(cassilla28)
lista_botones.append(cassilla29)
lista_botones.append(cassilla30)
lista_botones.append(cassilla31)
lista_botones.append(cassilla32)

#enlazar casillas

# fila1
cassilla1.setcassilla1(cassilla5)
cassilla1.setcassilla2(cassilla6)

cassilla2.setcassilla1(cassilla6)
cassilla2.setcassilla2(cassilla7)

cassilla3.setcassilla1(cassilla7)
cassilla3.setcassilla2(cassilla8)

cassilla4.setcassilla1(cassilla8)
cassilla4.setdireccionA("D")


#fila2
cassilla5.setcassilla1(cassilla9)
cassilla5.setcassillaAnt1(cassilla1)
cassilla4.setdireccionA("I")

cassilla6.setcassilla1(cassilla9)
cassilla6.setcassilla2(cassilla10)
cassilla6.setcassillaAnt1(cassilla1)
cassilla6.setcassillaAnt2(cassilla2)


cassilla7.setcassilla1(cassilla10)
cassilla7.setcassilla2(cassilla11)
cassilla7.setcassillaAnt1(cassilla2)
cassilla7.setcassillaAnt2(cassilla3)

cassilla8.setcassilla1(cassilla11)
cassilla8.setcassilla2(cassilla12)
cassilla8.setcassillaAnt1(cassilla3)
cassilla8.setcassillaAnt2(cassilla4)

# fila 3

cassilla9.setcassilla1(cassilla13)
cassilla9.setcassilla2(cassilla14)
cassilla9.setcassillaAnt1(cassilla5)
cassilla9.setcassillaAnt2(cassilla6)

cassilla10.setcassilla1(cassilla14)
cassilla10.setcassilla2(cassilla15)
cassilla10.setcassillaAnt1(cassilla6)
cassilla10.setcassillaAnt2(cassilla7)

cassilla11.setcassilla1(cassilla15)
cassilla11.setcassilla2(cassilla16)
cassilla11.setcassillaAnt1(cassilla7)
cassilla11.setcassillaAnt2(cassilla8)

cassilla12.setcassilla1(cassilla16)
cassilla12.setcassillaAnt1(cassilla8)
cassilla12.setdireccionA("D")



# fila4

cassilla13.setcassilla1(cassilla17)
cassilla13.setcassillaAnt1(cassilla9)
cassilla13.setdireccionA("I")



cassilla14.setcassilla1(cassilla17)
cassilla14.setcassilla2(cassilla18)
cassilla14.setcassillaAnt1(cassilla9)
cassilla14.setcassillaAnt2(cassilla10)


cassilla15.setcassilla1(cassilla18)
cassilla15.setcassilla2(cassilla19)
cassilla15.setcassillaAnt1(cassilla10)
cassilla15.setcassillaAnt2(cassilla11)


cassilla16.setcassilla1(cassilla19)
cassilla16.setcassilla2(cassilla20)
cassilla16.setcassillaAnt1(cassilla11)
cassilla16.setcassillaAnt2(cassilla12)


#Fila 5

cassilla17.setcassilla1(cassilla21)
cassilla17.setcassilla2(cassilla22)
cassilla17.setcassillaAnt1(cassilla13)
cassilla17.setcassillaAnt2(cassilla14)


cassilla18.setcassilla1(cassilla22)
cassilla18.setcassilla2(cassilla23)
cassilla18.setcassillaAnt1(cassilla14)
cassilla18.setcassillaAnt2(cassilla15)


cassilla19.setcassilla1(cassilla23)
cassilla19.setcassilla2(cassilla24)
cassilla19.setcassillaAnt1(cassilla15)
cassilla19.setcassillaAnt2(cassilla16)


cassilla20.setcassilla1(cassilla24)
cassilla20.setcassillaAnt1(cassilla16)
cassilla20.setdireccionA("D")




#  Fila 6
cassilla21.setcassilla1(cassilla25)
cassilla21.setcassillaAnt1(cassilla17)
cassilla21.setdireccionA("I")




cassilla22.setcassilla1(cassilla25)
cassilla22.setcassilla2(cassilla26)
cassilla22.setcassillaAnt1(cassilla17)
cassilla22.setcassillaAnt2(cassilla18)


cassilla23.setcassilla1(cassilla26)
cassilla23.setcassilla2(cassilla27)
cassilla23.setcassillaAnt1(cassilla18)
cassilla23.setcassillaAnt2(cassilla19)


cassilla24.setcassilla1(cassilla27)
cassilla24.setcassilla2(cassilla28)
cassilla24.setcassillaAnt1(cassilla19)
cassilla24.setcassillaAnt2(cassilla20)




# fila 7

cassilla25.setcassilla1(cassilla29)
cassilla25.setcassilla2(cassilla30)
cassilla25.setcassillaAnt1(cassilla21)
cassilla25.setcassillaAnt2(cassilla22)


cassilla26.setcassilla1(cassilla30)
cassilla26.setcassilla2(cassilla31)
cassilla26.setcassillaAnt1(cassilla22)
cassilla26.setcassillaAnt2(cassilla23)


cassilla27.setcassilla1(cassilla31)
cassilla27.setcassilla2(cassilla32)
cassilla27.setcassillaAnt1(cassilla23)
cassilla27.setcassillaAnt2(cassilla24)


cassilla28.setcassilla1(cassilla32)
cassilla28.setcassillaAnt1(cassilla24)
cassilla28.setdireccionA("D")


#fila 8

cassilla29.setcassillaAnt1(cassilla25)
cassilla29.setdireccionA("I")

cassilla30.setcassillaAnt1(cassilla25)
cassilla30.setcassillaAnt2(cassilla26)

cassilla31.setcassillaAnt1(cassilla26)
cassilla31.setcassillaAnt2(cassilla27)

cassilla32.setcassillaAnt1(cassilla27)
cassilla32.setcassillaAnt2(cassilla28)


root.mainloop()