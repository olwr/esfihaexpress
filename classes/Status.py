from enum import Enum

class Status(Enum):
    EM_ANDAMENTO = 0
    FINALIZADO = 1
    CANCELADO = 2

    def __str__(self):
        return self.name