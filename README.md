Para poder compilar la aplicacion solo es neceserio ejecutar

docker build -t simple-app .  

Posterior ejecutamos

docker run -it -p 8000:8000 -v %cmd%/usr/src/app simple-app  

Lo que nos ejecutara el contenedor en el

http://localhost:8000/

___________________________________________________________________

Para agregar o quitar transacciones solo es cuestion de agregarlos de la siguiente
forma

id,mm/dd,(+ or -)amount

En el archivo config.json podrán cambiar los valores de la conexión
de correo

Salvador Romero Hdez