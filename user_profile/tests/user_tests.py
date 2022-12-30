from django.test import TestCase
from base_user_manager.models import  C_user

class user_ (TestCase):
    def tests_create_user(self):
        # try create all types of users
        try:
            print("Test: creating user types [...] ")
            C_user.objects.create_student_user(username="Nk", first_name="Naa", last_name="Akewle", email="nk@mail.com", password="Nkk")
            C_user.objects.create_staff_user(username="Ray", first_name="Raymond" ,last_name="Appiah", email="Ray@mm.com", password="Rayz")
            C_user.objects.create_admin_user(username="SHad", first_name="Shadrack", email="shaddy1@gmail.com", last_name="Opoku", password="chuck")
            C_user.objects.create_superuser(username="hckr1", first_name="Brian", email="shaddy1@gmail.com", last_name="Cornor", password="chuck")
            print("Test: creating user types [ok]")
        except:
            raise Exception("Failed to create the variouse types of users!")

        try:
            Naa = C_user.objects.get(username="Nk")
            Ray = C_user.objects.get(username="Ray")
            shad = C_user.objects.get(username="SHad")
            hckr1 = C_user.objects.get(username="hckr1")
            print("Test: testing student user type: [...]")
            self.assertEqual(Naa.first_name, "Naa")
            self.assertTrue(Naa.is_student)
            self.assertFalse(Naa.is_staff)
            self.assertFalse(Naa.is_admin)
            self.assertFalse(Naa.is_superuser)
            print("Test: testing student user type: [ok]")

            print("Test: testing staff user type: [...]")
            self.assertEqual(Ray.first_name, "Raymond")
            self.assertFalse(Ray.is_student)
            self.assertTrue(Ray.is_staff)
            self.assertFalse(Ray.is_admin)
            self.assertFalse(Ray.is_superuser)
            print("Test: testing staff user type: [ok]")

            print("Test: testing admin user type: [...]")
            self.assertEqual(shad.first_name, "Shadrack")
            self.assertFalse(shad.is_student)
            self.assertFalse(shad.is_staff)
            self.assertTrue(shad.is_admin)
            self.assertFalse(shad.is_superuser)
            print("Test: testing admin user type: [ok]")

            print("Test: testing superuer user type: [...]")
            self.assertEqual(hckr1.first_name, "Brian")
            self.assertFalse(hckr1.is_student)
            self.assertFalse(hckr1.is_staff)
            self.assertTrue(hckr1.is_admin)
            self.assertTrue(hckr1.is_superuser)
            print("Test: testing superuser user type: [ok]")
        except:
            raise Exception("User types may not be properly set!")

