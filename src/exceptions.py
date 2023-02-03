class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ParserCompareStatus(Exception):
    """Вызывается, когда парсер нашел несоответсвие статусов."""


class ParserErrorPage(Exception):
    """Вызывается, когда возникла ошибка загрузки страницы."""
