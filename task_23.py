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


def vertikal_up ( ) :
    while wall_is_above ( ) == False and cell_is_filled ( ) == False :
        fill_cell ( )
        move_up ( )
    if wall_is_above ( ) == True :
        fill_cell ( )
        move_down ( )
        while wall_is_beneath ( ) == False :
            move_down ( )
        if wall_is_beneath ( ) and wall_is_on_the_right ( ) == False :
            move_right ( )


@task ( delay=0.01 )
def task_6_6 ( ) :
    move_right ( )
    while True :
        while wall_is_on_the_right ( ) == False and wall_is_above ( ) == True :
            move_right ( )
        if wall_is_on_the_right ( ) == False and wall_is_above ( ) == False :
            move_up ( )
            vertikal_up ( )
        if wall_is_on_the_right ( ) == True and wall_is_above ( ) == False :
            move_up ( )
            vertikal_up ( )
        if wall_is_on_the_right ( ) and wall_is_beneath ( ) :
            move_left ( )
            while wall_is_beneath ( ) :
                move_left ( )
            if wall_is_beneath ( ) == False and wall_is_above ( ) == False :
                break


if __name__ == '__main__' :
    run_tasks ( )
