'''
Вам дана двумерная матрица с индексом 0grid размером m x n, где (r, c)представляет:
Ячейка земли , если grid[r][c] = 0, или
Водная ячейка , содержащая grid[r][c]рыбу, если grid[r][c] > 0.
Рыболов может начать с любой водной ячейки (r, c)и может выполнять следующие операции любое количество раз:

Поймать всю рыбу в клетке (r, c), или
Переместитесь в любую соседнюю ячейку с водой .
Верните максимальное количество рыбы , которое рыбак может поймать, если он оптимально выберет свою начальную ячейку или0 если ячейки с водой не существует.
Соседняя ячейка ячейки (r, c), — это одна из ячеек (r, c + 1), (r, c - 1), (r + 1, c)или , (r - 1, c)если она существует.

Пример 1:
Вход: сетка = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
 Выход: 7
 Пояснение: Рыбак может начать с ячейки (1,3)и собрать 3 рыбы, затем перейти к ячейке (2,3) и собрать 4 рыбы.
'''


def find_max_num_fish(matrix):
    cells = []
    enumerate_matrix = enumerate(matrix)
    for y, row in enumerate_matrix:
        enumerate_row = enumerate(row)
        for cell_ in enumerate_row:
            cell = {'coordinates_x': cell_[0], 'coordinates_y': y, 'fish': cell_[1]}
            if cell['fish']:
                cells.append(cell)
    new_cells = []
    for cell in cells:
        neighbours = []
        for cell_ in cells:
            if (cell['coordinates_x'] == cell_['coordinates_x'] and
                    (cell['coordinates_y'] == cell_['coordinates_y'] + 1 or
                     cell['coordinates_y'] == cell_['coordinates_y'] - 1)):
                neighbours.append({'coordinates': (cell_['coordinates_x'], cell_['coordinates_y']), 'fish': cell_['fish']})
            elif (cell['coordinates_y'] == cell_['coordinates_y'] and
                    (cell['coordinates_x'] == cell_['coordinates_x'] + 1 or
                     cell['coordinates_x'] == cell_['coordinates_x'] - 1)):
                neighbours.append({'coordinates': (cell_['coordinates_x'], cell_['coordinates_y']), 'fish': cell_['fish']})
        new_cell = {'coordinates': (cell['coordinates_x'], cell['coordinates_y']), 'fish': cell['fish'],
                    'neighbours': neighbours}
        new_cells.append(new_cell)
    print(f"{new_cells=}")


    def find_cell(coordinates, row_cells):
        for current_cell in row_cells:
            if current_cell['coordinates'] == coordinates:
                return current_cell

    def add_cell_group(cell_, group_, verified_, fish_):
        if cell_['coordinates'] not in verified_:
            neighbours_coordinates = set()
            for neighbour in cell['neighbours']:
                neighbours_coordinates.add(neighbour['coordinates'])
            if not group_ or neighbours_coordinates & group_cells:
                group_.add(cell['coordinates'])
                verified_.add(cell['coordinates'])
                fish_ += cell_['fish']
                for coordinates in neighbours_coordinates:
                    if coordinates not in verified_:
                        neighbour_with_neighbours = find_cell(coordinates, new_cells)
                        print(f"{neighbour_with_neighbours=}")
                        add_cell_group(neighbour_with_neighbours, group_, verified_, fish_)
        else:
            pass

    result = 0
    # all_coordinates = list(map(lambda cell: cell['coordinates'], new_cells))
    for group in range(len(new_cells)):
        group_cells = set()
        verified = set()
        fish = 0
        for cell in new_cells:
            print(f"{cell=}")
            add_cell_group(cell, group_cells, verified, fish)
            if fish > result:
                result = fish
    print(f"{new_cells=}")
    # result = 0
    # verified = set()
    # print(new_cells)
    # for cell in new_cells:
    #     if cell['coordinates'] not in verified:
    #         fish = cell['fish']
    #         verified.add(cell['coordinates'])
    #         for cell_ in new_cells:
    #             if (cell_['coordinates'] not in verified
    #                     and cell_['coordinates'] != cell['coordinates']
    #                     and cell_['group'] == cell['group']):
    #                 fish += cell_['fish']
    #                 verified.add(cell_['coordinates'])
    #         if fish > result:
    #             result = fish
    # fish = [for cell in new_cells]
    return result


matrix1 = [[0,5],[8,4]]
print(f"{find_max_num_fish(matrix1)=}")

