# view
from model import init_field, is_win, EMPTY_SYMBOL, is_empty_cell,SIZE_FIELD,set_cell

FIRST_PLAYER = "X"
SECOND_PLAYER = "O"


def main():



    :return:

    field = init_field()
    print_field(field)

    current_player, next_player = FIRST_PLAYER, SECOND_PLAYER
    player_step(current_player)

    while True:
        player_step(field, current_player)
        print(field)
        if is_win(field):
            print_win_message(current_player)
            break
    enemy_step(current_player)

        if is_win(field):
            print_win_message(next_player)
            break


def player_step(field, player_symbol: str):
    while True
        try:
            coord = int(input("ведите ячейку для кода (1 до 9):"))
        except  ValueError:
            print("Вы ввели не целое число:")
            x = (coord -1 ) // SIZE_FIELD
            y = (coord -1 ) % SIZE_FIELD
            if not is_empty_cell(field, row_index= x, col_index= y:
                print("ячейка занята")
                set_cell(field,
                         row_index=x,
                         col_index=y,
                         player_symbol)


    if not 1 <= coord <= 9:
        print("Введите число от 1 до 9")


def enemy_step(player_symbol: str):
    player_step(player_symbol)


def print_field(field: list[list]) -> None:
    start_num =1
    for i in range(len(field)):
        for j in range(len(field[i])):
            print_symbol = start_num if field[i][j] == EMPTY_SYMBOL else field [i][j]
            start_num += 1
            print(print_symbol, end=" ")
        print()


def print_win_message
    if __name__ == "__main__":
        main()