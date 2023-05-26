import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Post


@pytest.fixture()
def user_fixture(db):
    return User.objects.create_user(username="arjun",password="arjun")


@pytest.mark.parametrize("title,content",[("Title","Content")])
def test_post(db,user_fixture,title,content):
    item=Post.objects.create(title=title,content=content,author=user_fixture)
    assert item.title == title

