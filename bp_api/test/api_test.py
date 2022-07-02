import pytest

import main


class TestAPI:

    post_keys = {"poster_name", "poster_avatar", "pic", "content", "pk", "views_count", "likes_count"}

    @pytest.fixture
    def app_instance(self):
        app = main.app
        # app.config.from_pyfile("testing.py")
        test_client = app.test_client()
        return test_client

    def test_all_posts_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        # print(result.data)
        assert result.status_code == 200
        assert type(result.json) == list
        assert len(result.json) != 0

    def test_all_posts_keys(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        list_of_posts = result.get_json()

        for post in list_of_posts:
            assert post.keys() == self.post_keys, "Неправильные ключи у полученного словаря"

    def test_post_status(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200
        assert type(result.json) == dict
        assert len(result.json) != 0

    def test_post_status_404(self, app_instance):
        result = app_instance.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 404

    def test_post_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys

    @pytest.mark.parametrize("pk", [(1), (2), (3), (4)])
    def test_post_correct_data(self, app_instance, pk):
        result = app_instance.get(f"/api/posts/{pk}", follow_redirects=True)
        post = result.get_json()
        assert post["pk"] == pk, f"Неправильный pk при запуске поста {pk}"
