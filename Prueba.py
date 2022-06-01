from Mandar_Correo import Mandar_Correo
from Mensaje import Mensaje

msg = Mensaje()
#Agregamos contenido al mensaje en formato html
msg.agregarContenido("<p>Agregamos un detalle al mensaje</p>")

#Agregamos una imagen al mensaje
msg.agregarContenido("<p><img src=\"http://www.gsampallo.com/blog/wp-content/uploads/2019/07/logo-gs_logo-fondo-negro.jpg\" height=\"15%\"	width=\"15%\"></p>")

mMail = Mandar_Correo()

mMail.destinatarios.append("rolfeador@gmail.com")


mMail.enviarCorreo(msg)