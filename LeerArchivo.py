import csv
from Mensaje import Mensaje

msg = Mensaje()

def Total_balance():
 count = 0
 with open('Datos-Bancarios.csv') as f:
   reader = csv.reader(f)
   for row in reader:
    count += int(row[2])
   return count

def Total_meses():
   listado = []
   
   counttotal = 0
   for i in range(12):
      
       with open('Datos-Bancarios.csv') as g:
           reader = csv.reader(g)
           counttotal = comparar(reader,i)
       listado.append(counttotal)  

   return listado
 
def Promedio_mes(valorbool):
    tmp = True
    tmp = valorbool
    listado = []
    counttotal = 0
    for i in range(12):
        with open('Datos-Bancarios.csv') as g:
           reader = csv.reader(g)
           if(tmp):
               counttotal = promedioplus(reader,i)
           else:
                counttotal = promediominus(reader,i)
        listado.append(counttotal)  

    return listado

def devolver_mes(mes):
    
  
    if(mes[1].isdigit()):
        mes = mes[0:1]
        
    else:
        mes = mes[0]
        

    return int(mes)

def comparar(reader,i):
    mes = 0
    count2= 0
    for row in reader:
           
           mes = devolver_mes(row[1])
           
           if(mes == i):
               count2 += 1
    return count2 

def promedioplus(reader,i):
    mes = 0
    countplus = 0
    count2= 0
    
    for row in reader:
           
           mes = devolver_mes(row[1])
           
           if(mes == i):
               if(int(row[2]) > 0):
                   print(row[2])
                   countplus += int(row[2])
               count2 += 1
    count = 0
    if(count2 > 0):
        count = countplus / count2
    return count      

def promediominus(reader,i):
    mes = 0
    countplus = 0
    count2= 0
    
    for row in reader:
           
           mes = devolver_mes(row[1])
           
           if(mes == i):
               if(int(row[2]) < 0):
                   print(row[2])
                   countplus += int(row[2])
               count2 += 1
    count = 0
    if(count2 != 0):
        count = countplus / count2
    return count           
    
def Nombre_Meses(i):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    return meses[i]


def get_correo():
    correo = ""
    correo = "Su balance total es {0} \n".format(Total_balance())
    count = 0
    lista = []
    lista = Total_meses()
    lista2 =[]
    lista2 = Promedio_mes(True)
    lista3 =[]
    lista3 = Promedio_mes(False)
    print(lista)
    for valor in lista:
        if(count > 0 and int(valor)>0):
            correo +="Numero de transacciones en {0} : {1} \n".format(Nombre_Meses(count-1),valor)
            correo += "Promedio cantidad de credito {0} \n".format(lista2[count])
            correo += "Promedio cantidad de debito {0} \n".format(lista3[count])
        count += 1

    return correo

def mensaje_final():
    msg.agregarContenido("<p> {0} </p>".format(get_correo()))
    


 
  
