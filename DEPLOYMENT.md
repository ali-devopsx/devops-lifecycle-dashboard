# DEPLOYMENT GUIDE - Digital Identity Portfolio

This guide covers deploying the portfolio to production servers.

## Pre-Deployment Checklist

Before deploying, ensure:
- [ ] All default data is loaded (`python manage.py migrate`)
- [ ] Admin account is created (`python manage.py createsuperuser`)
- [ ] Static files are collected (`python manage.py collectstatic`)
- [ ] `DEBUG = False` in settings.py (for production)
- [ ] `SECRET_KEY` is unique and secret
- [ ] `ALLOWED_HOSTS` is set correctly
- [ ] Database is backed up
- [ ] HTTPS certificate obtained (if using HTTPS)

---

## Production Settings

Update `cyber_portfolio/settings.py` for production:

```python
# SECURITY SETTINGS - CHANGE THESE FOR PRODUCTION
DEBUG = False  # CRITICAL: Set to False in production

# Use strong, random secret key (generate via: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
SECRET_KEY = 'your-very-long-random-secret-key-here'

# Add your domain(s)
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your-ip-address']

# ===== SECURITY FEATURES =====
# Only set these if using HTTPS
SECURE_SSL_REDIRECT = True                  # Redirect HTTP to HTTPS
SESSION_COOKIE_SECURE = True                # Only send cookies over HTTPS
CSRF_COOKIE_SECURE = True                   # Only send CSRF token over HTTPS
SECURE_HSTS_SECONDS = 31536000             # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True      # Include subdomains
SECURE_HSTS_PRELOAD = True                 # Add to HSTS preload list

# Content Security Policy (prevents XSS attacks)
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
    'script-src': ("'self'", 'cdnjs.cloudflare.com'),
    'style-src': ("'self'", 'cdnjs.cloudflare.com'),
    'img-src': ("'self'", 'data:', 'https:'),
    'font-src': ("'self'", 'cdnjs.cloudflare.com'),
}

# Additional security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_SECURITY_POLICY_REPORT_ONLY = False
```

---

## Hosting Platforms

### Option 1: Heroku (Easy, Free tier available)

**Prerequisites**: Heroku account, Git installed

**Steps**:
1. **Create Procfile** in project root:
```
web: gunicorn cyber_portfolio.wsgi
```

2. **Update requirements.txt**:
```bash
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

3. **Update settings.py** for Heroku:
```python
import os
from decouple import config

# Allow HTTPS redirect
SECURE_SSL_REDIRECT = True
SECURE_PROXY_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Use PostgreSQL on Heroku
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# WhiteNoise for static files
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... rest of middleware
]

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

4. **Create runtime.txt**:
```
python-3.10.13
```

5. **Deploy**:
```bash
heroku login
heroku create your-app-name
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Option 2: PythonAnywhere (Beginner-friendly)

**Steps**:
1. Create account at https://www.pythonanywhere.com/
2. Upload code via Web interface
3. Set up virtual environment:
   - Go to Web > Add a new web app
   - Choose Python 3.10
   - Choose Django
4. Edit configuration files as needed
5. Reload app

### Option 3: DigitalOcean (Affordable)

**Requirements**: DigitalOcean account, SSH knowledge

**Basic setup**:
1. Create Ubuntu 22.04 Droplet
2. SSH into droplet
3. Install Python, pip, virtualenv:
```bash
sudo apt update
sudo apt install python3-pip python3-venv git
```

4. Clone repository:
```bash
git clone https://github.com/yourusername/cyber_portfolio.git
cd cyber_portfolio
```

5. Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Run migrations:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

7. Install and configure Gunicorn + Nginx (advanced, see below)

### Option 4: AWS (Scalable, Complex)

**Services**: EC2, RDS, S3, CloudFront

**Recommended**: Use AWS Elastic Beanstalk for simplified deployment

```bash
pip install awsebcli
eb init -p python-3.10 cyber_portfolio
eb create cyber-portfolio-env
eb deploy
```

---

## Using Gunicorn + Nginx (Manual Setup)

### Install Gunicorn
```bash
pip install gunicorn
```

### Create Gunicorn Service File
Create `/etc/systemd/system/gunicorn.service`:
```
[Unit]
Description=gunicorn daemon for cyber_portfolio
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/cyber_portfolio
ExecStart=/path/to/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/path/to/cyber_portfolio/gunicorn.sock \
    cyber_portfolio.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Start Service
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### Configure Nginx
Create `/etc/nginx/sites-available/cyber_portfolio`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /path/to/cyber_portfolio/staticfiles/;
    }
    
    location /media/ {
        alias /path/to/cyber_portfolio/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/cyber_portfolio/gunicorn.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/cyber_portfolio /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## SSL/HTTPS Setup

### Using Let's Encrypt (Free)

1. **Install Certbot**:
```bash
sudo apt install certbot python3-certbot-nginx
```

2. **Obtain Certificate**:
```bash
sudo certbot certonly --nginx -d yourdomain.com -d www.yourdomain.com
```

3. **Update Nginx**:
```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # ... rest of config
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}
```

4. **Enable Auto-renewal**:
```bash
sudo systemctl enable certbot.timer
```

---

## Database Migration to Production

### PostgreSQL Setup (Recommended for production)

1. **Install PostgreSQL** (DigitalOcean/Ubuntu):
```bash
sudo apt install postgresql postgresql-contrib
```

2. **Create Database**:
```bash
sudo -u postgres createdb cyber_portfolio
sudo -u postgres createuser your_db_user
sudo -u postgres psql -c "ALTER USER your_db_user WITH PASSWORD 'secure_password';"
```

3. **Update Django Settings**:
```bash
pip install psycopg2-binary
```

Edit `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cyber_portfolio',
        'USER': 'your_db_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. **Run Migrations**:
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## Media Storage (Cloud)

### Using AWS S3

1. **Install boto3**:
```bash
pip install boto3 django-storages
```

2. **Update settings.py**:
```python
if USE_S3:
    # S3 Configuration
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_LOCATION = 'static'
    
    # Static and Media Files
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
```

3. **Upload files**:
```bash
python manage.py collectstatic
```

---

## Monitoring & Maintenance

### Check Application Status
```bash
sudo systemctl status gunicorn
sudo systemctl status nginx
```

### View Logs
```bash
# Django logs
sudo journalctl -u gunicorn -f

# Nginx error logs
sudo tail -f /var/log/nginx/error.log
```

### Update Application
```bash
cd cyber_portfolio
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

### Backup Database
```bash
python manage.py dumpdata > backup.json

# Or for PostgreSQL
pg_dump cyber_portfolio > backup.sql
```

### Restore Database
```bash
python manage.py loaddata backup.json

# Or for PostgreSQL
psql cyber_portfolio < backup.sql
```

---

## Email Configuration (Optional)

### Gmail SMTP
```python
# In settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use app password, not Gmail password
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### SendGrid
```python
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = 'your-sendgrid-api-key'
```

---

## Performance Optimization

### Enable Caching
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### CDN Configuration
- Upload static files to CDN (CloudFront, CloudFlare)
- Update `STATIC_URL` to CDN URL
- Serve images from CDN

### Database Optimization
```bash
# Create indexes
python manage.py sqlsequencereset identity | python manage.py dbshell

# Vacuum database
VACUUM ANALYZE;  # PostgreSQL
OPTIMIZE TABLE;  # MySQL
```

---

## Security Checklist

- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS configured
- [ ] SECRET_KEY is unique and secret
- [ ] HTTPS enabled with valid certificate
- [ ] SECURE_SSL_REDIRECT = True
- [ ] SESSION_COOKIE_SECURE = True
- [ ] CSRF_COOKIE_SECURE = True
- [ ] Database password is strong
- [ ] Admin interface protected (not at /admin/)
- [ ] Regular backups scheduled
- [ ] Error emails configured
- [ ] Security headers set
- [ ] CORS properly configured
- [ ] Rate limiting enabled (if needed)

---

## Troubleshooting Deployment

### Static files not loading
```bash
python manage.py collectstatic
# Restart web server
```

### 500 error
- Check error logs: `sudo tail -f /var/log/nginx/error.log`
- Verify database connection
- Check SECRET_KEY and DEBUG settings

### Database connection errors
- Verify database is running
- Check credentials in settings.py
- Ensure firewall allows database port

### Email not sending
- Verify SMTP credentials
- Check if app is blocked by Gmail
- Review error logs

---

## Getting Help

- Django Deployment Docs: https://docs.djangoproject.com/en/stable/howto/deployment/
- Gunicorn: https://gunicorn.org/
- Nginx: https://nginx.org/
- Let's Encrypt: https://letsencrypt.org/

---

**Last Updated**: May 2026
