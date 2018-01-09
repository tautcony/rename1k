#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rename1k
   Copyright (c) 2018, TautCony.
   Homepage: https://github.com/tautcony/rename1k

rename1k is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.
rename1k is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.
You should have received a copy of the GNU General Public License
along with GCC; see the file COPYING3.  If not see
<http://www.gnu.org/licenses/>.
"""
import math
import os
import sys
import argparse
from typing import List, Callable, Sequence


__version__ = '0.0.1'

SYMBOLS = '天地玄黃宇宙洪荒日月盈昃辰宿列張寒來暑往秋收冬藏閏餘成歲律呂調陽雲騰致雨露結為霜金生麗水玉出崑岡劍號巨闕珠稱夜光果珍李柰菜重芥薑海鹹河淡鱗潛羽翔龍師火帝鳥官人皇始制文字乃服衣裳推位讓國有虞陶唐弔民伐罪周發殷湯坐朝問道垂拱平章愛育黎首臣伏戎羌遐邇壹體率賓歸王鳴鳳在樹白駒食場化被草木賴及萬方蓋此身髮四大五常恭惟鞠養豈敢毀傷女慕貞絜男效才良知過必改得能莫忘罔談彼短靡恃己長信使可覆器欲難量墨悲絲染詩讃羔羊景行維賢剋念作聖德建名立形端表正空谷傳聲虛堂習聽禍因惡積福緣善慶尺璧非寶寸陰是競資父事君曰嚴與敬孝當竭力忠則盡命臨深履薄夙興溫凊似蘭斯馨如松之盛川流不息淵澄取映容止若思言辭安定篤初誠美慎終宜令榮業所基籍甚無竟學優登仕攝職從政存以甘棠去而益詠樂殊貴賤禮別尊卑上和下睦夫唱婦隨外受傅訓入奉母儀諸姑伯叔猶子比兒孔懷兄弟同氣連枝交友投分切磨箴規仁慈隱惻造次弗離節義廉退顛沛匪虧性靜情逸心動神疲守真志滿逐物意移堅持雅操好爵自縻都邑華夏東西二京背邙面洛浮渭據涇宮殿盤鬱樓觀飛驚圖寫禽獸畫綵仙靈丙舍傍啟甲帳對楹肆筵設席鼓瑟吹笙升階納陛弁轉疑星右通廣內左達承明既集墳典亦聚羣英杜稾鍾隸漆書壁經府羅將相路俠槐卿戶封八縣家給千兵高冠陪輦驅轂振纓世祿侈富車駕肥輕策功茂實勒碑刻銘磻溪伊尹佐時阿衡奄宅曲阜微旦孰營桓公匡合濟弱扶傾綺迴漢惠說感武丁俊乂密勿多士寔寧晉楚更霸趙魏困橫假途滅虢踐土會盟何遵約法韓弊煩刑起翦頗牧用軍最精宣威沙漠馳譽丹青九州禹跡百郡秦并嶽宗恆岱禪主云亭雁門紫塞雞田赤城昆池碣石鉅野洞庭曠遠緜邈巖岫杳冥治本於農務茲稼穡俶載南畝我藝黍稷稅熟貢新勸賞黜陟孟軻敦素史魚秉直庶幾中庸勞謙謹敕聆音察理鑒貌辨色貽厥嘉猷勉其祗植省躬譏誡寵增抗極殆辱近恥林皋幸即兩疏見機解組誰逼索居閒處沈默寂寥求古尋論散慮逍遙欣奏累遣慼謝歡招渠荷的歷園莽抽條枇杷晚翠梧桐早凋陳根委翳落葉飄颻遊鵾獨運凌摩絳霄耽讀翫市寓目囊箱易輶攸畏屬耳垣墻具膳飡飯適口充腸飽飫烹宰飢厭糟糠親戚故舊老少異糧妾御績紡侍巾帷房紈扇圓潔銀燭煒煌晝眠夕寐藍笋象床絃歌酒讌接盃舉觴矯手頓足悅豫且康嫡後嗣續祭祀烝嘗稽顙再拜悚懼恐惶牋牒簡要顧答審詳骸垢想浴執熱願涼驢騾犢特駭躍超驤誅斬賊盜捕獲叛亡布射遼丸嵇琴阮嘯恬筆倫紙鈞巧任釣釋紛利俗並皆佳妙毛施淑姿工顰妍笑年矢每催曦暉朗耀璇璣懸斡晦魄環照指薪修祜永綏吉劭矩步引領俯仰廊廟束帶矜莊徘徊瞻眺孤陋寡聞愚蒙等誚謂語助者焉哉乎也魛魢魨魷䰾魴鮋鮊魺鮃鮁鮎鮍鮓鮒鮐鱸鮑鱟鮺鮜鱠鰂鮳'
SOURCE_BIT_WIDTH = 8
TARGET_BIT_WIDTH = int(math.ceil(math.log2(len(SYMBOLS))))
LCM_OF_WIDTH = TARGET_BIT_WIDTH * SOURCE_BIT_WIDTH // math.gcd(SOURCE_BIT_WIDTH, TARGET_BIT_WIDTH)
SOURCE_TO_TARGET_SLICE_WIDTH = LCM_OF_WIDTH // SOURCE_BIT_WIDTH
TARGET_TO_SOURCE_SLICE_WIDTH = LCM_OF_WIDTH // TARGET_BIT_WIDTH
MASK_SOURCE = (1 << SOURCE_BIT_WIDTH) - 1
MASK_TARGET = (1 << TARGET_BIT_WIDTH) - 1


def chunks(l: Sequence[int], n: int) -> List:
    for i in range(0, len(l), n):
        yield l[i:i+n]


def encode(src: str) -> str:
    array_source = bytearray(src, encoding="utf-8")
    while len(array_source) % SOURCE_TO_TARGET_SLICE_WIDTH != 0:
        array_source.append(0)
    array_target = []
    for chunk in chunks(array_source, SOURCE_TO_TARGET_SLICE_WIDTH):
        num = 0
        for n in chunk:
            num = (num << SOURCE_BIT_WIDTH) | n
        for i in range(TARGET_TO_SOURCE_SLICE_WIDTH):
            array_target.append(
                (num >> ((TARGET_TO_SOURCE_SLICE_WIDTH - 1 - i) * TARGET_BIT_WIDTH)) & MASK_TARGET)
    return ''.join([SYMBOLS[i] for i in array_target])


def decode(src: str) -> str:
    array_target = [SYMBOLS.index(c) for c in src]
    array_source = []
    for chunk in chunks(array_target, TARGET_TO_SOURCE_SLICE_WIDTH):
        num = 0
        for n in chunk:
            num = (num << TARGET_BIT_WIDTH) | n
        for i in range(5):
            array_source.append(
                (num >> (SOURCE_TO_TARGET_SLICE_WIDTH - 1 - i) * SOURCE_BIT_WIDTH) & MASK_SOURCE)
    while array_source[-1] == 0:
        array_source.pop()
    return str(bytearray(array_source), encoding="utf-8")


def is_encoded(path: str) -> bool:
    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(path)
    base_name = os.path.basename(abs_path)
    for c in base_name:
        if SYMBOLS.find(c) == -1:
            return False
    return True


def transform_name(path: str, unary_op: Callable[[str], str]) -> None:
    def skip(file_path: str) -> bool:
        if is_encoded(file_path):
            if unary_op == encode:
                return True
        else:
            if unary_op == decode:
                return True
        return False
    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(path)
    if skip(abs_path):
        return
    dir_name = os.path.dirname(abs_path)
    base_name = os.path.basename(abs_path)

    transformed_base_name = unary_op(base_name)
    os.rename(os.path.join(dir_name, base_name), os.path.join(dir_name, transformed_base_name))


def transform(root_dir: str, unary_op: Callable[[str], str]) -> None:
    dir_list = []
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            dir_list.append(os.path.join(root, d))
        for f in files:
            transform_name(os.path.join(root, f), unary_op)
    for d in reversed(dir_list):
        transform_name(d, unary_op)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="rename1k",
                        description="使用base1k对文件名进行编/解码")
    parser.add_argument("-e", "--encode", action="store_true", dest="encode",
                        default=False, help="对文件名进行编码操作")
    parser.add_argument("-d", "--decode", action="store_true", dest="decode",
                        default=False, help="对文件名进行解码操作")
    parser.add_argument('list', metavar='T', type=str, nargs='+',
                        help='将要被处理的文件或文件夹')
    args = parser.parse_args()

    if args.encode and args.decode:
        print("Error: 这样的操作做不到啊", args)
        sys.exit(1)

    if not args.list:
        if args.encode or args.decode:
            print("Error: 请提供所需编/解码的文件/文件夹")
            sys.exit(1)
        else:
            args.print_help()
            sys.exit(0)

    operation = encode if args.encode else decode

    try:
        for arg in args.list:
            if os.path.isfile(arg):
                transform_name(arg, operation)
            else:
                transform(arg, operation)
                transform_name(arg, operation)
    except ValueError as error:
        print("Error: 源文件名并未被编码")
        sys.exit(1)
