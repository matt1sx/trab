##ISP

class celular():
    def audio(self):
        raise NotImplementedError
    
    def texto(self):
        raise NotImplementedError
    
    def camera(self):
        raise NotImplementedError

class iPhone(celular):
    def audio(self):
        # implementação de audio
        
    def texto(self):
        # implementação de texto
        
    def camera(self):
        # implementação da camera
        
class Nokia(celular):
    def audio(self):
        # implementação de audio
    
    def texto(self):
        # implementação de texto
    
    def camera(self):
        raise NotImplementedError

