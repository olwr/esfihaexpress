import unicodedata

def _normalize(text : str) -> str:
    """Remove acentos e caixa alta para tornar a comparação de sabores mais
        tolerante (ex.: 'camarao' deve encontrar 'Camarão')."""
    text = text.strip().lower()
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c)
    )

class EsfihaMenu:
    """Representa o cardápio da esfiharia."""

    menu : list[dict] = [
        {
            'Sabor': 'Frango',
            'Descrição': 'Frango desfiado temperado, queijo muçarela, catupiry e azeitona',
            'Preço': 13.00
        },
        {
            'Sabor': 'Queijo',
            'Descrição': 'Queijo muçarela, orégano e catupiry',
            'Preço': 13.00
        },
        {
            'Sabor': 'Camarão',
            'Descrição': 'Camarão temperado e queijo muçarela',
            'Preço': 15.00
        },
        {
            'Sabor': '3 queijos',
            'Descrição': 'Queijo muçarela, cheddar, gorgonzola e óregano',
            'Preço': 14.00
        },
        {
            'Sabor': 'Bacon e brócolis',
            'Descrição': 'Bacon, brócolis, queijo muçarela e cream cheese',
            'Preço': 14.00
        },
        {
            'Sabor': 'Calabresa',
            'Descrição': 'Calabresa triturada e queijo muçarela',
            'Preço': 13.00
        },
        {
            'Sabor': 'Carne de panela com cebola roxa',
            'Descrição': 'Carne de panela desfiada temperada, cebola roxa, queijo muçarela e cream cheese',
            'Preço': 15.00
        },
        {
            'Sabor': 'Alho e óleo',
            'Descrição': 'Queijo muçarela, alho, óregano e azeite',
            'Preço': 13.00
        },
        {
            'Sabor': 'Tomate Seco com gorgonzola',
            'Descrição': 'Tomate seco temperado, queijo muçarela, óregano e gorgonzola',
            'Preço': 15.00
        },
        {
            'Sabor': 'Cebola caramelizada',
            'Descrição': 'Cebola caramelizada e queijo muçarela',
            'Preço': 13.00
        }
    ]

    def __init__(self, menu : list[dict] | None = None):
        self.menu : list[dict] = menu if menu is not None else EsfihaMenu.menu

    def print_menu(self):
        if not self.menu:
            print('Cardápio vazio no momento.')
            return
        for item in self.menu:
            print(
                f"- {item['Sabor']} (R$ {item['Preço']:.2f}): {item['Descrição']}"
            )

    def in_menu(self, flavor : str) -> bool:
        """Verifica se um sabor existe no cardápio."""
        if not flavor:
            return False
        target = _normalize(flavor)

        for item in self.menu:
            if _normalize(item['Sabor']) == target:
                return True
        return False

    def get_price(self, flavor : str) -> float | int | None:
        """Retorna o preço de um sabor ou None se não existir."""
        if not flavor:
            return None
        target = _normalize(flavor)

        for item in self.menu:
            if _normalize(item['Sabor']) == target:
                return item['Preço']
        return None