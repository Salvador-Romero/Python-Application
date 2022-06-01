from fastapi import FastAPI
from LeerArchivo import get_correo
from Mandar_Correo import Mandar_Correo
from Mensaje import Mensaje

app = FastAPI()

@app.get("/")
def read_root():
    msg = Mensaje()
    msg.agregarContenido("<p> {0} </p>".format(get_correo()))
    mMail = Mandar_Correo()
    mMail.destinatarios.append("rolfeador@gmail.com")
    mMail.enviarCorreo(msg)

    return get_correo()
