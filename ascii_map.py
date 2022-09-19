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

import math, time

from universal_globals import (width, height, width2, height2, floorwidth2, floorheight2, clear_screen, constrain)
import getkey
from getkey import get_key
import console

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
    '.': ' ',
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

formatted_map_str = ""

# print(formatted_map_list)

x = 0
y = 0

def char_is_wall(char):
    return (char == "#" or char == "▓")
def is_wall(x_pos, y_pos):
    is_in_bounds = x_pos >= 0 and x_pos < map_data["width"] and y_pos >= 0 and y_pos < map_data["height"]
    if y_pos > map_data["height"]:
        print(True)
    return char_is_wall(formatted_map_list[y_pos][x_pos]) if is_in_bounds else True
def get_char_on_map(x_pos, y_pos):
    if x == x_pos and y == y_pos:
        return player_char
    else:
        is_in_bounds = x_pos >= 0 and x_pos < map_data["width"] and y_pos >= 0 and y_pos < map_data["height"]
        return formatted_map_list[y_pos][x_pos] if is_in_bounds else "▓"

def check_walls(x_count, y_count, up_is_wall, down_is_wall, left_is_wall, right_is_wall):
    to_left = x_count - 1
    to_right = x_count + 1
    to_up = y_count - 1
    to_down = y_count + 1
    if (up_is_wall == is_wall(x_count, to_up))\
     and (down_is_wall == is_wall(x_count, to_down))\
     and (left_is_wall == is_wall(to_left, y_count))\
     and (right_is_wall == is_wall(to_right, y_count)):
        return True
def ascii_map_main():
    global x, y, formatted_map_str
    
    clear_screen()
        
    formatted_map_str = ""
    # Add whitespace to the top
    for i in range(y - math.floor(height2), -1):
        formatted_map_str += (((" " * (floorwidth2-x-4)) + ("▓" * constrain(floorwidth2+x+4, 0, width)) + "\n") if (i == -2) else ("\n"))
    for y_count, y_value in enumerate(formatted_map_list):
        # Whitespace left
        for i in range(x - math.floor(width2), -1):
            if y_count >= y - height2 and y_count < y + height2 - 4:
                formatted_map_str += (("▓") if (i in [-2, -3, -4]) else (" "))
        # Actual stuff
        for x_count, x_value in enumerate(y_value):
            if x_count*2 > x - width2 and x_count*2 < x + width2 and y_count > y - height2 and y_count < y + height2 - 4:
                # if character is two characters long, leave it. else, add a space
                char_to_add = x_value if len(x_value) == 2 else x_value + " "
                # if character position is the player's position, replace it
                char_to_add = (player_char+" ") if (x_count*2 == x and y_count == y) else (char_to_add)
                
                # walls
                if char_is_wall(x_value):
                    """if this is a wall"""
                    """
                    elif is_wall(x_count, to_up)\
                     and is_wall(x_count, to_down)\
                     and is_wall(to_left, y_count)\
                     and is_wall(to_right, y_count):
                        char_to_add  = " "
                    """
                    
                    if check_walls(x_count, y_count, True, True, True, True):
                        char_to_add  = "╬═"
                    elif check_walls(x_count, y_count, False, True, True, True):
                        char_to_add  = "╦═"
                    elif check_walls(x_count, y_count, True, False, True, True):
                        char_to_add  = "╩═"
                    elif check_walls(x_count, y_count, True, True, False, True):
                        char_to_add  = "╠═"
                    elif check_walls(x_count, y_count, True, True, True, False):
                        char_to_add  = "╣ "
                    elif check_walls(x_count, y_count, False, False, True, True):
                        char_to_add  = "══"
                    elif check_walls(x_count, y_count, True, False, False, True):
                        char_to_add  = "╚═"
                    elif check_walls(x_count, y_count, False, True, False, True):
                        char_to_add  = "╔═"
                    elif check_walls(x_count, y_count, True, False, True, False):
                        char_to_add  = "╝ "
                    elif check_walls(x_count, y_count, True, True, False, False):
                        char_to_add  = "║ "
                    elif check_walls(x_count, y_count, False, True, True, False):
                        char_to_add  = "╗ "
                    elif check_walls(x_count, y_count, False, True, True, False):
                        char_to_add  = "╗ "
                    elif check_walls(x_count, y_count, False, True, True, False):
                        char_to_add  = "╗ "
                        
                    elif check_walls(x_count, y_count, True, False, False, False):
                        char_to_add  = "║ "
                    elif check_walls(x_count, y_count, False, True, False, False):
                        char_to_add  = "║ "
                    elif check_walls(x_count, y_count, False, False, True, False):
                        char_to_add  = "══"
                    elif check_walls(x_count, y_count, False, False, False, True):
                        char_to_add  = "══"
                formatted_map_str += char_to_add
        # Whitespace right
        # for i in range(map_data["width"]*2, x + math.floor(width2)+1):
        #     if y_count >= y - height2 and y_count < y + height2 - 4 and x > map_data["width"] / 2:
        #         formatted_map_str += (("▓") if (i == map_data["width"]+2) else (" "))
        if x > map_data["width"] * 2 - floorwidth2:
            formatted_map_str += "▓ "
        formatted_map_str = formatted_map_str[:-2]
        formatted_map_str += "\n"
    # Whitespace bottom
    for i in range(map_data["height"]+1, y + math.floor(height2) - 4):
        formatted_map_str += (((" " * (floorwidth2-x-4)) + ("▓" * constrain(floorwidth2+x+4, 0, width)) + "\n") if (i == map_data["height"]+1) else ("\n"))
    print(formatted_map_str)
    
    with open('levels/currMap.txt', "w") as f:
        f.write(formatted_map_str)
    
    print("HP: 100\nATK: 10")
    
    key = get_key()
    if key == 'left' and not is_wall(math.floor(x/2)-1, y):
        x -= 2
        console.log("Player moved left")
    elif key == 'right' and not char_is_wall(get_char_on_map(math.floor(x/2)+1, y)):
        x += 2
        console.log("Player moved right")
    elif key == 'up' and not char_is_wall(get_char_on_map(math.floor(x/2), y-1)):
        y -= 1
        console.log("Player moved up")
    elif key == 'down' and not char_is_wall(get_char_on_map(math.floor(x/2), y+1)):
        y += 1
        console.log("Player moved down")
    # x = constrain(x, 0, (map_data["width"] * 2) - 2)
    # y = constrain(y, 0, map_data["height"] - 1)
    
ascii_map_main()

while True:
    ascii_map_main()
    