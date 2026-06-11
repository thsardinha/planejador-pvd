# Contratos do Motor de Planejamento

## Objetivo

Definir os objetos de entrada e saída do motor de planejamento.

---

# Objeto SKU

Entrada:

```json
{
  "id": 1,
  "codigo": "8262133PVPF",
  "revestimento": "PVDF",
  "origem_material": "MDF",
  "minutagem": 6.38
}
```

---

# Objeto ItemPlanoMensal

```json
{
  "sku_id": 1,
  "quantidade": 8511
}
```

---

# Objeto SaldoSKU

Representa o saldo restante durante a execução.

```json
{
  "sku_id": 1,
  "saldo": 8511
}
```

---

# Objeto Familia

```json
{
  "familia": "PVDF_MDF",
  "skus": []
}
```

---

# Objeto ItemCarga

```json
{
  "sku_id": 1,
  "codigo": "8262133PVPF",
  "quantidade": 20,
  "minutagem": 127.6
}
```

---

# Objeto Carga

```json
{
  "familia": "PVDF_MDF",
  "quantidade_total": 50,
  "minutagem_total": 325.4,
  "itens": []
}
```

---

# Entrada do Gerador de Cargas

Lista de SKUs

Lista de saldos

---

# Saída do Gerador de Cargas

Lista de Cargas

---

# Regras

O gerador não grava banco.

O gerador não consulta SAP.

O gerador apenas recebe dados e devolve cargas.

---

# Responsabilidades

agrupador_familias.py

Recebe SKUs

Agrupa por família

---

gerador_cargas.py

Recebe famílias

Gera cargas

---

validador_cargas.py

Valida:

Família

Capacidade

Quantidade

Minutagem

```
```
