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


def line_right ( ) :
    move_down ( )
    fill_cell ( )
    move_down ( )
    move_right ( )
    fill_cell ( )
    move_right ( )
    move_up ( )
    fill_cell ( )
    move_left ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_right ( )
    if wall_is_on_the_right ( ) == False :
        move_right ( 2 )
    if wall_is_on_the_right ( ) == True and wall_is_beneath ( ) == False :  # изменить
        move_down ( 4 )
    if wall_is_on_the_right ( ) == True and wall_is_beneath ( ) == True :
        move_left ( )
        while wall_is_beneath ( ) == True and wall_is_on_the_left ( ) == False :
            move_left ( )
        if wall_is_on_the_left ( ) == True :
            move_up ( 3 )


def line_right5 ( ) :
    move_down ( )
    fill_cell ( )
    move_down ( )
    move_right ( )
    fill_cell ( )
    move_right ( )
    move_up ( )
    fill_cell ( )
    move_left ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_right ( )
    if wall_is_on_the_right ( ) == False :
        move_right ( 2 )
    if wall_is_on_the_right ( ) == True and wall_is_beneath ( ) == False :  # изменить
        move_down ( 2 )


def line_left ( ) :
    move_down ( )
    fill_cell ( )
    move_down ( )
    move_left ( )
    fill_cell ( )
    move_left ( )
    move_up ( )
    fill_cell ( )
    move_right ( )
    fill_cell ( )
    move_up ( )
    fill_cell ( )
    move_left ( )
    if wall_is_on_the_left ( ) == False :
        move_left ( 2 )
    if wall_is_on_the_left ( ) == True :
        move_down ( 4 )


def Line_4ch ( ) :
    for i in range ( 2 ) :
        for i in range ( 10 ) :
            line_right ( )
        for i in range ( 10 ) :
            line_left ( )


@task ( delay=0.005 )
def task_2_4 ( ) :
    Line_4ch ( )

    for i in range ( 10 ) :
        line_right5 ( )
    if wall_is_on_the_right ( ) == True and wall_is_beneath ( ) == True :
        move_left ( )
        while wall_is_beneath ( ) == True and wall_is_on_the_left ( ) == False :
            move_left ( )
            if wall_is_on_the_left ( ) == True :
                move_up ( 2 )
                break


if __name__ == '__main__' :
    run_tasks ( )
