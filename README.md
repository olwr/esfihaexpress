# Esfiha Express — Fila de Pedidos (FIFO)

**By: Oliver Benites [5058029]**

Mini-projeto acadêmico que demonstra a estrutura de dados **Fila (Queue / FIFO — First In, First Out)** aplicada a um contexto de sistema de pedidos de uma esfiharia fictícia.

O primeiro pedido registrado é o primeiro a ser finalizado, exatamente como uma fila de atendimento real.

## Estrutura de dados escolhida: Fila (FIFO)

A fila é implementada em `classes/FIFOService.py`, encapsulando uma `list` do Python e expondo apenas as operações típicas de uma fila:

| Operação          | Método           | Descrição                                              |
| ----------------- | ---------------- | ------------------------------------------------------ |
| Inserir           | `enqueue(order)` | Adiciona um pedido ao final da fila                    |
| Remover           | `dequeue()`      | Remove e retorna o pedido mais antigo (início da fila) |
| Consultar próximo | `peek()`         | Retorna o pedido mais antigo sem removê-lo             |
| Verificar vazia   | `is_empty()`     | Indica se a fila está vazia                            |

## Requisitos do trabalho e onde cada um foi implementado

| Requisito                              | Implementação                                                |
| -------------------------------------- | ------------------------------------------------------------ |
| Estrutura de dados (fila)              | `FIFOService` (`classes/FIFOService.py`), usada em `Menu.loop_menu()` |
| Função de **ordenação**, usada na main | `FIFOService.sort_queue(by='id')` — ordena os pedidos da fila pelo campo informado (padrão: ID do pedido). É chamada automaticamente sempre que o usuário escolhe a opção **"2 — Ver lista de pedidos"** no menu |
| Função de **busca**, usada na main     | `FIFOService.print_item(id)` — percorre a fila procurando um pedido por ID, usada na opção **"3 — Consultar um pedido"**. A mesma lógica de busca (`Menu._find_order`) também localiza o pedido correto para as opções **"4 — Cancelar pedido"** |

> Este projeto não possui interface gráfica (não é obrigatório pelo enunciado) — a demonstração acontece via menu interativo no terminal, que serve como "função main" do fluxo pedido pelo trabalho: **inserir pedidos → ordenar a lista → buscar/consultar um pedido específico**.

## Fluxo de demonstração

1. **Inserir elementos na fila** — opção `1`, cria um novo pedido (nome do cliente + um ou mais sabores do cardápio) e o adiciona ao final da fila (`enqueue`).
2. **Ordenar a fila** — opção `2`, ordena os pedidos por ID (`sort_queue`) e imprime a fila já ordenada.
3. **Buscar um elemento** — opção `3`, busca e exibe um pedido específico pelo número do pedido (`print_item`).
4. **Cancelar um pedido** — opção `4`, busca o pedido pelo ID, marca como `CANCELADO` e o remove da fila.
5. **Finalizar um pedido** — opção `5`, remove o pedido mais antigo da fila (`dequeue`) e marca como `FINALIZADO`.
6. **Sair** — opção `6`, encerra o programa.

## Cancelar uma operação em andamento

Em qualquer prompt que peça uma entrada (nome, sabor, quantidade, ID de pedido, etc.), digitar **`0`** interrompe a operação atual e volta imediatamente ao menu principal — útil, por exemplo, se o usuário escolheu a opção errada no menu (digitou `4` querendo `3`) ou desistiu no meio da criação de um pedido. Nenhum dado parcial é salvo quando isso acontece.

## Estrutura de arquivos

```
TrabalhoOliver/
├── main.py                     # Ponto de entrada do programa
├── classes/
│   ├── Menu.py                 # Menu interativo (laço principal / "main" do fluxo)
│   ├── FIFOService.py          # Estrutura de dados: fila FIFO + ordenação + busca
│   ├── Order.py                # Representa um pedido individual
│   ├── EsfihariaMenu.py        # Cardápio de sabores disponíveis
│   └── Status.py                # Enum com os status possíveis de um pedido
└── README.md
```

## Como executar

Requer Python 3.10+ (uso de `match/case` e union types `X | Y`).

```bash
python main.py
```

O programa exibirá um menu no terminal; basta seguir as instruções digitando o número da opção desejada.

## Exemplo de uso

```
1 - Fazer pedido            → cria pedidos #1, #2, #3
2 - Ver lista de pedidos    → lista ordenada por ID (sort_queue)
3 - Consultar um pedido     → busca pedido #2 pelo ID (print_item)
5 - Finalizar pedido        → remove o pedido mais antigo da fila (dequeue)
6 - Sair
```

## Tratamento de erros

O programa foi construído para não interromper a execução por exceções não tratadas: entradas inválidas (texto onde se espera número, sabor inexistente no cardápio, quantidade não positiva, ID de pedido inexistente, fila vazia ao tentar finalizar) são todas tratadas com mensagens explicativas, permitindo que o usuário tente novamente sem que o programa quebre.