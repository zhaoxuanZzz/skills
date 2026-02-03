---
name: web-presentation
description: Create modern, interactive web presentations as single-file HTML artifacts. Use this when users request creating slides, presentations, slide decks, web presentations, or browser-based presentations. Output .html files that can be opened directly in a browser or displayed as claude.ai artifacts.
license: Complete terms in LICENSE.txt
---

⚠️ **READ THIS ENTIRE FILE BEFORE CREATING A WEB PRESENTATION** ⚠️

# Web Presentation Skill

Create elegant, interactive presentations that run entirely in a web browser as single HTML files. Perfect for product launches, technical talks, educational content, and any scenario requiring modern, shareable slides.

## Overview

This skill creates self-contained HTML presentations with:
- **Smooth navigation** - Arrow keys, buttons, touch/swipe support
- **Multiple layouts** - Title, content, two-column, image+text, quotes, sections
- **Customizable themes** - Brand colors, fonts, gradients
- **Keyboard shortcuts** - Full keyboard control including fullscreen mode
- **Progress tracking** - Visual progress bar and slide counter
- **Responsive design** - Works on desktop, tablet, and mobile
- **Single-file output** - Everything embedded, no external dependencies (except fonts)

## When to Use This Skill

**Use for:**
✅ Product presentations and pitches
✅ Conference talks and tech presentations
✅ Educational slideshows and lectures
✅ Company all-hands or team updates
✅ Portfolio showcases
✅ Workshop materials
✅ Documentation walkthroughs

**Don't use for:**
❌ Static documents (use docx skill instead)
❌ Printable handouts (use pdf skill instead)
❌ Spreadsheet data (use xlsx skill instead)
❌ Rich media editing (needs external tools)

---

## Workflow

### Step 1: Understand the Requirements

Before creating anything, gather:
- **Topic/purpose:** What is the presentation about?
- **Audience:** Who will view it?
- **Key messages:** 3-5 main takeaways
- **Approximate length:** How many slides needed?
- **Visual style:** Professional, creative, minimal, bold?
- **Brand requirements:** Specific colors, fonts, or guidelines?

### Step 2: Plan the Structure

Organize content into logical sections:

**Standard presentation flow:**
1. **Title slide** - Opening with title, subtitle, author
2. **Overview/Agenda** - What will be covered
3. **Section 1** - First main topic
   - Supporting slides with details
4. **Section 2** - Second main topic
   - Supporting slides with details
5. **Section 3** - Third main topic (if needed)
   - Supporting slides with details
6. **Summary/Conclusion** - Key takeaways
7. **Thank you/Q&A** - Closing slide

**Typical slide counts:**
- **Quick pitch:** 5-10 slides
- **Standard presentation:** 15-25 slides
- **Long-form talk:** 30-50 slides
- **Workshop:** 50+ slides

### Step 3: Read the Template

**CRITICAL:** Before writing any code, read the template file:

```
templates/viewer.html
```

This template contains:
- ✅ **FIXED sections:** Header, footer, navigation, styling (DO NOT CHANGE)
- ✅ **VARIABLE sections:** SLIDES array, PRESENTATION config (CUSTOMIZE THESE)

**The template is your foundation.** Copy it and modify only the marked sections.

### Step 4: Define Slide Content

Create slides using the `SLIDES` array. Each slide is an object with:
- `layout`: Layout type (title, content, two-column, etc.)
- `content`: HTML content for the slide

**Example:**
```javascript
const SLIDES = [
    {
        layout: "title",
        content: `
            <h1>Product Launch 2024</h1>
            <div class="subtitle">Introducing the next generation</div>
            <div class="author">Jane Smith, Product Lead</div>
        `
    },
    {
        layout: "content",
        content: `
            <h2>What's New</h2>
            <p>We're excited to announce three major improvements:</p>
            <ul>
                <li>2x faster performance</li>
                <li>Enhanced security features</li>
                <li>Redesigned user interface</li>
            </ul>
        `
    },
    {
        layout: "section",
        content: `
            <div class="section-number">Part 1</div>
            <h2>Performance</h2>
        `
    }
    // ... more slides
];
```

### Step 5: Configure Theme

Set presentation metadata and colors in the `PRESENTATION` object:

```javascript
const PRESENTATION = {
    title: "Product Launch 2024",
    author: "Jane Smith",
    theme: {
        primary: "#d97757",    // Main color (buttons, headings)
        secondary: "#6a9bcc",  // Gradient accent
        accent: "#788c5d"      // Section backgrounds
    }
};
```

**Color selection tips:**
- Use brand colors if available
- Ensure sufficient contrast for readability
- Test colors together (primary + secondary should work in gradients)
- See `reference/themes.md` for preset themes and guidance

### Step 6: Generate and Validate

Create the HTML file with all customizations, then:

1. **Open in browser** - Test that slides load correctly
2. **Navigate through all slides** - Check flow and transitions
3. **Test keyboard shortcuts** - Arrow keys, space, F for fullscreen
4. **Check responsive behavior** - Resize window or test on mobile
5. **Verify content** - No typos, proper formatting
6. **Test fullscreen mode** - Press F or click fullscreen button

**Common issues to check:**
- Slides render correctly (no broken layouts)
- All text is readable (good contrast)
- Navigation works (buttons and keys)
- Progress bar updates
- Slide counter is accurate
- Theme colors applied correctly

### Step 7: Deliver

Provide the HTML file to the user with:
- **File name:** Descriptive name like `product-launch-2024.html`
- **Brief instructions:** "Open in any web browser. Use arrow keys or buttons to navigate. Press F for fullscreen."
- **Note about editing:** If they want to make changes, they can edit the SLIDES array in the HTML file

---

## Available Layouts

### 1. Title Slide (`layout: "title"`)

**Use for:** Opening, closing, major section breaks

```javascript
{
    layout: "title",
    content: `
        <h1>Main Title</h1>
        <div class="subtitle">Subtitle or description</div>
        <div class="author">Author or date (optional)</div>
    `
}
```

**Features:**
- Full-screen, centered
- Gradient background (primary → secondary)
- White text
- Large, impactful typography

---

### 2. Content Slide (`layout: "content"`)

**Use for:** Main content, bullet points, text, code

```javascript
{
    layout: "content",
    content: `
        <h2>Slide Title</h2>
        <p>Paragraph text...</p>
        <ul>
            <li>Bullet point one</li>
            <li>Bullet point two</li>
        </ul>
        <p>More text with <code>inline code</code>.</p>
        <pre>
function example() {
    return "code block";
}
        </pre>
    `
}
```

**Supported elements:**
- `<h2>` - Main heading (colored with primary theme)
- `<h3>` - Subheading
- `<p>` - Paragraphs
- `<ul>`, `<ol>`, `<li>` - Lists
- `<code>` - Inline code
- `<pre>` - Code blocks
- `<strong>`, `<em>` - Emphasis

---

### 3. Two-Column Layout (`layout: "two-column"`)

**Use for:** Comparisons, before/after, pros/cons

```javascript
{
    layout: "two-column",
    content: `
        <h2>Comparison</h2>
        <div class="columns">
            <div class="column">
                <h3>Before</h3>
                <ul>
                    <li>Slow performance</li>
                    <li>Complex setup</li>
                </ul>
            </div>
            <div class="column">
                <h3>After</h3>
                <ul>
                    <li>2x faster</li>
                    <li>Simple setup</li>
                </ul>
            </div>
        </div>
    `
}
```

**Best practices:**
- Balance content between columns
- Use parallel structure
- Title spans both columns

---

### 4. Image + Text (`layout: "image-text"`)

**Use for:** Product showcases, visual explanations, diagrams

```javascript
{
    layout: "image-text",
    content: `
        <img src="data:image/svg+xml,..." alt="Description">
        <div class="text-content">
            <h2>Feature Title</h2>
            <p>Description of the feature shown in the image.</p>
            <ul>
                <li>Key benefit one</li>
                <li>Key benefit two</li>
            </ul>
        </div>
    `
}
```

**Image options:**
- **Data URIs:** Embed SVG or base64-encoded images
- **External URLs:** Link to images (requires internet)
- **Recommended:** Use SVG for diagrams, icons, illustrations

---

### 5. Quote Slide (`layout: "quote"`)

**Use for:** Testimonials, impactful statements, emphasis

```javascript
{
    layout: "quote",
    content: `
        <blockquote>
            An impactful quote that emphasizes a key message.
        </blockquote>
        <cite>— Author Name</cite>
    `
}
```

**Features:**
- Large serif font
- Centered on light background
- Decorative quotation mark
- Great for breaks between sections

---

### 6. Section Divider (`layout: "section"`)

**Use for:** Major topic transitions, chapter breaks

```javascript
{
    layout: "section",
    content: `
        <div class="section-number">Section 1</div>
        <h2>Section Title</h2>
    `
}
```

**Features:**
- Full-screen colored background (accent color)
- White text
- Creates visual rhythm
- Use sparingly (2-4 per presentation)

---

## Design Guidelines

### Visual Hierarchy

**Create clear structure:**
- **Large to small:** Titles → Headings → Body text
- **Bold to regular:** Important points → Supporting details
- **Color emphasis:** Primary color → Body text color
- **Spacing:** More space = more importance

**Typography scale:**
- Title slides: 64px titles
- Content slides: 42px headings, 20px body text
- Keep line length under 80 characters
- Use generous line height (1.6-1.8)

### Content Density

**Per slide guidelines:**
- **Title slides:** 1 title + 1-2 supporting lines
- **Content slides:** 1 heading + 3-7 bullet points OR 2-3 paragraphs
- **Two-column:** 3-5 items per column
- **Image slides:** 1 image + short description

**Avoid:**
- ❌ Paragraphs longer than 4 lines
- ❌ More than 7 bullet points
- ❌ Tiny font sizes
- ❌ Wall of text
- ❌ Cramped spacing

### Color Usage

**Best practices:**
- **Primary color:** Headings, buttons, emphasis
- **Secondary color:** Gradients, accents
- **Accent color:** Section dividers, special elements
- **Text color:** Dark on light backgrounds
- **Consistency:** Use same colors for same purposes

**Accessibility:**
- Maintain 4.5:1 contrast ratio for normal text
- Maintain 3:1 contrast ratio for large text (18pt+)
- Don't rely solely on color to convey information
- Test with colorblind simulation tools

### Images and Graphics

**When to use:**
- Diagrams explaining complex concepts
- Product screenshots
- Data visualizations
- Icons for visual interest
- Logos and branding

**Best practices:**
- Use high-quality images (but keep file size reasonable)
- Include descriptive alt text
- Embed as data URIs for self-contained files
- Use SVG for diagrams and icons
- Keep images relevant to content

**Creating data URIs:**
```javascript
// For SVG:
const svgDataUri = `data:image/svg+xml,${encodeURIComponent(svgString)}`;

// For PNG/JPG (base64):
const imageDataUri = `data:image/png;base64,${base64String}`;
```

### Animation and Transitions

**Built-in transitions:**
- Slide transitions are smooth and professional
- 0.5s cubic-bezier easing
- Slides enter from right, exit to left
- No customization needed

**Avoid:**
- ❌ Adding custom animations (keep it simple)
- ❌ Distracting effects
- ❌ Auto-advancing slides
- ❌ Sound effects

---

## Advanced Customization

### Custom CSS

Add custom styles in the `<style>` section:

```css
/* Custom layout variant */
.slide.layout-content.highlight {
    background: linear-gradient(135deg, #fff5f5, #ffffff);
    border-left: 5px solid var(--theme-primary);
}

/* Custom text styling */
.slide h2.accent {
    color: var(--theme-accent);
}
```

Then use in slides:

```javascript
{
    layout: "content highlight",
    content: `<h2 class="accent">Special Slide</h2>...`
}
```

### JavaScript Customization

Modify behavior in the `<script>` section:

```javascript
// Auto-advance slides every 10 seconds
setInterval(() => {
    if (currentSlideIndex < SLIDES.length - 1) {
        nextSlide();
    }
}, 10000);

// Track slide views
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
        console.log('Advanced to slide', currentSlideIndex + 1);
    }
});
```

### Adding External Libraries

For charts, diagrams, or special effects:

```html
<!-- Add in <head> -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- Use in slide content -->
{
    layout: "content",
    content: `
        <h2>Sales Data</h2>
        <canvas id="salesChart"></canvas>
        <script>
            // Initialize chart when slide is active
            new Chart(document.getElementById('salesChart'), {...});
        </script>
    `
}
```

---

## Keyboard Shortcuts Reference

Provide these to users:

| Action | Shortcut |
|--------|----------|
| Next slide | `→` or `Space` |
| Previous slide | `←` |
| First slide | `Home` |
| Last slide | `End` |
| Toggle fullscreen | `F` |
| Show shortcuts | `?` |
| Close overlay | `Esc` |

**Mobile:** Swipe left/right to navigate

---

## Troubleshooting

### Slides Not Displaying

**Issue:** Blank screen or "initializing" message
**Solution:** Check JavaScript console for errors. Ensure SLIDES array is valid JavaScript.

### Layout Broken

**Issue:** Content overlapping or misaligned
**Solution:** Verify HTML structure matches layout requirements. Check for unclosed tags.

### Colors Not Applied

**Issue:** Default colors showing instead of custom theme
**Solution:** Check PRESENTATION.theme object syntax. Ensure colors are valid hex codes.

### Navigation Not Working

**Issue:** Buttons or keyboard don't advance slides
**Solution:** Check browser console for JavaScript errors. Ensure no syntax errors in SLIDES array.

### Images Not Showing

**Issue:** Broken image icons
**Solution:** Verify data URIs are properly formatted. Check for special characters that need encoding.

---

## Example Presentation Structures

### Product Launch (15 slides)

1. Title - Product name and tagline
2. Problem - Current pain points
3. Solution - How product solves it
4. Section - Features
5-8. Feature details (one per slide)
9. Section - Benefits
10-12. Benefit highlights
13. Pricing/Availability
14. Call to action
15. Thank you + contact

### Technical Talk (20 slides)

1. Title - Talk title and speaker
2. Agenda - What will be covered
3. Section - Background
4-6. Context and motivation
7. Section - Core Concept
8-12. Technical deep dive
13. Section - Demo/Examples
14-16. Code examples and walkthroughs
17. Section - Results/Impact
18-19. Outcomes and learnings
20. Q&A

### Educational Lesson (25 slides)

1. Title - Lesson topic
2. Learning objectives
3. Section - Introduction
4-7. Background concepts
8. Section - Core Content
9-17. Main teaching points (one concept per slide)
18. Section - Practice
19-22. Examples and exercises
23. Summary - Key takeaways
24. Additional resources
25. Questions

---

## Best Practices

### DO:
✅ Read the entire template before starting
✅ Plan slide structure before coding
✅ Use appropriate layouts for content type
✅ Keep slides focused (one main idea each)
✅ Test navigation and responsiveness
✅ Ensure good color contrast
✅ Provide clear slide titles
✅ Use consistent formatting
✅ Include a clear opening and closing
✅ Validate HTML and JavaScript syntax

### DON'T:
❌ Overcrowd slides with too much text
❌ Use more than 3-4 fonts
❌ Create slides without clear purpose
❌ Forget to test on different screen sizes
❌ Use low-contrast color combinations
❌ Add unnecessary animations
❌ Skip the validation step
❌ Mix different design styles
❌ Rely on internet connectivity (except for fonts)
❌ Create presentations longer than needed

---

## File Organization

After creation, the presentation file structure:

```
presentation-name.html (single file containing):
├── <head>
│   ├── Meta tags
│   ├── Google Fonts link
│   ├── CSS styles (inline)
│   └── Title
├── <body>
│   ├── Header (with title and controls)
│   ├── Slide container
│   ├── Footer (with navigation)
│   └── Keyboard shortcuts overlay
└── <script>
    ├── PRESENTATION config
    ├── SLIDES array
    └── Navigation logic
```

**Dependencies:**
- Google Fonts (Poppins, Lora, JetBrains Mono) - requires internet
- All other resources are inline (CSS, JavaScript)

---

## Additional Resources

**Reference Documentation:**
- `reference/layouts.md` - Detailed layout guide and examples
- `reference/themes.md` - Theme customization and color theory
- `templates/viewer.html` - Base template with comments

**Examples:**
- `examples/` - Complete presentation examples (to be created)

**External Tools:**
- [Coolors.co](https://coolors.co/) - Color palette generator
- [Google Fonts](https://fonts.google.com/) - Web font library
- [SVG OMG](https://jakearchibald.github.io/svgomg/) - SVG optimizer
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - Accessibility testing

---

## Summary

This skill creates modern, interactive presentations as single HTML files that work in any browser. The workflow is:

1. **Understand requirements** - Gather content and style preferences
2. **Plan structure** - Organize slides logically
3. **Read template** - Study `templates/viewer.html`
4. **Define slides** - Create SLIDES array with appropriate layouts
5. **Configure theme** - Set colors and metadata
6. **Generate file** - Create complete HTML presentation
7. **Validate** - Test thoroughly before delivery

**Key success factors:**
- Use appropriate layouts for content type
- Maintain clear visual hierarchy
- Keep content density reasonable
- Test navigation and responsiveness
- Ensure accessibility standards

**The result:** A professional, self-contained presentation that can be opened in any browser, shared easily, and navigated smoothly with keyboard or mouse.
