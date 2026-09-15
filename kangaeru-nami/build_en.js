// 英語版の各話 HTML を組み立てる（出力は ../kangaeru-nami-en/）
//   node build_en.js <出力名> "<title>" <theme> body-en/NN.html
//
// 注意：MathJax の設定行は HTML ソース上で \\( \\) でなければならない。
// build.js と同じ理由でバックスラッシュは fromCharCode で作る。
const fs = require('fs');
const p = require('path');

const BS = String.fromCharCode(92); // '\'
const MJ = "  window.MathJax = { tex:{inlineMath:[['" + BS + BS + "('," +
           "'" + BS + BS + ")']],displayMath:[['$$','$$']]}, svg:{fontCache:'global'} };";

const common = fs.readFileSync('_css_common.css', 'utf8');
const [, , out, title, theme, bodyf] = process.argv;
const th = fs.readFileSync(p.join('themes', theme + '.css'), 'utf8');
const body = fs.readFileSync(bodyf, 'utf8');

const OUTDIR = p.join('..', 'kangaeru-nami-en');
if (!fs.existsSync(OUTDIR)) fs.mkdirSync(OUTDIR);

const html = `<!DOCTYPE html>
<html lang="en">
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

const dest = p.join(OUTDIR, out);
fs.writeFileSync(dest, html);

// 検査：設定行が \\( \\) になっているか
const line = html.split('\n').find(s => s.indexOf('inlineMath') >= 0);
const ok = line.indexOf("['" + BS + BS + "('") >= 0;
console.log((ok ? 'OK   ' : 'BAD  ') + dest + '  ' + html.length + ' bytes');
if (!ok) { console.error('  MathJax setting line is broken: ' + line); process.exit(1); }
