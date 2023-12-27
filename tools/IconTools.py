import string

import svgwrite


def generate_svg(s, font_color):
    # 创建SVG对象，设置画布大小为16x16
    dwg = svgwrite.Drawing(f'{s}_{font_color}.svg', size=(16, 16))

    # 在SVG中绘制文本
    dwg.add(dwg.text(s, insert=(0, 12), font_size='12px', fill=font_color))

    # 保存SVG图片
    dwg.save()


letters = [letter for letter in string.ascii_uppercase[:24]]

for letter in letters:
    generate_svg(letter, 'black')
    generate_svg(letter, 'white')
