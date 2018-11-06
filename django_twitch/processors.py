from home.models import Settings


def global_variables(request):
    main = Settings.objects.all()[0]
    return {
        'site_title_short': main.site_title_short,
        'site_title_long': main.site_title_long,
        'site_description': main.site_description,
        'twitch_username': main.twitch_username.lower(),
        'site_favicon': main.site_favicon.name,
        'site_meta_image': main.site_meta_image.name,
        'site_meta_image_type': main.site_meta_image_type,
    }
