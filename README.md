**Wharton Preferred Base Django Layout**

(Well, preferred by tallen at least.)

This is an example Django Project. The goal of this is to educate the preferred WCIT project layout. You get these wonderful things out of the box:

* a .gitignore file with basically every editor, operating system and Pythontemp  file you want excluded automatically. (.gitignore)
* an example Apache configuration for the Django project (examples/apache-config.conf)
* settings done in the preferred style: in a settings subdirectory, separated by environment (django_base_project/settings/dev.py, base.py)
* a wsgi.py already set up for develop, stage and production environments.
* a requirements.txt file with the latest version of Django, and packages we will always be using: coverage for tests, Django-debug-toolbar, etc.

How to Use It (Assuming you're using the python-dev Vagrant box)

* Clone it:
    * git clone ssh://git@stash.wharton.upenn.edu:7999/wcit/django_base_project.git your_project_name
* Rename the Django project: 
    * find ./ -name "*.py" -exec sed -i 's/django_base_project/your_project_name/g' {} \;
    * mv your_project_name/django_base_project your_project_name/your_project_name
    * cp examples/apache-config.conf /etc/httpd/conf.d
* Modify the configuration to add your database credentials, if needed.
* Execute the following command to get everything up and running.
    * ./manage.py migrate
    * ./manage.py createsuperuser
    * sudo service httpd restart

* Please note, developing with "./manage.py runserver" is a much, much more pleasant experience. I recommend developing with that, and checking your Apache compatibility as your proceed
