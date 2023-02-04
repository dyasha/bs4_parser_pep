import logging

from requests import RequestException

from exceptions import ParserErrorPage, ParserFindTagException, ResponseError


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        if response is None:
            raise ResponseError()
        return response
    except RequestException:
        err_msg = f'Возникла ошибка при загрузке страницы {url}'
        raise ParserErrorPage(
            err_msg,
            logging.exception(
                err_msg,
                stack_info=True
            ))


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        raise ParserFindTagException(error_msg,
                                     logging.error(error_msg, stack_info=True))
    return searched_tag
