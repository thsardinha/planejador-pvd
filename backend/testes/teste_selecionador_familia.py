from backend.dominio.regras.selecionador_familia import SelecionadorFamilia, FamiliaDisponivel


def executar():
    familias = [
        FamiliaDisponivel(nome="PVDF_MDF", saldo_total=120),
        FamiliaDisponivel(nome="BP_MDP", saldo_total=80),
        FamiliaDisponivel(nome="ACR_MDF", saldo_total=40),
    ]

    escolhida = SelecionadorFamilia.selecionar(familias, familia_anterior="PVDF_MDF")

    print(escolhida)


if __name__ == "__main__":
    executar()