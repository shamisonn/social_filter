#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from nyan import (
        yes_no_input,
        social_filter,
        )


class TestNyan(unittest.TestCase):
    @patch('builtins.input')
    def test_yes(self, input):
        answers = ['y', 'ye', 'yes', 'Yes', 'YES']
        input.side_effect = answers
        for _ in answers:
            self.assertTrue(yes_no_input(''))

    @patch('builtins.input')
    def test_no(self, input):
        answers = ['', 'n', 'no', 'NO']
        input.side_effect = answers
        for _ in answers:
            self.assertFalse(yes_no_input(''))

    def test_social_filter(self):
        translated_words = (
                ("ラーメンおいしい", "にゃんにゃ"),
                ("ブチ殺すぞハゲ", "にゃんにゃーんぞにゃん"),
                ("死んだ方が良い奴もいる", "にゃーんだにゃんがにゃにゃんもにゃーん"),
                )

        for origin, nyaned in translated_words:
            translated = social_filter(origin)
            self.assertEqual(nyaned, translated)
