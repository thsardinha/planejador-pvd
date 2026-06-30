from dataclasses import dataclass


@dataclass
class Maquina:

    id: int

    nome: str

    meta_cargas_dia: int

    tempo_disponivel: float

    tempo_carga: float

    capacidade_pecas: int

    @property
    def capacidade_restante(self):

        return self.capacidade_pecas