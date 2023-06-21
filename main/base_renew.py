import os
from zipfile import ZipFile

import requests
import wget
from lxml import html

from main.defs import GRLS_ADDRESS, USERAGENT, SOURCEPATH


def base_renew():
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
        for file in SOURCEPATH.glob('*.zip'):
            unarchive_grls(file)
    except Exception as err:
        print(err)


def unarchive_grls(file):
    with ZipFile(file, 'r') as zip:
        for name in zip.namelist():
            unicode_name = name.encode('cp437').decode('cp866')
            with zip.open(name) as z:
                content = z.read()
                fullpath = SOURCEPATH / unicode_name
                with open(fullpath, 'wb') as f:
                    f.write(content)
    os.remove(file)
