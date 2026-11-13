# PDF 出版规范

- 源数据：data/chapters.json、data/cases.json、data/routes.json、data/plan30.json、data/sources.json
- 构建命令：python -m pip install weasyprint==68.0；系统安装 fonts-noto-cjk；python scripts/build_pdf.py
- 产物：site/downloads/ai-china-content-commerce-handbook.pdf（Pages）；pdf/ai-china-content-commerce-handbook-guide.pdf（GitHub 仓库）
- 视觉：A4、深海军蓝封面、黑白正文、克制品牌蓝、中文 Noto Sans CJK 字体、可点击来源、页码。
- 联系方式：微信 AIPMAndy、个人官网 https://metaver.vip/、公司官网 https://www.a6no1.cn/。
- 所有商业案例只可引用已列的公开来源；GMV/营收与利润必须区分；不使用虚构客户、成交或 AI 贡献因果。
- CI：每次构建生成 PDF，检查文件类型、长度和可提取中文文本；生成结果由 GitHub Actions 提交。
- 发布后还需要独立 PDF 阅读器渲染检查、移动端验证，CI 成功不能替代视觉 QA。
