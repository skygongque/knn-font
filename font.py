import requests
import re
from fontTools.ttLib import TTFont
""" 
把woff文件转成可以计算的数据，knn数据准备
数据为一个二维列表，第一列为真实字符值，其余列为该字符在字体文件中坐标展平结果
"""

def get_font_content():
    url = 'https://maoyan.com/board/1'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    font_url = 'http:' + re.findall(r"url\('(.*?\.woff)'\)", response.text)[0]
    return requests.get(font_url).content


def save_font():
    # 20210502测试网站字体文件为静态，无法通过该函数增加数据集
    for i in range(10):
        font_content = get_font_content()
        with open(f'./fonts/{i+1}.woff', 'wb') as f:
            f.write(font_content)


def get_coor_info(font, cli):
    glyf_order = font.getGlyphOrder()[2:]
    # print(glyf_order)
    # info = list()
    info = []
    for i, g in enumerate(glyf_order):
        coors = font['glyf'][g].coordinates
        # 把坐标数据展平
        coors = [_ for c in coors for _ in c]
        coors.insert(0, cli[i])
        info.append(coors)
    # print(info)
    return info


def get_font_data():
    font_1 = TTFont('./fonts/1.woff')
    cli_1 = [6, 7, 4, 9, 1, 2, 5, 0, 3, 8]
    coor_info_1 = get_coor_info(font_1, cli_1)

    font_2 = TTFont('./fonts/2.woff')
    cli_2 = [1, 3, 2, 7, 6, 8, 9, 0, 4, 5]
    coor_info_2 = get_coor_info(font_2, cli_2)

    font_3 = TTFont('./fonts/3.woff')
    cli_3 = [5, 8, 3, 0, 6, 7, 9, 1, 2, 4]
    coor_info_3 = get_coor_info(font_3, cli_3)

    font_4 = TTFont('./fonts/4.woff')
    cli_4 = [9, 3, 4, 8, 7, 5, 2, 1, 6, 0]
    coor_info_4 = get_coor_info(font_4, cli_4)

    font_5 = TTFont('./fonts/5.woff')
    cli_5 = [1, 5, 8, 0, 7, 9, 6, 3, 2, 4]
    coor_info_5 = get_coor_info(font_5, cli_5)

    font_6 = TTFont('./fonts/6.woff')
    cli_6 = [1, 5, 6, 3, 4, 8, 7, 0, 2, 9]
    coor_info_6 = get_coor_info(font_6, cli_6)

    font_7 = TTFont('./fonts/7.woff')
    cli_7 = [5, 0, 4, 2, 9, 1, 3, 6, 8, 7]
    coor_info_7 = get_coor_info(font_7, cli_7)

    font_8 = TTFont('./fonts/8.woff')
    cli_8 = [6, 2, 9, 4, 8, 0, 5, 7, 1, 3]
    coor_info_8 = get_coor_info(font_8, cli_8)

    font_9 = TTFont('./fonts/9.woff')
    cli_9 = [8, 2, 9, 1, 4, 7, 5, 6, 0, 3]
    coor_info_9 = get_coor_info(font_9, cli_9)

    font_static = TTFont('./fonts/static.woff')
    cli_static = [6, 3, 7, 9, 1, 8, 0, 4, 2, 5]
    coor_info_static = get_coor_info(font_static, cli_static)

    infos = coor_info_1 + coor_info_2 + coor_info_3 + \
        coor_info_4 + coor_info_5 + coor_info_6 + coor_info_7 + \
        coor_info_8 + coor_info_9 + coor_info_static
    return infos


if __name__ == '__main__':
    print(get_font_data())
