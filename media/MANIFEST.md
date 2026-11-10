# Media Manifest — GPT Images 2.6 GIF Showcase

Video: `../video/gpt-images-2.6-gif-showcase-16x9.mp4`
（1280×720, H.264 + 无音频, yuv420p, 55.97s, 6,409,095 bytes ≈ 6.1 MiB）
结构：片头 3s + 15 条片段 + 片尾 3s；每条带底部字幕（标题 + @作者 · 分类）。
素材来源：2026-11-05 自 X 原帖页面以 curl 抓取的 tweet_video mp4（未登录、未上传、未发布）。

| # | slug | 来源原帖 | 创作者 | 分类 | 本地文件 |
|---|---|---|---|---|---|
| 1 | bench-press | https://x.com/0xlangeai/status/2118186890352607550 | 蓝哥AI @0xlangeai | 健身动作拆解 | bench-press.mp4 |
| 2 | barbell-squat | https://x.com/0xlangeai/status/2118193839705858256 | 蓝哥AI @0xlangeai | 健身动作拆解 | barbell-squat.mp4 |
| 3 | deadlift | https://x.com/0xlangeai/status/2118193839705858256 | 蓝哥AI @0xlangeai | 健身动作拆解 | deadlift.mp4 |
| 4 | cat-moon | https://x.com/pradeepXkapoor/status/2118163822938816642 | Pradeep Kapoor @pradeepXkapoor | 动物与宠物 | cat-moon.mp4 |
| 5 | golden-dog | https://x.com/lemomo_ai/status/2118151430154637420 | Lemomo @lemomo_ai | Meme/表情包 | golden-dog.mp4 |
| 6 | gm-heart | https://x.com/bit_sister/status/2118162095422517527 | 比特小师妹 @bit_sister | 问候 | gm-heart.mp4 |
| 7 | mascot | https://x.com/yyyole/status/2118174068927013293 | 沐阳 @yyyole | 产品与吉祥物 | mascot.mp4 |
| 8 | watercolor-baby | https://x.com/genel_ai/status/2118164510372688095 | GENEL @genel_ai | 照片转风格动画 | watercolor-baby.mp4 |
| 9 | pixel-game | https://x.com/koguGameDev/status/2118144025886921043 | kogu @koguGameDev | 动态图标与素材 | pixel-game.mp4 |
| 10 | penguin | https://x.com/tetumemo/status/2118131886803534126 | テツメモ @tetumemo | Meme/表情包 | penguin.mp4 |
| 11 | purple-girl | https://x.com/gosrum/status/2118135904779055540 | 金のニワトリ @gosrum | 产品与吉祥物 | purple-girl.mp4 |
| 12 | pixel-cabin | https://x.com/aziz4ai/status/2118183501711462560 | AZIZ @aziz4ai | Meme/表情包 | pixel-cabin.mp4 |
| 13 | gpt-claude-dance | https://x.com/798145343h/status/2118164732989608405 | Gangban @798145343h | 产品与吉祥物 | gpt-claude-dance.mp4 |
| 14 | gpt-claude-dance2 | https://x.com/798145343h/status/2118164732989608405 | Gangban @798145343h | 产品与吉祥物 | gpt-claude-dance2.mp4 |
| 15 | rooster | https://x.com/liyue_ai/status/2118183557315371229 | 李岳 @liyue_ai | Meme/表情包 | rooster.mp4 |

## 未跳过的帖子
14 个指定帖子全部取到媒体，无一跳过（squat/deadlift 同帖 2 条、GPT 与 Claude 跳舞同帖 2 条，共 15 条片段）。

## 下载后核对未采用的候选（未进成片）
- watercolor-baby 帖的另一条视频：实拍真人照片，非水彩婴儿 GIF。
- pixel-game 帖的另一条视频：同一像素小人的另一姿势（作者另一版尝试）。
- penguin 帖的另外两条视频：哭泣动漫女孩，属回帖内容，非企鹅角色；企鹅 GIF（penguin.mp4）取自该帖引用内容——该主帖本身无媒体（og:image 为头像）。
- purple-girl 帖的另一条视频：同一紫发女孩的不同帧，重复。

## 备注
- 短片段已循环补足（penguin 原长仅 0.4s，循环 6 次至 2.4s；1s 级片段循环至约 3s），长片段截至 4s，未拉伸。
- 构建脚本：/tmp/showcase-build/build.sh（临时文件，成片与清单在 staging 目录内）。
