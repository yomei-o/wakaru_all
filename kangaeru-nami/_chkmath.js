const fs = require('fs');
const BS = String.fromCharCode(92);
// 英文の中の "pi"（predictions など）を拾わないよう、前後が英字でない場合だけ数える
const CMD = /(?<![A-Za-z])(Delta|alpha|beta|omega|lambda|sqrt|frac|times|approx|cdot|ell|tau|phi|mu|Gamma|gamma|infty|propto|Box|partial|pi)(?![A-Za-z])/g;

['body/index.html', 'body-en/index.html'].forEach(function (p) {
  const L = fs.readFileSync(p, 'utf8').split('\n');
  console.log('=== ' + p + ' ===');
  let ep = '?';
  const broken = new Set();
  L.forEach(function (l, i) {
    const m = l.match(/kangaeru-nami-(\d+)-/);
    if (m) ep = m[1];
    if (l.indexOf('<p>') < 0 && l.indexOf('<br>') < 0) return;
    // その行のバックスラッシュの数と、LaTeX 命令らしき語の数を比べる
    let bs = 0;
    for (const ch of l) if (ch === BS) bs++;
    const cmds = (l.match(CMD) || []).length;
    if (cmds >= 3 && bs === 0) broken.add(ep);
  });
  console.log('  バックスラッシュが全部 消えている回: ' + (broken.size ? [...broken].sort().join(', ') : 'なし'));
});
