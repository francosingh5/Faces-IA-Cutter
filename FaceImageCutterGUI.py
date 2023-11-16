from tkinter import *
from tkinter import filedialog
import tkinter
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np
import imutils


def recortar(count):
    cv2.imwrite(path + '/' + '{}.jpg'.format(count.get()), face)
    print("imagen guardada en: " + path)
    count.set(count.get() + 1)



def seleccionar_carpeta():
    
    global path
    path = filedialog.askdirectory()
    print(path)
    btnCV["state"] = NORMAL
    


def elegir_imagen():
    path_image = filedialog.askopenfilename(filetypes = [("image", ".jpg"), ("image", ".jpeg"), ("image", ".png")])
    if len(path_image) > 0 :
        
        global image
        global imagecpy
        
        #leer la imagen de entrada
        image = cv2.imread(path_image)
        imagecpy = image.copy()
        
        image = imutils.resize(image, height=380)
        
        #visualizar la img de entrada en la GUI
        imageToShow = imutils.resize(image, width=500)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)
        
        #label imagen de entrada
        lblImputImage.configure(image=img)
        lblImputImage.image = img
        
        btnFolder["state"] = NORMAL
             

def detectar_rostros():
    global count
    count = 1
    scale = 50

    var = tkinter.IntVar()
    var.set(1)
    
    global face
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    imageAux = imagecpy.copy()
    gray = cv2.cvtColor(imagecpy, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        
        cv2.rectangle(imagecpy, (x-scale, y-scale), (x+w+scale, y+h+scale), (0, 255, 0), 5)
        unitFace = imageAux[y-scale:y+h+scale , x-scale:x+w+scale]
        face = unitFace
    
        #visualizar la img de entrada en la GUI
        imageToShow = imutils.resize(imagecpy, width=500)
        imageToShow =cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)
        
        #visualizar la img de SALIDA CORTADA en la GUI
        imageToShow2 = imutils.resize(unitFace, width=200)
        imageToShow2 =cv2.cvtColor(imageToShow2, cv2.COLOR_BGR2RGB)
        im2 = Image.fromarray(imageToShow2)
        img2 = ImageTk.PhotoImage(image=im2)
        
        #label imagen de entrada
        lblOutputImage.configure(image=img)
        lblOutputImage.image = img
        
        #label imagen de salida
        lblOutputCutImage.configure(image=img2)
        lblOutputCutImage.image = img2

        """
        btnNext = Button(root, text="Siguiente", width=25, command)
        btnNext.grid(column=1, row=4, padx=5, pady=5)
        """

        btnCrop = Button(root, text="Recortar", width=25, command=lambda: recortar(var))
        btnCrop.grid(column=2, row=3, padx=5, pady=5)

        btnCrop.wait_variable(var)



        
        
    btnCrop["state"] = NORMAL
    #btnNext["state"] = NORMAL


image = None

#ventena principal
root = Tk()

#label donde se presentara la imagen de entrada
lblImputImage = Label(root)
lblImputImage.grid(column=0, row=2, columnspan=2)

#label donde se presentara la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column=0, row=2, columnspan=2)

#label donde se presentara la imagen a cortar
lblOutputCutImage = Label(root)
lblOutputCutImage.grid(column=2, row=2)

#boton de ingreso de imagen

btnFile = Button(root, text="Elegir Imagen", width=25, command=elegir_imagen)
btnFile.grid(column=0, row=0, columnspan=2)

btnFolder = Button(root, text="Seleccionar carpeta", width=25, command=seleccionar_carpeta)
btnFolder.grid(column=0, row=3)

btnCV = Button(root, text="Buscar Rostros", width=25, command=detectar_rostros)
btnCV.grid(column=1, row=3)

btnFolder["state"] = DISABLED
btnCV["state"] = DISABLED

root.mainloop()
