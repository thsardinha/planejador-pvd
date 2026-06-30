# ADR 001 - Estrutura do Sistema

## Status
Aceito

## Data
11/06/2026

## Contexto
O projeto Sistema de Planejamento PVD precisa evoluir de uma estrutura inicial funcional para uma base arquitetural profissional, de fácil manutenção, testes e evolução futura.

## Decisão
Adotar uma arquitetura com separação clara entre:

- domínio
- aplicação
- infraestrutura
- api

O domínio conterá as regras de negócio e entidades.
A aplicação coordenará os casos de uso.
A infraestrutura tratará banco, integrações e persistência.
A API exporá os endpoints para consumo externo.

## Consequências
- Mais clareza na manutenção
- Melhor testabilidade
- Menor acoplamento
- Facilidade para evoluir integração SAP e frontend
- Maior chance de sustentabilidade do sistema a longo prazo

## Estrutura base aprovada

backend/
├── dominio/
├── aplicacao/
├── infraestrutura/
├── api/
├── testes/

docs/
├── 01-visao-geral.md
├── 02-regras-de-negocio.md
├── 03-modelo-de-dados.md
├── 04-arquitetura.md
├── 07-historico-de-decisoes.md
└── adr/
    └── 001-estrutura-do-sistema.md