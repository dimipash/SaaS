# SaaS Django Project 🚀

A foundational Software as a Service (SaaS) solution built with Django, featuring user authentication, subscription management, and custom commands.

## 🌟 Features

### Core Functionality

-   User Authentication (django-allauth)
-   GitHub Login Integration
-   Profile Management
-   Visit Tracking
-   Custom Management Commands

### Payment & Subscriptions

-   Stripe Integration
-   Subscription Management
-   Reoccurring Payments via Products/Prices API
-   Dynamic Pricing Page
-   User Subscription Dashboard

### Infrastructure

-   Email Integration with Gmail
-   Railway Deployment Support
-   Neon PostgreSQL Integration
-   Django Groups and Permissions
-   Python Decouple for Environment Management
-   Whitenoise for Static File Serving

### CI/CD & Automation

-   GitHub Actions Workflows for Production Sync
-   Neon Database Branching for Testing
-   Automated Subscription Status Management
-   Vendor Asset Management (Tailwind/Flowbite)

## 🛠️ Tech Stack

-   **Backend:** Django 5.0, Python 3.12
-   **Database:** PostgreSQL (Neon)
-   **Payment Processing:** Stripe
-   **Containerization:** Docker
-   **Deployment:** Railway
-   **Static Files:** Whitenoise
-   **Frontend Styling:** Tailwind CSS, Flowbite

## 🚀 Getting Started

### Prerequisites

-   Python 3.12+
-   Docker (optional)
-   PostgreSQL
-   Stripe Account

### Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/dimipash/SaaS.git
    cd src
    ```

2.  **Set Up Virtual Environment**

    ```bash
    python -m venv venv
    # On Unix/macOS
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory:

    ```env
    BASE_URL=your_base_url_here
    DJANGO_SECRET_KEY=your_django_secret_key_here
    DJANGO_DEBUG=True
    DATABASE_URL=your_database_url_here
    EMAIL_HOST=your_email_host_here
    EMAIL_PORT=your_email_port_here
    EMAIL_USE_TLS=True
    EMAIL_USE_SSL=False
    EMAIL_HOST_USER=your_email_here
    EMAIL_HOST_PASSWORD=your_email_password_here
    STRIPE_SECRET_KEY=your_stripe_secret_key_here
    ADMIN_USER_EMAIL=your_admin_email_here
    ```

5.  **Database Setup**

    ```bash
    python src/manage.py migrate
    python src/manage.py createsuperuser
    ```

6.  **Start Development Server**
    ```bash
    python src/manage.py runserver
    ```

## 🛠️ Custom Management Commands

Located in `src/commando/management/commands/`:

-   `hello_world.py` - Test command
-   `vendor_pull.py` - Vendor data management
-   `sync_user_subs.py` - Subscription sync

Usage:

```bash
python src/manage.py <command_name>
```

### Subscription Sync Options

```bash
python src/manage.py sync_user_subs [options]

Options:
  --day-start     Start day for sync range
  --day-end       End day for sync range
  --days-left     Subscription days remaining
  --days-ago      Days ago to start sync
  --clear-dangling Clear invalid subscriptions
```

## 📁 Project Structure

```
src/
├── subscriptions/  # Subscription management
├── customers/      # Customer data
├── profiles/       # User profiles
├── visits/         # Visit tracking
└── commando/       # Custom commands
```

## 🧪 Testing

This project includes a comprehensive suite of tests to ensure the functionality and reliability of the application. The tests are organized by feature and can be found in the respective directories within the `src` folder.

### Running Tests

The project uses Pytest for running tests. To execute the tests, ensure you have all dependencies installed and run the following command:

```bash
pytest
```

### Continuous Integration

The project uses GitHub Actions for continuous integration, ensuring that all tests are run automatically on each push to the repository. The workflows are defined in the `.github/workflows` directory.

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

1. **Production Database Sync**

    - Automated Stripe subscription status sync
    - Scheduled execution
    - Replaces Celery beat server

2. **Testing Pipeline**
    - Neon database branching
    - Isolated test environment
    - Production data structure

### Neon Database Branching

Benefits:

-   Instant database cloning
-   Isolated testing environments
-   Production-like data
-   Zero risk to production

Implementation:

1. Create test database branch
2. Execute test suite
3. Clean up resources
