from classes import Status as StatusModule
from classes import EsfihariaMenu as EsfihariaMenuModule

class Order:
    """Representa um único pedido."""

    def __init__(self, order : dict | None = None):
        self.order = order if order is not None else {}

    def print_order(self):
        """Printa um único pedido"""
        itens = self.order.get('items', [])
        total = sum(item.get('price', 0) for item in itens)

        print(f"Nº do Pedido: {self.order.get('id', '-')}")
        print(f"Nome do cliente: {self.order.get('name', '-')}")
        if itens:
            print('Itens:')
            for item in itens:
                print(
                    f"  - {item['quantity']}x {item['flavor'].title()} "
                    f"(R$ {item['price']:.2f})"
                )
            print(f"Total: R$ {total:.2f}")
        else:
            print('Itens: nenhum item registrado')
        print(f"Status: {self.order.get('status', '-')}")

    def set_status(self, status : "StatusModule.Status"):
        """Seta o status do pedido"""
        self.order['status'] = status.name # ex: 'status': FINALIZADO

    def set_order(self, in_id):
        """Coleta os dados de um novo pedido interativamente, com validação
        de entrada em cada etapa para nunca derrubar o programa por causa
        de uma digitação inválida.
        """
        print(f'Número do Pedido: {in_id}')
        self.order['id'] = in_id

        name = input('Insira o nome do cliente: ').strip()
        while not name:
            name = input('Nome não pode ser vazio. Insira o nome do cliente: ').strip()
        self.order['name'] = name

        self.order['items'] = []
        esfiharia_menu = EsfihariaMenuModule.EsfihaMenu()

        while True:
            esfiharia_menu.print_menu()
            flavor = input('Insira o sabor: ').strip().lower()

            if not esfiharia_menu.in_menu(flavor):
                print('Sabor não encontrado no cardápio. Tente novamente.')
                continue

            quantity = None
            while quantity is None:
                raw_quantity = input('Insira a quantidade: ').strip()
                try:
                    parsed = int(raw_quantity)
                    if parsed < 0:
                        print('A quantidade deve ser um número inteiro maior que zero.')
                        continue
                    quantity = parsed
                except ValueError:
                    print('Quantidade inválida. Digite um número inteiro.')

            price = esfiharia_menu.get_price(flavor) * quantity
            self.order['items'].append({
                'flavor' : flavor,
                'quantity' : quantity,
                'price' : price,
            })

            more = input('Deseja pedir mais? [S/N]').strip().lower()

            if more != 's':
                break

        self.order['status'] = StatusModule.Status.EM_ANDAMENTO.name