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

    username = 'newuser'
    email = 'newuser@testmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_signup_page_template(self):
        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_form(self):

        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
