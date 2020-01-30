from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from .views import SignupView
from .forms import CustomCreationForm

class CustomTest(TestCase):

    def test_create_user(self):
        
        User = get_user_model()
        user = User.objects.create_user(
            username = 'test_user',
            email = 'test@testmail.com',
            password = 'testpassword'
        )

        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@testmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'test_user',
            email = 'test@testmail.com',
            password = 'testpassword'
        )

        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@testmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
    
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupView.as_view().__name__
        )
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')