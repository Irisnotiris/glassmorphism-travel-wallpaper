# 联网推测地点策略

阶段2使用。根据阶段1的图片分析结果，通过联网搜索找到最相似的真实地点。

## 搜索关键词构造

从分析结果中提取最有辨识度的特征组合，构造 2-3 个搜索 query。

### 关键词优先级
1. **标志性建筑/地貌**（最强线索）：圆顶教堂、斜塔、特定山峰
2. **建筑风格 + 地理特征**：地中海白墙小镇 + 悬崖海岸
3. **场景类型 + 地区线索**：瑞士雪山湖泊、日本京都寺庙

### 示例

| 图片分析结果 | 搜索 query |
|---|---|
| 地中海悬崖、彩色房屋、圆顶教堂 | "地中海 悬崖 彩色小镇 圆顶教堂" / "Amalfi Coast colorful cliff village" |
| 雪山、湖泊、木屋 | "瑞士 雪山 湖泊 木屋" / "Switzerland alpine lake wooden chalet" |
| 竹林、寺庙、石阶 | "日本 京都 竹林 寺庙" / "Kyoto bamboo grove temple" |
| 沙漠、仙人掌、红色岩石 | "美国西南部 沙漠 红色岩石 仙人掌" / "Arizona desert red rock cactus" |
| 水乡、石桥、白墙黑瓦 | "中国 江南 水乡 石桥" / "Jiangnan water town stone bridge" |

## 搜索执行

1. 调用 `general_search`，并行搜索 2-3 个 query（中英文混合，提高命中率）。
2. 阅读搜索结果中的标题和摘要，寻找反复出现的地名。
3. 如果多个 query 都指向同一个地点，置信度为**高**。
4. 如果只有模糊的区域匹配（如"地中海地区"），置信度为**中**，用区域级描述。
5. 如果完全找不到匹配，置信度为**低**，用泛化描述。

## 地点输出格式

```
地点名（英文）：Positano
地区/国家（英文）：Amalfi Coast, Italy
置信度：高
搜索依据：多个结果指向阿马尔菲海岸的彩色悬崖小镇，圆顶教堂为波西塔诺标志性建筑
```

## 置信度处理

- **高**：直接使用具体地名
- **中**：使用地区级名称（如 "Amalfi Coast" 而非具体小镇名），或用 "Coastal Village" 等泛化词
- **低**：使用场景泛化描述：
  - 海滩 → "Coastal View" / "Seaside Retreat"
  - 山地 → "Mountain Retreat" / "Alpine Vista"
  - 城市 → "City Escape" / "Urban View"
  - 森林 → "Forest Hideaway" / "Woodland Trail"
  - 沙漠 → "Desert Oasis" / "Arid Landscape"

## 注意事项

- 不要因为图片好看就硬套知名景点（如所有海滩都叫 "Maldives"）
- 中英文搜索结合，中文搜索对国内地点更准，英文对国际地点更准
- 如果图片中有清晰的文字/路牌，优先用那个作为搜索关键词
- 搜索结果只是推测，交付时可以说明"推测地点为 XXX"
