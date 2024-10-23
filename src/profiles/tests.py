from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

class ProfileViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test users
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            email='testuser@example.com',
            first_name='Test',
            last_name='User'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='12345',
            email='otheruser@example.com'
        )
        # Get view_user permission
        content_type = ContentType.objects.get_for_model(User)
        self.view_permission = Permission.objects.get(
            content_type=content_type,
            codename='view_user'
        )

    def test_profile_list_view_unauthenticated(self):
        """Test that unauthenticated users cannot access profile list"""
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_profile_list_view_authenticated_no_permission(self):
        """Test that authenticated users without permission cannot view list"""
        self.client.force_login(self.user)
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You do not have permission to view users")
        self.assertNotContains(response, self.other_user.username)

    def test_profile_list_view_with_permission(self):
        """Test that users with permission can view the list"""
        self.user.user_permissions.add(self.view_permission)
        self.client.force_login(self.user)
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.other_user.username)

    def test_profile_detail_view_unauthenticated(self):
        """Test that unauthenticated users cannot access profile details"""
        response = self.client.get(f'/profiles/{self.user.username}/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_profile_detail_view_authenticated_no_permission(self):
        """Test that authenticated users without permission can only see limited info"""
        self.client.force_login(self.user)
        response = self.client.get(f'/profiles/{self.other_user.username}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.other_user.username)
        self.assertContains(response, "You do not have permission to view users")

    def test_profile_detail_view_with_permission(self):
        """Test that users with permission can see full profile details"""
        self.user.user_permissions.add(self.view_permission)
        self.client.force_login(self.user)
        response = self.client.get(f'/profiles/{self.other_user.username}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.other_user.username)
        self.assertNotContains(response, "You do not have permission to view users")

    def test_profile_detail_view_own_profile(self):
        """Test that users can view their own profile"""
        self.client.force_login(self.user)
        response = self.client.get(f'/profiles/{self.user.username}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_profile_detail_view_nonexistent_user(self):
        """Test accessing a profile that doesn't exist"""
        self.client.force_login(self.user)
        response = self.client.get('/profiles/nonexistentuser/')
        self.assertEqual(response.status_code, 404)

    def test_profile_urls_reverse(self):
        """Test that URL reversing works correctly"""
        self.assertEqual(reverse('profile_list'), '/profiles/')
        self.assertEqual(
            reverse('profile_detail', kwargs={'username': 'testuser'}),
            '/profiles/testuser/'
        )