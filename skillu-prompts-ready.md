# SkillU GIF 提示词 — 可用清单（备稿，2026-11-06）

回答 2026-11-05 用户问题“这些提示词都放 skillu 里面去了么”：**还没有**。
15 条 GIF 里，能进 SkillU / 仓库 prompt 区的只有下面两条，其余 13 条作者没公开提示词。
本文件只整理、不发布；发布前需用户点头，且仓库 README 第 13 行“0 shared prompts”
与 x-cases 记录的李岳条目自相矛盾，需先定口径（见末尾）。

## 可用的两条

### 1. 李岳 @liyue_ai — 鸡你太美 3D 公鸡篮球舞（Meme）
- 原帖：https://x.com/liyue_ai/status/2118183557315371229
- 内容：穿背带裤的黄色 3D 卡通公鸡表演篮球舞蹈（接球、胯下运球、抛球、魔性跳舞）。
- 提示词状态：**逐字原文已确认**。2026-11-06 浏览器任务重读原帖核实：作者在帖中以
  “完整提示词：”引出，全文分【角色设定】【经典动作还原】【动画风格】【GIF 输出要求】
  四节，动作按接球→胯下运球→花式运球→抛球转唱跳→扭胯甩头五步展开，要求 1:1、
  约 4–5 秒、可循环。全文见原帖，不在此复述；入库时按仓库惯例（有公开 prompt 保留原文、
  链原帖、署作者）把原文写进 `prompts/rooster-basketball-dance.md`。
- 结论：这是 15 条里唯一一条可逐字发表的 prompt，SkillU 展示页和仓库都可以直接用，
  须保留作者署名与原帖链接。

### 2. 蓝哥AI @0xlangeai — 推胸动作拆解（健身动作拆解）
- 原帖：https://x.com/0xlangeai/status/2118186890352607550
- 作者原话（可逐字引用的一句话做法）：“让它做个健身推胸的 GIF”。
- 提示词状态：**一句话做法，非完整提示词**。可进 SkillU 当“作者原话”，不能冒充完整 prompt。

## 其余 13 条：无提示词
- 深蹲、硬拉（蓝哥AI）：未公开。data/gifs.json 中 prompt_status 均为 not-shared。
- 其余 11 条（金毛跳舞、GM 比心、水彩婴儿、像素小人、企鹅表情、紫发女孩、
  GPT 与 Claude 跳舞、月夜小屋、猫、圆头小人等）：x-cases 均记“未公开”。
- 按 2026-10-24 用户拍板：没有真实 prompt 的作品，整个 Prompt 区域不渲染，
  不写缺失说明、不贴占位文字。

## 待用户定的两件事
1. 李岳这条已确认是逐字原文，可直接按“有公开 prompt 保留原文”入库与上 SkillU；
   唯一待定的是等仓库建好一起推，还是先上 SkillU 展示页。
2. 口径矛盾已解决：README 说 0 条共享提示词是错的（x-cases 是对的），
   README 第 13、89 行需改写为 1 条逐字 prompt（李岳），其余 14 条无 prompt。

## 来源
- ~/workspace/gpt-images-2-6-gif-repo-staging/data/x-cases-2026-11-05.md（12 条 X 案例，2026-11-05 核实）
- ~/workspace/gpt-images-2-6-gif-repo-staging/data/gifs.json（仅 3 条健身条目，其余 12 条尚未入库）
- ~/workspace/gpt-images-2-6-gif-repo-staging/README.md（第 13、89 行）
