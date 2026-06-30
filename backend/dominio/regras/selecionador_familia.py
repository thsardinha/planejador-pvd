from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FamiliaDisponivel:
    nome: str
    saldo_total: int


class SelecionadorFamilia:
    @staticmethod
    def selecionar(familias: List[FamiliaDisponivel], familia_anterior: Optional[str] = None) -> Optional[FamiliaDisponivel]:
        if not familias:
            return None

        ordenadas = sorted(familias, key=lambda f: f.saldo_total, reverse=True)

        for familia in ordenadas:
            if familia.saldo_total > 0 and familia.nome != familia_anterior:
                return familia

        for familia in ordenadas:
            if familia.saldo_total > 0:
                return familia

        return None