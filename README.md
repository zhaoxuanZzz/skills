# Agent Skills

这是一个 Agent Skills 集合，用于扩展 Claude 的功能。

## 项目结构

```
skills/
├── .claude-plugin/          # Claude 插件配置
│   └── marketplace.json     # 插件市场配置文件
├── skills/                  # 技能集合
│   ├── skill-creator/       # 技能创建指南
│   └── web-presentation/    # 网页演示技能
├── spec/                    # 规范文档
│   └── agent-skills-spec.md # Agent Skills 规范
└── template/                # 模板文件
    └── SKILL.md             # 技能模板
```

## 包含的技能

### 1. skill-creator
为创建有效的技能提供指导。这个技能应该在用户想要创建新技能（或更新现有技能）时使用，这些技能可以扩展 Claude 的能力，包括专业知识、工作流或工具集成。

- **位置**: `./skills/skill-creator/`
- **文件**: [SKILL.md](./skills/skill-creator/SKILL.md)

**核心特性**:
- 专业工作流 - 特定领域的多步流程
- 工具集成 - 与特定文件格式或 API 协同工作的说明
- 领域专业知识 - 公司特定的知识、模式、业务逻辑
- 捆绑资源 - 复杂和重复任务的脚本、参考和资源

### 2. web-presentation
创建现代交互式网页演示，作为单文件 HTML工件。**现已升级为 Reveal.js 增强版！**当用户请求创建幻灯片、演示文稿、幻灯片组或基于浏览器的演示时使用。通过交互式问答引导，输出可直接在浏览器中打开或显示为 Claude.ai 工件的 .html 文件。

- **位置**: `./skills/web-presentation/`
- **文件**: [SKILL.md](./skills/web-presentation/SKILL.md)

**核心特性**:
- **🎬 高级动画** - Fragment 动画、Auto-Animate、自定义转场效果
- **🎤 演讲者工具** - 专业演讲者视图（备注、计时器、下一张预览，按 S 键）
- **🔍 智能导航** - 垂直嵌套幻灯片、概览模式（按 ESC）、全文搜索
- **💻 代码高亮** - 支持 190+ 编程语言，行号显示和分步高亮
- **📐 数学公式** - KaTeX 渲染，支持 LaTeX 复杂公式
- **🤝 交互式工作流** - 通过系统性提问引导创建（内容、样式、动画）
- **🎨 多种布局** - 标题、内容、两列、图像+文本、引用、章节、嵌套
- **⌨️ 键盘快捷键** - 完全键盘控制，包括全屏模式
- **📊 进度跟踪** - 可视化进度条和幻灯片计数器
- **📱 响应式设计** - 在桌面、平板和移动设备上运行
- **🔌 插件生态** - Markdown、图表、3D可视化、Mermaid 图表
- **🛠️ 完整 API** - 全面的 Reveal.js 编程接口
- **🚀 单文件输出** - 基于 CDN，无需构建过程

**新增模板**:
- `templates/viewer-reveal.html` - Reveal.js 增强版（推荐）
- `templates/viewer.html` - 经典自定义版

**新增文档**:
- `reference/layouts-reveal.md` - Reveal.js 完整布局和动画指南
- `examples/reveal-advanced-demo.html` - 完整特性展示

## 文件说明

- **marketplace.json**: 定义了这个技能集合的元数据和包含的技能列表
- **agent-skills-spec.md**: Agent Skills 的官方规范（详见 https://agentskills.io/specification）
- **SKILL.md (template)**: 创建新技能时的模板文件

## 开发指南

### 创建新技能
1. 在 `./skills/` 目录下创建新文件夹
2. 参考 `./template/SKILL.md` 创建 SKILL.md 文件
3. 添加相关的参考资料、脚本或示例
4. 在 `marketplace.json` 中注册新技能

### 技能规范
有关技能的详细规范，请参阅 [Agent Skills 规范](https://agentskills.io/specification)

## 许可证

各个技能都在其各自的 LICENSE.txt 文件中包含完整条款。

## 相关资源

- [Agent Skills 规范](https://agentskills.io/specification)
- [技能创建指南](./skills/skill-creator/SKILL.md)
