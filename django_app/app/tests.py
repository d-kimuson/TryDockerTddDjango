from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from unittest import TestCase, main
import os
import socket

base_url = 'http://{}:8000'.format(
    socket.gethostbyname(socket.gethostname())
)


class SampleTest(TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def tearDown(self) -> None:
        self.browser.quit()

    def test_user_story(self) -> None:
        # ユーザーがトップページにアクセスする
        self.browser.get(base_url + "/")

        # ページタイトルが Index であることを確認する
        self.assertEqual(
            'Index',
            self.browser.title,
            msg="Title is '{}'".format(self.browser.title)
        )


if __name__ == '__main__':
    main(warnings='ignore')
