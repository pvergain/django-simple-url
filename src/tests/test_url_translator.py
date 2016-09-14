from django.test import SimpleTestCase

from django_simple_url import URLTranslator


class URLTranslatorTests(SimpleTestCase):
    def setUp(self):
        self.translator = URLTranslator()

    def test_url_translator_maps_normal_url_to_url(self):
        self.assertEqual(
            self.translator.translate('/hello/world/'),
            r'\/hello\/world\/',
        )

    def test_url_translator_escapes_regex_special_characters(self):
        self.assertEqual(
            self.translator.translate('/hello.world/'),
            r'\/hello\.world\/'
        )

    def test_url_translator_maps_parameters_to_patterns(self):
        self.assertEqual(
            self.translator.translate('/:year/'),
            r'\/(?P<year>[A-Za-z0-9_]+)\/',
        )