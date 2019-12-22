# move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
# move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
# move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
# move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
# wall_is_above()	если сверху стена, возвращает True, иначе — False
# wall_is_beneath()	если снизу стена, возвращает True, иначе — False
# wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
# wall_is_on_the_right()	если справа стена, возвращает True, иначе — False

from pyrob.api import *


@task
def task_3_3 ( ) :
    while not wall_is_above ( ) :
        move_up ( )
    if wall_is_beneath ( ) == False :
        move_down ( )
    elif wall_is_on_the_right ( ) == False :
        move_right ( )
    elif wall_is_on_the_left ( ) == False :
        move_left ( )

    print ( wall_is_above ( ) , wall_is_beneath ( ) , wall_is_on_the_right ( ) , wall_is_on_the_left ( ) )


if __name__ == '__main__' :
    run_tasks ( )

    # elif wall_is_on_the_left() :
    #   move_right ()
    # elif wall_is_on_the_right()	:
    #    move_left ()
