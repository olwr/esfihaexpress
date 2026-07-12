from classes.Exceptions import BackToMenu

CANCEL_KEYWORD = '0'

def read_text(prompt: str) -> str:
    """Lê uma string do usuário.

    Digitar '0' em qualquer momento cancela a operação atual e levanta
    BackToMenu, que deve ser tratada por quem chamou (normalmente o
    laço do menu principal) para voltar ao menu sem quebrar o programa.
    """
    while True:
        value = input(f"{prompt} (ou '0' para voltar ao menu): ").strip()
        if value == CANCEL_KEYWORD:
            raise BackToMenu()
        if value:
            return value
        print('Este campo não pode ficar vazio.')

def read_int(prompt: str) -> int:
    """Lê um número inteiro do usuário, com a mesma opção de cancelar via '0'."""
    while True:
        raw_value = read_text(prompt)
        try:
            return int(raw_value)
        except ValueError:
            print('Valor inválido: digite um número inteiro.')

def read_positive_int(prompt: str) -> int:
    """Lê um número inteiro maior que zero, com a opção de cancelar via '0'."""
    while True:
        value = read_int(prompt)
        if value <= 0:
            print('O valor deve ser um número inteiro maior que zero.')
            continue
        return value
