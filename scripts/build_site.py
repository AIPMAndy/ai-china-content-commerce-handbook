from pathlib import Path
import json,html,shutil,urllib.parse
ROOT=Path(__file__).resolve().parent.parent
D=ROOT/'data';SITE=ROOT/'site'
keys=['cases','chapters','prompts','routes','plan30','sources'];obj={k:json.loads((D/(k+'.json')).read_text(encoding='utf-8')) for k in keys}
(SITE/'data.js').write_text('window.HANDBOOK_DATA = '+json.dumps(obj,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
for sub in ('chapters','cases'):(SITE/sub).mkdir(exist_ok=True)
S={x['id']:x for x in obj['sources']}
def esc(x):return html.escape(str(x),quote=True)
def wrap(title,body,description):
 return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0d142c"><meta name="description" content="{esc(description[:150])}"><title>{esc(title)}｜AI中国内容电商实战手册</title><link rel="stylesheet" href="../assets/style.css"><link rel="icon" href="../assets/favicon.svg" type="image/svg+xml"></head><body><header class="nav"><div class="container navin"><a class="brand" href="../index.html">AI 酋长 <b>ANDY</b> / 内容电商手册</a><nav class="links"><a href="../index.html#routes">选路径</a><a href="../index.html#chapters">30章</a><a href="../index.html#cases">案例</a><a href="../index.html#tools">利润工具</a><a href="../index.html#plan">执行计划</a></nav></div></header><main class="detail"><div class="container"><article class="detail-wrap">{body}</article></div></main><footer class="footer"><div class="container">AI 酋长 Andy · 以真实证据验证一笔生意 · <a href="../index.html">返回首页</a></div></footer></body></html>'''
for c in obj['chapters']:
 paragraphs=''.join(f'<li>{esc(step)}</li>' for step in c['steps']); refs=''.join(f'<li><a class="source" href="{esc(S[id]["url"])}" target="_blank" rel="noopener noreferrer">{esc(S[id]["title"])} ↗</a></li>' for id in c['relatedSources'])
 body=f'''<span class="tag">第 {c['id']} 章 · {esc(c['phase'])} · {esc(c['time'])}</span><h1>{esc(c['title'])}</h1><p class="lead">{esc(c['goal'])}</p><section class="callout"><strong>核心知识</strong><p>{esc(c['core'])}</p></section><h2>从0跟着做</h2><ol>{paragraphs}</ol><h2>验收标准</h2><p>{esc(c['accept'])}</p><h2>做不下去怎么办</h2><p>{esc(c['limit'])}</p><p>遇到账号资格、样品、预算等阻塞，记录阻塞原因与官方入口，改做不依赖该资格的内容小样，不能假装成功或成交。</p><h2>本章留下什么证据</h2><p>将原始来源URL/截图、操作日期、结果与下一步写入私有执行日志。若含客户、订单或个人信息，脱敏后才可公开。</p><h2>官方资料</h2><ul>{refs}</ul><p><a class="btn" href="../index.html#chapters">返回课程目录 →</a></p>'''
 (SITE/'chapters'/f'{c["id"]}.html').write_text(wrap(c['title'],body,c['goal']),encoding='utf-8')
for c in obj['cases']:
 s=S[c['source']];body=f'''<span class="tag">真实案例 {c['id']} · {esc(c['platform'])}</span><h1>{esc(c['name'])}</h1><p class="lead">{esc(c['model'])} · {esc(c['period'])} · 证据等级：{esc(c['evidence_tier'])}</p><div class="callout"><strong>来源披露的业绩（不等于利润）</strong><p>{esc(c['result'])}</p></div><h2>对方做了什么</h2><p>{esc(c['play'])}</p><h2>AI 在里面起了什么作用</h2><p>{esc(c['ai'])}</p><p>是否披露AI：{'是' if c['ai_disclosed'] else '否'}；是否披露净利润：{'是' if c['profit_disclosed'] else '否'}。</p><h2>能借鉴的最小动作</h2><p>{esc(c['takeaway'])}</p><h2>30 分钟实操复刻</h2><ol><li>选一个有真实样品或合法合作授权的商品。</li><li>只复刻其中一项内容打法，先写短视频/笔记脚本。</li><li>留作品、成本与可复核证据；未知数字写“未知”。</li><li>获得真实反馈后判断是商品问题还是内容问题。</li></ol><h2>来源与无法确认项</h2><p><a class="source" href="{esc(s['url'])}" target="_blank" rel="noopener noreferrer">查看原始来源：{esc(s['title'])} ↗</a></p><p>{esc(c['caution'])}</p><p>来源性质：{esc(s['kind'])}。结果属于当事商家/平台/报道披露，尚不等于独立财务审计。AI出现和业绩发生不能直接证明因果。</p><p><a class="btn" href="../index.html#cases">返回案例库 →</a></p>'''
 (SITE/'cases'/f'{c["id"]}.html').write_text(wrap(c['name'],body,c['play']),encoding='utf-8')
(SITE/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8')
base='https://aipmandy.github.io/ai-china-content-commerce-handbook/'
urls=[base]+[base+'chapters/'+x['id']+'.html' for x in obj['chapters']]+[base+'cases/'+x['id']+'.html' for x in obj['cases']]
(SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{html.escape(url)}</loc></url>\n' for url in urls)+'</urlset>\n',encoding='utf-8')
print('built',len(urls),'static pages + SPA')
