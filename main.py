from rdw_explorer import command_line_interface


def main() -> None:
    vehicles = command_line_interface.search_with_args()
    print(vehicles)

if __name__ == '__main__':
    main()
