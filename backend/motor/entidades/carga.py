from dataclasses import dataclass, field

from backend.motor.entidades.item_carga import ItemCarga


@dataclass
class Carga:

    familia: str

    itens: list[ItemCarga] = field(default_factory=list)

    @property
    def quantidade_total(self) -> int:

        return sum(
            item.quantidade
            for item in self.itens
        )

    @property
    def minutagem_total(self) -> float:

        return sum(
            item.minutagem_total
            for item in self.itens
        )