from pathlib import Path

PARSING_PEP_URL = 'https://peps.python.org/'
MAIN_DOC_URL = 'https://docs.python.org/3/'

PRETTY_STR = 'pretty'
FILE_STR = 'file'
LOGS_STR = 'logs'
PARSER_LOG_STR = 'parser.log'

BASE_DIR = Path(__file__).parent


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
COUNT_STATUS = [['Статус', 'Количество'],
                ['Active', 'Accepted', 0],
                ['Deferred', 0],
                ['Final', 0],
                ['Provisional', 0],
                ['Rejected', 0],
                ['Superseded', 0],
                ['Withdrawn', 0],
                ['Draft', 0]]
