class FIFOService:
    """Fila (FIFO) de pedidos."""

    def __init__(self, queue : list | None = None ):
        self.queue = queue if queue is not None else []

    def enqueue(self, order):
        self.queue.append(order)

    def dequeue(self):
        """Remove e retorna o pedido mais antigo da fila."""
        if self.is_empty():
            raise IndexError('Não há pedidos na fila.')
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError('Não há pedidos na fila.')
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def print_queue(self):
        if self.is_empty():
            print('Não há pedidos na fila no momento.')
            return
        for item in self.queue:
            item.print_order()
            print('-' * 30)

    def print_item(self, in_id):
        """Busca e imprime um pedido pelo ID."""
        for item in self.queue:
            if item.order.get('id') == in_id:
                item.print_order()
                return True
        print(f'Nenhum pedido encontrado com o número {in_id}')
        return False

    def delete_item(self, id_pedido) -> bool:
        """Remove da fila o pedido com o ID informado."""
        len_before = len(self.queue)
        self.queue = [item for item in self.queue if item.order['id'] != id_pedido]
        return len(self.queue) < len_before