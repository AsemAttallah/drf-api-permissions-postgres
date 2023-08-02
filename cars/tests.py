from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Car, Post

# Create your tests here.

class CarTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_car = Car.objects.create(
            type="BMW",
            purchaser=testuser1,
            desc="2021", 
        )
        test_car.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_cars_model(self):
        car = Car.objects.get(id=1)
        actual_purchaser = str(car.purchaser)
        actual_type = str(car.type)
        actual_desc = str(car.desc)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_type, "BMW")
        self.assertEqual(
            actual_desc, "2021"
        )

    def test_get_car_list(self):
        url = reverse("car_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cars = response.data
        self.assertEqual(len(cars), 1)
        self.assertEqual(cars[0]["type"], "BMW")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("car_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete_car(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("car_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_only_owner_can_get_car_detail(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("car_detail",args=[1])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_post = Post.objects.create(
            any_comment="very nice car", 
        )
        test_post.save()
    
    def test_post_model(self):
        post = Post.objects.get(id=1)
        actual_any_comment = str(post.any_comment)
        self.assertEqual(actual_any_comment, "very nice car")

    def test_get_post_list_without_login(self):
        url = reverse("post_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post = response.data
        self.assertEqual(len(post), 1)
        self.assertEqual(post[0]["any_comment"], "very nice car")