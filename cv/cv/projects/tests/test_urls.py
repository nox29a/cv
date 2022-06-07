from django.test import SimpleTestCase
from django.urls import reverse, resolve
from projects.views import skill_view, contact_view, project_gallery, register, project_detail

class TestUrls(SimpleTestCase):

    def test_base_url_resolves(self):
            url = reverse('base')
            self.assertEquals(resolve(url).func, skill_view)

    def test_gallery_url_resolves(self):
            url = reverse('gallery')
            self.assertEquals(resolve(url).func, project_gallery)

    def test_gallery_detail_url_resolves(self):
            url = reverse('project_detail', args=['2'])
            self.assertEquals(resolve(url).func, project_detail)

    def test_contact_url_resolves(self):
            url = reverse('contact')
            self.assertEquals(resolve(url).func, contact_view)

    def test_register_url_resolves(self):
            url = reverse('register')
            self.assertEquals(resolve(url).func, register)