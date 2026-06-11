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