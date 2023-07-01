import os
from zipfile import ZipFile

import requests
import wget
from lxml import html

from main.defs import GRLS_ADDRESS, USERAGENT, SOURCEPATH


def base_renew():
    get_grls()
    for file in SOURCEPATH.glob('*.zip'):
        process_zips(file)
    for file in SOURCEPATH.glob('*.xls'):
        process_xls(file)


def get_grls():
    url = GRLS_ADDRESS + 'GRLS.aspx'
    headers = {
        'User-agent': USERAGENT,
    }
    try:
        response = requests.get(url, headers=headers)
        root = html.fromstring(response.text)
        url = root.xpath('//div[@id="ctl00_plate_tdzip"]/button/@onclick')[0]
        url = GRLS_ADDRESS + url.split("'")[1]
        wget.download(url, str(SOURCEPATH))
    except Exception as err:
        print(err)


def process_zips(file):
    with ZipFile(file, 'r') as zf:
        for name in zf.namelist():
            unicode_name = name.encode('cp437').decode('cp866')
            with zf.open(name) as z:
                content = z.read()
                fullpath = SOURCEPATH / unicode_name
                with open(fullpath, 'wb') as f:
                    f.write(content)
    os.remove(file)


def process_xls(file):
    pass
