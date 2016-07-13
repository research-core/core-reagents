from django.conf import settings
from django import template

register = template.Library()


@register.assignment_tag()
def get_my_app_list(app_list):
    """
    This will filter the apps in the admin based on app and model as defined in Django settings
    Example: Reagents.EnzymeType (app is Reagents, model is EnzymeType)
    Override the default admin index.html template and insert the following before the app_list is rendered:
    {% load apps_filter %}{% get_my_app_list app_list as app_list %}
    """
    all_excluded_models = getattr(settings, 'EXCLUDE_ADMIN_APPS_MODELS', {})

    for app in app_list:
        models = app['models']
        match_app_models = [app_model_name.split('.')[1] for app_model_name in all_excluded_models if
                            app_model_name.split('.')[0] == str(app['name'])]
        filter_models = [model for model in models if model['object_name'] not in match_app_models]
        app['models'] = filter_models

    return app_list
