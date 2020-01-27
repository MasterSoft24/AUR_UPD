import unittest
from unittest.mock import Mock
from aur_upd import aur_updater
import os
import json


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # os.mkdir("./testdir")
        self.aur = aur_updater.aur_updater(False)

    def tearDown(self):
        # os.rmdir("./testdir")
        pass

    def test_get_package_current_version(self):
        mock = Mock()

        self.aur.exec_req_to_aur_api_info = mock

        mock.return_value = json.loads("{}")
        result = self.aur.get_package_current_version("")
        self.assertEqual(result, None)

        mock.return_value = json.loads('{"resultcount":0}')
        result = self.aur.get_package_current_version("")
        self.assertEqual(result, None)

        mock.return_value = json.loads('{"resultcount":1, "results":[{"Version":"1.2.3.4"}]}')
        result = self.aur.get_package_current_version("")
        self.assertEqual(result, "1.2.3.4")

    def test_get_updates_list(self):
        mock = Mock()
        self.aur.get_aur_packages = mock

        # pl = self.aur.get_aur_packages()

        mock.return_value = ['abtransfers 0.0.5.0-2', 'alice 2.4.3-1', 'amd-adl-sdk 9.0-1']
        pl = self.aur.get_updates_list()
        self.assertEqual(pl, [])

        mock.return_value = ['abtransfers 0.0.5.0-1', 'alice 2.4.3-1', 'amd-adl-sdk 9.0-1']
        pl = self.aur.get_updates_list()
        self.assertEqual(pl, ['abtransfers'])
        pass


if __name__ == '__main__':
    unittest.main()
