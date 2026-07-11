from classes import FIFOService
from classes import Order
from classes import Status

class Menu:
    def __init__(self, global_id : int = 0):
        self.global_id = global_id

    def loop_menu(self):
        fifo_service = FIFOService.FIFOService()

        while True:
            self.print_main_menu()
            option = input('Escolha a opção desejada: ').strip()
            print()

            try:
                match option:
                    case '1':
                        """Cria um pedido e o adiciona a fila"""
                        self.global_id += 1
                        new_order = Order.Order()
                        new_order.set_order(self.global_id)
                        fifo_service.enqueue(new_order)
                        print('Pedido registrado com sucesso!\n')

                    case '2':
                        """Printa a lista de pedidos"""
                        fifo_service.print_queue()

                    case '3':
                        """Consulta um pedido"""
                        id_pedido = self._read_int('Nº do pedido: ')
                        if id_pedido is not None:
                            fifo_service.print_item(id_pedido)

                    case '4':
                        """Cancela um pedido"""
                        id_pedido = self._read_int('Nº do pedido: ')
                        if id_pedido is None:
                            continue

                        founded_order = self._find_order(fifo_service, id_pedido)
                        if founded_order is None:
                            print(f'Nenhum pedido encontrado com o número {id_pedido}.')
                        else:
                            founded_order.set_status(id_pedido, Status.Status.CANCELADO)
                            fifo_service.delete_item(id_pedido)
                            print(f'Pedido {id_pedido} cancelado com sucesso!')

                    case '5':
                        """Finaliza um pedido (o mais antigo da fila)"""
                        if fifo_service.is_empty():
                            print('Não há pedidos na fila para finalizar.')
                        else:
                            finalized_order = fifo_service.dequeue()
                            finalized_order.set_status(
                                finalized_order.order.get('id'),
                                Status.Status.FINALIZADO,
                            )
                            print(
                                f"Pedido {finalized_order.order.get('id')} finalizado com sucesso!"
                            )

                    case '6':
                        print('Finalizando...')
                        break

                    case _:
                        print('Opção invalida! Tente novamente!')
                        continue
            except Exception as e:
                print(f'Ocorreu um erro inesperado ao processar a opção: {e}')

            print()

    @staticmethod
    def _read_int(prompt: str):
        """Lê um inteiro do usuário com tratamento de erro.

        Retorna None (em vez de lançar exceção) se o usuário digitar algo
        que não seja um número inteiro válido.
        """
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print('Valor inválido: digite um número inteiro.')
            return None

    @staticmethod
    def _find_order(fifo_service, id_pedido):
        """Procura, dentro da fila, o pedido com o ID informado."""
        for item in fifo_service.queue:
            if item.order.get('id') == id_pedido:
                return item
        return None

    @staticmethod
    def print_main_menu():
        '''Printa na saída do console o menu principal.'''
        print('####### Menu Principal #######')
        print('1 - Fazer pedido')
        print('2 - Ver lista de pedidos)')
        print('3 - Consultar um pedido')
        print('4 - Cancelar pedido')
        print('5 - Finalizar pedido')
        print('6 - Sair')
        print('\n')