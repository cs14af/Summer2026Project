from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from Birdie.models import Profile

class UserManagementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "testbird"
        self.password = "SuperSecret123!"
        self.email = "testbird@example.com"
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

    def test_profile_auto_created_on_user_creation(self):
        """Test that the signal creates a Profile when a User is created."""
        self.assertIsNotNone(self.user.profile)
        self.assertEqual(str(self.user.profile), f"@{self.username}")

    def test_login_success(self):
        """Test user login with valid credentials."""
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Redirects after login

    def test_login_failure(self):
        """Test user login with wrong password."""
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'WrongPassword123'
        })
        self.assertEqual(response.status_code, 200) # Re-renders login page with errors

    def test_protected_view_redirects_anonymous_user(self):
        """Test that unauthenticated users cannot access edit profile."""
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_edit_profile_authenticated(self):
        """Test that logged-in users can update their profile bio."""
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('edit_profile'), {
            'bio': 'Chirping from the nest!',
            'location': 'Austin, TX'
        })
        self.assertEqual(response.status_code, 302)
        
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.bio, 'Chirping from the nest!')

    def test_logout(self):
        """Test user logout."""
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)