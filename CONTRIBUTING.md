# 贡献作品

在 `data/gifs.json` 追加一项，参考已有条目的字段。

- `slug` 使用不重复的小写英文、数字与连字符。
- `title`、`description`、`category` 描述作品内容。
- `author` 填 X 用户名，不带 @；`post_url` 填原帖永久链接。
- `model` 填 `GPT Images 2.6`，`model_evidence` 记录原作者的明确说明。
- `prompt_status` 选择 `full`、`partial` 或 `not-shared`。前两种须填 `prompt` 与 `prompt_source`；没有公开则填 null，不自行补写。
- `gif_index` 选择原帖中的第几个 GIF，从 1 开始；GIF 位于引用帖时填 null，并在 `note` 中说明。
- `frame_ratio` 为抽帧相对位置，范围为大于等于 0、小于 1，默认 0.4。
- `added`、`checked` 填实际收录与核对日期，格式为 YYYY-MM-DD。
- `note` 记录多 GIF、引用帖、外部工具等影响理解的信息。

先核对作者原帖与 GIF。抽帧与校验脚本（`scripts/gallery.py`）待从 Kimi 合集仓库移植，移植完成前暂以人工核对为准。不要将登录资料、cookie、原 GIF 缓存或本地日志提交到仓库。

原帖仅写 Images 2.5 或版本不明的作品请先核实，不归入 GPT Images 2.6。更正出处或移除作品可提交 Issue，附对应原帖或目录条目。
