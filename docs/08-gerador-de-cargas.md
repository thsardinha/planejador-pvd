# Gerador de Cargas

## Objetivo

Transformar a demanda mensal enviada pelo PCP em cargas produtivas para a área PVD.

---

# Entradas

Plano Mensal

SKU

Quantidade

Dados Técnicos SAP

Revestimento

Origem Material

Minutagem

---

# Conceito de Família

Família é composta por:

Revestimento + Origem Material

Exemplo:

Revestimento = PVDF

Origem = MDF

Família:

PVDF_MDF

---

# Regras de Compatibilidade

Somente SKUs da mesma família podem compor a mesma carga.

---

# Capacidade da Carga

Capacidade máxima:

50 peças

Capacidade mínima:

Não definida.

---

# Prioridades do Algoritmo

Prioridade 1

Maximizar ocupação da carga.

Objetivo:

Aproximar a carga de 50 peças.

---

Prioridade 2

Maximizar variedade.

Quando possível:

2 ou mais SKUs na mesma carga.

---

# Exceções

Família contendo apenas um SKU:

Permitido gerar carga com SKU único.

---

# Tratamento de Sobras

Exemplo:

Saldo:

112 peças

Resultado esperado:

Carga 1 = 50

Carga 2 = 50

Carga 3 = 12

Posteriormente o sistema poderá redistribuir as sobras.

---

# Estratégia Inicial

Passo 1

Agrupar por família.

↓

Passo 2

Ordenar SKUs por saldo.

↓

Passo 3

Montar carga até 50 peças.

↓

Passo 4

Priorizar múltiplos SKUs.

↓

Passo 5

Gerar lista de cargas.

---

# Saída Esperada

Carga

Família

Quantidade Total

Minutagem Total

Itens da Carga

SKU

Quantidade

Minutagem

---

# Melhorias Futuras

Redistribuição automática de sobras.

Balanceamento avançado.

Otimização por minutagem.

Redução de setup.

Simulações de produtividade.
