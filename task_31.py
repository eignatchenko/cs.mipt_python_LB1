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

#!/usr/bin/python3

from pyrob.api import *

def run_right():
 while not wall_is_on_the_right():
  if not wall_is_beneath():
   return run_down
  move_right()
 return run_left

def run_left():
 while not wall_is_on_the_left():
  if not wall_is_beneath():
   return run_down
  move_left()

def run_down():
 while not wall_is_beneath():
  move_down()
 return run_right


@task(delay=0.001)
def task_8_30():
 runer = run_left
 if not wall_is_beneath():
  runer = run_down
 while runer:
  runer = runer()


if __name__ == '__main__':
 run_tasks()