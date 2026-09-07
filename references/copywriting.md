# 文案生成指南

阶段3使用。基于阶段2确定的地点，独立生成全部英文文案。全部使用英文，不使用中文。

## 文案字段

| 字段 | 位置 | 风格 | 示例 |
|---|---|---|---|
| `{{PLACE_TITLE}}` | 预览图下方，大号 | 地名，简洁有力 | "Positano" |
| `{{SUBTITLE}}` | 标题下方，小号 | 地区/国家，补充说明 | "Amalfi Coast, Italy" |
| `{{DISTANCE}}` | 预览图左下角，小号 | 距离标签 | "1.2 km" / "850m" |
| `{{WEATHER_LINE1}}` | 卡片底部左侧 | 天气/风况，简洁 | "Sea breeze · 12 km/h" |
| `{{WEATHER_LINE2}}` | 卡片底部右侧 | 时间/光线，氛围感 | "Golden Hour in 42 min" |

## 各字段生成规则

### 地点标题 (PLACE_TITLE)
- 用阶段2确定的英文地名
- 置信度高时用具体地名（"Positano"）
- 置信度中/低时用泛化描述（"Coastal Village" / "Mountain Retreat"）
- 不超过 3 个单词

### 副标题 (SUBTITLE)
- 地区 + 国家，逗号分隔
- 示例："Amalfi Coast, Italy" / "Swiss Alps" / "Kyoto, Japan"
- 置信度低时可以省略国家，只写地区或氛围（"Mediterranean Coast"）

### 距离 (DISTANCE)
- 根据场景合理推测：
  - 小镇/村落："365m" / "850m" / "1.2 km"
  - 观景点/山顶："2.4 km" / "Elevation 1,800m"
  - 海滩："50m to shore" / "200m"
- 用米或公里，保持简短

### 天气第一行 (WEATHER_LINE1)
根据地点和场景选择匹配的天气描述：

| 场景 | 示例 |
|---|---|
| 海滩/海岸 | "Sea breeze · 12 km/h" / "Ocean wind · 8 knots" / "Coastal breeze · mild" |
| 山地/雪山 | "Mountain wind · 15 km/h" / "Alpine air · 4°C" / "Crisp breeze · clear" |
| 城市 | "City breeze · 10 km/h" / "Urban air · mild" |
| 森林 | "Forest air · humid" / "Woodland breeze · calm" |
| 沙漠 | "Desert wind · warm" / "Arid breeze · 28°C" |
| 湖泊 | "Lake breeze · calm" / "Still water · 18°C" |

格式："天气类型 · 数值/描述"，用中点 · 分隔。

### 天气第二行 (WEATHER_LINE2)
优先用时间/光线相关描述，增加氛围感：

| 氛围 | 示例 |
|---|---|
| 暖色调/日落 | "Golden Hour in 42 min" / "Sunset in 1h" |
| 清晨/冷色调 | "Blue Hour approaching" / "Sunrise in 30 min" |
| 明亮/正午 | "Clear sky · UV 6" / "Midday sun · bright" |
| 雾感/阴天 | "Misty conditions" / "Overcast · soft light" |
| 通用 | "Golden Hour soon" / "Perfect light now" |

## 候选生成

生成 2 组候选文案，自动选择最贴合图片氛围的一组。示例：

**候选 A（偏具体）**
- PLACE_TITLE: "Positano"
- SUBTITLE: "Amalfi Coast, Italy"
- DISTANCE: "850m"
- WEATHER_LINE1: "Sea breeze · 12 km/h"
- WEATHER_LINE2: "Golden Hour in 42 min"

**候选 B（偏氛围）**
- PLACE_TITLE: "Coastal Village"
- SUBTITLE: "Mediterranean Coast"
- DISTANCE: "1.2 km"
- WEATHER_LINE1: "Ocean wind · mild"
- WEATHER_LINE2: "Sunset approaching"

用户在场时，可简短展示两组供选择；用户不在场时自动选 A（置信度高时）或 B（置信度低时）。

## 注意事项

- 全部英文，首字母大写
- 不要用 emoji 或特殊符号（除了中点 ·）
- 距离和天气数值要合理，不要出现明显矛盾（如雪山上写 "30°C"）
- 文案要短，适合卡片内的小字号显示
- 用户明确指定了地点/文案时，直接使用用户给的，跳过生成
