from enum import Flag, auto


class CreditStatus(Flag):
    PRE_PROCESSAMENTO = auto()
    PRE_APROVADO = auto()
    PENDENTE = auto()
    AGUARDANDO_DOCUMENTOS = auto()
    EM_ANALISE_MANUAL = auto()
    EM_ANALISE_OPERACIONAL = auto()
    EM_ANALISE_DOCUMENTAL = auto()
    CONTRATADO = auto()
    LIBERADO = auto()
    REPROVADO = auto()
    EXPIRADO = auto()
