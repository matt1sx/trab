from abc import ABC, abstractmethod

class Ligar(ABC):
    def audio(self):
        pass

class Texto(ABC):
    @abstractmethod
    def msg_texto(self):
        pass

class Camera(ABC):
    @abstractmethod
    def foto (self):
        pass

class iPhone(Ligar, Texto, Camera):
    def audio(self):
    # implementação de audio
    
    def msg_texto(self):
    # implementação de texto
    
    def foto(self):
    # implementação de fotos

class Nokia(Ligar, Texto):
    def audio(self):
    # implementação de audio  
    
    def msg_texto(self):
    # implementação de texto

class Pager(Texto):
    def msg_texto(self):
    # implementação de texto
