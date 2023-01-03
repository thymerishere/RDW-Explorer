from rdw_explorer import command_line_interface
from rdw_explorer.config import Config
from rdw_explorer.database.search import Search
from rdw_explorer.vehicle import Vehicle


def main() -> None:
    vehicles = command_line_interface.search_with_args()
    print(vehicles)

if __name__ == '__main__':
    main()
