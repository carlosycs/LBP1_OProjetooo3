class Vinho:
    def __init__(self, id, vinho, gosto, nacionalidade):
        self.id = id
        self.vinho = vinho
        self.gosto = gosto
        self.nacionalidade = nacionalidade

vinhos=[]

novo_vinho = Vinho(1, "IdTorres", "Suave", "Brasileiro")
vinhos.append(novo_vinho)