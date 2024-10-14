# SaaS Project

This is a Software as a Service (SaaS) project built with Django. The project is currently in progress and new features are being added regularly.

## Features

-   User Authentication: Allows users to register, log in, and manage their accounts.
-   Subscription Management: Enables users to subscribe to different service tiers.
-   Profile Management: Users can create and edit their profiles.
-   Visit Tracking: Keeps track of user visits to the application.
-   Customer Management: Allows for the management of customer information.

## New Feature: Command Management

We've recently added a new 'commando' app that provides custom management commands. This feature enhances the project's maintainability and allows for easier execution of routine tasks.

Key aspects of the Command Management feature:

-   Custom Django management commands
-   Includes a 'hello_world' command for testing and demonstration
-   Includes a 'vendor_pull' command for updating vendor information

## Project Status

This project is still under active development. New features are being added, and existing features may be subject to change. We appreciate your patience and feedback as we continue to improve the application.

### Installation

1. Clone the repository

2. Create a virtual environment and activate it:
   python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate

3. Install the required packages:
   pip install -r requirements.txt

4. Run migrations:
   python src/manage.py migrate

5. Start the development server:
   python src/manage.py runserver

## Docker Support

This project includes a Dockerfile for containerization. To build and run the Docker container:

1. Build the Docker image:
   docker build -t saas-django .

2. Run the container:
   docker run -p 8000:8000 saas-django

## Custom Management Commands

The project includes custom management commands located in `src/commando/management/commands/`:

-   `hello_world.py`: A simple command for testing
-   `vendor_pull.py`: Command for pulling vendor data (implementation details to be added)

To run a custom command:

python src/manage.py <command_name>

## Templates

The project uses a base template structure with separate files for CSS and JavaScript includes. Main templates are located in `src/templates/`.

## Deployment

This project is configured for deployment on Railway. The `railway.toml` file in the root directory contains the necessary configuration.

## Contributing

As this is an ongoing project, contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request
