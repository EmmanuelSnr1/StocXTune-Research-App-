
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import NewUser
from watchlists_api.models import UserWatchlist, WatchlistStocks
from rest_framework.test import APIClient


class WatchlistsTests(APITestCase):

    def test_view_watchlists(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('watchlists_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_watchlist(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.testuser1 = NewUser.objects.create_superuser(user_name='testuser1',
                                                         email = 'testuser1@example.com', first_name ='testuser1', password='123456789')
        
        self.testuser1.is_staff = True
        self.client.login(email=self.testuser1.username,
                          password='123456789')

        
        data = {
            "user":"new", "name":"testuser1","description":"testuser1"
        }
        
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_watchlist_update(self):

        client = APIClient()

        self.testuser1 = NewUser.objects.create_superuser(user_name='testuser1',
                                                         email = 'testuser1@example.com', first_name ='testuser1', password='123456789')
        self.testuser1 = NewUser.objects.create_superuser(user_name='testuser2',
                                                         email = 'testuser2@example.com', first_name ='testuser2', password='123456789')
                
        test_userwatchlist = UserWatchlist.objects.create(user_id = 1,name='test Watchlist',description='test Watchlist description')


        client.login(email=self.testuser1.email,
                     password='123456789')

        url = reverse(('watchlists_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "user": "New",
                "name": "test Watchlist",
                "description": "test Watchlist description ",
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)