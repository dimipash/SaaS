# SaaS Django Project

This is a Software as a Service (SaaS) project built with Django. The project includes features such as user authentication, subscription management, and custom management commands.

## Features

-   Python web development with Django
-   User Authentication (using django-allauth)
-   GitHub Login Integration
-   Sending Emails with Gmail
-   Deploy to Railway
-   Integrate Neon Postgres
-   Django Groups and User Permissions
-   Subscription Management
-   Custom Management Commands
-   Profile Management
-   Visit Tracking
-   Stripe Integration for Payments
-   Reoccurring payments via Products/Prices API
-   Pricing Page
-   User Subscription Management
-   Python Decouple for environment variables management
-   Django with Whitenoise for static file serving
-   Scheduled GitHub Actions Workflows for syncing production database with Stripe status (replacing Celery beat server)
-   Neon Branching for Postgres in GitHub Actions to leverage production data without touching it
-   Management commands for syncing user subscription status with correct permissions
-   Management commands for pulling vendor CSS/JS (Tailwind/Flowbite) for container-based builds

## Tech Stack

-   Django 5.0
-   Python 3.12
-   PostgreSQL (Neon)
-   Stripe for payment processing
-   Docker for containerization
-   Railway for deployment
-   Whitenoise for static file serving
-   Tailwind CSS and Flowbite for styling

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/dimipash/SaaS.git
    cd SaaS
    ```

2. Create a virtual environment and activate it:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
   Create a `.env` file in the root directory and add the following variables:

    ```
    DJANGO_DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    STRIPE_SECRET_KEY=your_stripe_secret_key
    BASE_URL=http://localhost:8000
    ```

5. Run migrations:

    ```
    python src/manage.py migrate
    ```

6. Create a superuser:

    ```
    python src/manage.py createsuperuser
    ```

7. Start the development server:
    ```
    python src/manage.py runserver
    ```

## Docker Support

This project includes Docker support. To build and run the Docker container:

1. Build the Docker image:

    ```
    docker build -t saas-django .
    ```

2. Run the container:
    ```
    docker run -p 8000:8000 saas-django
    ```

## Custom Management Commands

The project includes custom management commands located in `src/commando/management/commands/`:

-   `hello_world.py`: A simple command for testing
-   `vendor_pull.py`: Command for pulling vendor data
-   `sync_user_subs.py`: Command for syncing user subscriptions

To run a custom command:

```
python src/manage.py <command_name>
```

## Subscription Management

The project includes a robust subscription management system. Key features include:

-   Subscription plans and pricing
-   User subscription tracking
-   Subscription synchronization with Stripe

To sync user subscriptions, use the `sync_user_subs` management command:

```
python src/manage.py sync_user_subs [options]
```

Options include:

-   `--day-start`: Start day for the sync range
-   `--day-end`: End day for the sync range
-   `--days-left`: Number of days left in the subscription
-   `--days-ago`: Number of days ago to start the sync
-   `--clear-dangling`: Clear dangling subscriptions

## Project Structure

The project is organized into several Django apps:

-   `subscriptions`: Handles subscription logic and models
-   `customers`: Manages customer data
-   `profiles`: User profile management
-   `visits`: Tracks user visits
-   `commando`: Houses custom management commands

## GitHub Actions Workflows and Neon Branching

This project leverages GitHub Actions for automated workflows and Neon Branching for efficient database management in CI/CD pipelines.

### GitHub Actions Workflows

1. **Scheduled Production Sync**:

    - Automatically syncs the production database with Stripe subscription status.
    - Replaces the need for a dedicated Celery beat server.
    - Runs on a predefined schedule to ensure data consistency.

2. **Django Tests with Neon Branch**:
    - Creates a new branch of the production database for testing.
    - Runs Django tests against this isolated database branch.
    - Ensures test integrity without affecting production data.

### Neon Branching

Neon Branching is utilized to create instant, isolated copies of the production database for testing and development purposes.

-   **Benefits**:

    -   Zero-copy cloning: Branches are created instantly without copying data.
    -   Isolated testing: Each test run uses a fresh, isolated database branch.
    -   Production-like data: Tests run against a structure identical to production.
    -   Data safety: Production data remains untouched during testing.

-   **Usage in CI/CD**:
    1. A new branch is created before running tests.
    2. Tests are executed against this branch.
    3. The branch is deleted after tests complete.

This approach ensures that our CI/CD pipeline can run comprehensive tests with production-like data without any risk to the actual production database.
