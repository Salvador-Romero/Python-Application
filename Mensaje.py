class Mensaje(object):

    def __init__(self):

        self.subject = "Transacciones de su cuenta "

        self.head = "<html><h2><b> Datos </b></h2>"
        self.body = "<img src=\"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fstori-card&psig=AOvVaw2Fq78t9rdkxaD_rHNjEBXw&ust=1654151368695000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKCZ0pjQi_gCFQAAAAAdAAAAABAD\"><p> A continuacion se detallan los datos de su cuenta.</p>"
            

        

    def getMensaje(self):
        return self.head+self.body
    

    def agregarContenido(self,data):
        self.body = self.body + data