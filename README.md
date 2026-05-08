# Digital Identity Portfolio - Ali Mahmoud

A production-ready Django-based digital identity portfolio for a cybersecurity/DevOps engineer. Features a dark cyberpunk theme with glow effects, typing animations, and scroll-triggered fade-in/fade-out effects.

## Project Overview

This portfolio website showcases:
- **Dark Theme**: Deep background (#0a0a0a) with cyan (#00ffff) and magenta (#ff00ff) glow effects
- **Typing Effect**: Animated name appearance character-by-character
- **Scroll Animations**: Sections fade in when scrolling down, fade out when scrolling up (Intersection Observer)
- **Glass Morphism**: Frosted glass effect on cards with blur filters
- **Fully Database-Driven**: All content (profile, skills, projects, timeline) stored in database, editable via Django admin
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (default, easily switched to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3 (with modern features), Vanilla JavaScript
- **Icons**: FontAwesome 6.4+
- **Python**: 3.10+

## Project Structure

```
cyber_portfolio/
├── manage.py                      # Django management command
├── requirements.txt               # Python dependencies
├── db.sqlite3                     # Database (created after migrations)
├── cyber_portfolio/               # Django project folder
│   ├── __init__.py
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # Root URL routing
│   ├── wsgi.py                   # Production WSGI entry point
│   └── asgi.py                   # Async entry point
├── identity/                      # Main Django app
│   ├── migrations/               # Database migrations
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css         # Main stylesheet with dark theme
│   │   └── js/
│   │       └── script.js         # JavaScript for animations and effects
│   ├── templates/identity/
│   │   └── home.html             # Main portfolio page template
│   ├── __init__.py
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration (populates default data)
│   ├── models.py                 # Database models (Profile, Skill, Project, TimelineEvent)
│   ├── urls.py                   # App URL routing
│   ├── utils.py                  # Utility functions (populate_default_data)
│   └── views.py                  # View functions/classes
└── media/
    └── projects/                 # Uploaded project images folder
```

## Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 2. Clone or Download the Project
```bash
cd cyber_portfolio
```

### 3. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
This creates the database tables and applies Django's built-in migrations:
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Account)
Create an admin account to access the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### 7. Populate Default Data (Automatic)
The default data is automatically populated when you first run the server (via `apps.py` ready method).

### 8. Run Development Server
```bash
python manage.py runserver
```

The site will be available at: **http://127.0.0.1:8000/**

Admin panel: **http://127.0.0.1:8000/admin/**

## Default Data

The following data is automatically inserted into the database:

### Profile
- **Name**: Ali Mahmoud
- **Title**: Penetration Tester & Automation Engineer
- **Bio**: "I break systems to protect them.. and build defense lines with code."

### Skills (10 total)
1. IT Infrastructure
2. Linux (Kali, Ubuntu, RHEL)
3. Networking (TCP/IP, Firewalls, Wireshark)
4. DevOps
5. Git & GitFlow
6. GitHub Actions
7. Docker & Podman
8. Kubernetes (k8s)
9. Python / Bash
10. SIEM (Splunk, ELK)

### Projects (3 total)
1. **Threat-Hunter ELK Stack** - Open-source threat analysis platform with real-time dashboards
2. **CI/CD Security Pipeline** - GitHub Actions pipeline with vulnerability scanning
3. **Red Team Automation Tool** - Network penetration testing automation tool

### Timeline Events (4 total)
- 2018: Beginning of Passion
- 2020: Certified Ethical Hacker (CEH)
- 2022: Merging Security with DevOps
- 2024: Automating Attacks & Defense

## Editing Content via Django Admin

All portfolio content can be edited through Django Admin without touching code:

1. Go to: **http://127.0.0.1:8000/admin/**
2. Log in with your superuser credentials
3. Edit:
   - **Profile**: Single record with name, title, bio, contact phrase
   - **Skills**: Add/edit/delete skills with custom FontAwesome icons
   - **Projects**: Add/edit/delete projects with descriptions, tech stacks, images, and links
   - **Timeline Events**: Add/edit/delete career milestones

### Changing Icon Classes
FontAwesome icons are stored in the `icon_class` field. Reference: https://fontawesome.com/search

Examples:
- `fa-python` → Python icon
- `fa-docker` → Docker icon
- `fa-github` → GitHub icon
- `fa-linux` → Linux icon

## Features & Styling

### Dark Theme
- Background: `#0a0a0a` (deep black)
- Text: `#e0e0e0` (light gray)
- Accents: Cyan (#00ffff) and Magenta (#ff00ff)

### Glow Effects
- Cyan glow on headings and primary accents
- Magenta glow on secondary elements and hover states
- Layered text-shadow effects for depth

### Glass Morphism
- Cards use `backdrop-filter: blur(12px)`
- Semi-transparent background with subtle borders
- Creates a floating, futuristic appearance

### Animations
1. **Typing Effect**: Name appears character-by-character on page load
2. **Scroll Fade-In/Fade-Out**: Sections fade in when entering viewport, fade out when leaving
3. **Hover Effects**: Cards scale, glow, and transform on mouse over

## API Reference

### Views
- **home()**: Main portfolio page, retrieves all data from database and renders

### Models
- **Profile**: Single-record model for portfolio owner information
- **Skill**: Model for technologies/skills with icon classes and display order
- **Project**: Model for portfolio projects with descriptions and tech stacks
- **TimelineEvent**: Model for career timeline milestones

### Utility Functions
- **populate_default_data()**: Populates database with default values (called on app startup)

## Customization

### Change Colors
Edit CSS root variables in `identity/static/css/style.css`:
```css
:root {
    --bg-primary: #0a0a0a;
    --cyan: #00ffff;
    --magenta: #ff00ff;
    /* ... */
}
```

### Adjust Animations
- **Typing speed**: Modify delay in `identity/static/js/script.js` `typeCharacter()` function
- **Scroll fade animation**: Edit `--transition` in CSS or `threshold` in JavaScript Intersection Observer

### Change Database
To use PostgreSQL or MySQL instead of SQLite:

1. Update `settings.py` DATABASES configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'mysql'
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

2. Install driver: `pip install psycopg2` (PostgreSQL) or `pip install mysqlclient` (MySQL)
3. Run migrations again

## Production Deployment

### Important Security Changes
Before deploying to production, update `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'your-very-secret-key-change-this'

# Enable security features
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Recommended Hosting
- **Backend**: Heroku, PythonAnywhere, AWS, DigitalOcean
- **Static/Media**: AWS S3, Cloudinary, or local storage with Nginx
- **Database**: PostgreSQL on managed service or dedicated server

### WSGI Server (Production)
```bash
# Using Gunicorn
gunicorn cyber_portfolio.wsgi:application --bind 0.0.0.0:8000
```

## Troubleshooting

### Database errors during first run
**Solution**: Ensure migrations are applied:
```bash
python manage.py migrate
```

### Static files not loading
**Solution**: Collect static files and ensure STATIC_URL is configured:
```bash
python manage.py collectstatic
```

### Admin panel not accessible
**Solution**: Create superuser:
```bash
python manage.py createsuperuser
```

### Port 8000 already in use
**Solution**: Use different port:
```bash
python manage.py runserver 8001
```

## File Descriptions

| File | Purpose |
|------|---------|
| `models.py` | Database models for Profile, Skills, Projects, Timeline |
| `views.py` | Views that retrieve data and render templates |
| `admin.py` | Django admin configuration for editing content |
| `urls.py` | URL routing configuration |
| `apps.py` | App configuration and default data population |
| `utils.py` | Utility functions including populate_default_data |
| `style.css` | Complete styling with dark theme and effects |
| `script.js` | JavaScript for typing effect and scroll animations |
| `home.html` | Main template rendering all sections |
| `settings.py` | Django project configuration |

## Contributing

This is a personal portfolio project. To customize:
1. Edit content via Django admin
2. Modify styling in `style.css`
3. Update JavaScript in `script.js`
4. Add new models/views as needed

## License

This project is open for personal use and modification.

## Contact

- **Email**: ali@example.com (customize in contact links)
- **GitHub**: [Update in template](identity/templates/identity/home.html#L164)
- **LinkedIn**: [Update in template](identity/templates/identity/home.html#L170)

---

**Built with Django 4.2+ | Dark Theme with Cyberpunk Aesthetics | Fully Customizable**
