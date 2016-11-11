# -*- coding: utf-8 -*-
__author__ = 'shamison'

from twitter import *
import configparser
import os
import sys
import re

import MeCab

# config.iniから読み込み. consumer_keyとかを諸々書いておく
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
oauth_config = config['oauth']

# ツイートやらプロフィールを取ってくるため作成
tw = Twitter(
    auth=OAuth(
        oauth_config['token'],
        oauth_config['token_secret'],
        oauth_config['consumer'],
        oauth_config['consumer_secret']
    )    
)

def yes_no_input():
    yes = re.compile("^y(e|es)?$", flags=re.IGNORECASE)
    no = re.compile("^(no?)?$", flags=re.IGNORECASE)

    while True:
        choice = input("are you sure to tweet this? [y/N]: ")
        if yes.match(choice):
            return True
        elif no.match(choice):
            return False
        print("couldn't understand: %s" % choice)


def tweet(tweet_str):
    tw_str = social_filter(tweet_str)[0:120]
    print('TEXT: ' + tw_str)
    if yes_no_input():
        tw.statuses.update(status= tw_str+ ' #social_filter')

                                    
def social_filter(input_str):
    mt = MeCab.Tagger('mecabrc')
    texts_info = list(map(lambda t: t.split("\t"),
                     mt.parse(input_str).split("\n")))
    text = []
    for t in texts_info:
        if t[0] == 'EOS':
            break
        if t[1].startswith('助詞') or \
           t[1].startswith('助動詞') or \
           t[1].startswith('記号') or \
           t[1].startswith('副詞'):
            text.append(t[0])
        elif t[1].startswith('名詞'):
            text.append("にゃん")
        elif t[1].startswith('形容詞'):
            text.append("にゃ")
        elif t[1].startswith('動詞'):
            text.append("にゃーん")
        else:
            text.append(t)        
    return ''.join(text)

    
tweet(sys.argv[1])
