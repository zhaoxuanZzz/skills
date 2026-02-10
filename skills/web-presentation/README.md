# Web Presentation Skill (Powered by Reveal.js)

A skill for creating modern, interactive web presentations powered by **Reveal.js**. Supports **two modes**:
1. **Single-file mode**: Self-contained HTML presentations for quick sharing
2. **Repository mode**: Multi-presentation management system with GitHub Pages deployment

## 🎉 特性

### Mode 1: Single Presentation (单个演示文稿)
✨ **高级动画** - Fragment 动画、Auto-Animate、自定义转场  
🎤 **演讲者工具** - 专业演讲者视图（备注、计时器、下一张预览）  
🔍 **智能导航** - 垂直嵌套幻灯片、概览模式、全文搜索  
💻 **代码高亮** - 支持 190+ 编程语言，行号显示  
📐 **数学公式** - KaTeX 渲染，支持复杂公式  
🔌 **插件生态** - Markdown、图表、3D 可视化等  
🛠️ **完整 API** - 全面的编程控制接口  

### Mode 2: Presentation Repository (演示文稿仓库)
📁 **仓库结构** - 每个演示文稿独立文件夹，含元数据  
🖼️ **自动索引** - 自动生成美观的演示文稿画廊页面  
🏷️ **元数据系统** - JSON 元数据文件（标题、作者、日期、标签等）  
🌐 **GitHub Pages** - 一键部署到 GitHub Pages  
📸 **缩略图** - 每个演示文稿的可视化预览  
🔍 **可搜索** - 索引页支持标签和分类  
🛠️ **构建脚本** - Node.js 自动化索引生成  
📦 **模板系统** - 快速从模板创建新演示文稿

## Quick Start

### Mode 1: Single Presentation (单个演示文稿)
1. Read `SKILL.md` - 完整交互式工作流（Workflow A）
2. Use template: `templates/viewer-reveal.html` (Reveal.js 推荐)
3. Customize presentation config and slides
4. Open HTML file in any browser
5. Press **S** for speaker view, **ESC** for overview

### Mode 2: Presentation Repository (演示文稿仓库)
1. Read `SKILL.md` - 仓库模式工作流（Workflow B）
2. Skill creates complete repository structure automatically:
   - `presentations/` - 演示文稿文件夹
   - `templates/` - 模板文件
   - `scripts/` - 构建脚本
   - `package.json` - npm 配置
3. Create presentations using templates
4. Run `npm run build` to generate index
5. Deploy to GitHub Pages with `npm run deploy`

**For Repository Mode, the skill will:**
- ✅ Create folder structure
- ✅ Generate package.json and scripts
- ✅ Create templates for presentations and metadata
- ✅ Set up build automation
- ✅ Provide GitHub Pages deployment instructions

**For Reference:**
- `SKILL.md` - 完整工作流（含交互式提问指南）
- `reference/layouts-reveal.md` - Reveal.js 布局和动画完整指南
- `reference/layouts.md` - 经典布局参考
- `reference/themes.md` - 颜色主题和定制
- `examples/reveal-advanced-demo.html` - **Reveal.js 完整特性展示**
- `examples/product-launch-demo.html` - 产品发布示例

## What This Skill Does

Creates professional web presentations with:
- **Reveal.js Integration** - 业界领先的演示框架
- **6+ different slide layouts** (title, content, two-column, image+text, quote, section, nested)
- **Advanced animations** - Fragments, auto-animate, custom transitions
- **Speaker tools** - Notes, timer, next slide preview (press S)
- **Smart navigation** - Horizontal/vertical slides, overview mode (press ESC)
- **Code highlighting** - 190+ languages with line numbers
- **Math equations** - KaTeX support for complex formulas
- **Customizable themes** - Complete CSS variable system
- **Full API access** - Programmatic control and event handling
- **Interactive workflow** - Question-guided presentation creation
- **Fully responsive** - Desktop, tablet, mobile
- **Single file output** - Self-contained HTML (CDN-based)

## File Structure

### This Skill Directory
```
web-presentation/
├── SKILL.md                        # 主技能文档（两种模式工作流）
├── LICENSE.txt                     # Apache 2.0 license
├── README.md                       # This file
├── templates/
│   ├── viewer-reveal.html          # ⭐ Reveal.js 单个演示文稿模板
│   ├── viewer.html                 # 经典自定义模板
│   ├── presentation-template.html  # 🆕 仓库模式：演示文稿模板
│   ├── metadata-template.json      # 🆕 仓库模式：元数据模板
│   ├── index-template.html         # 🆕 仓库模式：索引页模板
│   ├── package-template.json       # 🆕 仓库模式：package.json 模板
│   ├── README-template.md          # 🆕 仓库模式：README 模板
│   ├── .gitignore-template         # 🆕 仓库模式：.gitignore 模板
│   └── custom-css-template.css     # 🆕 仓库模式：自定义 CSS 模板
├── scripts/
│   └── generate-index.js           # 🆕 仓库模式：索引生成脚本
├── reference/
│   ├── layouts-reveal.md           # Reveal.js 布局和动画完整指南
│   ├── layouts.md                  # 经典布局指南
│   └── themes.md                   # 主题定制指南
└── examples/
    ├── README.md                   # 示例文档
    ├── reveal-advanced-demo.html   # Reveal.js 完整特性展示
    └── product-launch-demo.html    # 产品发布演示
```

### Generated Repository Structure (Mode 2)

When using Repository Mode, the skill creates this structure:

```
my-presentation-repo/                # 您的演示文稿仓库
├── index.html                       # 🤖 自动生成的索引页（勿手动编辑）
├── .nojekyll                        # GitHub Pages 配置
├── package.json                     # npm 配置（含构建脚本）
├── package-lock.json                # 依赖锁定文件
├── presentations/                   # 所有演示文稿目录
│   ├── my-first-presentation/       # 单个演示文稿文件夹
│   │   ├── index.html              # 演示文稿 HTML
│   │   ├── metadata.json           # 元数据（标题、描述、标签等）
│   │   └── thumbnail.png           # 缩略图（800x600推荐）
│   └── another-presentation/
│       ├── index.html
│       ├── metadata.json
│       └── thumbnail.png
├── templates/                       # 模板文件
│   ├── presentation-template.html  # 演示文稿模板
│   ├── metadata-template.json      # 元数据模板
│   └── index-template.html         # 索引页模板
├── scripts/                         # 构建脚本
│   └── generate-index.js           # 扫描presentations/并生成index.html
├── assets/                          # 共享资源
│   └── css/
│       └── custom.css              # 全局自定义样式
└── README.md                        # 仓库使用说明
```

## Key Features

### Reveal.js 增强版特性
- ✅ **Fragment animations** - 渐进式内容显示
- ✅ **Auto-animate** - 元素平滑变换
- ✅ **Speaker view** - 演讲者备注和计时（按 S）
- ✅ **Overview mode** - 幻灯片缩略图（按 ESC）
- ✅ **Vertical slides** - 层级嵌套导航
- ✅ **Code highlighting** - 语法高亮 + 行号
- ✅ **Math rendering** - LaTeX 数学公式
- ✅ **Search** - 全文搜索（Ctrl+Shift+F）
- ✅ **Zoom** - Alt+Click 放大
- ✅ **Full API** - 完整编程接口

### 通用特性
- **No build process** - 直接编辑 HTML
- **Keyboard shortcuts** - 完整键盘控制
- **Mobile friendly** - 触摸手势支持
- **Accessible** - WCAG AA 标准
- **CDN-based** - 快速加载，无需本地依赖
- **Claude artifacts** - Can be displayed directly in claude.ai

## Repository Mode Workflow

### npm 脚本

| 命令 | 说明 |
|------|------|
| `npm run build` | 扫描 presentations/ 并生成 index.html |
| `npm run dev` | 启动本地开发服务器（http://localhost:8080） |
| `npm run deploy` | 构建 + Git 提交 + 推送 |

### 添加新演示文稿

```bash
# 1. 创建新目录
mkdir presentations/my-new-talk

# 2. 复制模板
cp templates/presentation-template.html presentations/my-new-talk/index.html
cp templates/metadata-template.json presentations/my-new-talk/metadata.json

# 3. 编辑内容
# - 编辑 index.html 添加幻灯片内容
# - 编辑 metadata.json 更新元数据

# 4. 添加缩略图（可选，推荐 800x600）
# 将图片保存为 presentations/my-new-talk/thumbnail.png

# 5. 重新生成索引
npm run build

# 6. 本地预览
npm run dev

# 7. 部署到 GitHub
npm run deploy
```

### 元数据 JSON 示例

```json
{
  "id": "my-presentation",
  "title": "我的演示文稿标题",
  "description": "简短描述，显示在索引页",
  "author": "作者名称",
  "date": "2026-02-10",
  "tags": ["技术", "教程"],
  "thumbnail": "thumbnail.png",
  "slides": 15,
  "language": "zh-CN",
  "category": "教程"
}
```

### GitHub Pages 部署

```bash
# 1. 推送到 GitHub
git add .
git commit -m "Initial commit"
git push origin main

# 2. 在 GitHub 仓库设置中：
# Settings → Pages
# Source: Deploy from a branch
# Branch: main / (root)
# 点击 Save

# 3. 访问您的演示文稿集合
# https://{username}.github.io/{repo-name}/
```

## Usage Scenarios

### Single Presentation Mode
✅ 快速一次性演讲  
✅ 通过邮件或聊天分享  
✅ 嵌入文档或网站  
✅ Claude.ai 工件展示  

### Repository Mode
✅ 管理多个演示文稿  
✅ 构建演示文稿作品集  
✅ 团队/组织演示文稿库  
✅ GitHub Pages 发布  
✅ 分类演示文稿集合  
✅ 专业演示文稿网站  

### Common Use Cases
✅ Product launches and pitches  
✅ Technical presentations  
✅ Educational slideshows  
✅ Company updates  
✅ Portfolio showcases  
✅ Workshop materials  

## Browser Support

Works in all modern browsers:
- Chrome/Edge ✅
- Firefox ✅
- Safari ✅
- Opera ✅

## License

Apache License 2.0 - See LICENSE.txt for details
