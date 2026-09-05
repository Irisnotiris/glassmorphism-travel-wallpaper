# 玻璃拟态旅行信息卡手机壁纸

一个 AI Agent Skill，将任意上传的照片转换为高级玻璃拟态旅行信息卡手机锁屏壁纸。

![License](https://img.shields.io/badge/license-MIT-blue)
![比例](https://img.shields.io/badge/比例-9%3A19.5-lightgrey)
![风格](https://img.shields.io/badge/风格-毛玻璃-9cf)

English | [简体中文](./README.zh-CN.md)

## 功能特性

- **9:19.5 超竖版画幅**（1080×2340）—— 专为现代手机锁屏优化
- **毛玻璃 UI 卡片** —— 真实细腻的磨砂玻璃质感，带细微高光、折射和光斑，参考 Apple Vision Pro / iOS Glass UI
- **动态内容** —— 地点名称、距离和天气信息根据图片内容自动生成英文文案
- **图片预处理裁剪** —— 自动将上传图片中心裁剪到 9:19.5，避免拉伸压缩
- **顶部留白** —— 卡片位于画面下半部分，留出干净空间给锁屏时间
- **文字唯一性** —— 每段文字只出现一次，无重复

## 卡片结构

1. **搜索框** —— "Search place..." 带放大镜图标和圆形 "+" 按钮
2. **照片预览** —— 从上传图片裁切的圆角图片
3. **距离标签** —— 如 "365m"，叠加在预览图左下角
4. **地点信息** —— 地点标题 + 副标题，位于预览图下方
5. **Directions 按钮** —— 半透明圆角按钮，在预览图右下角
6. **天气信息** —— 卡片底部两行小字

## 安装

直接将本仓库地址发给你的 AI agent，让它安装并使用此 skill。Agent 会自动克隆或下载仓库，读取 `SKILL.md` 获取工作流，并应用到你的图片生成任务中。

示例："安装并使用这个 skill：https://github.com/Irisnotiris/glassmorphism-travel-wallpaper"

## 使用方法

1. 向你的 AI agent 上传任意旅行照片
2. 说："把这张图做成玻璃拟态旅行壁纸"
3. Skill 会自动：
   - 读取并分析你的图片
   - 中心裁剪到 9:19.5
   - 根据图片内容自动生成匹配的英文地点/天气文案
   - 使用图片编辑工具生成壁纸
   - 执行质量自检（玻璃质感、文字唯一性、构图）

## 示例

| 输入 | 输出 |
|---|---|
| ![输入](./examples/input.jpg) | ![输出](./examples/output.jpg) |

输入：阿马尔菲海岸悬崖小镇照片 → 输出：9:19.5 锁屏壁纸，含毛玻璃卡片、"Ravello Village / Amalfi Coast" 地点信息和天气详情。

## 文件结构

```
glassmorphism-travel-wallpaper/
├── SKILL.md                          # Skill 主文件（工作流、质量自检）
├── README.md                         # 英文文档
├── README.zh-CN.md                   # 中文文档
├── examples/
│   ├── input.jpg                     # 示例输入照片
│   └── output.jpg                    # 示例输出壁纸
├── references/
│   └── prompt-template.md            # 核心生成提示词模板（含占位符）
└── scripts/
    └── crop_to_ratio.py              # 图片中心裁剪工具
```

## 提示词模板占位符

| 占位符 | 说明 | 示例 |
|---|---|---|
| `{{IMAGE_DESCRIPTION}}` | 上传图片的一句话描述 | "阿马尔菲海岸悬崖小镇，彩色房屋，地中海" |
| `{{DISTANCE}}` | 距离文字（自动推断） | "365m" |
| `{{PLACE_TITLE}}` | 地点标题（自动推断） | "Ravello Village" |
| `{{SUBTITLE}}` | 地点副标题（自动推断） | "Amalfi Coast" |
| `{{WEATHER_LINE1}}` | 第一行天气（自动推断） | "Sea breeze · 12 km/h" |
| `{{WEATHER_LINE2}}` | 第二行天气（自动推断） | "Golden Hour in 42 min" |

## 相关项目

- [glassmorphism-travel-card](https://github.com/Irisnotiris/glassmorphism-travel-card) —— 3:4 海报版（即将上线）

## 许可证

MIT
