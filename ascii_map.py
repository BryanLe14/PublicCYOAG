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

player_char = "@"

ascii_graphics_data = {
    '&': '&',
    '#': '#',
    '.': '.',
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
    yc2 = (y_count)
    formatted_map_list.append("")
    for x_count, x_value in enumerate(y_value):
        formatted_map_list[yc2] += ascii_graphics_data[x_value]

# print(formatted_map_list)

x = 0
y = 0

def ascii_map_main():
    global x, y
    
    clear_screen()
        
    formatted_map_str = ""
    # Add whitespace to the top
    for i in range(y - math.floor(height2), -1):
        formatted_map_str += (("▓" * width + "\n") if (i == -2) else ("\n"))
    for y_count, y_value in enumerate(formatted_map_list):
        # Whitespace left
        for i in range(x - math.floor(width2), -1):
            if y_count >= y - height2 and y_count < y + height2 - 4:
                formatted_map_str += (("▓") if (i == -2 or i == -3) else ("-"))
        # Actual stuff
        for x_count, x_value in enumerate(y_value):
            if x_count*2 > x - width2 and x_count*2 < x + width2 and y_count > y - height2 and y_count < y + height2 - 4:
                char_to_add = x_value if len(x_value) == 2 else x_value + " "
                formatted_map_str += (player_char+" ") if (x_count*2 == x and y_count == y) else (char_to_add)
        # Whitespace right
        for i in range(map_data["width"]*2, x + math.floor(width2)+1):
            if y_count >= y - height2 and y_count < y + height2 - 4 and x > map_data["width"] / 2:
                formatted_map_str += (("▓") if (i == map_data["width"]+1) else ("-"))
        formatted_map_str += "\n"
    # Whitespace bottom
    for i in range(map_data["height"]+1, y + math.floor(height2) - 4):
        formatted_map_str += "▓" * width + "\n"
    print(formatted_map_str)
    
    with open('levels/currMap.txt', "w") as f:
        f.write(formatted_map_str)
    
    key = get_key()
    if key == 'left':
        x -= 2
    elif key == 'right':
        x += 2
    elif key == 'up':
        y -= 1
    elif key == 'down':
        y += 1
    
ascii_map_main()

while True:
    ascii_map_main()