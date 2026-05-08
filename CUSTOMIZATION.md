# CUSTOMIZATION GUIDE - Digital Identity Portfolio

This guide explains how to customize every aspect of the portfolio.

## Content Customization

### Profile Information

**Via Admin Panel** (Recommended):
1. Go to http://127.0.0.1:8000/admin/
2. Click "Profile"
3. Edit:
   - Name
   - Title
   - Bio (bio_strong)
   - Contact phrase

**Via Python Shell**:
```bash
python manage.py shell
from identity.models import Profile

profile = Profile.objects.first()
profile.name = "Your Name"
profile.title = "Your Title"
profile.bio_strong = "Your bio"
profile.save()

exit()
```

### Adding/Editing Skills

**Via Admin Panel**:
1. Go to http://127.0.0.1:8000/admin/
2. Click "Skills"
3. Click "Add Skill"
4. Fill in:
   - **Name**: Skill name (e.g., "Python", "Docker")
   - **Icon Class**: FontAwesome icon (e.g., "fa-python")
   - **Order**: Display order (lower number = appears first)

**Icon Resources**:
- FontAwesome Icons: https://fontawesome.com/icons
- Common icons:
  - Programming: fa-python, fa-js, fa-java, fa-php
  - DevOps: fa-docker, fa-kubernetes (use fa-cloud), fa-server
  - Tools: fa-github, fa-git-alt, fa-gitlab
  - Security: fa-lock, fa-shield-alt, fa-user-secret
  - Other: fa-database, fa-cloud, fa-network-wired

### Adding/Editing Projects

**Via Admin Panel**:
1. Go to http://127.0.0.1:8000/admin/
2. Click "Projects"
3. Click "Add Project"
4. Fill in:
   - **Title**: Project name
   - **Description**: Detailed description (appears on hover)
   - **Tech Stack**: Comma-separated list (e.g., "Python, Docker, Kubernetes")
   - **Image**: Upload screenshot (optional)
   - **Link**: External URL (GitHub, demo, etc.) - optional
   - **Order**: Display order

### Adding/Editing Timeline Events

**Via Admin Panel**:
1. Go to http://127.0.0.1:8000/admin/
2. Click "Timeline Events"
3. Click "Add Timeline Event"
4. Fill in:
   - **Year**: Year of event
   - **Title**: Event name/headline
   - **Description**: Event details
   - **Order**: Display order

---

## Visual Customization

### Color Theme

Edit `identity/static/css/style.css` root variables:

```css
:root {
    /* Change background */
    --bg-primary: #0a0a0a;      /* Main background */
    --bg-secondary: #1a1a2e;    /* Card background */
    
    /* Change text colors */
    --text-primary: #e0e0e0;    /* Main text */
    --text-secondary: #a0a0a0;  /* Dimmer text */
    
    /* Change accent colors (glow/highlight) */
    --cyan: #00ffff;            /* Primary accent */
    --magenta: #ff00ff;         /* Secondary accent */
}
```

### Example: Change to Green/Purple Theme
```css
:root {
    --cyan: #00ff00;            /* Green */
    --magenta: #ff0080;         /* Pink */
    --text-primary: #e0e0e0;
    --bg-primary: #0a0a0a;
}
```

### Example: Lighter Dark Theme
```css
:root {
    --bg-primary: #1a1a2e;      /* Lighter background */
    --bg-secondary: #2a2a4e;    /* Lighter cards */
    --text-primary: #ffffff;    /* Brighter text */
    --text-secondary: #b0b0b0;
}
```

### Typography

Change fonts in CSS (around line 70):
```css
body {
    font-family: 'Courier New', 'Courier', monospace;  /* Monospace (hacker theme) */
    /* Alternative fonts:
       'Courier New' - monospace
       'Arial', sans-serif - clean
       'Georgia', serif - elegant
       'Trebuchet MS' - modern
    */
}
```

### Animations

#### Change typing speed
In `identity/static/js/script.js`, find the `typeCharacter()` function:
```javascript
// Slow it down (200-300ms per character)
const delay = Math.random() * 250 + 200;

// Speed it up (30-80ms per character)
const delay = Math.random() * 50 + 30;
```

#### Change scroll animation fade duration
In `identity/static/css/style.css`:
```css
.fade-in {
    transition: opacity 0.8s ease, transform 0.8s ease;  /* Change 0.8s */
    /* Faster: 0.4s */
    /* Slower: 1.5s */
}
```

#### Change scroll fade trigger threshold
In `identity/static/js/script.js`:
```javascript
const observer = new IntersectionObserver((entries) => {
    // ...
}, {
    threshold: 0.1,  /* Change this (0-1) */
    /* 0 = trigger when any part is visible */
    /* 0.5 = trigger when 50% is visible */
    /* 1 = trigger when fully visible */
});
```

### Cards and Borders

Edit glass effect styling:
```css
.glass {
    background: rgba(26, 26, 46, 0.7);
    backdrop-filter: blur(12px);  /* Blur intensity */
    border: 1px solid rgba(0, 255, 255, 0.1);  /* Border color */
}
```

- **Increase blur**: Change `blur(12px)` to `blur(20px)`
- **More transparent**: Change `rgba(..., 0.7)` to `rgba(..., 0.5)`
- **Stronger border glow**: Change `0.1)` to `0.3)`

### Spacing

Adjust spacing in CSS root variables:
```css
:root {
    --spacing-small: 0.5rem;
    --spacing-medium: 1rem;
    --spacing-large: 2rem;
    --spacing-xl: 3rem;
}
```

Example:
```css
--spacing-xl: 5rem;  /* Bigger sections */
--spacing-large: 1rem;  /* Tighter layout */
```

### Responsive Breakpoints

Edit mobile breakpoints in CSS (around line 480):
```css
/* Tablets and smaller */
@media (max-width: 768px) {
    /* Styles for tablets */
}

/* Mobile phones */
@media (max-width: 480px) {
    /* Styles for small phones */
}
```

---

## Layout Customization

### Change Hero Section
Edit `identity/templates/identity/home.html`:
```html
<section id="hero" class="fade-in">
    <div class="container">
        <div class="hero-content">
            <h1 id="typed-name"></h1>
            <!-- Add custom content here -->
        </div>
    </div>
</section>
```

Add buttons, additional text, or background effects.

### Change Section Order
In `home.html`, reorder sections:
```html
<!-- Move sections in this file to change order -->
<section id="hero">...</section>
<section id="about">...</section>
<section id="projects">...</section>  <!-- Move this higher -->
<section id="skills">...</section>
```

### Hide Sections (Keep but invisible)
```html
<!-- Add style="display: none;" to hide -->
<section id="about" style="display: none;">
    ...
</section>
```

### Add New Sections
```html
<!-- Add new section before footer -->
<section id="new-section" class="fade-in">
    <div class="container">
        <h2>New Section Title</h2>
        <!-- Your content here -->
    </div>
</section>
```

Don't forget to add CSS styling in `style.css`!

---

## Contact Links Customization

Edit contact links in `home.html` (around line 160):

```html
<!-- Change email -->
<a href="mailto:your-email@example.com" class="contact-link">

<!-- Change GitHub -->
<a href="https://github.com/your-username" target="_blank" class="contact-link">

<!-- Change LinkedIn -->
<a href="https://linkedin.com/in/your-profile" target="_blank" class="contact-link">

<!-- Add new link -->
<a href="https://your-link.com" target="_blank" class="contact-link">
    <i class="fas fa-icon-name contact-icon"></i>
    Link Label
</a>
```

---

## Advanced Customization

### Add Image Gallery
Add to template:
```html
<section id="gallery" class="fade-in">
    <div class="container">
        <h2>Gallery</h2>
        <div class="gallery-grid">
            {% for image in images %}
                <img src="{{ image.url }}" alt="Gallery image">
            {% endfor %}
        </div>
    </div>
</section>
```

Add CSS:
```css
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.gallery-grid img {
    width: 100%;
    border-radius: 8px;
    transition: transform 0.3s;
}

.gallery-grid img:hover {
    transform: scale(1.05);
}
```

### Add Blog Section
Create new model in `models.py`:
```python
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
```

Then register in `admin.py` and add to template.

### Add Dark/Light Theme Toggle
```javascript
// Add to script.js
function toggleTheme() {
    document.body.classList.toggle('light-theme');
    localStorage.setItem('theme', document.body.className);
}

// Restore saved theme
window.addEventListener('load', () => {
    const saved = localStorage.getItem('theme');
    if (saved) document.body.className = saved;
});
```

### Add Smooth Scroll Animation
Add to script.js:
```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        target.scrollIntoView({ behavior: 'smooth' });
    });
});
```

---

## SEO Customization

Edit meta tags in `home.html`:
```html
<title>Your Name - Portfolio</title>
<meta name="description" content="Your professional description">
<meta name="keywords" content="keyword1, keyword2, keyword3">
```

Add Open Graph for social sharing:
```html
<meta property="og:title" content="Your Name - Portfolio">
<meta property="og:description" content="Your description">
<meta property="og:image" content="{% static 'images/preview.png' %}">
<meta property="og:url" content="https://yourdomain.com">
```

---

## Performance Optimization

### Compress Images
- Use tools like TinyPNG, ImageOptim
- Recommended size: <500KB per image
- Format: PNG for graphics, JPG for photos

### Minify CSS/JS
- Use online minifiers or build tools
- Reduces file size, improves loading time

### Lazy Load Images
```html
<img src="image.jpg" loading="lazy" alt="description">
```

### Cache Static Files
Add to settings.py:
```python
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
```

---

## Common Customization Tasks

### Change site title globally
```python
# In settings.py
SITE_NAME = "Ali Mahmoud"
```

### Add Google Analytics
```html
<!-- Add to base template before </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

### Add Custom Font
```html
<!-- In <head> -->
<link href="https://fonts.googleapis.com/css2?family=YOUR+FONT&display=swap" rel="stylesheet">
```

```css
body {
    font-family: 'Your Font', sans-serif;
}
```

---

## Testing Changes

1. Start development server: `python manage.py runserver`
2. Open browser to http://127.0.0.1:8000/
3. Modify files and save
4. Refresh browser (Ctrl+F5 for hard refresh)
5. Check console for errors (F12 > Console)

---

## Troubleshooting Customization

### Changes not showing
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache
- Restart development server

### Template errors
- Check Django console for error messages
- Verify template syntax
- Test with `python manage.py check`

### CSS not working
- Verify file path in template
- Check syntax errors
- Ensure static files are collected

---

For more help, see README.md and SETUP.md
