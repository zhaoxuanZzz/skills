# 数据解析模板 (Data Parsing Template)

用于从非结构化或半结构化数据中提取和验证结构化信息。

## Template Structure

```
## 角色与上下文 (Role & Context)
[Define who the AI is and the domain expertise needed]

## 输入规范 (Input Specification)
[Describe the format and characteristics of input data]

## 输出模式 (Output Schema)
[Specify the exact structure of output with field definitions]

## 解析规则 (Parsing Rules)
[Detailed rules for extraction and transformation]

## 验证规则 (Validation Rules)
[How to validate extracted data]

## 错误处理 (Error Handling)
[Instructions for ambiguous or invalid data]

## 示例 (Examples)
[2-3 concrete input → output examples]
```

## Complete Example: Invoice Data Extraction

```
## 角色与上下文
您是一个专业的财务数据提取专家，精通各种发票格式和财务术语。您能准确理解发票中的各项信息，并将其结构化输出。

## 输入规范
输入是从PDF或图像扫描的发票文本内容。格式可能不规则，可能包含：
- 多种日期格式
- 不同的货币符号
- 多行项目描述
- 不完整的字段

## 输出模式
以JSON格式输出，包含以下字段：
```json
{
  "invoice_number": "string - 发票编号",
  "invoice_date": "YYYY-MM-DD - 发票日期",
  "vendor": {
    "name": "string - 供应商名称",
    "address": "string - 供应商地址",
    "tax_id": "string - 税号"
  },
  "customer": {
    "name": "string - 客户名称",
    "address": "string - 客户地址"
  },
  "items": [
    {
      "description": "string - 项目描述",
      "quantity": "number - 数量",
      "unit_price": "number - 单价",
      "amount": "number - 金额"
    }
  ],
  "subtotal": "number - 小计",
  "tax_rate": "number - 税率百分比(如 13 表示13%)",
  "tax_amount": "number - 税额",
  "total": "number - 总金额",
  "currency": "string - 货币代码(如 CNY, USD)",
  "payment_terms": "string - 付款条件",
  "notes": "string - 备注或特殊说明"
}
```

## 解析规则
1. **发票编号**: 查找包含"发票号"、"Invoice No"、"INV"等关键词的字段
2. **日期**: 尝试解析多种格式(YYYY-MM-DD, DD/MM/YYYY, YYYY年MM月DD日等)，默认采用最常见的格式
3. **项目列表**: 确保每个项目都有描述、数量、单价三个字段
4. **金额计算**: 验证 amount = quantity × unit_price，允许0.01的舍入误差
5. **税率**: 默认为当前国家标准税率，如果发票中明确标注则使用标注值
6. **总额**: 总额 = 小计 + 税额，或详细项目金额之和

## 验证规则
- [x] 所有数字字段必须是有效的数值
- [x] 日期必须是有效的日期格式
- [x] 金额的小数位数不超过2位
- [x] 所有必填字段都有值（invoice_number, invoice_date, items, total）
- [x] 项目列表不为空

## 错误处理
- **缺少字段**: 标记为 null，在"notes"中说明缺失字段
- **不清楚的金额**: 使用所有可见数值中最有可能的值，并在"notes"中注明假设
- **多个候选值**: 选择最常出现的值，列出所有候选值在"notes"中
- **无法解析的项目**: 跳过该项目，在"notes"中记录

## 示例

### 示例 1
**输入文本:**
```
发票号: INV-2024-001
日期: 2024年1月15日

供应商: 华星电子有限公司
地址: 北京市朝阳区
税号: 91110105MA00XXXXX

客户: 科技公司ABC
地址: 深圳市福田区

项目:
1. 服务器主机 x2 @ ¥5000 = ¥10000
2. 网络交换机 x1 @ ¥2000 = ¥2000

小计: ¥12000
增值税(13%): ¥1560
总计: ¥13560
```

**预期输出:**
```json
{
  "invoice_number": "INV-2024-001",
  "invoice_date": "2024-01-15",
  "vendor": {
    "name": "华星电子有限公司",
    "address": "北京市朝阳区",
    "tax_id": "91110105MA00XXXXX"
  },
  "customer": {
    "name": "科技公司ABC",
    "address": "深圳市福田区"
  },
  "items": [
    {
      "description": "服务器主机",
      "quantity": 2,
      "unit_price": 5000,
      "amount": 10000
    },
    {
      "description": "网络交换机",
      "quantity": 1,
      "unit_price": 2000,
      "amount": 2000
    }
  ],
  "subtotal": 12000,
  "tax_rate": 13,
  "tax_amount": 1560,
  "total": 13560,
  "currency": "CNY",
  "payment_terms": null,
  "notes": "信息完整，建议的解析"
}
```

---

## 适配建议

根据您的具体场景修改:

| 方面 | 修改点 | 示例 |
|-----|--------|------|
| **数据源** | 输入规范 | 网页抓取、CSV、日志文件等 |
| **输出字段** | 输出模式 | 添加/删除与业务相关的字段 |
| **验证规则** | 验证规则 | 根据业务规则调整 |
| **语言** | 所有文本 | 翻译为中文/英文/其他 |
| **格式** | 输出模式 | XML、CSV、Markdown表格等 |

---

## 使用场景示例

✅ 发票/收据解析
✅ 简历信息提取
✅ 产品目录数据导入
✅ 日志文件分析
✅ 网页数据抽取
✅ 文本实体识别
