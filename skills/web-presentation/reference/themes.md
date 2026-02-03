# Web Presentation Theme Reference

This document describes how to customize the visual theme of your web presentations.

## Theme System Overview

The Web Presentation template uses CSS custom properties (variables) for easy theming. All theme colors are defined in the `:root` selector and can be overridden in the `PRESENTATION` configuration object.

## Default Theme

The default theme uses Anthropic brand colors:

```javascript
const PRESENTATION = {
    title: "My Presentation",
    author: "Your Name",
    theme: {
        primary: "#d97757",    // Anthropic Orange
        secondary: "#6a9bcc",  // Anthropic Blue
        accent: "#788c5d"      // Anthropic Green
    }
};
```

**Color usage:**
- **Primary:** Main headings, progress bar, navigation buttons, highlights
- **Secondary:** Gradient accents, alternative buttons
- **Accent:** Section dividers, tertiary elements

---

## CSS Variables Reference

### Core Theme Variables

```css
:root {
    /* Theme colors (customizable) */
    --theme-primary: #d97757;
    --theme-secondary: #6a9bcc;
    --theme-accent: #788c5d;
    --theme-bg: #faf9f5;
    --theme-text: #141413;
    --theme-text-light: #b0aea5;
    
    /* Typography */
    --font-sans: 'Poppins', sans-serif;
    --font-serif: 'Lora', serif;
    --font-mono: 'JetBrains Mono', monospace;
}
```

### Brand Colors (Fixed)

These are Anthropic brand colors and should generally not be changed:

```css
:root {
    --anthropic-dark: #141413;
    --anthropic-light: #faf9f5;
    --anthropic-mid-gray: #b0aea5;
    --anthropic-light-gray: #e8e6dc;
    --anthropic-orange: #d97757;
    --anthropic-blue: #6a9bcc;
    --anthropic-green: #788c5d;
}
```

---

## Preset Themes

### 1. Professional Blue (Default Variant)

**Best for:** Corporate presentations, business reports

```javascript
theme: {
    primary: "#2563eb",     // Strong blue
    secondary: "#0891b2",   // Cyan
    accent: "#059669"       // Green
}
```

**Character:** Clean, trustworthy, professional

---

### 2. Warm Sunset

**Best for:** Creative presentations, marketing materials

```javascript
theme: {
    primary: "#f97316",     // Orange
    secondary: "#ec4899",   // Pink
    accent: "#8b5cf6"       // Purple
}
```

**Character:** Energetic, creative, warm

---

### 3. Forest Green

**Best for:** Environmental topics, natural themes

```javascript
theme: {
    primary: "#059669",     // Emerald
    secondary: "#0d9488",   // Teal
    accent: "#84cc16"       // Lime
}
```

**Character:** Natural, calming, organic

---

### 4. Monochrome

**Best for:** Minimalist designs, technical content

```javascript
theme: {
    primary: "#18181b",     // Near black
    secondary: "#52525b",   // Gray
    accent: "#a1a1aa"       // Light gray
}
```

**Character:** Minimal, elegant, focused

---

### 5. Vibrant Purple

**Best for:** Tech presentations, modern designs

```javascript
theme: {
    primary: "#7c3aed",     // Purple
    secondary: "#2563eb",   // Blue
    accent: "#ec4899"       // Pink
}
```

**Character:** Modern, tech-savvy, bold

---

### 6. Earth Tones

**Best for:** Academic, research, sustainability topics

```javascript
theme: {
    primary: "#92400e",     // Brown
    secondary: "#b45309",   // Amber
    accent: "#065f46"       // Dark green
}
```

**Character:** Grounded, serious, natural

---

## Custom Theme Creation

### Step 1: Choose Your Colors

Use a color palette generator or design system:
- [Coolors.co](https://coolors.co/) - Generate palettes
- [Adobe Color](https://color.adobe.com/) - Color wheel tool
- Use existing brand colors
- Ensure sufficient contrast for accessibility

### Step 2: Define Relationships

**Primary color:** Most prominent, used for emphasis
- Should be bold and eye-catching
- Used in headings, buttons, links

**Secondary color:** Complementary or analogous to primary
- Should work well with primary in gradients
- Used for accents and variety

**Accent color:** Provides additional variation
- Can be contrasting or part of the same family
- Used sparingly for special elements

### Step 3: Test Contrast

Ensure your colors meet accessibility standards:

**WCAG AA Requirements:**
- Normal text: 4.5:1 contrast ratio
- Large text (18pt+): 3:1 contrast ratio

**Tools:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- Browser DevTools

### Step 4: Apply Your Theme

```javascript
const PRESENTATION = {
    title: "My Presentation",
    author: "Your Name",
    theme: {
        primary: "#your-primary-color",
        secondary: "#your-secondary-color",
        accent: "#your-accent-color"
    }
};
```

---

## Typography Customization

### Default Fonts

The template uses Google Fonts:

- **Sans-serif (Poppins):** UI elements, body text
- **Serif (Lora):** Titles, headings
- **Monospace (JetBrains Mono):** Code blocks

### Changing Fonts

**Option 1: Use different Google Fonts**

1. Update the `<link>` tag in the `<head>`:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
```

2. Update CSS variables:

```css
:root {
    --font-sans: 'Inter', sans-serif;
    --font-serif: 'Playfair Display', serif;
    --font-mono: 'Fira Code', monospace;
}
```

**Option 2: Use system fonts** (for better performance)

```css
:root {
    --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-serif: 'Georgia', 'Times New Roman', serif;
    --font-mono: 'SF Mono', 'Monaco', 'Consolas', monospace;
}
```

### Font Pairing Guidelines

**Classic combinations:**
- **Serif + Sans:** Playfair Display + Inter
- **Modern:** Montserrat + Open Sans
- **Elegant:** Cormorant + Work Sans
- **Technical:** IBM Plex Sans + IBM Plex Mono

**Avoid:**
- Using more than 3 font families
- Pairing similar fonts
- Overusing decorative fonts

---

## Advanced Customization

### Background Patterns

Add subtle texture to slides:

```css
.slide {
    background-image: url('data:image/svg+xml,...');
    background-size: 50px 50px;
    background-blend-mode: multiply;
    background-color: white;
}
```

### Gradient Variations

Customize title slide gradients:

```css
.slide.layout-title {
    background: linear-gradient(135deg, 
        var(--theme-primary) 0%, 
        var(--theme-secondary) 50%,
        var(--theme-accent) 100%
    );
}
```

### Shadow Customization

Adjust slide shadow depth:

```css
.slide {
    box-shadow: 0 30px 80px rgba(20, 20, 19, 0.2);
}
```

### Animation Timing

Modify slide transitions:

```css
.slide {
    transition: all 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## Dark Mode Theme

Create a dark theme variation:

```javascript
theme: {
    primary: "#60a5fa",     // Light blue
    secondary: "#a78bfa",   // Light purple
    accent: "#34d399"       // Light green
}
```

Then add custom CSS:

```css
:root {
    --theme-bg: #1f2937;           /* Dark gray */
    --theme-text: #f9fafb;         /* Near white */
    --theme-text-light: #9ca3af;  /* Medium gray */
}

.slide {
    background: #111827;  /* Darker background */
    color: #f9fafb;
}

.presentation-header,
.presentation-footer {
    background: rgba(31, 41, 55, 0.95);
    border-color: #374151;
}
```

---

## Theming Best Practices

### DO:
✅ Choose colors with purpose (align with brand or topic)
✅ Test on different screens and devices
✅ Ensure sufficient contrast for readability
✅ Use consistent color meanings (primary = emphasis)
✅ Limit to 3-4 main colors
✅ Consider color blindness accessibility

### DON'T:
❌ Use colors that clash or compete
❌ Sacrifice readability for aesthetics
❌ Overuse gradients or effects
❌ Mix too many visual styles
❌ Forget to test in fullscreen mode
❌ Use pure black (#000) or pure white (#fff) for large areas

---

## Color Psychology Guide

**Red (#dc2626):** Urgency, passion, attention
**Orange (#f97316):** Energy, creativity, friendliness
**Yellow (#eab308):** Optimism, clarity, warmth
**Green (#059669):** Growth, nature, success
**Blue (#2563eb):** Trust, professionalism, calm
**Purple (#7c3aed):** Innovation, luxury, creativity
**Gray (#52525b):** Neutrality, balance, sophistication
**Brown (#92400e):** Stability, earthiness, reliability

---

## Resources

### Color Tools
- **Coolors:** Generate color palettes
- **Adobe Color:** Color wheel and harmonies
- **ColorHunt:** Curated color palettes
- **Paletton:** Advanced color scheme designer

### Accessibility Tools
- **WebAIM Contrast Checker:** WCAG compliance
- **Colorblind Web Page Filter:** Simulate color blindness
- **Stark:** Figma plugin for accessibility

### Font Resources
- **Google Fonts:** Free web fonts
- **Font Pair:** Font pairing inspiration
- **Typewolf:** Typography inspiration

---

## Examples

See complete themed presentations in the `examples/` directory:
- `corporate-blue.html` - Professional business theme
- `creative-sunset.html` - Warm, creative theme
- `minimal-mono.html` - Minimalist monochrome
- `nature-green.html` - Earth tones and natural theme
