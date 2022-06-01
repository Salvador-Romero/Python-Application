from smtplib import SMTP

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from Mensaje import Mensaje

import json
import io

class Mandar_Correo(object):

	def __init__(self):

		self.destinatarios = []
		self.parametros = json.load(open("config.json", "r"))


	def enviarCorreo(self,mensaje):
		smtp = SMTP(self.parametros["smtp"])
		smtp.login(self.parametros["mail"], self.parametros["password"])

		correo = MIMEMultipart()
		
		correo['Subject'] = mensaje.subject
		correo['From'] = self.parametros["mail"]
		
		texto = MIMEText(mensaje.getMensaje(), 'html')
		correo.attach(texto)

		for destino in self.destinatarios:
			print ("Enviando correo a ",destino)
			correo['To'] = destino
			smtp.sendmail(self.parametros["mail"], destino, correo.as_string())

		

		smtp.quit()    