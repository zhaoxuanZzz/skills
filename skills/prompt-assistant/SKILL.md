---
name: prompt-assistant
description: Generate and optimize prompts for various AI use cases. This skill provides specialized prompt templates for structured data parsing, complex multi-step tasks, and markdown-formatted outputs with sections, content, and visual elements. Use this when users need help crafting, refining, or adapting prompts for different scenarios.
license: MIT
---

⚠️ **PLEASE READ THIS ENTIRE FILE BEFORE GENERATING PROMPTS** ⚠️

# Prompt Assistant Skill

Help users generate, optimize, and adapt high-quality AI prompts for diverse use cases. This skill provides **specialized templates** for different scenarios, ensuring prompts are precise, structured, and effective.

## Overview

This skill helps with:
- 🎯 **Prompt generation** - Create effective prompts from scratch
- 🔄 **Prompt optimization** - Refine existing prompts for better results
- 📋 **Template selection** - Match the right template to the use case
- 📊 **Structured outputs** - Parse data with consistent formatting
- 🔪 **Complex decomposition** - Break down multi-step tasks
- 📝 **Markdown formatting** - Generate well-structured markdown with sections, content, and diagrams

## When to Use This Skill

**Use for:**
✅ Generating prompts for data parsing and extraction
✅ Creating multi-step instruction prompts
✅ Building prompts that require markdown structured output
✅ Optimizing prompts for better AI responses
✅ Adapting prompts for different tools/models
✅ Creating system prompts and role-based prompts

**Don't use for:**
❌ Direct task execution (use domain-specific skills instead)
❌ General conversation (not needed for simple questions)
❌ Content that violates policies

---

## Core Concept: Scenario-Based Templates

This skill uses **4 primary template categories** based on different use cases:

### 1️⃣ **Data Parsing Template**
Use when the user needs **structured, consistent output** from unstructured data.

**Characteristics:**
- Requires precise data extraction
- Output needs schema/format validation
- Often involves JSON, CSV, or table formats
- Example use cases: Invoice parsing, entity extraction, log analysis

**Key prompt elements:**
```markdown
## Role & Context
Define the parser's expertise and context

## Input Specification
Describe the format of incoming data

## Output Schema
Specify exact output structure with examples

## Parsing Rules
- Rule 1: ...
- Rule 2: ...
- Rule 3: ...

## Error Handling
Instructions for ambiguous or invalid data

## Examples
- Example 1: [Input] → [Expected Output]
- Example 2: [Input] → [Expected Output]
```

### 2️⃣ **Complex Task Decomposition Template**
Use when the user needs **step-by-step instructions** for multi-part problems.

**Characteristics:**
- Large task with multiple phases
- Sequential dependencies between steps
- Requires intermediate validation
- Example use cases: Content creation, analysis, research planning

**Key prompt elements:**
```markdown
## Objective
Clear, measurable end goal

## Phase Overview
High-level breakdown of major phases

## Detailed Steps
Phase 1: [Step 1a, 1b, 1c...]
Phase 2: [Step 2a, 2b, 2c...]
Phase 3: [Step 3a, 3b, 3c...]

## Success Criteria
How to validate each phase

## Key Considerations
Important context and constraints

## Fallback Options
Alternative approaches if something fails
```

### 3️⃣ **Markdown Structured Output Template**
Use when the user needs **formatted markdown output** with specific sections, hierarchy, and visual elements.

**Characteristics:**
- Output must be well-structured markdown
- Different section types (narrative, code, diagrams)
- Visual hierarchy and readability important
- Example use cases: Documentation, reports, educational content

**Key prompt elements:**
```markdown
## Output Structure
Section 1: [Description]
Section 2: [Description]
Section 3: [Description]

## Formatting Rules
- Use H2 (##) for main sections
- Use H3 (###) for subsections
- Bold for emphasis: **term**
- Code blocks: \`\`\`language

## Visual Elements
- ✅ Use checkmarks for done items
- ❌ Use X for issues
- 📌 Use pins for important info
- 📊 Describe diagrams as Mermaid or ASCII

## Content Guidelines
- Write in [tone/style]
- Keep sections under [target length]
- Include [specific elements]

## Example Output
[Detailed example showing desired structure]
```

### 4️⃣ **Prompt Optimization Template**
Use when the user wants to **improve an existing prompt**.

**Characteristics:**
- Take user's existing prompt
- Identify weaknesses
- Propose improvements
- Validate with examples

**Key analysis elements:**
```markdown
## Current Prompt Analysis
- Clarity: [Assessment]
- Completeness: [Assessment]
- Structure: [Assessment]
- Examples: [Assessment]
- Constraints: [Assessment]

## Identified Issues
1. Issue: [problem] → Impact: [effect]
2. Issue: [problem] → Impact: [effect]

## Optimization Recommendations
1. Clarify the objective
2. Add structured output format
3. Include more specific examples
4. Better error handling instructions

## Optimized Prompt
[Full improved prompt]

## Before/After Comparison
- Before: [snippet showing old approach]
- After: [snippet showing new approach]
- Expected improvement: [description]
```

---

## Workflow: How to Use This Skill

### Step 1: **Understand User's Needs** (Always ask questions first)

Before generating any prompt, ask the user:

```
💡 让我帮你创建完美的提示词！首先，我需要了解您的需求：

🎯 **任务目标：**
1. 您想要AI完成什么任务？
2. 输入数据或信息的格式是什么？
3. 您期望的输出是什么（格式、结构、长度）？

📊 **场景分类：**
4. 这个任务属于以下哪一类？
   - □ 数据解析（从文本/文件中提取结构化数据）
   - □ 复杂多步任务（多个阶段的工作流）
   - □ Markdown文档生成（需要格式化的结构化输出）
   - □ 优化现有提示词（我已有提示词想改进）

⚙️ **具体需求：**
5. 是否有特殊要求？
   - 输出格式要求？
   - 数据验证规则？
   - 错误处理方式？
   - 特定的示例或参考？

📋 **约束条件：**
6. 有什么限制条件吗？
   - Token预算（长度限制）？
   - 特定的格式标准？
   - 需要支持的语言或工具？
```

### Step 2: **Select Appropriate Template**

Based on responses, recommend:
- ✅ **Data Parsing Template** if task involves extraction, validation, structuring
- ✅ **Complex Decomposition** if task has multiple dependent phases
- ✅ **Markdown Output** if needs formatted, readable documentation
- ✅ **Optimization** if improving existing prompt

### Step 3: **Generate Tailored Prompt**

Create the prompt by:
1. Starting with template structure
2. Filling in user-specific details
3. Adding examples from user's context
4. Ensuring clarity and completeness

### Step 4: **Present as Markdown Block**

Always present the generated prompt in a **fenced markdown code block**:

````markdown
```
[Generated Prompt Here]
```
````

With clear sections:
- **Purpose**: What this prompt does
- **When to use it**: Best use cases
- **How to adapt**: Customization guidance
- **The Prompt**: The actual prompt text
- **Example usage**: Before/after or input/output examples

### Step 5: **Offer Refinement**

After generating, always ask:

```
✨ **这个提示词可以如何改进？**

- 是否需要调整输出格式？
- 需要添加更多示例吗？
- 有特定的业务规则需要包含？
- 是否需要为不同工具改编？
```

---

## Template Files Reference

See `/templates` directory for detailed templates:
- `data-parsing-template.md` - Structured data extraction
- `complex-decomposition-template.md` - Multi-step workflows
- `markdown-output-template.md` - Formatted documentation
- `prompt-optimization-guide.md` - Improving existing prompts
- `role-based-system-prompt-template.md` - System level prompts
- `financial-rule-analysis-prompt.md` - **[新增]** 财务规则集分析与输出（优化提示词）
- `financial-rule-output-template.md` - **[新增]** 财务规则集结构化输出模板
- `financial-rule-output-example.md` - **[新增]** 财务规则集输出示例

## Reference Materials

See `/reference` directory for:
- `best-practices.md` - Prompt engineering best practices
- `common-patterns.md` - Proven prompt patterns
- `anti-patterns.md` - What to avoid
- `tools-specific-prompts.md` - Prompts optimized for specific AI tools

---

## Best Practices for Generated Prompts

✅ **DO:**
- [x] Start with clear role/context
- [x] Define inputs explicitly
- [x] Specify output format precisely
- [x] Include 2-3 concrete examples
- [x] Set constraints and boundaries
- [x] Add fallback/error handling
- [x] Use clear formatting and structure

❌ **DON'T:**
- [ ] Use vague language or unclear intent
- [ ] Assume the AI understands context
- [ ] Mix multiple unrelated tasks
- [ ] Forget to specify format requirements
- [ ] Leave edge cases undefined
- [ ] Write overly long prompts without structure
- [ ] Forget examples

---

## Example Scenarios

### Scenario 1: Data Parsing - Invoice Extraction
**User:** "I need to extract invoice data from PDFs"
**Recommended Template:** Data Parsing Template
**Output:** Prompt with schema for invoice fields, parsing rules, error handling

### Scenario 2: Content Generation - Product Launch Blog
**User:** "I need a step-by-step guide for writing product launch content"
**Recommended Template:** Complex Decomposition Template
**Output:** Prompt with phases for research, outline, drafting, editing, publishing

### Scenario 3: Documentation - API Reference Generator
**User:** "I need to generate API documentation in markdown with examples"
**Recommended Template:** Markdown Structured Output Template
**Output:** Prompt with markdown structure, formatting rules, example sections

### Scenario 4: Improving a Prompt
**User:** "Here's my prompt but it's not giving good results"
**Recommended Template:** Prompt Optimization Template
**Output:** Analysis of issues, improvements, and the optimized prompt

---

## Template Syntax Reference

When building prompts, use these consistent elements:

```markdown
## [Section Title]
Description of what goes here

### [Subsection]
More specific details

**Bold text:** For key terms
`code`: For variables or commands
- Bullet: For lists
- More items:

> Quote: For important notes or examples
```

---

## Support and Customization

### For Tool-Specific Prompts
If user needs prompts for specific models (Claude, GPT, Gemini, etc.), ensure:
- Prompt syntax matches tool requirements
- Any tool-specific features are leveraged
- Output format is compatible

### For Multiple Languages
If user requests prompts in non-English:
- Generate prompt in requested language
- Maintain same structure and clarity
- Note any language-specific patterns

### For Integration/API Usage
If prompt will be used in code/automation:
- Make variables clear: `{variable_name}`
- Specify placeholder format
- Include usage example
