# Web Presentation Layout Reference

This document describes the available slide layouts in the Web Presentation template and how to use them effectively.

## Available Layouts

### 1. Title Slide (`layout-title`)

**Use for:** Opening slides, section breaks, or closing slides

**Structure:**
```javascript
{
    layout: "title",
    content: `
        <h1>Main Title</h1>
        <div class="subtitle">Subtitle or tagline</div>
        <div class="author">Author name or additional info</div>
    `
}
```

**Styling:**
- Centered text
- Large, bold typography
- Gradient background using primary and secondary theme colors
- White text
- Perfect for impactful moments

**Best practices:**
- Keep title concise (1-6 words)
- Use subtitle for context or description
- Author field optional

---

### 2. Content Slide (`layout-content`)

**Use for:** Main content, bullet points, text blocks, code examples

**Structure:**
```javascript
{
    layout: "content",
    content: `
        <h2>Slide Title</h2>
        <p>Paragraph text goes here. You can include multiple paragraphs.</p>
        <ul>
            <li>Bullet point one</li>
            <li>Bullet point two</li>
            <li>Bullet point three</li>
        </ul>
        <p>You can also use inline <code>code snippets</code>.</p>
        <pre>
// Code blocks work too
function example() {
    return "formatted code";
}
        </pre>
    `
}
```

**Supported elements:**
- `<h2>` - Main slide heading (colored with theme primary)
- `<h3>` - Subheadings
- `<p>` - Paragraphs
- `<ul>`, `<ol>`, `<li>` - Lists
- `<code>` - Inline code
- `<pre>` - Code blocks
- `<strong>`, `<em>` - Text emphasis

**Best practices:**
- Limit to 5-7 bullet points per slide
- Use headings to create hierarchy
- Keep paragraphs concise
- Code blocks should be short and focused

---

### 3. Two Column Layout (`layout-two-column`)

**Use for:** Comparisons, parallel concepts, before/after, pros/cons

**Structure:**
```javascript
{
    layout: "two-column",
    content: `
        <h2>Slide Title</h2>
        <div class="columns">
            <div class="column">
                <h3>Left Column Title</h3>
                <p>Left column content...</p>
                <ul>
                    <li>Item one</li>
                    <li>Item two</li>
                </ul>
            </div>
            <div class="column">
                <h3>Right Column Title</h3>
                <p>Right column content...</p>
                <ul>
                    <li>Item one</li>
                    <li>Item two</li>
                </ul>
            </div>
        </div>
    `
}
```

**Best practices:**
- Balance content between columns
- Use parallel structure (similar formatting in both columns)
- Title spans both columns
- Great for comparison tables or side-by-side explanations

---

### 4. Image + Text Layout (`layout-image-text`)

**Use for:** Visual explanations, product showcases, diagrams with descriptions

**Structure:**
```javascript
{
    layout: "image-text",
    content: `
        <img src="data:image/svg+xml,..." alt="Description">
        <div class="text-content">
            <h2>Title</h2>
            <p>Description of the image or additional context.</p>
            <ul>
                <li>Key point one</li>
                <li>Key point two</li>
            </ul>
        </div>
    `
}
```

**Image options:**
- Use data URIs for embedded images
- Use CDN URLs for external images
- SVG for diagrams and illustrations
- PNG/JPG for photos

**Best practices:**
- Image should be high quality
- Alt text is important for accessibility
- Text content should complement, not repeat, the image
- Image appears on left, text on right

---

### 5. Quote Layout (`layout-quote`)

**Use for:** Testimonials, impactful quotes, philosophical statements

**Structure:**
```javascript
{
    layout: "quote",
    content: `
        <blockquote>
            The quote text goes here. Keep it concise and impactful.
        </blockquote>
        <cite>— Author Name</cite>
    `
}
```

**Styling:**
- Large, serif font
- Centered on light background
- Decorative quotation mark
- Attribution below quote

**Best practices:**
- Keep quotes short (1-3 sentences)
- Always attribute the source
- Use for emphasis and breaks between sections

---

### 6. Section Divider (`layout-section`)

**Use for:** Major section breaks, chapter markers, topic transitions

**Structure:**
```javascript
{
    layout: "section",
    content: `
        <div class="section-number">Section 1</div>
        <h2>Section Title</h2>
    `
}
```

**Styling:**
- Full-screen colored background (using theme accent color)
- White text
- Large, bold typography
- Centered content

**Best practices:**
- Use sparingly (major transitions only)
- Section number is optional
- Keep title short (1-4 words)
- Creates visual rhythm in long presentations

---

## Layout Selection Guide

**Choose your layout based on content type:**

| Content Type | Recommended Layout |
|--------------|-------------------|
| Title/Opening | `layout-title` |
| Main content with text and bullets | `layout-content` |
| Comparisons or parallel ideas | `layout-two-column` |
| Visual + explanation | `layout-image-text` |
| Impactful quote | `layout-quote` |
| Section break | `layout-section` |
| Code examples | `layout-content` |

---

## Mixing Layouts

A good presentation uses varied layouts to maintain visual interest:

**Suggested flow:**
1. **Title slide** - Introduction
2. **Content slide** - Overview
3. **Section slide** - Topic 1
4. **Content slides** - Details
5. **Two-column slide** - Comparison
6. **Quote slide** - Emphasis
7. **Section slide** - Topic 2
8. **Image-text slide** - Visual explanation
9. **Content slides** - More details
10. **Title slide** - Conclusion

**Visual rhythm:**
- Alternate between text-heavy and visual slides
- Use section dividers to create chapters
- Break up long sections with quotes
- Balance information density

---

## Customization Tips

### Modifying Layouts

If you need custom layouts, add CSS classes in the `<style>` section:

```css
/* Custom layout example */
.slide.layout-custom {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 40px;
}
```

Then use it in your slide:

```javascript
{
    layout: "custom",
    content: `<div>Custom content structure</div>`
}
```

### Layout-Specific Styling

Target specific layouts for unique styling:

```css
/* Make all title slides use a different color */
.slide.layout-title {
    background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
}

/* Adjust content slide padding */
.slide.layout-content {
    padding: 80px 100px;
}
```

---

## Responsive Behavior

All layouts are responsive:

- **Desktop (>1024px):** Full layout as designed
- **Tablet (768px-1024px):** Two-column layouts collapse to single column, font sizes adjust
- **Mobile (<768px):** All layouts stack vertically, reduced padding and font sizes

The template handles this automatically - no additional work needed.

---

## Accessibility Considerations

- All layouts support keyboard navigation
- Images should have descriptive `alt` text
- Color contrast meets WCAG AA standards
- Font sizes are readable at all screen sizes
- Focus states are clearly visible

---

## Examples

See the `examples/` directory for complete presentation examples using all layout types.
