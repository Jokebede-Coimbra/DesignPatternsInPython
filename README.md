# Design Patterns

## Introdução
Padrões de projeto são soluções típicas para problemas comuns em projeto de software. Eles são como plantas de obra pré-fabricadas que você pode customizar para resolver um problema de projeto recorrente em seu código.

## 1. Adapter
- O padrão Adapter é um padrão estrutural que permite a colaboração de classes que, de outra forma, não poderiam trabalhar juntas devido a interfaces incompatíveis. Ele atua como um intermediário que permite que objetos com interfaces incompatíveis se comuniquem entre si.

## 2. Strategy
- O padrão de projeto Strategy (Estratégia) é um padrão comportamental que define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Ele permite que o cliente escolha o algoritmo a ser utilizado dinamicamente, sem alterar a estrutura do cliente.

**Principais Componentes:**

- **Context (Contexto):** Mantém uma referência a uma estratégia e pode trocar essa estratégia dinamicamente. O contexto delega a execução da estratégia para o objeto estratégia.

- **Strategy (Estratégia):** Interface comum para todas as estratégias concretas. Geralmente, declara um método que representa o algoritmo que as classes concretas implementarão.

- **ConcreteStrategy (Estratégia Concreta):** Implementa o algoritmo definido na interface Strategy. Vários ConcreteStrategy podem existir para fornecer diferentes implementações de um mesmo comportamento.
