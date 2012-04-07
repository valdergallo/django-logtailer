from distutils.core import setup

setup(
    name='logtailer',
    description='Allows the viewing of any log file entries in real time directly from the Django admin interface. It allows you to filter on logs with regex and offer also a log clipboard for save desired log lines to the django db.',
    packages=['logtailer'],
)