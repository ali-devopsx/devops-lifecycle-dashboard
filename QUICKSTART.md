# QUICK START - Digital Identity Portfolio

Get your portfolio running in 5 minutes!

## 🚀 Quick Setup

```bash
# 1. Navigate to project
cd cyber_portfolio

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Setup database
python manage.py migrate

# 6. Create admin account
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

## 🌐 Access Your Portfolio

- **Portfolio**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

**Default Data**: Automatically loaded on first run!

---

## 📝 What's Included

### ✅ Features
- Dark cyberpunk theme with cyan/magenta glow effects
- Typing animation for name
- Scroll-triggered fade-in/fade-out effects
- Glass morphism card effects
- Fully responsive (mobile, tablet, desktop)
- Completely database-driven (editable via admin)
- 10 pre-loaded skills
- 3 sample projects
- 4 career timeline events
- Contact section

### 📁 Key Files
```
cyber_portfolio/
├── identity/
│   ├── models.py          # Profile, Skill, Project, TimelineEvent
│   ├── views.py           # View logic
│   ├── admin.py           # Django admin configuration
│   ├── static/
│   │   ├── css/style.css      # Dark theme with effects (1000+ lines)
│   │   └── js/script.js       # Animations & typing effect
│   └── templates/
│       └── home.html          # Main template
├── settings.py            # Django configuration
├── requirements.txt       # Python dependencies
├── README.md             # Full documentation
├── SETUP.md              # Detailed setup guide
├── CUSTOMIZATION.md      # How to customize
└── DEPLOYMENT.md         # How to deploy
```

---

## ✏️ Edit Content

### Via Django Admin (Easiest)
1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Edit:
   - **Profile**: Name, title, bio
   - **Skills**: Add/edit technologies with icons
   - **Projects**: Add/edit projects with descriptions
   - **Timeline Events**: Add/edit career milestones

### Edit Contact Links
In `identity/templates/identity/home.html`, search for "contact-links" section and update:
```html
<!-- Change email -->
<a href="mailto:your-email@example.com">

<!-- Change GitHub/LinkedIn/Twitter -->
<a href="https://github.com/your-username">
```

### Change Colors
Edit `identity/static/css/style.css` root variables:
```css
:root {
    --cyan: #00ffff;        /* Change to your color */
    --magenta: #ff00ff;     /* Change to your color */
}
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **README.md** | Complete overview and reference |
| **SETUP.md** | Detailed installation guide |
| **CUSTOMIZATION.md** | How to customize every aspect |
| **DEPLOYMENT.md** | How to deploy to production |

---

## 🎨 Customization Examples

### Change Typing Speed
In `identity/static/js/script.js`:
```javascript
// Faster: 30-80ms per character
const delay = Math.random() * 50 + 30;

// Slower: 200-300ms per character
const delay = Math.random() * 250 + 200;
```

### Change Animation Duration
In `identity/static/css/style.css`:
```css
.fade-in {
    transition: opacity 0.8s ease, transform 0.8s ease;
    /* Change 0.8s to make faster/slower */
}
```

### Add New Skill
1. Go to Admin > Skills
2. Click "Add Skill"
3. Enter name (e.g., "Kubernetes")
4. Find icon at https://fontawesome.com/ (e.g., "fa-cloud")
5. Save

---

## 🔒 Important Notes

### Before Going Live
1. Change `SECRET_KEY` in settings.py to something random
2. Set `DEBUG = False` in settings.py
3. Update `ALLOWED_HOSTS` with your domain
4. Enable HTTPS
5. Use PostgreSQL instead of SQLite

See **DEPLOYMENT.md** for full production checklist.

---

## ⚠️ Troubleshooting

### Database Error on First Run
```bash
python manage.py migrate
```

### Admin Panel Shows "Page Not Found"
```bash
python manage.py createsuperuser
```

### CSS/JS Not Loading
```bash
# Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
# Or collect static files:
python manage.py collectstatic
```

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
```

---

## 📦 Tech Stack

- **Framework**: Django 4.2+
- **Database**: SQLite (default) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Icons**: FontAwesome 6.4+
- **Python**: 3.10+

---

## 🎯 Next Steps

1. **View the site**: http://127.0.0.1:8000/
2. **Edit admin**: http://127.0.0.1:8000/admin/
3. **Customize colors**: Edit `static/css/style.css`
4. **Update contact**: Edit email/social links in `home.html`
5. **Deploy**: Follow DEPLOYMENT.md for hosting options

---

## 💡 Tips

- Keep admin URL private in production
- Regularly backup your database
- Test changes on mobile too (responsive design)
- Use strong passwords in production
- Enable HTTPS when deploying

---

## 📞 Common Commands

```bash
# Start server
python manage.py runserver

# Access admin shell
python manage.py shell

# Create backup
python manage.py dumpdata > backup.json

# Restore backup
python manage.py loaddata backup.json

# Check for errors
python manage.py check

# Collect static files (production)
python manage.py collectstatic
```

---

## ⭐ Key Features At a Glance

| Feature | Location |
|---------|----------|
| Typing Effect | `static/js/script.js` line 24-50 |
| Scroll Animation | `static/js/script.js` line 53-87 |
| Dark Theme | `static/css/style.css` line 1-20 |
| Models & Data | `models.py` & `utils.py` |
| Admin Interface | `admin.py` |
| Contact Links | `templates/home.html` line 160+ |

---

## 🎓 Learning Resources

- Django Docs: https://docs.djangoproject.com/
- CSS Grid: https://css-tricks.com/snippets/css/complete-guide-grid/
- JavaScript ES6: https://es6.io/
- FontAwesome Icons: https://fontawesome.com/icons

---

**🎉 You're all set! Start editing and have fun!**

For detailed guides, see README.md, SETUP.md, CUSTOMIZATION.md, or DEPLOYMENT.md
