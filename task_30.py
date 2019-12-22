from pyrob.api import *

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


def count_field_size ( ):
    i = 1
    if not wall_is_on_the_left ( ):
        # im in left corner
        move_left ( )
    while not wall_is_beneath ( ):
        move_down ( )
        i += 1
    return i


def run_left ( ) :
    while not wall_is_on_the_left ( ) :
        move_left ( )


def run_down ( ) :
    while not wall_is_beneath ( ) :
        move_down ( )


@task ( delay=0.1 )
def task_9_3 ( ):
    field_size = 0
    field_size = count_field_size ( )
    
    while field_size > 0 :
        for move in (move_up,move_right,move_down,move_left) :
            i = 1
            while i < field_size :
                print("move ",move.__name__, "because i=",i," field_size=",field_size)
                move ( )
                if i < field_size - 1 :
                    fill_cell ( )
                i += 1
        move_up ( );
        move_right ( )
        field_size = field_size - 2
    run_down ( )
    run_left ( )


if __name__ == '__main__':
    run_tasks ( )