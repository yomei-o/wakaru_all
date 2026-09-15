// 各話 HTML を組み立てる
//   node build.js <出力> "<title>" <theme> body/NN.html
//
// 注意：MathJax の設定行は HTML ソース上で \\( \\) （バックスラッシュ 2 個）
// でなければならない。JS 文字列リテラル '\\(' が \( に評価されて
// MathJax に渡るため。テンプレートリテラル内でのエスケープ段数の事故を
// 避けるため、バックスラッシュは fromCharCode で作る。
const fs = require('fs');
const p = require('path');

const BS = String.fromCharCode(92); // '\'
const MJ = "  window.MathJax = { tex:{inlineMath:[['" + BS + BS + "('," +
           "'" + BS + BS + ")']],displayMath:[['$$','$$']]}, svg:{fontCache:'global'} };";

const common = fs.readFileSync('_css_common.css', 'utf8');
const [, , out, title, theme, bodyf] = process.argv;
const th = fs.readFileSync(p.join('themes', theme + '.css'), 'utf8');
const body = fs.readFileSync(bodyf, 'utf8');

const html = `<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title}</title>
<script>
${MJ}
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js" id="MathJax-script"></script>
<style>
${th}${common}</style>
</head>
<body>
${body}</body>
</html>
`;

fs.writeFileSync(out, html);

// 検査：設定行が \\( \\) になっているか
const line = html.split('\n').find(s => s.indexOf('inlineMath') >= 0);
const ok = line.indexOf("['" + BS + BS + "('") >= 0;
console.log((ok ? 'OK   ' : 'BAD  ') + out + '  ' + html.length + ' bytes');
if (!ok) { console.error('  MathJax 設定行が壊れています: ' + line); process.exit(1); }
