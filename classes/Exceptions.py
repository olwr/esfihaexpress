class BackToMenu(Exception):
    """Levantada quando o usuário decide interromper a operação atual
    (digitando o comando de cancelar) e voltar ao menu principal.
    """
    pass