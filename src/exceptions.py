class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ResponseError(Exception):
    """Вызывается, когда response пустой."""
    pass


class ParserCompareStatus(Exception):
    """Вызывается, когда парсер нашел несоответсвие статусов."""
    pass


class ParserErrorPage(Exception):
    """Вызывается, когда возникла ошибка загрузки страницы."""
    pass
