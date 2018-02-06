from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.core.servers.basehttp import get_internal_wsgi_application
from django.core.wsgi import get_wsgi_application
from django.test import SimpleTestCase, override_settings


class GetInternalWSGIApplicationTest(SimpleTestCase):
    @override_settings(WSGI_APPLICATION="config.wsgi.application")
    def test_success(self):
        """
        If ``WSGI_APPLICATION`` is a dotted path, the referenced object is
        returned.
        """
        app = get_internal_wsgi_application()

        from config.wsgi import application

        self.assertIs(app, application)

    @override_settings(WSGI_APPLICATION=None)
    def test_default(self):
        """
        If ``WSGI_APPLICATION`` is ``None``, the return value of
        ``get_wsgi_application`` is returned.
        """
        # Mock out get_wsgi_application so we know its return value is used
        fake_app = object()

        def mock_get_wsgi_app():
            return fake_app

        from django.core.servers import basehttp

        _orig_get_wsgi_app = basehttp.get_wsgi_application
        basehttp.get_wsgi_application = mock_get_wsgi_app

        try:
            app = get_internal_wsgi_application()

            self.assertIs(app, fake_app)
        finally:
            basehttp.get_wsgi_application = _orig_get_wsgi_app

    @override_settings(WSGI_APPLICATION="wsgi.noexist.app")
    def test_bad_module(self):
        msg = "WSGI application 'wsgi.noexist.app' could not be loaded; Error importing"
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            get_internal_wsgi_application()

    @override_settings(WSGI_APPLICATION="wsgi.wsgi.noexist")
    def test_bad_name(self):
        msg = "WSGI application 'wsgi.wsgi.noexist' could not be loaded; Error importing"
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            get_internal_wsgi_application()
