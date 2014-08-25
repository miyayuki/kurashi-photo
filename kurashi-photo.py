#!/usr/bin/env python
# -*- coding: utf-8 -*-                                                                              
import codecs
import datetime
import dateutil.parser
import os.path
import sys
import twitter
import urllib
import urllib2

#日付を取得
d = datetime.datetime.today()
y = d - datetime.timedelta(hours=25)
today = '%s-%s-%s' % (d.year, d.month, d.day)
yesterday = '%s-%s-%s' % (y.year, y.month, y.day)
print today, yesterday

# URLから画像をローカルに保存しファイル名を変更
img = urllib.urlopen("http://www.kurashi-no-techo.co.jp/images/daily/today.jpg")
localfile = open( os.path.basename(today), 'wb')
localfile.write(img.read())
todayImg = today+".jpg"
os.rename(os.path.basename(today),todayImg) 

img.close()
localfile.close()

sizeT = os.path.getsize(todayImg)
sizeY = os.path.getsize(yesterday+".jpg")
print sizeT
print sizeY

if sizeT == sizeY:
	print "SAME IMAGE "

api = twitter.Api(
consumer_key = '',
consumer_secret = '',
access_token_key = '',
access_token_secret = ''
)

post = u"今日の編集部です。　http://~~/"+todayImg
api.PostUpdate(status=post)