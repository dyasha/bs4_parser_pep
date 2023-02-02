class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ParserCompareStatus(Exception):
    """Вызывается, когда парсер нашел несоответсвие статусов."""
