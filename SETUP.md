# SETUP GUIDE - Digital Identity Portfolio

This guide will walk you through setting up the portfolio website from scratch.

## Quick Start (5 Minutes)

### Step 1: Install Python Dependencies
```bash
# Navigate to the project directory
cd cyber_portfolio

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Setup Database
```bash
# Apply migrations (creates database tables)
python manage.py migrate

# Create admin account
python manage.py createsuperuser
# Follow prompts: choose username, email, password
```

### Step 3: Run Server
```bash
python manage.py runserver
```

### Step 4: Access the Site
- **Portfolio**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

That's it! Default data is automatically populated on first run.

---

## Detailed Setup

### Prerequisites Check
```bash
# Check Python version (should be 3.10+)
python --version

# Check pip is installed
pip --version
```

### Virtual Environment (Recommended)

Why use virtual environment? It isolates project dependencies and prevents conflicts.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Deactivate when done:**
```bash
deactivate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **Django 4.2.11**: Web framework
- **Pillow 10.2.0**: Image processing for uploaded images
- **python-decouple**: Environment variable management
- **gunicorn**: Production server (optional)
- **whitenoise**: Static file serving (optional)

### Database Setup

#### Create Database
```bash
python manage.py migrate
```

This creates `db.sqlite3` with all necessary tables:
- auth_user
- identity_profile
- identity_skill
- identity_project
- identity_timelineevent

#### Create Admin User
```bash
python manage.py createsuperuser
```

Example:
```
Username: admin
Email: admin@example.com
Password: (your secure password)
Password (again): (repeat)
```

### Default Data Insertion

Data is automatically created when you first run the server. The `apps.py` file contains logic that:
1. Checks if default data exists
2. Creates Profile, Skills, Projects, and Timeline events if not present
3. Uses `get_or_create` to prevent duplicates

Manual trigger (if needed):
```bash
python manage.py shell
>>> from identity.utils import populate_default_data
>>> populate_default_data()
>>> exit()
```

### Run Development Server

```bash
python manage.py runserver
```

Output should show:
```
Starting development server at http://127.0.0.1:8000/
```

**To stop**: Press `Ctrl+C`

**To run on different port**:
```bash
python manage.py runserver 8001
```

---

## Accessing Django Admin

1. Navigate to: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. You can now:
   - Edit Profile (name, title, bio)
   - Add/edit/delete Skills
   - Add/edit/delete Projects (including images)
   - Add/edit/delete Timeline Events
   - Manage users

### Admin Tips
- **Inline editing**: Double-click order numbers to edit directly in the list
- **Search**: Use search boxes to find skills or projects quickly
- **Ordering**: Change display order using the order field
- **Images**: Click "Choose File" to upload project screenshots

---

## File Structure After Setup

```
cyber_portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── SETUP.md (this file)
├── .gitignore
├── .env.example
├── db.sqlite3 (created after migrate)
├── staticfiles/ (created after collectstatic)
├── media/
│   └── projects/ (uploaded images go here)
├── cyber_portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── identity/
    ├── migrations/
    ├── static/
    │   ├── css/style.css
    │   └── js/script.js
    ├── templates/identity/
    │   └── home.html
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── apps.py
    └── utils.py
```

---

## Common Commands

### Django Management
```bash
# Start development server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create new migration from model changes
python manage.py makemigrations

# Access interactive shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic

# Create superuser
python manage.py createsuperuser

# Show all available commands
python manage.py help
```

### Managing Data
```bash
# Access Django shell
python manage.py shell

# Import models
from identity.models import Profile, Skill, Project, TimelineEvent

# View all profiles
Profile.objects.all()

# Get single profile
profile = Profile.objects.first()
print(profile.name)

# Create new skill (if needed)
Skill.objects.create(
    name="Rust",
    icon_class="fa-crate",
    order=11
)

# Update skill
skill = Skill.objects.get(name="Python / Bash")
skill.order = 15
skill.save()

# Delete skill
skill = Skill.objects.get(name="Some Skill")
skill.delete()

# Exit shell
exit()
```

---

## Editing Portfolio Content

### Via Django Admin (Recommended)
1. Go to http://127.0.0.1:8000/admin/
2. Click on any model (Profile, Skill, Project, TimelineEvent)
3. Edit fields and click Save

### Via Management Shell
```bash
python manage.py shell

from identity.models import Profile

# Update profile
profile = Profile.objects.first()
profile.bio_strong = "New bio text here"
profile.save()

exit()
```

### Via Code (models.py)
Edit default values in `identity/utils.py` `populate_default_data()` function, then:
```bash
# Delete current data (optional)
python manage.py shell
>>> from identity.models import Profile, Skill, Project, TimelineEvent
>>> Profile.objects.all().delete()
>>> Skill.objects.all().delete()
>>> Project.objects.all().delete()
>>> TimelineEvent.objects.all().delete()
>>> exit()

# Run populate again
python manage.py runserver
```

---

## Static Files

### Development
During development (`DEBUG=True`), Django automatically serves static files from:
- `identity/static/css/style.css`
- `identity/static/js/script.js`

### Production
Before deploying, collect all static files:
```bash
python manage.py collectstatic
```

This copies static files to `staticfiles/` directory. Serve this directory with Nginx or Apache.

---

## Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

To use environment variables, install `python-decouple`:
```bash
pip install python-decouple
```

Then update `settings.py`:
```python
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='your-default-key')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=lambda v: [s.strip() for s in v.split(',')])
```

**Never commit `.env` file to version control!**

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution**: Virtual environment not activated or dependencies not installed
```bash
# Activate venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install requirements
pip install -r requirements.txt
```

### Issue: "RuntimeError: database is locked"
**Solution**: Close other connections to database
```bash
# Restart Django server
# Or restart your IDE/terminal
```

### Issue: Database errors on first run
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: Admin panel shows "page not found"
**Solution**: Ensure superuser is created and you're logged in
```bash
python manage.py createsuperuser
```

### Issue: Static files not loading (CSS/JS broken)
**Solution**: Collect static files
```bash
python manage.py collectstatic
```

### Issue: Port 8000 already in use
**Solution**: Use different port
```bash
python manage.py runserver 8001
```

### Issue: Can't upload project images
**Solution**: Ensure media directory exists and has write permissions
```bash
# Create media/projects directory if it doesn't exist
mkdir media
mkdir media/projects
```

---

## Next Steps

1. **Customize Profile**: Go to admin, edit Profile name, title, bio
2. **Add Your Skills**: Create skills with your actual expertise
3. **Add Your Projects**: Upload project descriptions and images
4. **Update Contact Links**: Modify email/GitHub/LinkedIn URLs in template
5. **Deploy**: See DEPLOYMENT.md for hosting options

---

## Getting Help

### Official Documentation
- Django: https://docs.djangoproject.com/
- FontAwesome Icons: https://fontawesome.com/icons
- Django Admin: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

### Common Issues
- Check Python/Django versions match requirements.txt
- Ensure database migrations are applied
- Verify static files are collected for production

---

**Last Updated**: May 2026
**Django Version**: 4.2+
**Python Version**: 3.10+
