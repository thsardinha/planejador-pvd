from dataclasses import dataclass
from datetime import date


@dataclass
class Programacao:

    data_programacao: date

    maquina_id: int

    carga_id: int

    sequencia_carga: int