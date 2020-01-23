MONGO_HOST = 'localhost'
MONGO_PORT = 27017

#MONGO_USERNAME = '<username>'
#MONGO_PASSWORD = '<password>'
#MONGO_AUTH_SOURCE = '<dbname>'

MONGO_DBNAME = 'urlpars'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#'url_id' has True in 'required' and 'unique', so it can't be used twice or more
schema = {    
    'url_id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
        'unique': True,
    },
    'url_input': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
    },   
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}

tags = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'url_id'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {
    'tags': tags,
}