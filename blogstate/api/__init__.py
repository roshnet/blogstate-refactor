from dotenv import load_dotenv
import os
import requests


class SecureAgent(object):
    """Perform secure API calls for the application"""

    load_dotenv()
    HOST = os.getenv('API_HOST')
    KEY = os.getenv('API_KEY')

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
            True, if credentials match.
            False, otherwise.
        """
        # TODO: Validate structure of `creds`

        status = self.secure_post('login', creds)
        # CAUTION: Do not use "/login" as argument for `secure_post()`,
        # as `os.path.join` discards host name in presence of '/'.
        if status['status'] == "pass":
            return True
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
            True, if user was created successfully.
            False, otherwise.
        """
        # TODO: Validate structure of incoming fields.

        status = self.secure_post('signup', fields)
        if status['status'] == 'pass':
            return True
        return False
