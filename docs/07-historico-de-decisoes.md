# DECISÃO 001

Data:
11/06/2026

Responsável:
Thiago Sardinha

Descrição:

Padronização dos módulos da aplicação utilizando nomes no plural para APIs, repositórios e serviços relacionados a entidades de domínio.

Exemplos:

maquinas.py
maquinas_repositorio.py
servico_maquinas.py

Objetivo:

Melhorar legibilidade e consistência do projeto.

# DECISÃO 002

Data:
11/06/2026

Responsável:
Thiago Sardinha

Descrição:

Definição inicial das regras do gerador de cargas.

1. Quando possível, as cargas deverão conter 2 ou mais SKUs.
2. Cargas com 1 SKU serão permitidas quando forem menos produtivas ou inevitáveis.
3. Famílias com apenas 1 SKU poderão gerar carga normalmente.
4. Sobras de saldo deverão ser redistribuídas sempre que possível.
5. Cada carga deverá respeitar o limite máximo de 50 peças.
6. A prioridade do algoritmo será ocupar a carga antes de maximizar variedade.

# DECISÃO 003

Data:
11/06/2026

Responsável:
Thiago Sardinha

Descrição:

A compatibilidade de carga será definida inicialmente pela combinação de revestimento e origem do material.

A capacidade de cada carga não será fixada de forma definitiva nesta fase, pois depende da validação da engenharia sobre a quantidade de peças por gancheira para cada produto.

Até a definição final, o sistema deverá permitir parametrização da capacidade.

# DECISÃO 004

Data:
11/06/2026

Responsável:
Thiago Sardinha

Descrição:

No diarizador, a prioridade será a ocupação das máquinas através da meta de cargas por dia.

A minutagem será utilizada como indicador de acompanhamento e não como restrição principal da programação.

Ordem de prioridade:

1. Meta de cargas por máquina
2. Minutagem diária