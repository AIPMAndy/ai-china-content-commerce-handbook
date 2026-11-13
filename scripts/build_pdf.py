#!/usr/bin/env python3
"""Build a print-quality, source-linked PDF from this repository's public content."""
import argparse
import html
import json
import os
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/'data'

def esc(x):
    return html.escape(str('' if x is None else x),quote=True)

def link(url,label):
    url=str(url or '').strip()
    return f'<a href="{esc(url)}">{esc(label)} ↗</a>' if urlparse(url).scheme in ('http','https') else esc(label)

def card(number,title,body,typ=''):
    return f'<article class="card {typ}"><div class="overline">{esc(number)}</div><h3>{esc(title)}</h3>{body}</article>'

CSS=r"""
@page{size:A4;margin:20mm 19mm 19mm;@top-left{content:"AI CHIEF ANDY / CONTENT COMMERCE";font-size:8pt;letter-spacing:.08em;color:#586577}@top-right{content:"OPEN-SOURCE HANDBOOK";font-size:8pt;color:#8290a0}@bottom-left{content:"星觉科技  ·  AIPMAndy";font-size:8pt;color:#586577}@bottom-right{content:counter(page);font-size:8pt;color:#586577}}
@page:first{margin:0;@top-left{content:none}@top-right{content:none}@bottom-left{content:none}@bottom-right{content:none}}
*{box-sizing:border-box}html{font-family:"Noto Sans CJK SC","Noto Sans SC",sans-serif;font-size:10pt;color:#1c2835}body{margin:0;line-height:1.65}
.cover{height:297mm;background:#101c2c;color:#fff;padding:35mm 28mm 24mm;page-break-after:always;position:relative}
.cover .overline{color:#8ab4f5;letter-spacing:.16em;font-size:10pt;margin-bottom:19mm}
.cover h1{font-size:34pt;line-height:1.2;letter-spacing:-.035em;margin:0 0 15mm;font-weight:730}
.cover .subtitle{font-size:14pt;line-height:1.8;color:#d3dae4;max-width:125mm}
.cover .ruleline{height:1px;background:#526477;margin-top:30mm;margin-bottom:11mm}
.cover .stats{display:flex;gap:14mm;margin:18mm 0 19mm}.cover .stat b{font-size:25pt;color:#fff;display:block;line-height:1.1}.cover .stat span{color:#bdcadd;font-size:8.6pt}
.cover .imprint{position:absolute;left:28mm;bottom:24mm;color:#abb9c7;font-size:9pt}
.head{border-bottom:1px solid #dce2e9;padding-bottom:6mm;margin-bottom:8mm;page-break-after:avoid}
.head h2{font-size:24pt;line-height:1.22;letter-spacing:-.035em;margin:2.5mm 0 1mm}.head p{font-size:10pt;color:#667281;margin:1mm 0}
.overline{font-size:8pt;font-weight:750;letter-spacing:.11em;color:#2457b2}
.intro{page-break-after:always}.lead{color:#4c5d70;font-size:10.2pt;margin:3mm 0 5mm}
.card{border:1px solid #dfe5ed;border-radius:4mm;padding:6mm 7mm;margin-bottom:5.5mm;background:#fff;break-inside:avoid}
.card h3{font-size:15pt;line-height:1.33;letter-spacing:-.025em;margin:2mm 0 3mm;color:#16253a}
.card p{font-size:9.3pt;margin:2mm 0}.card h4{font-size:9pt;color:#192d45;margin:4mm 0 1.8mm}
.card ol{padding-left:6mm;margin:2mm 0 3mm}.card li{padding-left:.5mm;margin:1mm 0;font-size:9.2pt}
.chapter{break-inside:auto}.chapter h3{font-size:16pt}.chapter .overline{font-size:7.8pt}
.chapter-sub{font-size:8pt;color:#69798a}.rule{background:#eff3f8;border-left:3px solid #426ab0;padding:3mm 4mm}
.rule p{margin:1mm 0}.decision{border-top:1px solid #e1e7ee;border-bottom:1px solid #e1e7ee;padding:3mm 0;margin:5mm 0 3mm}.decision p{margin:0}
.small{font-size:8.7pt!important;color:#667281}.source-list{margin:2mm 0;padding-left:6mm}.source-list li{font-size:8.2pt;margin:.7mm 0}
a{color:#2457b2;text-decoration:none}.source-date{color:#7a8794;margin-left:1mm;font-size:7.3pt}
.route{break-inside:avoid}.route dl{margin:0}.route dt{font-size:8.5pt;font-weight:700;color:#2457b2;margin-top:2mm}.route dd{margin:0 0 1.5mm;font-size:9.2pt}
.case{break-inside:avoid;margin-bottom:4mm}.case h3{font-size:13.5pt}.case p{font-size:8.7pt;margin:1.8mm 0}
.fact{font-size:7.8pt;color:#6b7890;background:#f0f3f7;padding:1.5mm 3mm;border-radius:3mm;display:inline-block}
.days{margin:8mm 0 12mm;break-inside:avoid}.day-table{border-collapse:collapse;width:100%;font-size:8.8pt;margin:2.3mm 0}
.day-table td{padding:2.9mm 3.6mm;border-bottom:1px solid #e2e7ee;vertical-align:top}.daynum{font-size:15pt;color:#2457b2;font-weight:700;width:16mm}
.day-table b{display:block}.day-table span{color:#687585;font-size:7.7pt}
.note{background:#f1f4f8;border-left:3px solid #2457b2;padding:5mm 6mm;border-radius:2mm;margin:7mm 0}
.contact{page-break-before:always;background:#111d2d;color:#fff;min-height:215mm;padding:25mm 20mm 14mm}
.contact .overline{color:#91baff}.contact h2{font-size:30pt;line-height:1.24;letter-spacing:-.035em;margin:8mm 0 10mm}
.contact p{color:#c4d2df;font-size:11pt;line-height:1.85}.contact .contact-box{margin-top:19mm;border-top:1px solid #52647a;padding-top:9mm}
.contact .contact-box p{margin:2mm 0;font-size:10pt}.contact a{color:#d8e6fb;word-wrap:break-word}
.contact .legal{font-size:8.6pt;line-height:1.85;color:#a5b4c5;margin-top:24mm}
"""

def make(chapters,cases,routes,days,sources,date):
    src={x['id']:x for x in sources}
    routes_html=''
    for i,r in enumerate(routes,1):
        desc=f'<p class="lead">{esc(r.get("intro"))}</p><dl><dt>先完成</dt><dd>{esc(r.get("first"))}</dd><dt>开始门槛</dt><dd>{esc(r.get("gate"))}</dd><dt>风险边界</dt><dd>{esc(r.get("danger"))}</dd></dl>'
        routes_html+=card(f'ROUTE {i:02d} / {r.get("platform","")}',r.get('title',''),desc,'route')
    chapters_html=''
    for i,ch in enumerate(chapters,1):
        steps=''.join(f'<li>{esc(x)}</li>' for x in ch.get('steps',[]))
        refs=''
        for id in ch.get('relatedSources',[]):
            s=src.get(id)
            if s:refs+=f'<li>{link(s.get("url"),s.get("title"))} <span class="source-date">{esc(s.get("date"))} · {esc(s.get("kind"))}</span></li>'
        body=(f'<div class="chapter-sub">{esc(ch.get("phase"))} · 预计 {esc(ch.get("time"))}</div>'
              f'<p class="lead">{esc(ch.get("goal"))}</p><div class="rule"><b>本章关键</b><p>{esc(ch.get("core"))}</p></div>'
              f'<h4>照着执行</h4><ol>{steps}</ol><div class="decision"><b>验收标准</b><p>{esc(ch.get("accept"))}</p></div>'
              f'<p class="small"><b>边界与失败处理：</b>{esc(ch.get("limit"))}</p>'
              + (f'<h4>官方或原始参考</h4><ul class="source-list">{refs}</ul>' if refs else ''))
        chapters_html+=card(f'CHAPTER {i:02d} / {ch.get("deliverable","")}',ch.get('title',''),body,'chapter')
    cases_html=''
    for cs in cases:
        s=src.get(cs.get('source'),{})
        body=(f'<div class="fact">{esc(cs.get("platform"))} · {esc(cs.get("period"))} · {esc(cs.get("evidence_tier","待核实"))}</div>'
              f'<p><b>来源披露：</b>{esc(cs.get("result"))}。这不等于净利润，也不代表本项目作者的业务成果。</p>'
              f'<p><b>公开做法：</b>{esc(cs.get("play"))}</p><p><b>AI 使用：</b>{esc(cs.get("ai"))}</p>'
              f'<p><b>可复用动作：</b>{esc(cs.get("takeaway"))}</p><p class="small">限制：{esc(cs.get("caution"))}</p>'
              f'<p class="small"><b>原始来源：</b>{link(s.get("url"),s.get("title","查阅来源"))}</p>')
        cases_html+=card(cs.get('id','CASE'),cs.get('name',''),body,'case')
    groups=''
    for i in range(0,len(days),10):
        table=''
        for day in days[i:i+10]:
            table+=f'<tr><td class="daynum">{esc(day.get("day"))}</td><td><b>{esc(day.get("title"))}</b><span>{esc(day.get("proof"))}</span></td></tr>'
        groups+=f'<section class="days"><div class="overline">SPRINT {i//10+1:02d}</div><table class="day-table">{table}</table></section>'
    page=lambda number,title,subtitle:f'<header class="head"><div class="overline">{number}</div><h2>{title}</h2><p>{subtitle}</p></header>'
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>AI 中国内容电商保姆级实战手册 · AI 酋长 Andy</title><meta name="author" content="AI 酋长 Andy"><style>{CSS}</style></head><body>
<section class="cover"><div class="overline">XINGJUE TECHNOLOGY / OPEN KNOWLEDGE</div><h1>AI 中国内容电商<br>保姆级实战手册</h1>
<p class="subtitle">从选对商业模式到完成真实生意验证。用 AI 提高效率，但不靠夸张截图、伪造数据或空洞模板。</p>
<div class="ruleline"></div><div class="stats"><div class="stat"><b>{len(chapters):02d}</b><span>实操章节</span></div><div class="stat"><b>{len(cases):02d}</b><span>公开来源案例</span></div><div class="stat"><b>{len(routes):02d}</b><span>商业路线</span></div><div class="stat"><b>{len(days):02d}</b><span>行动计划天数</span></div></div>
<div class="imprint">AI 酋长 Andy / 星觉科技<br>微信 AIPMAndy · metaver.vip · a6no1.cn<br>PDF 生成日期：{esc(date)} · 免费开源</div></section>
<section class="intro">{page('00 / READ FIRST','从真实问题出发','不是“看了就能赚钱”，而是每一步留下证据。')}
<div class="note"><b>使用顺序</b><p>选商业路径 → 按章节做实验 → 用原始数据算净贡献 → 复盘并调整。第三方商业案例仅按来源披露，不代表作者实绩。</p></div>
<p><b>包含：</b>30章实操、案例拆解、30天行动表、官方来源；在线版还有筛选工具、利润计算器和进度记录。</p>
<p><b>不包含：</b>保证成交、固定收益预测、账号权限代办或未经授权的客户联系方式。</p>
<p><b>互动网站：</b>{link('https://aipmandy.github.io/ai-china-content-commerce-handbook/','阅读网站与利润测算')}</p>
<p><b>源代码：</b>{link('https://github.com/AIPMAndy/ai-china-content-commerce-handbook','GitHub 开源仓库')}</p>
<div class="note"><b>更新原则</b><p>平台规则、费用和直播政策经常变化，按实际官方入口为准。没有公开净利润，就不要把 GMV 或销售额写成利润。</p></div>
</section>
{page('PART 01 / BUSINESS PATHWAYS','选择一条商业路线','优先验证一个模型，避免把资源分散到五个平台。')}{routes_html}
{page('PART 02 / ACTIONABLE HANDBOOK','30 章 · 一章一个交付物','每章保留目标、执行动作、验收标准和来源。')}{chapters_html}
{page('PART 03 / PUBLIC SOURCES','公开案例 · 学动作，不抄业绩','所有案例均来自公开来源，证据等级与未知条件明确标示；不是作者客户案例。')}{cases_html}
{page('PART 04 / 30 DAY SPRINT','30 天行动清单','完成任务不代表获得了收入。')}{groups}
<section class="contact"><div class="overline">PART 05 / CONTACT & COOPERATION</div><h2>把方案落地到<br>你的真实业务。</h2>
<p>本手册永久免费。如果你是商家、创作者或企业负责人，正在评估 AI 如何用于获客、内容运营和业务流程，欢迎带着具体问题与证据来沟通。</p>
<div class="contact-box"><p><b>微信：</b>AIPMAndy（搜索添加）</p>
<p><b>个人官网：</b>{link('https://metaver.vip/','metaver.vip')}</p><p><b>公司官网：</b>{link('https://www.a6no1.cn/','www.a6no1.cn')}</p>
<p><b>咨询服务：</b>{link('https://metaver.vip/services','metaver.vip/services')}</p>
<p><b>开源仓库：</b>{link('https://github.com/AIPMAndy/ai-china-content-commerce-handbook','GitHub / AIPMAndy')}</p></div>
<p class="legal">免责声明：本资料仅供学习与实验，不承诺流量、成交、收益或排名。第三方案例是原始来源的公开披露，具体资质、平台收费与适用规则以实时官方信息为准。</p>
</section></body></html>'''

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default=str(ROOT/'site'/'downloads'/'ai-china-content-commerce-handbook.pdf'))
    parser.add_argument('--date',default=os.environ.get('PDF_EDITION_DATE','2026-11-14'))
    args=parser.parse_args()
    data={n:json.loads((DATA/f'{n}.json').read_text(encoding='utf-8')) for n in ('chapters','cases','routes','plan30','sources')}
    for n,v in data.items():
        if not isinstance(v,list):raise ValueError(f'{n}: expected a list')
    from weasyprint import HTML
    target=Path(args.output).resolve()
    target.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=make(data['chapters'],data['cases'],data['routes'],data['plan30'],data['sources'],args.date),base_url=str(ROOT)).write_pdf(target)
    if target.stat().st_size < 25000 or target.read_bytes()[:4]!=b'%PDF':
        raise RuntimeError('Generated PDF failed validation')
    print(f'PDF: {target}; chapters={len(data["chapters"])} cases={len(data["cases"])} bytes={target.stat().st_size}')

if __name__=='__main__':main()
