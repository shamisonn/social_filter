#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'shamison, matsub'

import configparser
import os
import sys
import re

import MeCab

import twitter

# config.iniから読み込み. consumer_keyとかを諸々書いておく
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
oauth_config = config['oauth']
words_config = config['words']

# ツイートやらプロフィールを取ってくるため作成
tw = twitter.Api(
    consumer_key=oauth_config['consumer'],
    consumer_secret=oauth_config['consumer_secret'],
    access_token_key=oauth_config['token'],
    access_token_secret=oauth_config['token_secret'])


def yes_no_input(msg):
    yes = re.compile("^y(e|es)?$", flags=re.IGNORECASE)
    no = re.compile("^(no?)?$", flags=re.IGNORECASE)
    
    while True:
        choice = input(msg + " [y/N]: ")
        if yes.match(choice):
            return True
        elif no.match(choice):
            return False
        else:
            print("couldn't understand: %s" % choice)


def tweet(tweet_str):
    tw_str = social_filter(tweet_str)[:120]
    print('TEXT:', tw_str)
    if yes_no_input("Are you sure to tweet this?"):
        tw.PostUpdate(tw_str+' #social_filter')


def convert(text_info):
    noun = re.compile("^名詞")
    adj = re.compile("^形容詞")
    verb = re.compile("^動詞")

    for t in text_info:
        if t[0] == 'EOS':
            break

        if noun.match(t[1]):
            yield words_config['noun']
        elif adj.match(t[1]):
            yield words_config['adjective']
        elif verb.match(t[1]):
            yield words_config['verb']
        else:
            yield t[0]


def social_filter(input_str):
    mt = MeCab.Tagger('mecabrc')
    text_info = map(lambda t: t.split("\t"),
                    mt.parse(input_str).split("\n"))    
    return ''.join(convert(text_info))


def interactive():
    print("-- interactive mode --")
    while yes_no_input("Would you like to tweet?"):
        raw_tweet = input("tweet > ")
        tweet(raw_tweet)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        tweet(sys.argv[1])
    else:
        interactive()
