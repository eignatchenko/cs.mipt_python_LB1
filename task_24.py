#!/usr/bin/python3
# move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
# move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
# move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
# move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
# wall_is_above()	если сверху стена, возвращает True, иначе — False
# wall_is_beneath()	если снизу стена, возвращает True, иначе — False
# wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
# wall_is_on_the_right()	если справа стена, возвращает True, иначе — False

# fill_cell()	Закрасить текущую клетку
# cell_is_filled()	Возвращает True, если текущая клетка закрашена
# mov(r, v)	Поместить значение v в регистр r

def krest_fill ( ) :
    fill_cell ( )
    move_down ( )
    move_right ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_right ( )
    fill_cell ( )
    move_up ( )
    move_left ( )
    fill_cell ( )


from pyrob.api import *


@task ( delay=0.01 )
def task_2_1 ( ) :
    move_right ( )
    move_down ( 2 )
    krest_fill ( )
    move_left ( )


if __name__ == '__main__' :
    run_tasks ( )
