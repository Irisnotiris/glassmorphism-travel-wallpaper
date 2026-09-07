# 玻璃拟态旅行信息卡手机壁纸

一个 AI Agent Skill，将任意上传的照片转换为高级玻璃拟态旅行信息卡手机锁屏壁纸——具备智能地点识别和上下文感知文案生成能力。

![License](https://img.shields.io/badge/license-MIT-blue)
![比例](https://img.shields.io/badge/比例-9%3A19.5-lightgrey)
![风格](https://img.shields.io/badge/风格-毛玻璃-9cf)

English | [简体中文](./README.zh-CN.md)

## 功能特性

- **9:19.5 超竖版画幅**（1080×2340）—— 专为现代手机锁屏优化
- **毛玻璃 UI 卡片** —— 真实细腻的磨砂玻璃质感，带细微高光、折射和光斑，参考 Apple Vision Pro / iOS Glass UI
- **智能地点识别** —— 分析图片并联网搜索，推测最相似的真实地点
- **上下文感知文案** —— 基于确认的地点和图片氛围，生成匹配的英文地点标题、副标题、距离和天气文案
- **图片预处理裁剪** —— 自动将上传图片中心裁剪到 9:19.5，避免拉伸压缩
- **锁屏感知构图** —— 卡片位于画面下半部分，留出干净空间给锁屏时间（通过 iOS 锁屏场景描述引导，而非硬性百分比）
- **文字唯一性** —— 每段文字只出现一次，无重复

## 工作原理 —— 五阶段工作流

```
1. 图片分析  →  2. 联网推测地点  →  3. 文案生成  →  4. 生成壁纸  →  5. 质检交付
```

1. **图片分析** —— 识别场景类型、地理特征、建筑风格、标志性元素和主色调
2. **联网推测地点** —— 从分析结果提取关键词，联网搜索最相似的真实地点（附置信度）
3. **文案生成** —— 基于确认的地点生成 2 组英文文案候选（地点标题、副标题、距离、两行天气），自动选最优
4. **生成壁纸** —— 裁剪图片、填入文案、调用生图工具生成
5. **质检交付** —— 验证构图、玻璃质感、文案准确性/唯一性、背景保真度

## 卡片结构

1. **搜索框** —— "Search place..." 带放大镜图标和圆形 "+" 按钮
2. **照片预览** —— 从上传图片裁切的圆角图片
3. **距离标签** —— 如 "1.2 km"，叠加在预览图左下角
4. **地点信息** —— 地点标题 + 副标题，位于预览图下方
5. **Directions 按钮** —— 半透明圆角按钮，在预览图右下角
6. **天气信息** —— 卡片底部两行小字

## 安装

直接将本仓库地址发给你的 AI agent，让它安装并使用此 skill。Agent 会自动克隆或下载仓库，读取 `SKILL.md` 获取工作流，并应用到你的图片生成任务中。

示例："安装并使用这个 skill：https://github.com/Irisnotiris/glassmorphism-travel-wallpaper"

## 使用方法

1. 向你的 AI agent 上传任意旅行照片
2. 说："把这张图做成玻璃拟态旅行壁纸"
3. Skill 会自动运行五阶段工作流

## 示例

| 输入 | 输出 |
|---|---|
| ![输入](./examples/input.jpg) | ![输出](./examples/output.jpg) |

输入：阿马尔菲海岸悬崖小镇照片 → 输出：9:19.5 锁屏壁纸，含毛玻璃卡片、推测地点 "Ravello Village / Amalfi Coast" 和上下文感知天气详情。

## 文件结构

```
glassmorphism-travel-wallpaper/
├── SKILL.md                          # Skill 主文件（五阶段工作流）
├── README.md                         # 英文文档
├── README.zh-CN.md                   # 中文文档
├── examples/
│   ├── input.jpg                     # 示例输入照片
│   └── output.jpg                    # 示例输出壁纸
├── references/
│   ├── prompt-template.md            # 核心生成提示词模板（含占位符）
│   ├── image-analysis.md             # 图片分析指南
│   ├── location-search.md            # 联网推测地点策略
│   └── copywriting.md                # 文案生成指南
└── scripts/
    └── crop_to_ratio.py              # 图片中心裁剪工具
```

## 提示词模板占位符

所有占位符由工作流前置阶段确定，不由生图模型自行推断。

| 占位符 | 来源 | 示例 |
|---|---|---|
| `{{IMAGE_DESCRIPTION}}` | 阶段1（图片分析） | "故宫宫殿，金色屋顶，红柱，晚霞" |
| `{{DISTANCE}}` | 阶段3（文案生成） | "1.2 km" |
| `{{PLACE_TITLE}}` | 阶段2+3（地点+文案） | "Forbidden City" |
| `{{SUBTITLE}}` | 阶段2+3（地点+文案） | "Beijing, China" |
| `{{WEATHER_LINE1}}` | 阶段3（文案生成） | "Evening breeze · calm" |
| `{{WEATHER_LINE2}}` | 阶段3（文案生成） | "Golden Hour now" |

## 相关项目

- [glassmorphism-travel-card](https://github.com/Irisnotiris/glassmorphism-travel-card) —— 3:4 海报版

## 许可证

MIT
