// 目次 index.html を組み立てる
//   node build_index.js
// MathJax 設定行の注意は build.js と同じ。
const fs = require('fs');

const BS = String.fromCharCode(92); // '\'
const MJ = "  window.MathJax = { tex:{inlineMath:[['" + BS + BS + "('," +
           "'" + BS + BS + ")']],displayMath:[['$$','$$']]}, svg:{fontCache:'global'} };";

const css = fs.readFileSync('_css_index.css', 'utf8');
const body = fs.readFileSync('body/index.html', 'utf8');

const root = `  :root{
    --ink:#1a1c22; --ink-soft:#4a4e5a;
    --paper:#f5f7fa; --paper-edge:#d7dee8;
    --side:#17304f; --side-bg:#e9eef6;
    --rule:#c9d4e2; --hair:#a8b8cc;
    --acc:#1c3f63; --ops:#a85a12;
  }
`;

const html = `<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>考える波 ── シリーズ目次</title>
<script>
${MJ}
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js" id="MathJax-script"></script>
<style>
${root}${css}</style>
</head>
<body>
${body}</body>
</html>
`;

fs.writeFileSync('index.html', html);

const line = html.split('\n').find(s => s.indexOf('inlineMath') >= 0);
const ok = line.indexOf("['" + BS + BS + "('") >= 0;
console.log((ok ? 'OK   ' : 'BAD  ') + 'index.html  ' + html.length + ' bytes');
if (!ok) { console.error('  MathJax 設定行が壊れています: ' + line); process.exit(1); }
