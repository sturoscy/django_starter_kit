
# Log Settings

ROLLBAR = {
    'access_token': 'POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/absolute/path/to/code/root',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
	    'verbose': {
		     'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
         'datefmt' : "%d/%b/%Y %H:%M:%S"
	    },
	    'simple': {
		    'format': '%(levelname)s %(message)s',
	    },
	    
    },
    'filters': {
	    'require_debug_false' : {
		    '()': 'django.utils.log.RequireDebugFalse',
	    },
	    'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
      },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filters': ['require_debug_true'],
            'filename': 'logs/django_dev.log',
        },
        'console': {
	        'level': 'DEBUG',
	        'class': 'logging.StreamHandler',
	        'formatter': 'simple'
        },
	    'mail_admins': {
		    'level': 'CRITICAL',
		    'filters' : ['require_debug_false'],
		    'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
	     },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
	        'handlers': ['mail_admins'],
	        'level': 'CRITICAL',
	        'propagate': False,
        },
    },
}