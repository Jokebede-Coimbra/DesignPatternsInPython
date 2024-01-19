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

## 3. Singleton
- O Singleton é um padrão de projeto de criação que garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a essa instância.

**Principais Características:**
  
- **Única Instância:** O Singleton garante que uma classe tenha apenas uma instância e fornece um método global para acessar essa instância.

- **Acesso Global:** O Singleton fornece um ponto de acesso global à instância única, permitindo que outras classes obtenham referência a essa instância.

- **Controle de Acesso:** Geralmente, o Singleton controla o acesso à sua única instância, garantindo que ela seja criada apenas quando necessário.

## 4. Decorator
- Os decoradores em Python são uma maneira poderosa de modificar ou estender o comportamento de funções ou métodos sem alterar diretamente seu código. Eles são aplicados usando o símbolo @ seguido do nome do decorador acima da definição da função.

## 5. Observer
- Observer é um padrão comportamental que define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente. Este padrão é comumente usado para implementar sistemas de eventos e listeners.

## 6. Facade
- O padrão de projeto Facade é um padrão estrutural que fornece uma interface simplificada para um conjunto mais amplo e complexo de interfaces em um subsistema, tornando mais fácil para os clientes (ou outras partes do sistema) interagirem com esse subsistema.

**Principais Características:**

- **Simplicidade de Interface:** A Facade fornece uma interface única e simplificada que esconde a complexidade do subsistema subjacente.

- **Encapsulamento:** O padrão promove o encapsulamento, isolando os detalhes internos do subsistema e fornecendo uma interface mais amigável.

- **Desacoplamento:** Facade reduz a dependência entre o cliente e as classes do subsistema, permitindo que o cliente interaja apenas com a Facade.