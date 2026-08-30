# -*- coding: utf-8 -*-
"""
「物理を簡単にする」各話の自己完結 HTML を組み立てる。
外部依存は MathJax の CDN のみ（シリーズ共通の流儀）。CSS は各ファイルに埋め込まれる。

使い方：
    from mkpage import build
    build(out='../wakaru-ct-08-quantum.html', acc='#1d3f56', ops='#9a5a1e',
          title='...', ep='第 8 回 ／ ...', eyebrow='...',
          h1='量子力学に、<br>入れてみる', sub='...', byline_l='...', byline_r='...',
          body=BODY, script=SCRIPT, hint='...')
"""
import io, os

def _hex(c): return tuple(int(c[i:i+2],16) for i in (1,3,5))
def _mix(c, f, base=(255,255,255)):
    r,g,b=_hex(c)
    return '#%02x%02x%02x' % tuple(int(round(f*x+(1-f)*y)) for x,y in ((r,base[0]),(g,base[1]),(b,base[2])))
def _dark(c, f=0.82):
    r,g,b=_hex(c)
    return '#%02x%02x%02x' % (int(r*f),int(g*f),int(b*f))

CSS = """  :root{
    --ink:#1a1c22; --ink-soft:#4a4e5a;
    --paper:{PAPER}; --paper-edge:{EDGE};
    --side:{ACC}; --side-bg:{SIDEBG};
    --warn:#8a4b2f;
    --calc:{CALC}; --calc-bg:{CALCBG};
    --rule:{RULE}; --hair:{HAIR};
    --acc:{ACC};
    --grid:{GRID};
    --ops:{OPS};
    --warnc:#a83a22;
  }
  *{box-sizing:border-box;}
  html{-webkit-text-size-adjust:100%;}
  body{margin:0;background:var(--paper-edge);color:var(--ink);
    font-family:"Hiragino Mincho ProN","Yu Mincho","YuMincho",'Noto Serif JP',serif;
    line-height:1.92;font-size:17px;letter-spacing:.01em;}
  .sheet{max-width:760px;margin:32px auto;background:var(--paper);
    padding:64px 70px 90px;box-shadow:0 1px 0 rgba(0,0,0,.04),0 20px 60px rgba(0,0,0,.10);
    border:1px solid var(--paper-edge);}
  .series{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12px;letter-spacing:.3em;color:var(--acc);margin:0 0 6px;font-weight:700;
    display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px;}
  .series .ep{color:var(--ink-soft);letter-spacing:.14em;font-weight:600;font-size:11.5px;}
  .eyebrow{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12px;letter-spacing:.16em;color:var(--side);margin:0 0 22px;font-weight:600;}
  h1{font-size:37px;line-height:1.28;margin:0 0 8px;font-weight:600;letter-spacing:.02em;}
  h1 .sub{display:block;font-size:17.5px;color:var(--ink-soft);font-weight:400;margin-top:13px;
    letter-spacing:.04em;line-height:1.7;}
  .byline{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12.5px;color:var(--ink-soft);letter-spacing:.06em;margin-top:24px;padding-top:16px;
    border-top:2px solid var(--ink);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;}
  h2{font-size:22px;font-weight:600;margin:52px 0 4px;letter-spacing:.03em;line-height:1.42;}
  h2 .n{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    color:var(--acc);font-size:13px;letter-spacing:.12em;display:block;margin-bottom:3px;font-weight:600;}
  h3{font-size:17px;font-weight:600;margin:28px 0 2px;letter-spacing:.02em;color:#25272e;}
  p{margin:15px 0;}
  .lead{font-size:19px;line-height:1.85;}
  em{font-style:normal;background:linear-gradient(transparent 62%, {EM} 62%);padding:0 .05em;}
  strong{font-weight:600;}

  .aside{margin:24px 0;background:var(--side-bg);border-left:3px solid var(--side);padding:16px 22px;
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:14.5px;line-height:1.8;color:{DEEP};}
  .aside .tag,.caveat .tag,.calc .tag{display:block;font-size:11px;letter-spacing:.2em;font-weight:700;margin-bottom:7px;}
  .aside .tag{color:var(--side);}
  .caveat{margin:24px 0;background:#f6ede4;border-left:3px solid var(--warn);padding:16px 22px;
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:14.5px;line-height:1.8;color:#3f2a1c;}
  .caveat .tag{color:var(--warn);}
  .calc{margin:26px 0;background:var(--calc-bg);border:1px solid {CALCB};border-left:3px solid var(--calc);
    padding:18px 24px 8px;border-radius:2px;}
  .calc .tag{color:var(--calc);font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;}
  .calc .lbl{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:13px;color:var(--calc);font-weight:600;margin:12px 0 -6px;letter-spacing:.04em;}

  .fig{margin:26px 0;padding:18px 20px 20px;background:{FIGBG};border:1px solid var(--rule);border-radius:4px;}
  .fig .cap{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12.5px;color:var(--ink-soft);margin-bottom:10px;letter-spacing:.03em;}
  .fig canvas{width:100%;height:auto;display:block;background:#fff;border:1px solid var(--grid);border-radius:2px;}
  .controls{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin-top:14px;
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:13px;color:var(--ink-soft);}
  .controls label{display:flex;flex-direction:column;gap:4px;min-width:200px;flex:1;}
  .controls .val{color:var(--acc);font-weight:700;}
  input[type=range]{width:100%;accent-color:var(--acc);}
  .readout{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:13.5px;margin-top:10px;padding:9px 13px;border-radius:3px;font-weight:600;line-height:1.6;
    background:var(--calc-bg);color:var(--calc);}
  .legend{display:flex;gap:16px;flex-wrap:wrap;font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12px;color:var(--ink-soft);margin-top:8px;}
  .legend span{display:inline-flex;align-items:center;gap:6px;}
  .swatch{width:14px;height:3px;border-radius:2px;display:inline-block;}

  mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%;}
  .divider{text-align:center;color:var(--hair);letter-spacing:1em;margin:46px 0;font-size:12px;}
  .keybox{margin:30px 0;padding:20px 26px;border:1.5px solid var(--ink);background:{KEYBG};border-radius:2px;}
  .keybox .lbl{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:11px;letter-spacing:.2em;color:var(--ink-soft);font-weight:700;margin-bottom:4px;}

  .tblwrap{overflow-x:auto;margin:26px 0;}
  table.ce{border-collapse:collapse;width:100%;min-width:520px;
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:13.5px;line-height:1.7;}
  table.ce th,table.ce td{border:1px solid var(--rule);padding:10px 13px;text-align:left;vertical-align:top;}
  table.ce thead th{background:var(--calc-bg);color:var(--calc);font-weight:700;font-size:12.5px;letter-spacing:.04em;}
  table.ce tbody th{background:{THBG};font-weight:600;white-space:nowrap;}
  table.ce td.mid{text-align:center;font-variant-numeric:tabular-nums;}
  table.ce tr.hi td,table.ce tr.hi th{background:{HI};}
  table.ce tr.hi{outline:2px solid var(--acc);outline-offset:-2px;}
  table.ce code{font-size:12.5px;}

  .seven{margin:26px 0;border:1px solid var(--rule);border-radius:5px;overflow:hidden;}
  .seven .row{display:flex;gap:14px;padding:13px 18px;border-bottom:1px solid var(--rule);
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:14px;line-height:1.7;}
  .seven .row:last-child{border-bottom:none;}
  .seven .row.hi{background:{HI};}
  .seven .mk{flex-shrink:0;width:24px;font-weight:700;font-size:13px;color:var(--acc);}
  .seven .txt strong{display:block;margin-bottom:2px;}
  .seven .txt span{color:var(--ink-soft);font-size:13px;}

  .prob{margin:30px 0;padding:22px 26px 10px;border:1.5px dashed var(--acc);border-radius:2px;background:{PROBBG};}
  .prob .lbl{font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:11px;letter-spacing:.2em;color:var(--acc);font-weight:700;margin-bottom:10px;}
  .prob ol{margin:0;padding-left:1.3em;} .prob li{margin:10px 0;}
  details{margin-top:12px;font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:14px;}
  summary{cursor:pointer;color:var(--acc);font-weight:600;letter-spacing:.04em;}
  details[open] summary{margin-bottom:8px;} .ans{color:{DEEP};line-height:1.75;}

  .record{margin:52px 0 8px;padding:30px 34px;border:1.5px solid var(--rule);border-radius:2px;
    background:linear-gradient(180deg,{KEYBG},var(--side-bg));}
  .record h2{margin-top:0;} .record p:last-child{margin-bottom:0;}
  .next{margin:24px 0 0;padding:16px 22px;background:var(--calc-bg);border-radius:2px;
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;font-size:14px;color:{DEEP};}
  .next .lbl{font-size:11px;letter-spacing:.2em;color:var(--acc);font-weight:700;margin-bottom:6px;display:block;}
  .foot{margin-top:56px;padding-top:20px;border-top:1px solid var(--rule);
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12px;color:var(--ink-soft);line-height:1.7;letter-spacing:.03em;}

  @media print{
    @page{size:A4;margin:18mm 16mm;}
    body{background:#fff;font-size:11pt;line-height:1.72;}
    .sheet{box-shadow:none;border:none;margin:0;max-width:none;padding:0;}
    h1{font-size:24pt;} h1 .sub{font-size:12.5pt;}
    h2{font-size:15pt;margin-top:24pt;break-after:avoid;} h3{font-size:12.5pt;break-after:avoid;}
    .lead{font-size:12.5pt;}
    .aside,.caveat,.calc,.keybox,.record,.prob,.next,.fig,.tblwrap,.seven{break-inside:avoid;}
    .aside,.caveat,.calc{font-size:9.7pt;}
    .controls{display:none;} details{display:none;} .no-print{display:none;}
  }
  @media (max-width:640px){ .sheet{padding:40px 18px 60px;margin:0;} h1{font-size:26px;} body{font-size:16px;} }
  .hint{max-width:760px;margin:18px auto 0;
    font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",'Noto Sans JP',sans-serif;
    font-size:12.5px;color:{HINT};text-align:center;letter-spacing:.05em;}
"""

PAGE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<script>
  window.MathJax = { tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['$$','$$']]}, svg:{fontCache:'global'} };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js" id="MathJax-script"></script>
<style>
{CSS}</style>
</head>
<body>
<article class="sheet">

<p class="series">物理を簡単にする <span class="ep">{EP}</span></p>
<p class="eyebrow">{EYEBROW}</p>

<h1>{H1}
<span class="sub">{SUB}</span></h1>

<p class="byline"><span>{BYL}</span><span>{BYR}</span></p>

{BODY}

</article>
<p class="hint no-print">{HINT_TEXT}</p>
{SCRIPT}
</body>
</html>
"""

def build(out, acc, ops, title, ep, eyebrow, h1, sub, byline_l, byline_r,
          body, script='', hint='印刷 / PDF 化：⌘+P（Windows は Ctrl+P）。「答えを見る」で解答が開きます。'):
    pal = dict(
        ACC=acc, OPS=ops,
        PAPER=_mix(acc,0.035), EDGE=_mix(acc,0.15),
        SIDEBG=_mix(acc,0.085), CALC=_dark(acc,0.80), CALCBG=_mix(acc,0.115),
        RULE=_mix(acc,0.24), HAIR=_mix(acc,0.38), GRID=_mix(acc,0.125),
        EM=_mix(acc,0.21), DEEP=_dark(acc,0.86), CALCB=_mix(acc,0.30),
        FIGBG=_mix(acc,0.018), KEYBG=_mix(acc,0.010), THBG=_mix(acc,0.065),
        HI=_mix(acc,0.19), PROBBG=_mix(acc,0.075), HINT=_mix(acc,0.62),
    )
    css = CSS
    for k,v in pal.items(): css = css.replace('{'+k+'}', v)
    html = (PAGE.replace('{CSS}', css).replace('{TITLE}', title).replace('{EP}', ep)
                .replace('{EYEBROW}', eyebrow).replace('{H1}', h1).replace('{SUB}', sub)
                .replace('{BYL}', byline_l).replace('{BYR}', byline_r)
                .replace('{BODY}', body).replace('{SCRIPT}', script)
                .replace('{HINT_TEXT}', hint))
    io.open(out,'w',encoding='utf-8').write(html)
    # 簡易検証
    import re
    ok = all(html.count(a)==html.count(b) for a,b in
             [('<article','</article>'),('<style','</style>'),('<canvas','</canvas>'),
              ('<table','</table>'),('<ol','</ol>')])
    dv = len(re.findall(r'<div\b',html)) == html.count('</div>')
    print(f"{os.path.basename(out)}: {len(html)} chars  tags={ok}  div={dv}")
    return ok and dv
