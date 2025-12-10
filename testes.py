# As funções não são testáveis, dependem de interações com usuário.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f"Nome da pessoa: {self.nome}"
    
isa = Pessoa("isab'")
print(isa) # A saída é: Nome da pessoa: isab'