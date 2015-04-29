## Django Starter Kit (v1.0)

### Table of Contents
- Introduction
- Included Plugins
- Components & Standards
- Getting Started
- Static File Management
    - Overview
    - Getting Started with Static Files
    - Vendor Files
    - JavaScripts
    - CoffeeScripts
    - Stylesheets and SASS
- Error Handling with Rollbar
    - Overview
    - Installation
    - Getting a Rollbar Account
    - Custom Handling
- Django Base Theme
    - Overview
- Selenium and Unit Testing
    - Overview

### Introduction
Django Starter Kit (v 1.0) is a boilerplate for developing web applications. 
**Built using Django v 1.7.7.**

### Included Plugins
- [Django Base Theme](https://github.com/chadwhitman/Django-Base-Theme)
- [Django Bootstrap](https://github.com/dyve/django-bootstrap3)
- [Django Compressor](https://github.com/django-compressor/django-compressor)
- [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)
- [Django Filter](https://github.com/alex/django-filter)
- [Django Pyodbc Azure](https://github.com/michiya/django-pyodbc-azure)
- [Django Rest Framework](https://github.com/tomchristie/django-rest-framework/tree/master)
- [Argparse](https://code.google.com/p/argparse/)
- [Coverage](https://bitbucket.org/ned/coveragepy)
- [Markdown](http://pythonhosted.org//Markdown/)
- [Pyodbc](https://github.com/mkleehammer/pyodbc)
- [Pytz](http://pythonhosted.org//pytz/)
- [Rollbar](https://github.com/rollbar/pyrollbar)
- [Sqlparse](https://github.com/andialbrecht/sqlparse)

### Components & Standards
- .gitignore file with editors, operating systems and Pythontemp files you want excluded.
- settings done in the preferred style: in a settings subdirectory, separated by environment: 
    - project/settings/base.py
    - project/settings/prod.py
    - project/settings/dev.py
    - project/settings/vagrant.py
- wsgi.py set up for develop, stage and production environments.
- requirements.txt file that includes the above plugins and Django version 1.7.7.
- bower.json file included for managing third party javascript vendor files
- gulpfile.js included for static files automation (javascripts, coffeescripts, sass, eco templates, etc.)
- node package manager (packages.json) file included for gulp dependencies

### Getting Started
- Clone it:
    - git clone ssh://git@stash.wharton.upenn.edu:7999/caos/django_starter_kit.git your_project_name
- Rename the Django project: 
    - find ./ -name "*.py" -exec sed -i 's/django_starter_kit/your_project_name/g' {} \;
    - mv your_project_name/django_starter_kit your_project_name/your_project_name
    - cp examples/apache-config.conf /etc/httpd/conf.d
- Modify the configuration to add your database credentials, if needed.
- Execute the following commands to get everything up and running.
    - ./manage.py migrate
    - ./manage.py createsuperuser
    - sudo service httpd restart

### Static File Management

#### Overview
The Django Starter Kit comes with two methods of client-side static file management - **collectstatic** and **gulp**. You will use **collectstatic** for any 3rd party plugins added via the requirements.txt file and subsequently placed in INSTALLED_APPS. For any internally developed apps, you will use **gulp** and the gulpfile.

### Getting Started with Static Files

#### Node and NPM
The node package manager (NPM) is used to manage node javascript packages that are used in the gulp file (see below). 

- add any additional npm packages to the included default packages.json file
- run `npm install`
    - this will take some time depending on your system (5 - 10 minutes)

#### GulpJS
The starter kit uses gulp to manage and automate client-side dependencies. For more info on gulp, please visit their website here - [GulpJS Docs](https://github.com/gulpjs/gulp/tree/master/docs). The available gulp commands are:

- `./gulp serve`
- `./gulp javascripts`
- `./gulp coffee`
- `./gulp eco`
- `./gulp bower`
- `./gulp sass`
- `./gulp images`

`./gulp build` will run all of the above commands except for serve. `./gulp serve` will run a proxy server for runserver or apache located at localhost:3000 that watches for changes in coffeescripts, javascripts, and sass files and run the appropriate gulp task and reload the browser using the browser-sync node package. `./gulp serve` should only be run in development

#### Vendor Files
Vendor files are managed through [bower](http://bower.io). Your vendor requirements should be added to the [bower.json](http://bower.io/docs/creating-packages/#bowerjson) file in the dependencies section. You can search for [bower packages](http://bower.io/search "bower search") on bower's website.

After adding any additional requirements, run the following commands:

<pre><code>./bower install
./gulp bower</code></pre>

The bower install command installs vendor files to static_dev/bower_components. Running `./gulp bower` will concat and minimize all vendor files to static/javascripts/vendor.js and static/stylesheets/vendor.css

- add vendor javascripts to any template using:

<pre><code>{% compress js %}
    &lt;script type="text/javascript" src="{% static "javascripts/vendor.js" %}"&gt;&lt;/script&gt;
{% endcompress %}</code></pre>

- add vendor Stylesheets to any template using:

<pre><code>{% compress css %}
    &lt;link rel="stylesheet" href="{% static "stylesheets/vendor.css" %}" type="text/css" charset="utf-8"&gt;
{% endcompress %}</code></pre>

- if you add additional vendor files to bower.json, you will need to re-run `./bower install` and `./gulp bower`

#### JavaScripts
The Starter Kit comes with Backbone and Underscore installed via the bower.json file. Backbone apps are scaffolded as follows:

<pre><code>|-- static_dev
    |-- javascripts
        |-- app1
            |-- models
            |-- collections
            |-- views
            |-- routers
            |-- main.js
        |-- app2
            |-- models
            |-- collections
            |-- views
            |-- routers
            |-- main.js
        ...
        |-- appn
            |-- models
            |-- collections
            |-- views
            |-- routers
            |-- main.js</code></pre>

If you don't want to use Backbone or Underscore in your app, then simply remove the entries in the bower.json file and scaffold your javascripts directory however you like, keeping with the following structure:

<pre><code>|-- static_dev
    |-- javascripts
        |-- app
            |-- *.js</code></pre>

When you are ready, run `./gulp javascripts` 

- this will concat and minify javascripts
- after the task is run, an app.js file will be placed in the static/javascripts/ directory
- add the file to any template with:

<pre><code>{% compress js %}
    &lt;script type="text/javascript" src="{% static "javascripts/app.js" %}"&gt;&lt;/script&gt;
{% endcompress %}</code></pre>

#### CoffeeScripts
CoffeeScripts are scaffolded the same way as javascripts:

<pre><code>|-- static_dev
    |-- coffescripts
        |-- app1
            |-- models
            |-- collections
            |-- views
            |-- routers
            |-- main.coffee
        |-- app2
            |-- models
            |-- collections
            |-- views
            |-- routers
            |-- main.coffee
        ...
        |-- appn
            |-- models
            |-- collections
            |-- views
            |-- routers
            |-- main.coffee</code></pre>

or without backbone:

<pre><code>|-- static_dev
    |-- coffeescripts
        |-- app
            |-- *.coffee</code></pre>

Run `./gulp coffee`

- this will compile, concat and minify coffeescripts
- it will also copy compiled to javascript versions of the files into static_dev/javascripts
- after the task is run, an app.js file will be placed in the static/javascripts/ directory
- add the file to any template with:

<pre><code>{% compress js %}
    &lt;script type="text/javascript" src="{% static "javascripts/app.js" %}"&gt;&lt;/script&gt;
{% endcompress %}</code></pre>

#### Stylesheets and SASS
Place all sass (scss) stylesheets in static_dev/scss

- run `./gulp sass`
- sass files are combined, compiles, and minified
- after the task is run, a custom.css file will be placed in the static/stylesheets directory
- add the file to any template with:

<pre><code>{% compress css %}
    &lt;link rel="stylesheet" href='{% static 'stylesheets/custom.css' %}' type="text/css" charset="utf-8"&gt;
{% endcompress %</code></pre>

### Error Handling with Rollbar

#### Overview ####
Rollbar is a plugin that reports on your application's exceptions and errors. Learn more via the links below:

#### Links

- Git: https://github.com/rollbar/pyrollbar
- Website: https://rollbar.com/docs/notifier/pyrollbar/
- Rollbar overview: https://rollbar.com/docs/
- Rollbar Error Tracking: https://rollbar.com/error-tracking/

#### Installation

    pip install rollbar

Add to the bottom of your middleware classes:  

    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'

Add this to your base.py file:

<pre><code>ROLLBAR = {
    'access_token': 'POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/absolute/path/to/code/root',
}</code></pre>

#### Setting Up Your Rollbar Account
- If you are part of CAOS or the Custom Applications team, contact us and we will give you access to Wharton's Rollbar account
- If you are not a member of CAOS, you can create a free personal or team [rollbar account](https://rollbar.com/signup/) 
- From there, create your own project in the dashboard and set your token key in your settings dictionary configuration.

#### Custom Rollbar Handling
You can also set Rollbar error reporting manually, by adding functions like this to your code:

    rollbar.report_message('Got an IOError in the main loop', 'warning', request)

See [Rollbar documentation](https://rollbar.com/docs/notifier/pyrollbar/) for more examples and helpful tips.

### Django Base Theme

#### Overview ####
Django Base Theme is a responsive front-end boilerplate designed for Wharton apps that includes helpful plugins, components and standards. DBT's installation and use is already documented here: [https://github.com/wharton/django-base-theme](https://github.com/wharton/django-base-theme)
    
### Selenium and Unit Testing

#### Overview
