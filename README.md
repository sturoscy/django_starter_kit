## Django Starter Kit (v1.1)

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
- Contributors

### Introduction
Django Starter Kit (version 1.1) is a boilerplate for developing web applications. 
**Built using Django 1.7.8**

### Included Django Plugins
- [argparse==1.2.1](https://code.google.com/p/argparse/)
- [base-theme==1.0](https://github.com/chadwhitman/Django-Base-Theme)
- [coverage==3.7.1](https://bitbucket.org/ned/coveragepy)
- [django>=1.8,<1.9](https://github.com/django/django)
- [django-appconf==1.0.1](https://github.com/jezdez/django-appconf)
- [django-compressor==1.4](https://github.com/django-compressor/django-compressor)
- [django-debug-toolbar==1.2.1](https://github.com/django-debug-toolbar/django-debug-toolbar)
- [django-filter==0.9.2](https://github.com/alex/django-filter)
- [django-pyodbc-azure==1.2.1](https://github.com/michiya/django-pyodbc-azure)
- [djangorestframework==3.1.0](https://github.com/tomchristie/django-rest-framework/tree/master)
- [Markdown==2.6.1](http://pythonhosted.org//Markdown/)
- [pyodbc==3.0.10](https://github.com/mkleehammer/pyodbc)
- [pytz==2014.7](http://pythonhosted.org//pytz/)
- [PyYAML==3.11](https://github.com/yaml/pyyaml)
- [requests==2.7.0](https://github.com/kennethreitz/requests)
- [rollbar==0.9.9](https://github.com/rollbar/pyrollbar)
- [six==1.9.0](https://github.com/kelp404/six)
- [sqlparse==0.1.13](https://github.com/andialbrecht/sqlparse)

### Components & Standards
- .gitignore file with editors, operating systems and Pythontemp files you want excluded.
- settings done in the preferred style: in a settings subdirectory, separated by environment: 
	- project/settings/base.py
	- project/settings/prod.py
	- project/settings/dev.py
	- project/settings/vagrant.py
- wsgi.py set up for develop, stage and production environments.
- requirements.txt file that includes the above plugins and Django version >=1.8,<1.9
- bower.json file included for managing third party javascript vendor files
- gulpfile.js included for static files automation (javascripts, coffeescripts, sass, eco templates, etc.)
- node package manager (packages.json) file included for gulp dependencies

### Getting Started
1. Clone vagrant box
    - `git clone ssh://git@stash.wharton.upenn.edu:7999/vagrant/python-dev.git`
    - `cd python-dev`
    - `vagrant up` (go get coffee, this will take awhile)
    - `vagrant ssh`
    - check the python-dev-node documentation at https://stash.wharton.upenn.edu/projects/CAOS/repos/python-dev-node/browse
        - follow steps 1 - 3 here - https://help.github.com/articles/generating-ssh-keys/ - to generate ssh keys
        - run `cat < ~/.ssh/id_rsa.pub` after generating your keys and copy the output
        - paste ssh keys to your stash account here - https://stash.wharton.upenn.edu/plugins/servlet/ssh/account/keys
2. From ssh session
    - create virtualenv
        - `mkvirtualenv your_project_name`
        - `workon your_project_name`
    - clone the django_starter_kit into /vagrant/html/
        - `cd /vagrant/html/`
        - `pip install django==1.7.8`
        - `django-admin startproject --template=https://github.com/sturoscy/django_starter_kit/archive/master.zip your_project_name`
        - `cd your_project_name`
    - update your apache-config.conf file
        - `sudo vim /etc/httpd/conf.d/apache-config.conf`
        - make sure you replace the name of your virtualenv and the name of your project where applicable
3. Rename references to django_starter_kit in the Django project: 
    - `find -name "*.py" -exec sed -r -i'' -e 's/django_starter_kit/your_project_name/g' {} \;`
    - mv your_project_name/django_starter_kit your_project_name/your_project_name  
4. Check the /vagrant/html/your_project_name/settings folder
    - this folder contains various django settings that relate to different environments
5. Execute the following commands to get everything up and running.
    - `pip install -r requirements.txt`
    - `./manage.py migrate`
    - `./manage.py collectstatic`
    - `sudo service httpd restart`

    #### Steps to get bower and gulp running (not required)

6. Copy NPM requirements:
    - `cp /vagrant/dependencies/node_modules.zip /vagrant/html/your_project_name`
    - `unzip /vagrant/html/your_project_name/node_modules.zip`
    - `rm /vagrant/html/your_project_name/node_modules.zip`
7. Create symlinks to gulp and bower
    - `ln -s /vagrant/html/your_project_name/node_modules/gulp/bin/gulp.js /vagrant/html/your_project_name/gulp`
    - `ln -s /vagrant/html/your_project_name/node_modules/bower/bin/bower /vagrant/html/your_project_name/bower`

    #### Using cosign and Penn SSO

8. Check the .htaccess file in the root of the project and uncomment the following lines:

    <pre><code>CosignProtected On
    AuthType Cosign
    Require valid-user
    CosignRequireFactor  UPENN.EDU</pre></code>

9. See https://github.com/wharton/wharton-cosign-auth for more info on getting everything setup after updating the .htaccess file

### Static File Management

#### Overview
The Django Starter Kit comes with two methods of client-side static file management - **collectstatic** and **gulp**. Use of bower and gulp gives you more control over your static files, but is much more complicated to get up and running than collectstatic.

### Getting Started with Static Files

#### Collectstatic
The Django Starter Kit uses django's built-in static file management and is well-documented on [django's](https://docs.djangoproject.com/en/1.7/ref/contrib/staticfiles/) main site. In short, running collectstatic will look for static files in a few different places - see [STATICFILES_FINDERS](https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-STATICFILES_FINDERS)

- in app directories as long as the app is in the INSTALLED_APPs tuple in settings/base.py
    - django.contrib.staticfiles.finders.AppDirectoriesFinder
    - for example, your_app_name/static/your_app_name/*.css|*.js
- in the static_dev directory
    - django.contrib.staticfiles.finders.FileSystemFinder
    - for example, static_dev/javascripts/*.js and/or static_dev/css/*.css

#### Node and NPM 
#### Note: the following few sections can be skipped if you are not going to use node and npm
The node package manager (NPM) is used to manage node javascript packages that are used in the gulp file (see below). 

- make sure you complete steps 6 and 7 in **Getting Started**
- add any additional npm packages to the included default packages.json file
- run `npm install --cache`

#### GulpJS
The starter kit uses gulp to manage and automate client-side dependencies. For more info on gulp, please visit their website here - [GulpJS Docs](https://github.com/gulpjs/gulp/tree/master/docs). 

`./gulp help` will list available gulp main and sub-commands. The gulpfile.js file is heavily commented for more clarity.

`./gulp build` will build all of the projects dependencies (coffeescript or javascript, javascript templates, styles, and images). 

`./gulp serve` will run a proxy server for apache located at https://vagrant.wharton.upenn.edu:3000 that watches for changes in coffeescripts, javascripts, and sass files and will run the appropriate gulp task, restart apache, and reload the browser using the browser-sync node package. `./gulp serve` should only be run in development

#### Vendor Files
Vendor files are managed through [bower](http://bower.io). Your vendor requirements should be added to the [bower.json](http://bower.io/docs/creating-packages/#bowerjson) file in the dependencies section. You can search for [bower packages](http://bower.io/search "bower search") on bower's website.

After adding any additional requirements, run the following commands:

<pre><code>./bower install
./gulp bower</code></pre>

The bower install command installs vendor files to static_dev/bower_components. Running `./gulp bower` will concat and minimize all vendor files to static/javascripts/vendor.min.js and static/stylesheets/vendor.css

- add vendor javascripts to any template using:

<pre><code>{% compress js %}
    &lt;script type="text/javascript" src="{% static "javascripts/vendor.min.js" %}"&gt;&lt;/script&gt;
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

When you are ready, run `./gulp scripts-javascripts` 

- this will concat and minify javascripts
- after the task is run, an app.min.js file will be placed in the static/javascripts/ directory
- add the file to any template with:

<pre><code>{% compress js %}
    &lt;script type="text/javascript" src="{% static "javascripts/app.min.js" %}"&gt;&lt;/script&gt;
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

Run `./gulp scripts-coffee`

- this will compile, concat and minify coffeescripts
- it will also copy compiled to javascript versions of the files into static_dev/javascripts
- after the task is run, an app.min.js file will be placed in the static/javascripts/ directory
- add the file to any template with:

<pre><code>{% compress js %}
    &lt;script type="text/javascript" src="{% static "javascripts/app.min.js" %}"&gt;&lt;/script&gt;
{% endcompress %}</code></pre>

#### Stylesheets and SASS
Place all sass (scss) stylesheets in static_dev/scss

- run `./gulp styles-sass`
- sass files are combined, compiled, and minified
- after the task is run, a app.min.css file will be placed in the static/stylesheets directory
- add the file to any template with:

<pre><code>{% compress css %}
    &lt;link rel="stylesheet" href='{% static 'stylesheets/app.min.css' %}' type="text/css" charset="utf-8"&gt;
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

Rollbar is already included in the requirements.txt file. Settings for rollbar are only included in the prod.py settings file (since we only want to use it for production). Check that file and replace the following with your info:

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
Django Base Theme is a responsive front-end boilerplate designed for Wharton Django/Python apps that includes helpful plugins, components and standards. Installation and use is already documented here: [https://github.com/wharton/django-base-theme](https://github.com/wharton/django-base-theme)
    
### Selenium and Unit Testing

#### Overview
Once you have the starter kit installed, run `./manage.py runserver 0.0.0.0:8000` to start a python server and go to localhost:8001/test. That page has more information regarding UnitTesting in the starter kit. Also, a few basic unit testing examples can be found in the following directories and files:

<pre><code>|-- django_starter_kit
    |-- tests.py
    |-- views.py
|-- templates
    |-- test_view
        |-- test_view_page.html</code></pre>

### Contributors
##### (in alphabetical order)
- Tim Allen
- Mikhail Oza
- Steve Turoscy
- Chad Whitman
