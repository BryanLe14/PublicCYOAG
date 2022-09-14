"""
https://en.wikipedia.org/wiki/Block_Elements

▀
▁
▂
▃
▄
▅
▆
▇
█
▉
▊
▋
▌
▍
▎
▏
▐
░
▒
▓
▔
▕
▖
▗
▘
▙
▚
▛
▜
▝
▞
▟

https://www.unicode.org/versions/Unicode1.0.0/CodeCharts2.pdf
Blocks: p.319

https://www.w3.org/TR/xml-entity-names/025.html
─
━
│
┃
┄
┅
┆
┇
┈
┉
┊
┋
┌
┍
┎
┏
┐
┑
┒
┓
└
┕
┖
┗
┘
┙
┚
┛
├
┝
┞
┟
┠
┡
┢
┣
┤
┥
┦
┧
┨
┩
┪
┫
┬
┭
┮
┯
┰
┱
┲
┳
┴
┵
┶
┷
┸
┹
┺
┻
┼
┽
┾
┿
╀
╁
╂
╃
╄
╅
╆
╇
╈
╉
╊
╋
╌
╍
╎
╏
═
║
╒
╓
╔
╕
╖
╗
╘
╙
╚
╛
╜
╝
╞
╟
╠
╡
╢
╣
╤
╥
╦
╧
╨
╩
╪
╫
╬
╭
╮
╯
╰
╱
╲
╳
╴
╵
╶
╷
╸
╹
╺
╻
╼
╽
╾
╿
"""

import math
import time

from universal_globals import (width, height, width2, height2, clear_screen)
import getkey
from getkey import get_key

ascii_map = []

for y in range(height-1):
    map_line_str = ""
    for x in range(width):
        map_line_str += "-"
    ascii_map.append(map_line_str)

# print("".join(ascii_map))

block_size = 2
player_char = "@"

ascii_graphics_data = {
    '&': ['&&' * block_size for i in range(block_size)],
    '#': ['##' * block_size for i in range(block_size)],
    '.': ['.' * block_size for i in range(block_size)],
}

map_data = {
    "map": None,
}
with open('levels/1.txt') as f:
    map_data["map"] = [x.strip() for x in f.readlines()]

map_data["width"] = len(map_data["map"][0])
map_data["height"] = len(map_data["map"])

def createRoom():
    pass


formatted_map_list = []
for y_count, y_value in enumerate(map_data["map"]):
    yc2 = (y_count * block_size)
    for yi in range(block_size):
        formatted_map_list.append("")
    for x_count, x_value in enumerate(y_value):
        for xi in range(block_size):
            formatted_map_list[(yc2 + xi)] += ascii_graphics_data[x_value][xi]

# print(formatted_map_list)

x = 0
y = 0

def ascii_map_main():
    global x, y
    
    clear_screen()
        
    formatted_map_str = ""
    for i in range(y - math.floor(height2), -1):
        formatted_map_str += "▓" * width + "\n"
    for y_count, y_value in enumerate(formatted_map_list):
        for i in range(x - math.floor(width2), -1):
            if y_count >= y - height2 and y_count < y + height2 - 4:
                formatted_map_str += "▓"
        for x_count, x_value in enumerate(y_value):
            if x_count*2 > x - width2 and x_count*2 < x + width2 and y_count > y - height2 and y_count < y + height2 - 4:
                char_to_add = x_value if len(x_value) == 2 else x_value + " "
                formatted_map_str += (player_char+" ") if (x_count == x and y_count == y) else (char_to_add)
        formatted_map_str += "\n"
    
    print(formatted_map_str.strip())
    
    key = get_key()
    if key == 'left':
        x -= 1
    elif key == 'right':
        x += 1
    elif key == 'up':
        y -= 1
    elif key == 'down':
        y += 1
    
ascii_map_main()

while True:
    ascii_map_main()
