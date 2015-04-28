## Django Starter Kit (v1.0)

### Table of Contents
- Introduction
- Included Plugins
- Components & Standards
- Getting Started
- Error Handling with Rollbar
  - Overview
	- Installation
	- Getting a Rollbar Account
	- Custom Handling
- Django Base Theme
  - Overview
- Selenium and Unit Testing
	- Overview
	- Etc. Etc..

### Introduction
Django Starter Kit (v 1.0) is a boilerplate for developing web applications.

### Plugins Include
- Django Rest Framework
- Django Debug Toolbar
- Rollbar
- Django Base Theme
- Django Bootstrap
- Argparse
- Coverage
- Django Compressor
- Django Filter
- Django Pyodbc Azure
- Markdown
- Pytz
- Sqlparse
- Pyodbc

### Components & Standards
- .gitignore file with editors, operating systems and Pythontemp files you want excluded.
- example Apache configuration for the Django project (examples/apache-config.conf)
- settings done in the preferred style: in a settings subdirectory, separated by environment: 
	- project/settings/dev.py
	- project/settings/base.py
- wsgi.py set up for develop, stage and production environments.
- requirements.txt file that includes the above plugins and Django version 1.7.7.

### Getting Started
- Clone it:
    - git clone ssh://git@stash.wharton.upenn.edu:7999/caos/django_starter_kit.git your_project_name
- Rename the Django project: 
    - find ./ -name "*.py" -exec sed -i 's/django_starter_kit/your_project_name/g' {} \;
    - mv your_project_name/django_starter_kit your_project_name/your_project_name
    - cp examples/apache-config.conf /etc/httpd/conf.d
- Modify the configuration to add your database credentials, if needed.
- Execute the following command to get everything up and running.
    - ./manage.py migrate
    - ./manage.py createsuperuser
    - sudo service httpd restart

### Error Handling with Rollbar

####Overview & Links

- Rollbar reports on application exceptions and errors.
  - Git: https://github.com/rollbar/pyrollbar
  - Website: https://rollbar.com/docs/notifier/pyrollbar/
  - Rollbar docs: https://rollbar.com/docs/

####Installation

<pre><code>pip install rollbar</code></pre>

Add to the bottom of your middleware classes:  

<pre><code>'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'</code></pre>

Add this to your base.py file:

<pre><code>ROLLBAR = {
    'access_token': 'POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/absolute/path/to/code/root',
}</code></pre>

####Setting Up Your Rollbar Account
- Contact us and we will give you access to Wharton's Rollbar account.
- From there, create your project in the dashboard and set your token key in your 
  settings dictionary
  configuration

#### Custom Rollbar Handling
You can also set rollbar error reporting manually, by adding functions this to your code:

<pre><code>rollbar.report_message('Got an IOError in the main loop', 'warning')</code></pre>

See Rollbar documentation for more examples and helpful tips.

### Django Base Theme

####Overview
Django Base Theme is a responsive front-end boilerplate designed for Wharton apps that includes helpful plugins,
components and standards. DBT's installation and use is already documented here: 
<pre><code>https://github.com/wharton/django-base-theme</code></pre>
  
### Selenium and Unit Testing

####Overview
