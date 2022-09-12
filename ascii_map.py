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
from universal_globals import *

ascii_map = []

for y in range(height-1):
    map_line_str = ""
    for x in range(width):
        map_line_str += "-"
    ascii_map.append(map_line_str)

# print("".join(ascii_map))


ascii_graphics_data = {
    '&': [
        "&&",
        "&&"
    ],
    '#': [
        "##",
        "##"
    ],
    '.': [
        "..",
        ".."
    ],
}

map_data = {
    "map": [
        "&....#............................................",
        ".....#............................................",
        ".....#............................................",
        ".....#............................................",
        ".....#............................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
        "..................................................",
    ],
    "walls": [
        
    ]
}
map_data["width"] = len(map_data["map"][0])
map_data["height"] = len(map_data["map"])

def createRoom():
    pass


formatted_map_list = []
for y_count, y_value in enumerate(map_data["map"]):
    yc2 = (y_count * 2)
    # formatted_map_list[yc2] = formatted_map_list[(yc2 + 1)] = ""
    formatted_map_list.append("")
    formatted_map_list.append("")
    for x_count, x_value in enumerate(y_value):
        formatted_map_list[yc2] += ascii_graphics_data[x_value][0]
        formatted_map_list[(yc2 + 1)] += ascii_graphics_data[x_value][1]

# print(formatted_map_list)

x = 0
y = 0

formatted_map_str = ""

for i in range(y - math.floor(height2), -1):
    formatted_map_str += "▓" * width + "\n"
for y_count, y_value in enumerate(formatted_map_list):
    for i in range(x - math.floor(width2), -1):
        formatted_map_str += "▓"
    for x_count, x_value in enumerate(y_value):
        if x_count > x - width2 and x_count < x + width2 and y_count > y - height2 and y_count < y + height2:
            formatted_map_str += x_value
    formatted_map_str += "\n"

print(formatted_map_str)