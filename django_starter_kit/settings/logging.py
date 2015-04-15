
# Log Settings

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
				    'class': 'django.utils.log.AdminEmailHandler'
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
        'dsk' : {
	        'handlers': ['console','file', 'mail_admins'],
	        'level' : 'DEBUG',
	        'propagate': True,
        },
    },
}