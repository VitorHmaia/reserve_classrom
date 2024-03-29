from django.db import models

class ClassEntity:
    
    def __init__(self, nome, responsael, id) -> None:
        self.id = id
        self.nome = nome
        self.responsavel = responsael
        

        
    def __str__(self) -> str:
        return (f"Class <{self.temperature}>")
    
    def __getattribute__(self, __name: str) -> any:
        if (__name=='date'):
            return object.__getattribute__(self, __name).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return object.__getattribute__(self, __name)