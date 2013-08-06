import os
import flaskr
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Before each test, set up a blank database"""
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def login(self,username,password):
        pass

    def test_empty_db(self):
        rv = self.app.get('/')
        assert "No entries " in rv.data


if __name__ == '__main__':
    unittest.main()
