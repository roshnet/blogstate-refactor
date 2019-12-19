import os
import inspect
import requests


class SecureAgent(object):
    """Perform secure API calls for the application"""

    def __init__(self, envfile_name='.env'):
        this_module = inspect.getfile(inspect.currentframe())
        this_dir = os.path.dirname(this_module)
        envfile_path = os.path.join(this_dir, envfile_name)
        with open(envfile_path) as fp:
            self.HOST = fp.readline().rstrip("\n")
            self.KEY = fp.readline().rstrip("\n")

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
            :key title:         (str) Title of the post
            :key body:          (str) Body of the post
            :key preview_text:  (str) Preview text for the post

        :return:
            True, if post was successfully created.
            False, otherwise.
        """
        status = self.secure_post('posts/new', fields)
        if status['status'] == 'pass':
            return True
        return False

    def fetch_user_info(self, username, params={}):
        endpoint = 'users/{}'.format(username)
        info = self.secure_get(endpoint)
        if info['status'] == 'pass':
            return info['result']
        return False

    def fetch_posts_by_author(self, username, params={}):
        endpoint = 'posts/{}'.format(username)
        posts = self.secure_get(endpoint)
        if posts['status'] == 'pass':
            return posts['result']

    def fetch_post_by_id(self, username, post_url):
        endpoint = 'posts/{}/{}'.format(username, post_url)
        post = self.secure_get(endpoint)
        if post['status'] == 'pass':
            return post['result']
        return False

    def fetch_post_titles(self, username):
        endpoint = 'posts/titles/{}'.format(username)
        titles = self.secure_get(endpoint)
        if titles['status'] == 'pass':
            return titles['result']
        return False
