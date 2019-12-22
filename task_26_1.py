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


from pyrob.api import *


def start_line ( ) :
    move_down ( )
    fill_cell ( )
    move_down ( )
    move_right ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_right ( )
    move_down ( )
    fill_cell ( )
    move_right ( )


def line_left ( ) :
    move_right ( )
    fill_cell ( )
    move_down ( )
    move_right ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_right ( )
    move_down ( )
    fill_cell ( )
    if wall_is_on_the_right ( ) :
        move_down ( 4 )
    move_right ( )


@task ( delay=0.25 )
def task_2_4 ( ) :
    while wall_is_on_the_right ( ) == True and wall_is_beneath ( ) == False :
        move_down ( 4 )
    while wall_is_on_the_left ( ) == False and wall_is_beneath ( ) == False :
        pass

    while wall_is_on_the_left ( ) == True and wall_is_beneath ( ) == False :
        move_down ( 2 )

    while wall_is_beneath ( ) == True and wall_is_on_the_left ( ) == False :
        move_left ( )
        if wall_is_on_the_left ( ) == True :
            move_up ( 2 )
            break


if __name__ == '__main__' :
    run_tasks ( )
