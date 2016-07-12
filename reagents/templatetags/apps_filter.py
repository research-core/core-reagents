from django.conf import settings
from django import template

register = template.Library()

@register.assignment_tag()
def get_my_app_list(app_list):
    """
    This will reorder the apps in the admin using weights defined in the RHEC_ADMIN_APP_WEIGHTS dict.
    The names, unfortunately, must be the verbose names displayed in the admin, not the actual app name,
    because that is what is in the admin app_list var.
    The app_list argument object is modified, it does not return a value.
    Usage: Define your app weights in settings.py like so:
    RHEC_ADMIN_APP_WEIGHTS = {'Sites': 1,
                              'Auth' : 2}
    Override the default admin index.html template and insert the following before the app_list is rendered:
    {% load admin_app_order %}{% reorder_admin_apps app_list %}
    """
    all_excluded_models = getattr(settings, 'EXCLUDE_ADMIN_APPS_MODELS', {})

    #print(all_excluded_models)

    for app in app_list:
        print(str(app['name']))
        models = app['models']
        #print([model['object_name'] for model in models])
        app_excluded_models = [model_name.split('.')[1] for model_name in all_excluded_models if model_name.split('.')[0] == str(app['name'])]
        #app_excluded_models = [model_name.split('.')[1] for model_name in all_excluded_models]
        #print(app_excluded_models)
        #print(models)
        filter_models = [model for model in models if model['object_name'] not in app_excluded_models]
        app['models'] = filter_models
        #print([model['object_name'] for model in app['models']])

    return app_list