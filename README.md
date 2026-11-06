# AI 中国内容电商保姆级实战教程 🇨🇳

> 作者：**AI 酋长 Andy**｜完全免费开源｜资料复核基准：**2026-11-05**  
> 覆盖：抖音、快手、小红书、视频号/微信小店、淘宝直播  
> 目标：帮助一个没有电商经验的人，用 AI 提高研究、策划、内容、复盘效率，**完成真实的商业验证，而非只看热闹和截图**。

![License](https://img.shields.io/badge/license-MIT-blue) ![docs](https://img.shields.io/badge/chapters-30-5369da) ![cases](https://img.shields.io/badge/real_cases-37-5369da) ![prompts](https://img.shields.io/badge/AI_prompts-26-5369da)

## 先打开完整网站

**离线打开 [site/index.html](site/index.html)** 就能使用：路径选择、章节搜索、37 案例库、三种利润计算器、AI 提示词复制、30 天执行打卡和 CSV 导出。网站没有登录，没有后台，不上传你的经营数据。

GitHub Pages 发布后入口将是 `https://aipmandy.github.io/ai-china-content-commerce-handbook/`（**本仓库目前仅为本地交付，未声称已上线**）。

## 为什么做这个项目

中国内容电商已经不是简单的“拍视频卖货”。从用户需求、选品、供应链、内容、直播、交易、仓储到退款，每个环节都会改变利润。AI 最适合帮普通人消除重复劳动，让选品/素材/数据处理更快，但**AI 不能替代真实产品、真实成交与真实售后**。

很多带货课程只展示大 GMV，而不是现金账。本项目把“付了多少钱、退了多少钱、成本去了哪里”放在教程最前面。

## 5 分钟选对自己的经营路线

| 你现在有什么 | 先走哪条路线 | 第一阶段做什么 | 最大盲点 |
|---|---|---|---|
| 有表达能力，没有货 | 达人/买手分销 | 真实试用一款商品，做3条可挂商品内容 | 样品和内容成本大于佣金 |
| 有靠谱商品和发货能力 | 商家自营 | 筛3款，算单笔贡献再上架 | 广告/退款侵蚀利润 |
| 有老客户/实体门店 | 老客户内容销售 | 拿10个客户常问问题拍内容 | 熟人成交不代表公域有效 |
| 有工厂/产地货源 | 工厂实拍与自播 | 一款商品完成工艺、质检、使用演示 | 生产与履约拖累现金流 |
| 有AI与商业内容能力 | **B端AI电商内容服务** | 诊断1家商家，提交3个样片/脚本和4周试点 | 对GMV负责却无法控制价格与供货 |
| 已有专业垂直IP | 专业内容+匹配商品 | 先征集粉丝购买需求再测3款 | 卖无关商品消耗长期信任 |

**作者适配优先路线**：已有 AI 产品化与企业合作基础时，先验证“商家 AI 内容增效试点”更容易产生可交付样本；有合适供应链后再做自营或分销。这是按资源约束提出的优先次序，不代表项目作者已靠内容电商获得特定收入。

## 开始之前的三项任务（40 分钟）

1. **选一个平台，不铺开五个。** 打开 [平台决策手册](docs/02-platforms.md)，核对当前带货权限、入驻资质、类目、保证金与收费页面，截屏存档。
2. **选一个商品或真实商家。** 填 [需求调研表](templates/demand_research.csv) 与 [SKU 打分卡](templates/sku_scorecard.csv)。没有货可以选择达人真实试用或商家服务诊断。
3. **先算真实贡献。** 用网站[利润计算器](site/index.html#tools)，填成本、佣金、退货、广告与人工。若还拿不到报价，明确标注“模拟”，不把它当决策依据。

## 完整目录

| 资源 | 数量 | 内容 |
|---|---:|---|
| [30章教程](content/) | 30 | 每章：核心逻辑、3个动作、验收物、失败替代、证据来源 |
| [有来源的商家案例](research/) | 37 | 原始URL、结果口径、AI是否披露、可复用动作、无法确认项 |
| [AI Prompt 指令](prompts/) | 26 | 选平台、选品、脚本、直播、售后、成本、B端服务等 |
| [CSV表格模板](templates/) | 14 | 经营漏斗、采购、供应链、财务、客户服务、内容实验、30天现金流 |
| [平台与实战手册](docs/) | 15+ | 6条路径、7天第一单、30/90天、分平台操作、交付与审核 |
| [交互网站](site/index.html) | 1 + 68 | 首页互动及30章/37案例的独立静态页面 |
| [自动测试](tests/) | 17项 | 8项数据一致性+9项财务边界用例；浏览器E2E仍待验证 |
| [完整示例SKU](examples/demo-travel-organizer/) | 7份 | 同一个模拟商品从需求、脚本、上架到直播、经济账的全流程产出 |
| [对抗式审核](docs/13-redteam.md) | 6个角色 | 新手、商家、财务、平台、客户、工程师轮流挑错 |

## 先把完整示例走一遍

以一个**完全虚构的旅行收纳袋**为演练对象，查看 [真实商品上线前必须准备的7份材料](examples/README.md)，包含 [五平台脚本](examples/demo-travel-organizer/03-five-platform-scripts.md)、[商品详情及FAQ](examples/demo-travel-organizer/04-listing-and-faq.md)、[首周财务复盘](examples/demo-travel-organizer/06-week-report.md)。**所有价格与订单都明确是演算样例，不是商业战报**。

## 先学这7章

1. [01｜四种赚钱模型](content/) — 谁付钱、谁背风险。
2. [03｜五平台选择](content/) — 内容、购买人群、供货、开店资格。
3. [04｜需求研究](content/) — 先找到真的想买的人。
4. [05｜SKU经济账](content/) — 算退款后真正剩多少钱。
5. [07｜供应商样品验收](content/) — 真货真证据。
6. [12｜AI脚本一题三拍](content/) — 同一商品只变一个创意。
7. [29｜7天首单演练](content/) — 不许刷单与造假数据。

也可以从 [30天计划](site/index.html#plan) 直接开始执行。

## 37个案例的正确读法

- **商业打法**：例如一本堂用工艺故事和产品改良、世大家展示研发草稿、李嗲在直播间同时讲缺点、范小洛坚持真人直播、飞鱼互动利用 AIGC 量产素材。
- **指标口径**：GMV / 支付GMV / 去购GMV / 直播收入 / 利润完全不同；各来源按原文保留。匿名商家的结果单独降低可核验性。
- **AI归因**：多数经典带货案例**没有公开证据说明使用AI**；平台披露 AIGC 产出也不能证明增长由 AI 单独造成。
- **可复制部分**：一个选品理由、一个真实镜头、一个分销试验、一张成本表。**不复制头部大促预算或利润想象**。

也可阅读 [37案完整索引](CASEBOOK.md)，或直接下载 [37案来源审计CSV](data/cases.csv)，用表格逐案核对。

优先阅读：[一本堂](site/cases/C001.html) · [淳壹亿（AI案例）](site/cases/C002.html) · [合夏（AI案例）](site/cases/C003.html) · [世大家水杯](site/cases/C027.html) · [李嗲](site/cases/C030.html) · [范小洛](site/cases/C031.html) · [阿骏](site/cases/C035.html)。

## AI最应该用在哪

| 环节 | 可交给AI | 必须自己验收 |
|---|---|---|
| 需求调研 | 对真实评论分类、提炼购买理由 | 原始链接、发布时间、是否有购买意图 |
| 选品 | 整理报价、制作打分表 | 实物、供应链、类目资质与售后责任 |
| 内容生产 | 脚本、分镜、字幕、剪辑建议 | 商品真实展示、事实、授权、AI标识 |
| 直播 | 话术清单、切片选点、疑问分类 | 直播实时纠错、人工负责销售承诺 |
| 广告 | 分组计划和数据汇总 | 真实消耗、结算、退款与样本量 |
| 客服 | 已核实FAQ检索、回答提纲 | 退款政策、库存、物流、个人信息 |
| B端服务 | 试点提案、周报与验收清单 | 客户确认、素材授权、付款、交付 |

## 五条硬性口径

1. **不拿 GMV 冒充利润。** 本站财务模型为教学模型，默认数值为假设，字段和退款成本公开可检查。
2. **不发虚构的商品效果、买家秀或直播截图。** 不知道的商品参数必须回到实物/资质检查。
3. **AI生成内容要按规则标识。** 2025-09-01起执行的 [AI生成合成内容标识办法](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm) 以及 2026-02-01起执行的 [直播电商监督管理办法](https://www.cac.gov.cn/2026-01/07/c_1769516655383334.htm) 均值得在开播前核对。
4. **带货/开店门槛、费率、开放功能实时变动。** 教程只提供官方入口，最终核对当前商家后台与所属类目。
5. **真人、供应链、售后、支付和资格不可由AI替代。** 内容做得快，不代表单笔交易真的赚钱。

## 开源项目怎么运行

直接双击 `site/index.html`。所有数据通过同域的静态 `site/data.js` 预置，不依赖本地 HTTP 服务，也不调用第三方数据接口。

重新生成数据和静态页面（Python 3.10+）：

```bash
python scripts/build_data.py
python scripts/build_site.py
python -m unittest discover -s tests -v
```

用于静态站点发布的文件在 `site/`。通过 GitHub Actions 部署 Pages。**部署前先把仓库名称设置为 `ai-china-content-commerce-handbook`；如果改仓库名，需同步更新 `scripts/build_site.py` 中的 `base` 再重新生成 sitemap.xml。**

## 推荐的 GitHub 发布步骤

1. 登录 `https://github.com/new`，创建公开仓库 `ai-china-content-commerce-handbook`，不要提前创建 README、License、gitignore。
2. 在源码目录运行：

```bash
git init
git add .
git commit -m "feat: open-source China AI content commerce playbook"
git branch -M main
git remote add origin https://github.com/AIPMAndy/ai-china-content-commerce-handbook.git
git push -u origin main
```

3. 到 **Settings → Pages → Build and deployment → Source → GitHub Actions**；工作流 `.github/workflows/pages.yml` 在 `main` 分支触发。
4. 到 **Actions** 检查测试和部署，再进入 Pages 链接验收移动端和桌面端。

## 90天商业化路线

会AI、懂商业但还没有货源的人，阅读 [90天B端试点→真实交付→复购路线](docs/17-90-day-go-to-market.md)，只卖能交付和验收的改进，不拍胸脯保证GMV。

## 更新案例与贡献

新增案例必须在 `scripts/build_data.py` 和 `data/sources.json` 中提供：商家身份、平台、发布日期、原始网页、指标口径、是否真的出现 AI、至少一项可学的动作与无法确认项。**不能把推测写成实际收入。** 见 [贡献指南](CONTRIBUTING.md)。

## 作者与愿景

由 **AI 酋长 Andy** 发起，项目愿景：**让更多人类通过 AI 实现财富自由和精神自由。** 免费开放完整方法、学习材料与工具，让更多人拿自己的真实数据去检验一笔生意能不能成立。

[作者 GitHub](https://github.com/AIPMAndy) · [知识库](https://kb.metaver.vip/) · [品牌站](https://metaver.vip/)

MIT License。素材、平台标识、品牌与第三方资料各归原权利人所有；项目案例以简要事实和来源链接呈现，不复制其原文全文。