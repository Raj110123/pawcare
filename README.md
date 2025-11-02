# pawcare
# 🐾 PawCare - Animal Rescue Management System

<div align="center">

**A comprehensive Django-based web application for managing rescued animals and tracking rescue reports**

[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.38+-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Database Models](#-database-models)
- [URL Configuration](#-url-configuration)
- [Usage](#-usage)
- [Admin Interface](#-admin-interface)
- [Media Files](#-media-files)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**PawCare** is a web application designed to help animal rescue organizations manage their rescued animals efficiently. The system allows users to:

- 📝 View a list of all rescued animals
- 🖼️ Display animal photos and details
- 📊 Track rescue reports with status updates
- 👤 Manage rescue operations through an admin interface
- 📍 Record rescue locations and notes

The application is built using **Django**, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

---

## ✨ Features

### Core Functionality

- ✅ **Animal Management**: Complete CRUD operations for rescued animals
- ✅ **Rescue Reports**: Track rescue operations with status updates (Pending, In Progress, Completed)
- ✅ **Photo Gallery**: Upload and display animal photos
- ✅ **User Management**: Django's built-in authentication system
- ✅ **Admin Dashboard**: Django admin interface for easy data management
- ✅ **Responsive Design**: Mobile-friendly UI with modern styling

### Animal Information

- Animal name, species, breed, and age
- Animal photos with image upload support
- Detailed view pages for each animal
- Associated rescue reports for each animal

### Rescue Report Tracking

- Report status tracking (Pending → In Progress → Completed)
- Location information
- Detailed notes and descriptions
- Reporter assignment
- Timestamp tracking (reported_at)

---

## 🛠️ Tech Stack

### Backend Framework
- **Django 5.2** - High-level Python web framework
  - Built-in admin interface
  - ORM (Object-Relational Mapping)
  - Template engine
  - Authentication system
  - URL routing
  - Middleware support

### Database
- **SQLite3** - Lightweight, file-based database
  - Perfect for development and small-scale deployments
  - No separate database server required
  - Easy to backup and migrate

### Frontend
- **Django Templates** - Django's template language
- **HTML5** - Semantic markup
- **CSS3** - Custom styling with:
  - Responsive design
  - Modern color schemes
  - Hover effects and transitions
  - Card-based layouts

### Python
- **Python 3.8+** - Programming language
- **Django Framework** - Web framework components:
  - `django.contrib.admin` - Admin interface
  - `django.contrib.auth` - Authentication
  - `django.contrib.contenttypes` - Content type framework
  - `django.contrib.sessions` - Session management
  - `django.contrib.messages` - Messaging framework
  - `django.contrib.staticfiles` - Static file handling

### Additional Components
- **Pillow** (Recommended) - Python Imaging Library for image handling
- **Pathlib** - Object-oriented filesystem paths
- **OS Module** - Operating system interface utilities

---

## 📁 Project Structure

```
pawcare-main/
│
├── PawCare/                      # Main project directory
│   ├── paw/                      # Django project settings
│   │   ├── __init__.py          # Package initialization
│   │   ├── settings.py          # Project settings & configuration
│   │   ├── urls.py              # Root URL configuration
│   │   ├── wsgi.py              # WSGI config for deployment
│   │   └── asgi.py              # ASGI config for async support
│   │
│   ├── rescue/                   # Main Django app
│   │   ├── migrations/          # Database migrations
│   │   │   └── 0001_initial.py # Initial database schema
│   │   ├── templates/           # HTML templates
│   │   │   └── rescue/
│   │   │       ├── animal_list.html    # Animal listing page
│   │   │       └── animal_detail.html  # Animal detail page
│   │   ├── __init__.py
│   │   ├── admin.py             # Admin interface configuration
│   │   ├── apps.py              # App configuration
│   │   ├── models.py            # Database models (Animal, RescueReport)
│   │   ├── views.py             # View functions
│   │   ├── urls.py              # App URL routing
│   │   └── tests.py             # Unit tests
│   │
│   ├── media/                    # User-uploaded files
│   │   └── animals/             # Animal photos storage
│   │
│   ├── animals/                  # Temporary/media animal images
│   │
│   ├── manage.py                 # Django management script
│   └── db.sqlite3                # SQLite database file
│
├── README.md                     # Project documentation (this file)
└── db.sqlite3                    # Root level database (if exists)
```

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Virtual Environment** (Recommended) - For isolating project dependencies
- **Git** (Optional) - For version control

### Recommended Python Packages

- `Django >= 5.2` - Web framework
- `Pillow >= 10.0.0` - Image processing library (for image uploads)

---

## 🚀 Installation & Setup

### Step 1: Clone or Download the Repository

```bash
# If using Git
git clone <repository-url>
cd pawcare-main

# Or extract the downloaded ZIP file
```

### Step 2: Navigate to Project Directory

```bash
cd PawCare
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
# Install Django
pip install django

# Install Pillow for image handling (recommended)
pip install pillow

# Or install from requirements file (if created)
pip install -r requirements.txt
```

### Step 5: Run Database Migrations

```bash
# Create database tables
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)

```bash
# Create an admin user to access Django admin panel
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email address
- Password

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

---

## 🗄️ Database Models

### Animal Model

The `Animal` model stores information about rescued animals:

| Field      | Type           | Description                          |
|------------|----------------|--------------------------------------|
| `name`     | CharField(100) | Animal's name                        |
| `species`  | CharField(50)  | Type of animal (dog, cat, etc.)     |
| `breed`    | CharField(50)  | Animal breed (optional)              |
| `age`      | PositiveInteger| Age in years (optional)              |
| `photo`    | ImageField     | Animal photo (stored in `media/animals/`) |
| `id`       | BigAutoField   | Primary key (auto-generated)         |

**Relationship**: One Animal can have multiple RescueReports (One-to-Many)

### RescueReport Model

The `RescueReport` model tracks rescue operations:

| Field          | Type                    | Description                                    |
|----------------|-------------------------|------------------------------------------------|
| `animal`       | ForeignKey(Animal)      | Associated animal                              |
| `reporter`     | ForeignKey(User)        | User who reported the rescue (optional)        |
| `status`       | CharField(50)           | Status: 'pending', 'in_progress', 'completed'  |
| `location`     | CharField(255)          | Location where animal was rescued              |
| `notes`        | TextField               | Additional notes (optional)                    |
| `reported_at`  | DateTimeField           | Auto-generated timestamp                       |
| `id`           | BigAutoField            | Primary key (auto-generated)                   |

**Relationships**:
- Many-to-One with Animal (one animal can have many reports)
- Many-to-One with User (one user can create many reports)

---

## 🔗 URL Configuration

### Root URLs (`paw/urls.py`)

```python
- /admin/              → Django admin interface
- /                    → Redirects to /animals/
- /animals/            → Animal list view (via rescue app)
- /media/              → Media file serving (in development)
```

### Rescue App URLs (`rescue/urls.py`)

```python
- /animals/            → animal_list view (list all animals)
- /animals/<id>/       → animal_detail view (individual animal details)
```

### URL Patterns

| URL Pattern          | View Function    | Description                    |
|----------------------|-----------------|--------------------------------|
| `/`                  | Redirect        | Redirects to `/animals/`       |
| `/admin/`            | Admin Panel     | Django admin interface         |
| `/animals/`          | `animal_list`   | Display all rescued animals    |
| `/animals/<pk>/`     | `animal_detail` | Display animal details & reports |

---

## 💻 Usage

### Accessing the Application

1. **Home/Animal List**: Navigate to `http://127.0.0.1:8000/`
   - Displays all rescued animals in a card-based layout
   - Click on any animal card to view details

2. **Animal Detail Page**: Click on any animal from the list
   - Shows complete animal information
   - Displays all associated rescue reports
   - Shows animal photos if available

3. **Admin Interface**: Navigate to `http://127.0.0.1:8000/admin/`
   - Login with superuser credentials
   - Manage animals and rescue reports
   - Add, edit, or delete records

### Adding Animals via Admin

1. Go to `/admin/`
2. Login with superuser credentials
3. Click on **Animals** under **RESCUE** section
4. Click **Add Animal** button
5. Fill in:
   - Name (required)
   - Species (required)
   - Breed (optional)
   - Age (optional)
   - Photo (optional - upload image)
6. Click **Save**

### Creating Rescue Reports via Admin

1. Go to `/admin/`
2. Click on **Rescue Reports** under **RESCUE** section
3. Click **Add Rescue Report** button
4. Fill in:
   - Animal (select from dropdown)
   - Reporter (select user, optional)
   - Status (Pending/In Progress/Completed)
   - Location (required)
   - Notes (optional)
5. Click **Save**

---

## 🔐 Admin Interface

### Accessing Django Admin

1. Navigate to: `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials created via `createsuperuser`

### Admin Features

- ✅ **Animal Management**: Create, read, update, delete animals
- ✅ **Rescue Report Management**: Manage all rescue reports
- ✅ **User Management**: Manage users and permissions (Django default)
- ✅ **Media File Management**: View and manage uploaded images
- ✅ **Database Browsing**: Browse all database records
- ✅ **Bulk Actions**: Delete multiple records at once

### Registered Models

- `Animal` - Manage animal records
- `RescueReport` - Manage rescue report records

---

## 📸 Media Files

### Media Configuration

- **Media URL**: `/media/`
- **Media Root**: `PawCare/media/`
- **Animal Photos**: Stored in `PawCare/media/animals/`

### File Upload

- Supported image formats: JPG, JPEG, PNG, GIF, WEBP
- Images are automatically resized/processed (if Pillow is installed)
- Files are stored in the `media/animals/` directory

### Serving Media Files in Development

Media files are automatically served in development mode when `DEBUG = True` in `settings.py`:

```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Note**: For production, configure your web server (nginx, Apache) to serve media files directly.

---

## 🧪 Development

### Running Migrations

```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

### Creating a New App

```bash
python manage.py startapp <app_name>
```

### Collecting Static Files

```bash
# Collect static files for deployment
python manage.py collectstatic
```

### Django Shell

```bash
# Access Django shell for database queries
python manage.py shell
```

Example:
```python
from rescue.models import Animal, RescueReport

# Get all animals
animals = Animal.objects.all()

# Get animals by species
dogs = Animal.objects.filter(species='Dog')

# Get rescue reports for an animal
animal = Animal.objects.get(id=1)
reports = animal.reports.all()
```

---

## 🎨 Frontend Styling

### Color Scheme

- **Primary Color**: SteelBlue (#4682b4)
- **Accent Color**: Tomato (#ff6347)
- **Background**: Light Blue (#f0f8ff)
- **Card Background**: White (#fff)

### Responsive Design

- Desktop: Multi-column card layout
- Tablet: Adjusted card width
- Mobile: Single column layout (max-width: 768px)

### UI Features

- Card-based animal listings
- Hover effects on images and links
- Smooth transitions and animations
- Clean, modern interface
- Accessible navigation

---

## 📝 Code Structure

### Views (`rescue/views.py`)

- **`animal_list(request)`**: Displays all animals in a list view
- **`animal_detail(request, pk)`**: Shows individual animal details with rescue reports

### Models (`rescue/models.py`)

- **`Animal`**: Database model for rescued animals
- **`RescueReport`**: Database model for rescue operation reports

### Templates

- **`animal_list.html`**: Main listing page with animal cards
- **`animal_detail.html`**: Detailed view for individual animals

---

## 🔧 Configuration

### Settings Overview (`paw/settings.py`)

Key configurations:

- **`DEBUG = True`**: Development mode (set to `False` for production)
- **`SECRET_KEY`**: Django secret key (change in production)
- **`ALLOWED_HOSTS`**: List of allowed hostnames (configure for production)
- **`INSTALLED_APPS`**: Registered Django applications
- **`DATABASES`**: Database configuration (SQLite3 by default)
- **`MEDIA_URL`**: URL prefix for media files
- **`MEDIA_ROOT`**: Filesystem path for media files

### Security Notes

⚠️ **For Production Deployment:**

1. Set `DEBUG = False`
2. Generate a new `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL, MySQL)
5. Set up proper media file serving
6. Use HTTPS
7. Configure proper security middleware

---

## 🚀 Deployment

### Recommended Platforms

- **Heroku**: Easy Django deployment
- **PythonAnywhere**: Free Python hosting
- **DigitalOcean**: VPS hosting
- **AWS**: Scalable cloud hosting
- **Railway**: Modern deployment platform

### Deployment Checklist

- [ ] Set `DEBUG = False`
- [ ] Generate new `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up production database
- [ ] Configure static file serving
- [ ] Configure media file serving
- [ ] Set up SSL/HTTPS
- [ ] Configure environment variables
- [ ] Run migrations on production
- [ ] Create production superuser

---

## 🐛 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'django'"**
   - Solution: Install Django: `pip install django`

2. **"OperationalError: no such table"**
   - Solution: Run migrations: `python manage.py migrate`

3. **"Images not displaying"**
   - Solution: Check `MEDIA_URL` and `MEDIA_ROOT` settings
   - Ensure media files are being served in development

4. **"Permission denied" on media uploads**
   - Solution: Check file permissions on `media/` directory

5. **"Invalid SECRET_KEY"**
   - Solution: Generate new key or check settings file

---

## 📚 Additional Resources

### Django Documentation

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/5.2/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)

### Learning Resources

- [Django for Beginners](https://djangoforbeginners.com/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 Python style guide
- Write clear commit messages
- Add comments for complex code
- Test your changes thoroughly
- Update documentation as needed

---

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👥 Authors

- **Project Maintainer** - Initial work

---

## 🙏 Acknowledgments

- Django framework community
- Animal rescue organizations worldwide
- Open source contributors

---

## 📞 Support

For support, questions, or suggestions:

- Open an issue on GitHub
- Contact the project maintainer

---

<div align="center">

**Made with ❤️ for Animal Rescue Organizations**

*Last Updated: 2025*

</div>
