from django.contrib.auth import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse

class TestRegistration(TestCase):
    def test_user_registration(self):
        self.client.post(
            reverse('users:register'),
            data={
                'username':'behruz',
                'first_name':'Behruz',
                'last_name':'Israiljonov',
                'email':'behruz@gmail.com',
                'password':'somepassword',
            }
        )
        user = CustomUser.objects.get(username='behruz')
        self.assertEqual(user.first_name, 'Behruz')
        self.assertEqual(user.last_name, 'Israiljonov')
        self.assertEqual(user.email, 'behruz@gmail.com')
        self.assertNotEquals(user.password, 'somepassword')
        self.assertTrue(user.check_password('somepassword'))

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'first_name': 'Behruz',
                'password': '<PASSWORD>'
            }
        )
        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'username', 'Ushbu maydon to\'ldirilishi shart.')

class LoginTest (TestCase):
    def setUp(self):
        db_user = CustomUser.objects.create(username='behruz', first_name='Behruz')
        db_user.set_password('somepassword')
        db_user.save()

    def test_success_login(self):


        self.client.post(
            reverse('users:login'),
            data = {
                'username': 'behruz',
                "password": "somepassword"
            }
        )

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)


    def test_wrong_login(self):


        self.client.post(
            reverse('users:login'),
            data={
                'username': 'other-user',
                "password": "somepassword"
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        self.client.post(
            reverse('users:login'),
            data={
                'username': 'other-user',
                "password": "somepassword"
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)



        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)
        self.client.post(
            reverse('users:login'),
            data={
                'username': 'behruz',
                "password": "wrong-password"
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)




    def test_logged_out(self):
        db_user = CustomUser.objects.create(username='behruz', first_name='Behruz')
        db_user.set_password('somepassword')
        db_user.save()
        self.client.login(username='behruz',password='somepassword')
        self.client.get(reverse('users:logout'))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)





