# 📑 PROJECT INDEX - Digital Identity Portfolio

Complete guide to all files and how to use them.

---

## 🚀 Getting Started

**Start here** if you're new:
1. Read [QUICKSTART.md](QUICKSTART.md) - 5 minute setup
2. Follow [SETUP.md](SETUP.md) - Detailed installation
3. Check out the running site at http://127.0.0.1:8000/

---

## 📖 Documentation Files

### Main Documentation
- **[README.md](README.md)** - Complete project overview, features, tech stack
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute quick start guide
- **[SETUP.md](SETUP.md)** - Detailed setup and installation instructions
- **[CUSTOMIZATION.md](CUSTOMIZATION.md)** - How to customize every aspect
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment guides

### Reference
- **[.env.example](.env.example)** - Example environment variables
- **[requirements.txt](requirements.txt)** - Python dependencies

---

## 🐍 Django Project Files

### Project Configuration
- **[cyber_portfolio/settings.py](cyber_portfolio/settings.py)**
  - Django configuration, database setup, installed apps
  - Static/media file configuration
  - Security settings (update before production!)

- **[cyber_portfolio/urls.py](cyber_portfolio/urls.py)**
  - Root URL routing, includes identity app URLs
  - Static/media file serving configuration

- **[cyber_portfolio/wsgi.py](cyber_portfolio/wsgi.py)**
  - WSGI entry point for production servers

- **[cyber_portfolio/asgi.py](cyber_portfolio/asgi.py)**
  - ASGI entry point for async servers

- **[manage.py](manage.py)**
  - Django management command utility
  - Usage: `python manage.py <command>`

---

## 🎨 Identity App Files

### Models & Database
- **[identity/models.py](identity/models.py)** ⭐ CORE FILE
  - **Profile**: Single record for portfolio owner
    - Fields: name, title, bio_strong, contact_phrase
  - **Skill**: Technologies/skills with icons
    - Fields: name, icon_class, order
  - **Project**: Portfolio projects
    - Fields: title, description, tech_stack, image, link, order
  - **TimelineEvent**: Career timeline milestones
    - Fields: year, title, description, order

- **[identity/utils.py](identity/utils.py)**
  - `populate_default_data()`: Inserts default records into database
  - Uses `get_or_create()` to prevent duplicates
  - Called on app startup and every view

- **[identity/migrations/](identity/migrations/)**
  - Auto-generated migration files
  - Track database schema changes
  - Applied with `python manage.py migrate`

### Views & Routing
- **[identity/views.py](identity/views.py)** ⭐ CORE FILE
  - `HomeView`: Class-based view for portfolio homepage
  - `home()`: Function-based view alternative
  - Retrieves all data from database and renders template

- **[identity/urls.py](identity/urls.py)**
  - App URL patterns
  - Routes `/` to home view

### Admin Interface
- **[identity/admin.py](identity/admin.py)** ⭐ CORE FILE
  - Django admin configuration for all models
  - `ProfileAdmin`: Prevents multiple profiles, prevents deletion
  - `SkillAdmin`: Inline editing of order field
  - `ProjectAdmin`: Search, inline editing, image upload
  - `TimelineEventAdmin`: Ordering and search

### App Configuration
- **[identity/apps.py](identity/apps.py)**
  - App configuration class
  - `ready()` method: Calls `populate_default_data()` on startup
  - Ensures default data exists before rendering

---

## 🎨 Frontend Files

### Templates
- **[identity/templates/identity/home.html](identity/templates/identity/home.html)** ⭐ CORE FILE
  - Main portfolio template (complete page)
  - Sections: Hero, About, Skills, Projects, Timeline, Contact, Footer
  - Uses Django template tags to display database content
  - All sections have `class="fade-in"` for scroll animations
  - FontAwesome icons: https://fontawesome.com/icons

### Stylesheets
- **[identity/static/css/style.css](identity/static/css/style.css)** ⭐ CORE FILE
  - Complete CSS styling (1000+ lines, heavily commented)
  - **Root variables**: Dark theme colors, cyan/magenta accents
  - **Global styles**: Typography, links, code blocks
  - **Layout**: Sections, containers, responsive grid
  - **Animations**: Fade-in/fade-out, typing cursor, hover effects
  - **Components**: Hero, About, Skills, Projects, Timeline, Contact
  - **Glass effect**: Blur backdrop filters on cards
  - **Responsive**: Mobile breakpoints at 768px and 480px
  - Colors:
    - Background: `#0a0a0a` (deep black)
    - Text: `#e0e0e0` (light gray)
    - Cyan accent: `#00ffff`
    - Magenta accent: `#ff00ff`

### JavaScript
- **[identity/static/js/script.js](identity/static/js/script.js)** ⭐ CORE FILE
  - **Typing effect**: Character-by-character animation of name
    - Function: `initTypingEffect()`
    - Delay: 50-150ms per character (randomized)
  - **Scroll animations**: Fade-in/fade-out on scroll
    - Function: `initScrollFadeEffect()`
    - Uses Intersection Observer API
    - Threshold: 10% visible to trigger animation
  - **Interactions**: Hover effects on cards
    - Function: `initInteractions()`
  - Utility functions: `scrollToElement()`, `getScrollPercentage()`

---

## 📊 Database Models & Data

### Default Data (Automatically Loaded)

**Profile** (1 record)
```python
name: "Ali Mahmoud"
title: "Penetration Tester & Automation Engineer"
bio_strong: "I break systems to protect them.. and build defense lines with code."
contact_phrase: "No ordinary contact form. Just send a signal to:"
```

**Skills** (10 records)
1. IT Infrastructure - fa-network-wired
2. Linux (Kali, Ubuntu, RHEL) - fa-linux
3. Networking (TCP/IP, Firewalls, Wireshark) - fa-globe
4. DevOps - fa-cogs
5. Git & GitFlow - fa-git-alt
6. GitHub Actions - fa-github
7. Docker & Podman - fa-docker
8. Kubernetes (k8s) - fa-cloud
9. Python / Bash - fa-python
10. SIEM (Splunk, ELK) - fa-chart-line

**Projects** (3 records)
1. Threat-Hunter ELK Stack - ELK, Docker, Python, Suricata
2. CI/CD Security Pipeline - GitHub Actions, Docker, Snyk, Trivy
3. Red Team Automation Tool - Bash, Python, Metasploit API

**Timeline Events** (4 records)
1. 2018 - Beginning of Passion
2. 2020 - Certified Ethical Hacker (CEH)
3. 2022 - Merging Security with DevOps
4. 2024 - Automating Attacks & Defense

---

## 🔧 Development Workflow

### First Time Setup
```
1. Install Python 3.10+
2. Create virtual environment: python -m venv venv
3. Activate it: venv\Scripts\activate (Windows)
4. Install dependencies: pip install -r requirements.txt
5. Migrate database: python manage.py migrate
6. Create admin: python manage.py createsuperuser
7. Run server: python manage.py runserver
8. Open http://127.0.0.1:8000/
9. Edit admin at http://127.0.0.1:8000/admin/
```

### Common Development Tasks

**Modify HTML template**
- Edit: `identity/templates/identity/home.html`
- Refresh browser to see changes immediately

**Modify styles**
- Edit: `identity/static/css/style.css`
- Hard refresh: Ctrl+Shift+R to bypass cache

**Modify JavaScript**
- Edit: `identity/static/js/script.js`
- Refresh browser to reload script

**Add new model field**
- Edit: `identity/models.py`
- Create migration: `python manage.py makemigrations`
- Apply migration: `python manage.py migrate`
- Register in admin: `identity/admin.py`

**Edit database content**
- Via Django Admin: http://127.0.0.1:8000/admin/
- Via shell: `python manage.py shell`

**Create backup**
```bash
python manage.py dumpdata > backup.json
python manage.py loaddata backup.json  # To restore
```

---

## 🚀 Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete guides.

### Hosting Options
- **Heroku** (easiest)
- **PythonAnywhere** (beginner-friendly)
- **DigitalOcean** (affordable)
- **AWS** (scalable)
- **Self-hosted** (full control)

### Pre-Production Checklist
- [ ] Change SECRET_KEY
- [ ] Set DEBUG = False
- [ ] Update ALLOWED_HOSTS
- [ ] Configure HTTPS
- [ ] Backup database
- [ ] Collect static files
- [ ] Test admin functionality

---

## 🎨 Customization Guide

See [CUSTOMIZATION.md](CUSTOMIZATION.md) for detailed examples.

### Quick Changes
- **Colors**: Edit `:root` variables in `style.css`
- **Fonts**: Edit `body` font-family in `style.css`
- **Contact links**: Edit template links in `home.html`
- **Typing speed**: Adjust delay in `script.js`
- **Animation speed**: Edit `transition` in `style.css`

### Advanced Changes
- Add new sections to template
- Create new models for additional content
- Integrate third-party services (analytics, email, etc.)
- Create custom admin pages
- Build REST API with Django REST Framework

---

## 🔐 Security Notes

### Development
- `DEBUG = True` (OK for local development)
- Default SQLite database (OK for local testing)

### Production
- Set `DEBUG = False`
- Change `SECRET_KEY` to random value
- Update `ALLOWED_HOSTS` with actual domain
- Switch to PostgreSQL or MySQL
- Enable HTTPS
- Set security headers
- Use environment variables for secrets

See [DEPLOYMENT.md](DEPLOYMENT.md) for security checklist.

---

## 📚 File Organization by Purpose

### Database & Backend
- models.py → Define data structure
- views.py → Prepare data for display
- admin.py → Manage content
- utils.py → Utility functions
- urls.py → Routing

### Frontend
- home.html → Structure
- style.css → Styling
- script.js → Interactivity

### Configuration
- settings.py → Django settings
- requirements.txt → Dependencies
- manage.py → Django CLI

### Documentation
- README.md → Full reference
- SETUP.md → Installation
- QUICKSTART.md → Quick start
- CUSTOMIZATION.md → How to customize
- DEPLOYMENT.md → How to deploy

---

## 🎯 Quick Reference

| Task | File | Command |
|------|------|---------|
| Change colors | style.css | Edit `:root` variables |
| Edit content | admin.py | Go to /admin/ |
| Change template | home.html | Edit HTML sections |
| Add animation | script.js | Add JavaScript |
| Add database field | models.py | Add field, then migrate |
| Deploy to production | settings.py | See DEPLOYMENT.md |
| View site | Any | http://127.0.0.1:8000/ |
| Access admin | Any | http://127.0.0.1:8000/admin/ |

---

## 💬 Getting Help

1. Check relevant documentation file above
2. Search for error message online
3. Check Django documentation: https://docs.djangoproject.com/
4. Review code comments in relevant file

---

## 🎓 Learning Path

1. **Beginner**: Read QUICKSTART.md, SETUP.md
2. **Intermediate**: Customize via admin, modify CSS/colors
3. **Advanced**: Edit models, create new features, deploy

---

**All files are heavily commented with explanations!**

Each major file contains detailed comments explaining:
- What the file does
- How different sections work
- Why certain patterns are used
- Common customization points

---

*Last updated: May 2026*
*Django 4.2+ | Python 3.10+ | Production-Ready*
