import requests


class GitHub:
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
            )
        body = r.json()

        return body

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def get_user_following(self, username):
        r = requests.get(f'https://api.github.com/users/{username}/following')
        body = r.json()

        return body

    def is_following(self, username, target_username):
        following = self.get_user_following(username)
        if following is None:
            return False
        return any(user['login'] == target_username for user in following)
