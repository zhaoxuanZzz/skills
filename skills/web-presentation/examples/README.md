# Web Presentation Examples

This directory contains complete example presentations demonstrating the features and capabilities of the Web Presentation skill.

## Available Examples

### 1. Product Launch Demo (`product-launch-demo.html`)

A complete product launch presentation showcasing all available layouts and features.

**Demonstrates:**
- All 6 layout types (title, content, two-column, image+text, quote, section)
- Custom theme colors (professional blue)
- Proper slide flow and structure
- Code examples and formatting
- Progressive disclosure of information

**Slide count:** 13 slides

**Theme:** Professional blue (suitable for business/corporate presentations)

**To view:** Open `product-launch-demo.html` in any modern web browser

---

## How to Use These Examples

### Viewing

1. **Double-click** the HTML file to open in your default browser
2. Or **right-click** → Open with → Choose your browser
3. Use **arrow keys** or **on-screen buttons** to navigate
4. Press **F** for fullscreen mode
5. Press **?** to see keyboard shortcuts

### Learning from Examples

Each example is fully self-contained and can be:
- **Viewed** as reference for layout ideas
- **Copied** as a starting point for your own presentations
- **Modified** to match your content and brand
- **Studied** to understand the code structure

### Modifying

To create your own presentation based on an example:

1. **Copy** the HTML file
2. **Edit** the `PRESENTATION` object:
   ```javascript
   const PRESENTATION = {
       title: "Your Title Here",
       author: "Your Name",
       theme: {
           primary: "#your-color",
           secondary: "#your-color",
           accent: "#your-color"
       }
   };
   ```

3. **Edit** the `SLIDES` array:
   ```javascript
   const SLIDES = [
       {
           layout: "title",
           content: `<h1>Your Content</h1>`
       },
       // Add more slides...
   ];
   ```

4. **Save** and reload in browser

---

## Creating New Presentations

When creating your own presentations from scratch:

1. **Start with** `templates/viewer.html` (the base template)
2. **Read** `../SKILL.md` for complete workflow guidance
3. **Reference** `../reference/layouts.md` for layout options
4. **Reference** `../reference/themes.md` for color schemes
5. **Look at** these examples for inspiration

---

## Tips for Effective Presentations

### Structure
- Start with a strong title slide
- Use section dividers to break up content
- Limit to 5-7 bullet points per slide
- End with a clear call-to-action

### Visual Design
- Choose colors that work well together
- Ensure good contrast for readability
- Use images sparingly but effectively
- Maintain consistent styling throughout

### Navigation
- Test all slides before presenting
- Use keyboard shortcuts during presentation
- Practice slide transitions
- Know your content flow

---

## Browser Compatibility

All examples work in modern browsers:
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

**Note:** Internet Explorer is not supported.

---

## Additional Examples Coming Soon

Future examples will include:
- Technical conference talk
- Educational lesson plan
- Creative portfolio showcase
- Minimal monochrome theme
- Dark mode presentation

---

## Questions or Issues?

If you find issues with these examples or have suggestions for improvements, please refer to the main skill documentation in `../SKILL.md`.
