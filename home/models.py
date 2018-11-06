from django.db import models
from django.contrib.auth.models import User


class Social(models.Model):
    name = models.CharField(max_length=255, help_text='Used for the alternative text for the resource.')
    enabled = models.BooleanField(default=False, help_text='Must be checked to show up on the site.')
    url = models.URLField(blank=True, help_text='Full URL that the user will be taken to on click.')
    icon = models.CharField(max_length=255, help_text='Path to existing icon or full URL to remote icon.<br> '
                                                      'Recommended icons are 512x512 transparent PNGs.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Social'


class Settings(models.Model):
    site_title_short = models.CharField(max_length=255, help_text='Title that appears in the main menu.')
    site_title_long = models.CharField(max_length=255, help_text='Title that appears in the browser tab, '
                                                                 'bookmarks and site metadata.')
    site_description = models.CharField(max_length=255, help_text='Description that appears in og tags, '
                                                                  'metadata, and search engines descriptions.')
    twitch_username = models.CharField(max_length=15, help_text='Twitch username for displaying video/chat on '
                                                                'the homepage.')
    site_favicon = models.ImageField(upload_to='assets', help_text='Icon that appears in browser tabs and bookmarks. '
                                                                   '<br>Recommended icon is up to 256x256 ICO.')
    site_meta_image = models.ImageField(upload_to='assets', help_text='Image that appears when url is unfurled.<br> '
                                                                      'Recommended image is 512x512 transparent PNG.')
    site_meta_image_type = models.CharField(max_length=255, help_text='Valid image mime type. Ex: PNG uses: image/png')

    def __str__(self):
        return 'Main Site Settings: {}'.format(self.site_title_short)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


class About(models.Model):
    about_title = models.CharField(max_length=255, help_text='Title of the About Page.')
    about_first_paragraph = models.TextField(blank=True, help_text='Main paragraph of the About Page.')
    about_second_paragraph = models.TextField(blank=True, help_text='Second paragraph of the About Page.')
    about_image = models.ImageField(upload_to='assets', blank=True, help_text='Image that appears on the About Page.')

    def __str__(self):
        return 'About Page Settings: {}'.format(self.about_title)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
