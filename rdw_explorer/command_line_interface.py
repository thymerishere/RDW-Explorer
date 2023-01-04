import argparse
from rdw_explorer.config import Config

from rdw_explorer.database.search import Search

def search_with_args():
    args = _get_args()
    print(args)
    search = Search(Config())
    vehicles = search.dict_search(args)
    return vehicles

def _get_args():
    parser = argparse.ArgumentParser()
    _add_args(parser)
    args = parser.parse_args()
    return vars(args)

def _add_args(parser: argparse.ArgumentParser):
    arguments = [
        ('-m', '--merk'),
        ('-k', '--kenteken'),
        ('-o', '--handelsbenaming'),
    ]
    
    for argument in arguments:
        parser.add_argument(*argument)

