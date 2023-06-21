from pathlib import Path

USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
            '(KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
GRLS_ADDRESS = 'https://grls.rosminzdrav.ru/'
SOURCEPATH = Path.cwd() / 'sources'
CHROMEDRIVER = Path.cwd() / 'chromedriver.exe'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + (SOURCEPATH / 'grls.db').as_posix()
SQLALCHEMY_TRACK_MOD = False
