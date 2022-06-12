from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    random_text = 'anything random'

    def setUp(self):
        Post.objects.create(text=PostModelTest.random_text)

    def test_post_content(self):
        post = Post.objects.get(pk=1)

        self.assertEqual(f'{post.text}', PostModelTest.random_text)


class EmptyHomePageViewTest(TestCase):
    def test_empty_homepage(self):
        response = self.client.get(reverse('posts:homepage'))

        self.assertTemplateUsed(response, 'posts/post_list.html')
        self.assertContains(response, text='No messages yet', status_code=200)


class HomePageViewTest(TestCase):
    post_texts = ['salman', 'farooq', '3310', 'anything']

    def setUp(self):
        for text in HomePageViewTest.post_texts:
            Post.objects.create(text=text)

    def test_homepage_contains_posts(self):
        response = self.client.get(reverse('posts:homepage'))

        for text in HomePageViewTest.post_texts:
            self.assertContains(response, text=text, status_code=200)
