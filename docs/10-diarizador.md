# Diarizador V1

## Objetivo

Distribuir as cargas geradas entre as máquinas e os dias de produção.

---

## Regra 001

A programação deverá respeitar a meta diária de cargas de cada máquina.

Fonte:

Tabela MAQUINA

Campo:

meta_cargas_dia

---

## Regra 002

A distribuição deverá seguir a ordem de geração das cargas.

Não haverá reordenação.

Não haverá priorização.

Não haverá otimização nesta versão.

---

## Regra 003

A sequência operacional será:

HC566

HC567

HC582

HC583

HC584

---

## Regra 004

Distribuição por rodada.

Exemplo:

1ª carga HC566

1ª carga HC567

1ª carga HC582

1ª carga HC583

1ª carga HC584

2ª carga HC566

2ª carga HC567

...

---

## Regra 005

Ao atingir a meta diária de todas as máquinas:

Avançar para o próximo dia.

---

## Regra 006

A minutagem não será utilizada como restrição de programação.

A minutagem será utilizada apenas como indicador.
