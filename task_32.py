#!/usr/bin/python3

_methods = """
доступные методы:
move_left(n=1)  Пройти n клеток влево (по умолчанию n = 1)
move_right(n=1) Пройти n клеток вправо (по умолчанию n = 1)
move_up(n=1)    Пройти n клеток вверх (по умолчанию n = 1)
move_down(n=1)  Пройти n клеток вниз (по умолчанию n = 1)
wall_is_above() если сверху стена, возвращает True, иначе — False
wall_is_beneath()   если снизу стена, возвращает True, иначе — False
wall_is_on_the_left()   если слева стена, возвращает True, иначе — False
wall_is_on_the_right()  если справа стена, возвращает True, иначе — False
fill_cell() Закрасить текущую клетку
cell_is_filled()    Возвращает True, если текущая клетка закрашена
mov(r, v)   Поместить значение v в регистр r
"""

from pyrob.api import *

@task(delay=0.005)

def task_8_18():
    filled_cells = 0
    def corridor(filled_cells_corridor):
        n = 0
        filled_cells_corridor = 0
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                filled_cells_corridor += 1
                #print(filled_cells_corridor)
            elif not cell_is_filled():
                fill_cell()
            n += 1
        move_down(n)
        move_right()
        return filled_cells_corridor

    while wall_is_beneath():
        if not wall_is_above():
            filled_cells += corridor(filled_cells)

        else:
            fill_cell()
            move_right()
    #print('total {}'.format(filled_cells))

    mov('ax', filled_cells)

if __name__ == '__main__':
    run_tasks()
