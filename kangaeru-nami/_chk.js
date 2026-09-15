const fs=require('fs');
const f=process.argv[2];
const s=fs.readFileSync(f,'utf8');
const B=String.fromCharCode(92);
let o=0,c=0;
for(let i=0;i<s.length-1;i++){if(s[i]===B&&s[i+1]==='(')o++;if(s[i]===B&&s[i+1]===')')c++;}
const dd=(s.match(/[$][$]/g)||[]).length;
const dvo=(s.match(/<div/g)||[]).length, dvc=(s.match(/<\/div>/g)||[]).length;
const tbo=(s.match(/<table/g)||[]).length, tbc=(s.match(/<\/table>/g)||[]).length;
console.log(f,'inline',o,c,' $$',dd,' div',dvo,dvc,' table',tbo,tbc, (o===c&&dd%2===0&&dvo===dvc&&tbo===tbc)?'OK':'NG');
