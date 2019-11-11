from dotenv import load_dotenv
import os
import requests


class SecureAgent(object):
    """Perform secure API calls for the application"""

    load_dotenv()
    HOST = os.getenv('API_HOST')
    KEY = os.getenv('API_KEY')

    @classmethod
    def secure_get(self, endpoint, params={}):
        """
        Performs GET calls to API with auth-header specified.

        :param endpoint:    The endpoint to call
        :param params:      (optional) <dict> for GET body

        :return:            <dict> of response JSON
        """
        URL = os.path.join(self.HOST, endpoint)
        return requests.get(URL,
                            json=params,
                            headers={
                               "Authorization": self.KEY
                            }).json()

    @classmethod
    def secure_post(self, endpoint, params):
        """
        Performs POST calls to API with auth-header specified.

        :param endpoint:    The endpoint to call
        :param params:      <dict> for POST body

        :return:            <dict> of response JSON
        """
        URL = os.path.join(self.HOST, endpoint)
        return requests.post(URL,
                             json=params,
                             headers={
                                "Authorization": self.KEY
                             }).json()

    def login(self, creds):
        """
        Create a login attempt.

        :param username:    Username
        :param passwd:      Password

        :return:
            JSON response <dict>, if credentials match.
            False, otherwise.
        """
        # TODO: Validate structure of `creds`

        status = self.secure_post('login', creds)
        # CAUTION: Do not use "/login" as argument for `secure_post()`,
        # as `os.path.join` discards host name in presence of '/'.
        if status['status'] == "pass":
            return status
        return False

    def signup(self, fields):
        """
        Create a new user with specified details.
        :param fields:      A dict containing fields as follows:
            :key username:    (str) Username
            :key passwd:      (str) Password
            :key email:       (str) Email Address
            :key name:        (str) Full Name

        :return:
            JSON response <dict>, if user was created successfully.
            False, otherwise.
        """
        # TODO: Validate structure of incoming fields.

        status = self.secure_post('signup', fields)
        if status['status'] == 'pass':
            return status
        return False

    def publish(self, fields):
        """
        Create an entry in the posts' table with the information supplied.

        :param fields:          A dict containing fields as follows:
            :key author_uid:    (int) user_id
            :key title:         (str) Post Title
            :key body:          (str) Post Body

        :return:
            True, if post was successfully created.
            False, otherwise.
        """
        status = self.secure_post('posts/new', fields)
        if status['status'] == 'pass':
            return True
        return False

    def fetch_info(self, username, params={}):
        endpoint = 'fetch/{}'.format(username)
        info = self.secure_get(endpoint)
        if info['status'] == 'pass':
            return info['userinfo']
        return False

    def fetch_posts_by_author(self, username, params={}):
        endpoint = 'posts/{}'.format(username)
        posts = self.secure_get(endpoint)
        if posts['status'] == 'pass':
            return posts['posts']

    def fetch_post_by_id(self, username, post_url):
        endpoint = '{}/post/{}'.format(username, post_url)
        post = self.secure_get(endpoint)
        if post['status'] == 'pass':
            return post
        return False
