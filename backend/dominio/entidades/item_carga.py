from dataclasses import dataclass


@dataclass
class ItemCarga:

    sku_id: int
    codigo: str
    quantidade: int
    minutagem_unitaria: float

    @property
    def minutagem_total(self) -> float:
        return self.quantidade * self.minutagem_unitaria