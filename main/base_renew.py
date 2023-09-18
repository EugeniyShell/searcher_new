import os
from zipfile import ZipFile

import requests
import wget
import xlrd
from lxml import html

from .db import Substantion, db
from .defs import GRLS_ADDRESS, USERAGENT, SOURCEPATH


def base_renew():
    get_grls()
    for file in SOURCEPATH.glob('*.zip'):
        process_zips(file)
        os.remove(file)
    for file in SOURCEPATH.glob('*-Действующий.xls'):
        process_xls(file)
    for file in SOURCEPATH.glob('*.xls'):
        os.remove(file)


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


def process_xls(file):
    try:
        wb = xlrd.open_workbook(file)
        for sh in wb.sheets():
            process_cells(sh)
    except Exception as err:
        print(err)


def process_cells(sheet):
    if sheet.cell(4, 10).value == \
            'Торговое наименование\nлекарственного препарата':
        for n in range(6, sheet.nrows - 2):
            analyze(sheet.cell(n, 10).value, sheet.cell(n, 11).value)
    else:
        print(f'{sheet.name} - Invalid Sheet Format')


def analyze(_tn, _mnn):
    if _mnn == '~':
        _mnn = _tn
    if not Substantion.query.filter_by(commonname=_mnn, drugname=_tn).first():
        db.session.add(Substantion(commonname=_mnn, drugname=_tn,
                                   commonname_normalized=_mnn.lower(),
                                   drugname_normalized=_tn.lower()))
