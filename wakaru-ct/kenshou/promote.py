# -*- coding: utf-8 -*-
"""目次で、準備中の mini 行を公開カードに昇格させる。"""
import io,re,sys
def promote(num, href, h3, desc, key, extra=''):
    p='../index.html'
    s=io.open(p,encoding='utf-8').read()
    m=re.search(r'<li><span class="num">第%d回</span>.*?</li>\n'%num, s, re.S)
    if not m: print('mini 行が見つかりません: 第%d回'%num); return False
    s=s[:m.start()]+s[m.end():]
    card=('<a class="ep" href="%s">\n'
          '  <span class="no">第 %d 回 <span class="badge b-new">公開</span> '
          '<span style="color:#5f6a7a;font-weight:600">動く図つき</span>%s</span>\n'
          '  <h3>%s</h3>\n  <p>%s</p>\n  <span class="key">%s</span>\n</a>\n\n') % (href,num,extra,h3,desc,key)
    nxt=re.search(r'<ol class="mini">\n<li><span class="num">第%d回</span>'%(num+1), s)
    if nxt: s=s[:nxt.start()]+card+s[nxt.start():]
    else:
        li=re.search(r'<li><span class="num">第%d回</span>'%(num+1), s)
        if li:
            ol=s.rfind('<ol class="mini">',0,li.start())
            s=s[:ol]+card+s[ol:]
        else:
            # 最後の 1 本：空になった mini リストを取り除き、その位置に置く
            m2=re.search(r'<ol class="mini">\s*</ol>\s*', s)
            if m2:
                s=s[:m2.start()]+card+s[m2.end():]
            else:
                print('挿入位置が見つかりません'); return False
    io.open(p,'w',encoding='utf-8').write(s)
    o=len(re.findall(r'<div\b',s)); c=s.count('</div>')
    print('index: a.ep=%d  div %d/%d %s'%(s.count('<a class="ep"'),o,c,'OK' if o==c else '*** MISMATCH ***'))
    return True
