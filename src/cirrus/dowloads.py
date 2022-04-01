from datetime import date
from multiprocessing import Pool
from os import mkdir
from os.path import isdir
from shutil import rmtree

from bs4 import BeautifulSoup
from requests import get

from cirrus.util.config import logger, settings

today = date.today()
url_cempa_files = (
    f'https://tatu.cempa.ufg.br/BRAMS-dataout/{today.strftime("%Y%m%d")}00/'
)


class NotTheInformationForToday(Exception):
    """Not the Information for today"""

    pass


def get_links(link=''):
    request = get(f'{url_cempa_files}{link}')
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, features="html5lib")
        return [
            _link
            for _link in [i.get('href') for i in soup.find_all('a')]
            if '.gra' in _link
        ]
    raise NotTheInformationForToday


def save_file(args):
    try:
        url, file_name = args
        logger.debug(f"Dowload: {url.split('/')[-1].replace('.gra','')}")
        request = get(url)
        with open(file_name, 'wb') as f:
            f.write(request.content)

        request = get(url.replace('.gra', '.ctl'))
        with open(file_name.replace('.gra', '.ctl'), 'wb') as f:
            f.write(request.content)
        return True

    except Exception as error:
        logger.exception('Erro ao tentar baixar os dados {error}')
        return False


def downloads_files():
    downloads_dir = f'{settings.CEMPADIR}downloads'
    if isdir(downloads_dir):
        rmtree(downloads_dir)
    mkdir(downloads_dir)

    files_link = [
        (f'{url_cempa_files}{file}', f'{downloads_dir}/{file}')
        for file in get_links()
    ]
    logger.info('Starting Data Download')
    with Pool(settings.N_POOL) as workers:
        result = workers.map(save_file, files_link)
    logger.info('End Data Dowload')
    return all(result)

if __name__ == '__main__':
    downloads_files()

