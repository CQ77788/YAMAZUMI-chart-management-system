# YAMAZUMI Management Application - Deployment Guide

This guide explains how to deploy the YAMAZUMI Management application to various free cloud platforms.

## Application Overview

The YAMAZUMI Management application is a Flask-based web application that helps manage manufacturing processes and workflows. It features:
- User authentication system
- Factory management
- Process section management
- Database storage using SQLite

## Deployment Options

### Option 1: Deploy to Heroku (Recommended)

1. Sign up for a free Heroku account at [https://heroku.com](https://heroku.com)
2. Install the Heroku CLI from [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
4. Add the Heroku PostgreSQL addon for persistent database storage:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```
5. Push your code to Heroku:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-app-name
   git push heroku main
   ```

### Option 2: Deploy to Render

1. Sign up for a free Render account at [https://render.com](https://render.com)
2. Connect your GitHub/GitLab account to Render
3. Create a new Web Service and select your repository
4. Configure the build:
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn server:app`
5. Set environment variables if needed
6. Deploy

### Option 3: Deploy to PythonAnywhere

1. Sign up for a free PythonAnywhere account at [https://pythonanywhere.com](https://pythonanywhere.com)
2. Upload your files using the dashboard or git
3. Create a new web app using Flask
4. Configure the virtual environment and install dependencies
5. Set the WSGI configuration file to point to your Flask app

## Configuration Files Included

- `Procfile`: Defines the command to run your application
- `requirements.txt`: Lists Python dependencies including gunicorn
- `runtime.txt`: Specifies the Python version to use
- Modified `server.py`: Updated to handle environment variables and production settings

## Important Notes

1. **Database**: The application currently uses SQLite, which may not persist on some cloud platforms. Consider migrating to PostgreSQL for production deployments.
2. **Security**: The SECRET_KEY should be set as an environment variable in production
3. **Static Files**: All HTML, JS, and other static files are served from the root directory

## Environment Variables

Set these environment variables in your cloud platform:
- `SECRET_KEY`: A random string for session encryption
- `PORT`: Port number (usually set automatically by the platform)

## Troubleshooting

- If your app fails to start, check the deployment logs for error messages
- Make sure all dependencies in requirements.txt are compatible with the cloud platform
- Verify that your application binds to the PORT environment variable

## Post-Deployment

After deploying, visit your application URL to confirm it's running. You can then register a new user account and begin managing your factories and processes.