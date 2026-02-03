# Web Presentation Layout Reference (Reveal.js)

This document describes the available slide layouts powered by Reveal.js and how to use them with advanced animation features.

## Table of Contents

1. [Title Slide](#1-title-slide)
2. [Content Slide](#2-content-slide)
3. [Two-Column Layout](#3-two-column-layout)
4. [Image + Text Layout](#4-image--text-layout)
5. [Quote Slide](#5-quote-slide)
6. [Section Divider](#6-section-divider)
7. [Nested Slides](#7-nested-slides-vertical-navigation)
8. [Fragment Animations](#fragment-animations)
9. [Auto-Animate](#auto-animate)
10. [Plugin Integrations](#plugin-integrations)

---

## 1. Title Slide

**Use for:** Opening slides, section breaks, closing slides

### Basic Structure
```html
<section class="slide-title" data-transition="zoom">
    <h1>Main Title</h1>
    <p class="subtitle">Subtitle or description</p>
    <p class="author">Author Name | Date</p>
</section>
```

### With Fragment Animations
```html
<section class="slide-title" data-transition="zoom">
    <h1 class="fragment fade-up">Main Title</h1>
    <p class="subtitle fragment fade-up">Subtitle appears second</p>
    <p class="author fragment fade-up">Author appears last</p>
</section>
```

### With Custom Background
```html
<section class="slide-title" data-background-gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
    <h1>Branded Title</h1>
    <p class="subtitle">With custom gradient</p>
</section>
```

**Styling Features:**
- Centered, full-screen layout
- Gradient background (primary → secondary colors)
- Large typography with text shadow
- Recommended transition: `zoom`, `fade`, or `convex`

**Best Practices:**
- ✅ Keep title concise (1-6 words)
- ✅ Use subtitle for context
- ✅ Author/date optional
- ✅ Use zoom transition for impact

---

## 2. Content Slide

**Use for:** Main content, bullet points, text, code examples

### Basic Structure
```html
<section class="slide-content">
    <h2>Slide Title</h2>
    <p>Introduction paragraph...</p>
    <ul>
        <li>Bullet point one</li>
        <li>Bullet point two</li>
        <li>Bullet point three</li>
    </ul>
</section>
```

### With Progressive Reveal (Fragments)
```html
<section class="slide-content">
    <h2>Progressive Disclosure</h2>
    <ul>
        <li class="fragment">Appears first</li>
        <li class="fragment">Appears second</li>
        <li class="fragment">Appears third</li>
        <li class="fragment highlight-red">Highlights in red</li>
    </ul>
    
    <aside class="notes">
        Emphasize the highlighted point.
        Spend 2 minutes on this slide.
    </aside>
</section>
```

### With Code Highlighting
```html
<section class="slide-content">
    <h2>Code Example</h2>
    <pre><code class="language-python" data-trim data-line-numbers="1-3|5-7">
def calculate_total(items):
    total = sum(item.price for item in items)
    return total

# Usage example
items = [Item(10), Item(20)]
result = calculate_total(items)
    </code></pre>
    
    <aside class="notes">
        Lines 1-3 show the function definition.
        Lines 5-7 demonstrate usage.
    </aside>
</section>
```

### With Multiple Code Blocks (Auto-Animate)
```html
<section data-auto-animate>
    <h2>Evolution of Code</h2>
    <pre><code data-trim data-line-numbers>
let x = 10;
    </code></pre>
</section>

<section data-auto-animate>
    <h2>Evolution of Code</h2>
    <pre><code data-trim data-line-numbers>
let x = 10;
let y = 20;
let sum = x + y;
console.log(sum);
    </code></pre>
</section>
```

**Supported Elements:**
- `<h2>`, `<h3>` - Headings (styled with theme colors)
- `<p>` - Paragraphs
- `<ul>`, `<ol>`, `<li>` - Lists with custom bullets
- `<code>` - Inline code (monospace)
- `<pre><code>` - Code blocks with syntax highlighting
- `<strong>` - Bold (colored with accent)
- `<em>` - Italic (colored with primary)

**Best Practices:**
- ✅ Limit to 5-7 bullet points
- ✅ Use fragments for progressive reveal
- ✅ Add speaker notes for presentation context
- ✅ Highlight specific code lines with `data-line-numbers`
- ❌ Don't overcrowd with text

---

## 3. Two-Column Layout

**Use for:** Comparisons, before/after, pros/cons, parallel concepts

### Basic Structure
```html
<section>
    <h2>Comparison</h2>
    <div class="two-column">
        <div>
            <h3>Left Column</h3>
            <ul>
                <li>Point one</li>
                <li>Point two</li>
            </ul>
        </div>
        <div>
            <h3>Right Column</h3>
            <ul>
                <li>Point one</li>
                <li>Point two</li>
            </ul>
        </div>
    </div>
</section>
```

### With Fragment Animations
```html
<section>
    <h2>Before vs After</h2>
    <div class="two-column">
        <div class="fragment fade-right">
            <h3>Before 😰</h3>
            <ul>
                <li>Slow performance</li>
                <li>Complex setup</li>
                <li>Limited features</li>
            </ul>
        </div>
        <div class="fragment fade-left">
            <h3>After ✨</h3>
            <ul>
                <li>2x faster</li>
                <li>One-click setup</li>
                <li>Full-featured</li>
            </ul>
        </div>
    </div>
</section>
```

### With Progressive Item Reveal
```html
<section>
    <h2>Pros and Cons</h2>
    <div class="two-column">
        <div>
            <h3>Pros</h3>
            <ul>
                <li class="fragment">Easy to use</li>
                <li class="fragment">Fast performance</li>
                <li class="fragment">Great support</li>
            </ul>
        </div>
        <div>
            <h3>Cons</h3>
            <ul>
                <li class="fragment">Higher cost</li>
                <li class="fragment">Learning curve</li>
            </ul>
        </div>
    </div>
</section>
```

**Best Practices:**
- ✅ Balance content between columns
- ✅ Use parallel structure
- ✅ Animate columns separately for impact
- ✅ Limit to 3-5 items per column
- ❌ Don't create uneven content distribution

---

## 4. Image + Text Layout

**Use for:** Product showcases, visual explanations, diagrams

### Basic Structure
```html
<section>
    <div class="image-text">
        <div>
            <h2>Feature Name</h2>
            <p>Description of the feature...</p>
            <ul>
                <li>Benefit one</li>
                <li>Benefit two</li>
            </ul>
        </div>
        <div>
            <img src="https://via.placeholder.com/600x400" alt="Feature screenshot">
        </div>
    </div>
</section>
```

### With Fragment Animations
```html
<section>
    <div class="image-text">
        <div>
            <h2>New Dashboard</h2>
            <p class="fragment">A completely redesigned interface...</p>
            <ul>
                <li class="fragment">Real-time updates</li>
                <li class="fragment">Customizable widgets</li>
                <li class="fragment">Dark mode support</li>
            </ul>
        </div>
        <div class="fragment fade-left">
            <img src="dashboard.png" alt="Dashboard screenshot">
        </div>
    </div>
</section>
```

### With Auto-Animate (Image Transformation)
```html
<section data-auto-animate>
    <h2>Before</h2>
    <div class="image-text">
        <div><p>Old interface design</p></div>
        <img src="old.png" data-id="product" style="width: 400px;">
    </div>
</section>

<section data-auto-animate>
    <h2>After</h2>
    <div class="image-text">
        <div><p>New modern design</p></div>
        <img src="new.png" data-id="product" style="width: 600px;">
    </div>
</section>
```

### With SVG Inline
```html
<section>
    <div class="image-text">
        <div>
            <h2>Architecture</h2>
            <ul>
                <li class="fragment">Microservices</li>
                <li class="fragment">API Gateway</li>
                <li class="fragment">Load Balancer</li>
            </ul>
        </div>
        <div>
            <svg width="400" height="300">
                <rect class="fragment" x="50" y="50" width="100" height="80" fill="#2E86AB"/>
                <rect class="fragment" x="200" y="50" width="100" height="80" fill="#A23B72"/>
                <line class="fragment" x1="100" y1="130" x2="250" y2="130" stroke="#F18F01" stroke-width="2"/>
            </svg>
        </div>
    </div>
</section>
```

**Best Practices:**
- ✅ Use high-quality images
- ✅ Include descriptive alt text
- ✅ Animate image and text separately
- ✅ Use SVG for diagrams and icons
- ✅ Reveal image after text for narrative flow
- ❌ Don't use tiny images

---

## 5. Quote Slide

**Use for:** Testimonials, impactful statements, emphasis, breaks

### Basic Structure
```html
<section class="slide-quote" data-background-gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
    <blockquote>
        An impactful quote that emphasizes a key message
        and inspires the audience.
    </blockquote>
    <cite>— Author Name, Title</cite>
</section>
```

### With Fragment Animation
```html
<section class="slide-quote" data-background-gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
    <blockquote class="fragment fade-up">
        "The best way to predict the future is to invent it."
    </blockquote>
    <cite class="fragment fade-up">— Alan Kay, Computer Scientist</cite>
</section>
```

### With Background Image
```html
<section class="slide-quote" 
         data-background-image="background.jpg" 
         data-background-opacity="0.3">
    <blockquote>
        "Innovation distinguishes between a leader and a follower."
    </blockquote>
    <cite>— Steve Jobs</cite>
</section>
```

**Best Practices:**
- ✅ Keep quotes concise (1-3 sentences)
- ✅ Always attribute the source
- ✅ Use for breaks between sections
- ✅ Choose meaningful, relevant quotes
- ❌ Don't overuse (1-2 per presentation)

---

## 6. Section Divider

**Use for:** Major topic transitions, chapter breaks

### Basic Structure
```html
<section class="slide-section" data-background-gradient="linear-gradient(135deg, #A23B72 0%, #F18F01 100%)">
    <h2>Part Two</h2>
</section>
```

### With Fragment and Number
```html
<section class="slide-section" data-transition="convex" data-background-gradient="linear-gradient(135deg, #2E86AB 0%, #A23B72 100%)">
    <div class="fragment" style="font-size: 0.5em; opacity: 0.8;">Section 02</div>
    <h2 class="fragment">Key Features</h2>
</section>
```

### With Icon
```html
<section class="slide-section" data-background-color="#2d6a4f">
    <div style="font-size: 4em;">🚀</div>
    <h2>Launch Phase</h2>
</section>
```

**Best Practices:**
- ✅ Use sparingly (2-4 per presentation)
- ✅ Choose distinct colors for each section
- ✅ Use convex or zoom transitions
- ✅ Keep text minimal
- ❌ Don't use for every topic change

---

## 7. Nested Slides (Vertical Navigation)

**Use for:** Hierarchical content, deep dives, optional details

### Basic Structure
```html
<!-- Main topic (horizontal) -->
<section>
    <section>
        <h2>Main Topic</h2>
        <p>Press ↓ to dive deeper</p>
    </section>
    
    <!-- Subtopic 1 (vertical) -->
    <section>
        <h3>Subtopic 1</h3>
        <p>Detailed explanation...</p>
    </section>
    
    <!-- Subtopic 2 (vertical) -->
    <section>
        <h3>Subtopic 2</h3>
        <p>More details...</p>
    </section>
    
    <!-- Subtopic 3 (vertical) -->
    <section>
        <h3>Subtopic 3</h3>
        <p>Even more details...</p>
    </section>
</section>

<!-- Next main topic (horizontal) -->
<section>
    <h2>Next Topic</h2>
</section>
```

### With Progressive Depth
```html
<section>
    <!-- Overview -->
    <section>
        <h2>Performance Optimization</h2>
        <ul>
            <li>Caching</li>
            <li>Compression</li>
            <li>Lazy Loading</li>
        </ul>
        <p style="font-size: 0.7em; opacity: 0.7;">↓ Explore each technique</p>
    </section>
    
    <!-- Deep dive 1 -->
    <section>
        <h3>Caching Strategy</h3>
        <pre><code class="language-javascript">
const cache = new Map();
function memoize(fn) {
    return (...args) => {
        const key = JSON.stringify(args);
        if (!cache.has(key)) {
            cache.set(key, fn(...args));
        }
        return cache.get(key);
    };
}
        </code></pre>
    </section>
    
    <!-- Deep dive 2 -->
    <section>
        <h3>Compression</h3>
        <p>Gzip vs Brotli comparison...</p>
    </section>
    
    <!-- Deep dive 3 -->
    <section>
        <h3>Lazy Loading</h3>
        <p>Implementation patterns...</p>
    </section>
</section>
```

**Best Practices:**
- ✅ Use for optional technical details
- ✅ Indicate vertical navigation visually (↓ arrow)
- ✅ Keep vertical stacks to 3-5 slides
- ✅ Main flow should work without vertical slides
- ❌ Don't nest too deeply (max 2 levels)

---

## Fragment Animations

Progressive reveal of content within a slide.

### Basic Fragments
```html
<ul>
    <li class="fragment">Default fade-in</li>
    <li class="fragment fade-up">Slide up</li>
    <li class="fragment fade-down">Slide down</li>
    <li class="fragment fade-left">Slide from right</li>
    <li class="fragment fade-right">Slide from left</li>
</ul>
```

### Emphasis Fragments
```html
<ul>
    <li class="fragment grow">Grows larger</li>
    <li class="fragment shrink">Shrinks smaller</li>
    <li class="fragment strike">Strikes through</li>
    <li class="fragment highlight-red">Highlights red</li>
    <li class="fragment highlight-blue">Highlights blue</li>
    <li class="fragment highlight-green">Highlights green</li>
</ul>
```

### Custom Fragment Order
```html
<p class="fragment" data-fragment-index="3">Third</p>
<p class="fragment" data-fragment-index="1">First</p>
<p class="fragment" data-fragment-index="2">Second</p>
```

### Combining Multiple Fragments
```html
<span class="fragment fade-in">
    <span class="fragment highlight-red">
        <span class="fragment fade-out">
            Fades in → Highlights red → Fades out
        </span>
    </span>
</span>
```

### Fragment in Lists (Recommended Pattern)
```html
<section>
    <h2>Key Benefits</h2>
    <ul>
        <li class="fragment"><strong>Fast</strong> - 2x performance improvement</li>
        <li class="fragment"><strong>Secure</strong> - Enterprise-grade encryption</li>
        <li class="fragment"><strong>Scalable</strong> - Handles 1M+ users</li>
    </ul>
</section>
```

---

## Auto-Animate

Smooth transitions between slide states.

### Basic Auto-Animate
```html
<section data-auto-animate>
    <h2>Auto-Animate Demo</h2>
</section>

<section data-auto-animate>
    <h2 style="margin-top: 200px; color: red;">Auto-Animate Demo</h2>
</section>
```

### Element Matching with data-id
```html
<section data-auto-animate>
    <div data-id="box" style="height: 100px; background: blue;"></div>
</section>

<section data-auto-animate>
    <div data-id="box" style="height: 300px; background: red;"></div>
</section>
```

### Code Morphing
```html
<section data-auto-animate>
    <h2>Code Evolution</h2>
    <pre><code data-trim data-id="code">
let x = 10;
    </code></pre>
</section>

<section data-auto-animate>
    <h2>Code Evolution</h2>
    <pre><code data-trim data-id="code">
let x = 10;
let y = 20;
let sum = x + y;
console.log(sum);
    </code></pre>
</section>
```

### Auto-Animate Settings
```html
<section data-auto-animate 
         data-auto-animate-easing="cubic-bezier(0.770, 0.000, 0.175, 1.000)"
         data-auto-animate-duration="2.0">
    <h2>Slow Animation</h2>
</section>
```

---

## Plugin Integrations

### Code Highlighting (Highlight.js)

**Supported Languages:** 190+ including JavaScript, Python, Java, C++, Go, Rust, SQL, HTML, CSS, etc.

```html
<section>
    <h2>Python Example</h2>
    <pre><code class="language-python" data-trim data-line-numbers>
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(f"Result: {result}")
    </code></pre>
</section>
```

**Highlight Specific Lines:**
```html
<pre><code class="language-javascript" data-trim data-line-numbers="1-2|4-6|8">
function calculate(x, y) {
    const sum = x + y;
    
    if (sum > 100) {
        return "Large number";
    }
    
    return sum;
}
</code></pre>
```

### Math Equations (KaTeX)

**Inline Math:**
```html
<p>The famous equation $E = mc^2$ shows mass-energy equivalence.</p>
```

**Display Math:**
```html
<section>
    <h2>Quadratic Formula</h2>
    <p>$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$</p>
</section>
```

**Multi-line Equations:**
```html
<p>
$$
\begin{aligned}
\nabla \times \vec{\mathbf{B}} &= \mu_0 \vec{\mathbf{J}} + \mu_0\epsilon_0 \frac{\partial \vec{\mathbf{E}}}{\partial t} \\
\nabla \cdot \vec{\mathbf{E}} &= \frac{\rho}{\epsilon_0}
\end{aligned}
$$
</p>
```

### Markdown Support

**External Markdown:**
```html
<section data-markdown="slides.md" 
         data-separator="^\n---\n$" 
         data-separator-vertical="^\n--\n$">
</section>
```

**Inline Markdown:**
```html
<section data-markdown>
    <textarea data-template>
        ## Slide Title
        
        - Point one <!-- .element: class="fragment" -->
        - Point two <!-- .element: class="fragment" -->
        
        **Bold** and *italic* text
        
        ```javascript
        const code = "highlighted";
        ```
    </textarea>
</section>
```

### Charts (Chart.js Integration)

```html
<!-- In <head> -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0"></script>

<!-- In slide -->
<section>
    <h2>Sales Growth</h2>
    <canvas id="salesChart" width="800" height="400"></canvas>
    <script>
        Reveal.on('slidechanged', event => {
            if (event.currentSlide.querySelector('#salesChart')) {
                new Chart(document.getElementById('salesChart'), {
                    type: 'line',
                    data: {
                        labels: ['Q1', 'Q2', 'Q3', 'Q4'],
                        datasets: [{
                            label: 'Revenue',
                            data: [12, 19, 25, 30],
                            borderColor: '#2E86AB',
                            backgroundColor: 'rgba(46, 134, 171, 0.1)',
                            tension: 0.4
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: { display: true }
                        }
                    }
                });
            }
        });
    </script>
</section>
```

### Diagrams (Mermaid Integration)

```html
<!-- In <head> -->
<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true, theme: 'dark' });
</script>

<!-- In slide -->
<section>
    <h2>System Architecture</h2>
    <div class="mermaid">
    graph TD
        A[Client] -->|HTTPS| B[Load Balancer]
        B --> C[Server 1]
        B --> D[Server 2]
        C --> E[(Database)]
        D --> E
    </div>
</section>
```

---

## Best Practices Summary

### ✅ DO:
- Use fragments for progressive reveal
- Add speaker notes to all important slides
- Leverage auto-animate for transformations
- Highlight code lines for clarity
- Use nested slides for optional deep dives
- Test all animations and transitions
- Include alt text for images
- Use appropriate transitions per slide type
- Keep fragment animations subtle
- Balance text and visuals

### ❌ DON'T:
- Overuse animations (causes distraction)
- Create overly deep nested structures
- Forget to test speaker view
- Use more than 2-3 fragment styles per slide
- Rely on color alone for information
- Create walls of text
- Use tiny fonts (< 24px)
- Animate every element
- Mix too many transition types
- Ignore accessibility

---

## Quick Reference Table

| Layout | Class | Best For | Key Feature |
|--------|-------|----------|-------------|
| Title | `slide-title` | Opens, closes, breaks | Full-screen impact |
| Content | `slide-content` | Main content, lists | Fragments, code |
| Two-Column | `two-column` | Comparisons | Parallel content |
| Image+Text | `image-text` | Visual explanations | Image showcase |
| Quote | `slide-quote` | Emphasis, breaks | Large typography |
| Section | `slide-section` | Chapter breaks | Colored background |
| Nested | `<section><section>` | Hierarchical content | Vertical navigation |

---

*For complete examples, see `examples/reveal-advanced-demo.html`*  
*For theme customization, see `themes.md`*  
*For Reveal.js API, see `SKILL.md`*
