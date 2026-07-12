from classes import Status as StatusModule
from classes import EsfihariaMenu as EsfihariaMenuModule
from classes import InputUtils as InputUtilsModule

class Order:
    """Representa um único pedido."""

    def __init__(self, order : dict | None = None):
        self.order : dict = order if order is not None else {}

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

    def set_status(self, status : StatusModule.Status):
        """Seta o status do pedido"""
        self.order['status'] = status.name # ex: 'status': FINALIZADO

    def set_order(self, in_id : int):
        """Coleta os dados de um novo pedido interativamente, com validação
        de entrada em cada etapa para nunca derrubar o programa devido a uma digitação inválida.

        A qualquer momento o usuário pode digitar '0' para cancelar a
        criação do pedido — isso levanta BackToMenu (ver InputUtils),
        que propaga para quem chamou este método (Menu.loop_menu), sem
        deixar o pedido parcialmente criado na fila.
        """
        print(f'Número do Pedido: {in_id}')
        self.order['id'] = in_id

        name = InputUtilsModule.read_text('Insira o nome do cliente')
        self.order['name'] = name.title()

        self.order['items'] = []
        esfiharia_menu = EsfihariaMenuModule.EsfihaMenu()

        while True:
            esfiharia_menu.print_menu()
            flavor = InputUtilsModule.read_text('Insira o sabor').lower()

            if not esfiharia_menu.in_menu(flavor):
                print('Sabor não encontrado no cardápio. Tente novamente.')
                continue

            quantity = InputUtilsModule.read_positive_int('Insira a quantidade')

            flavor_price = esfiharia_menu.get_price(flavor)
            if flavor_price is None:
                print('Sabor não encontrado no cardápio. Tente novamente.')
                continue

            price = flavor_price * quantity
            self.order['items'].append({
                'flavor' : flavor,
                'quantity' : quantity,
                'price' : price,
            })

            more = InputUtilsModule.read_text('Deseja pedir mais? [S/N]').lower()

            if more != 's':
                break

        self.order['status'] = StatusModule.Status.EM_ANDAMENTO.name