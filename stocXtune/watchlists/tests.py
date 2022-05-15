# Create your tests here.
from django.test import TestCase
from watchlists_api.models import UserWatchlist
from users.models import NewUser
import datetime


class Test_Create_Userwatchlist(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        now = datetime.datetime(2022, 5, 15, 11, 27, 6, 546490)
        testuser1 = NewUser.objects.create_user(user_name='testuser1',email = 'testuser1@example.com', first_name ='testuser1', password='123456789')
        test_userwatchlist = UserWatchlist.objects.create(user_id = 1,name='test Watchlist',description='test Watchlist description')
        
    def test_blog_content(self):
        now1 = datetime.datetime(2022, 5, 15, 11, 27, 6, 546490)
        userwatchlist = UserWatchlist.objects.get(id=1)
        user = f'{userwatchlist.user}'
        name = f'{userwatchlist.name}'
        description = f'{userwatchlist.description}'
        created_at = f'{userwatchlist.created_at}'
        self.assertEqual(user,'testuser1')
        self.assertEqual(name, 'test Watchlist')
        self.assertEqual(description, 'test Watchlist description')
        
        
        