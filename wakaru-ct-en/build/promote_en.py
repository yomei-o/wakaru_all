# -*- coding: utf-8 -*-
"""mkindex.py の mini リストに入っている回を、card に昇格させる。
使い方:  python promote_en.py  したあと mkindex.py を実行する。
下の PROMO に (番号, href, 見出し, 説明, キー) を足していく。"""
import io
import re
import sys


def promote(num, href, title, desc, key, path='mkindex.py'):
    s = io.open(path, encoding='utf-8').read()
    # mini リストから該当行を消す
    pat = re.compile(r"^ \(%d,'.*?'\),\n" % num, re.M)
    if not pat.search(s):
        print('  ep%d: mini entry not found (already promoted?)' % num)
        return False
    s = pat.sub('', s)
    # apos-guard: a straight apostrophe would break the single-quoted Python string
    title=title.replace(chr(39),chr(0x2019)); desc=desc.replace(chr(39),chr(0x2019)); key=key.replace(chr(39),chr(0x2019))
    card = ("BODY += card(%d,'%s','%s',\n  '%s',\n  '%s')\n\n"
            % (num, href, title, desc, key))
    # 直後の mini ブロックの直前に card を挿す
    idx = s.find('BODY += mini([')
    while idx != -1:
        block_end = s.find('])', idx)
        block = s[idx:block_end]
        nums = [int(m) for m in re.findall(r'^ \((\d+),', block, re.M)]
        if nums and min(nums) > num:
            s = s[:idx] + card + s[idx:]
            break
        idx = s.find('BODY += mini([', idx + 1)
    else:
        # last episode: no mini block follows, so append after the final card
        marker = "BODY += card("
        last = s.rfind(marker)
        if last == -1:
            print('  ep%d: no insertion point' % num)
            return False
        end = s.find("')\n\n", last)
        if end == -1:
            print('  ep%d: could not find the end of the last card' % num)
            return False
        end += len("')\n\n")
        s = s[:end] + card + s[end:]
        # drop the now-empty mini list, if any
        s = re.sub(r"BODY \+= mini\(\[\s*\]\)\n+", '', s)
    io.open(path, 'w', encoding='utf-8').write(s)
    print('  ep%d promoted' % num)
    return True


if __name__ == '__main__':
    import json
    if len(sys.argv) == 2:
        rows = json.load(io.open(sys.argv[1], encoding='utf-8'))
    else:
        rows = []
    for r in rows:
        promote(*r)
