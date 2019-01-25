
# 現在のディレクトリに画像を812枚生成

import requests
import re
from PIL import Image
import numpy as np
import urllib.request


URL = 'https://www.pokemon.jp'
pat1 = '/zukan/images/m/[0-9a-zA-Z]*.png'
pat2 = '[0-9a-zA-Z]*.png'


def get_HTML(url):
	html = requests.get(url)
	html.encoding = 'utf-8'
	html = html.text
	html = html.splitlines()
	return html


for ID in range(1,810):

	X = (str(ID)).zfill(3)
	html=get_HTML( 'https://www.pokemon.jp/zukan/detail/'+X+'.html' )


	for a in html:
		result = re.search(pat1,a)

		if result:
			A = re.findall(pat1,a)
			TAG = re.findall(pat2,A[0])

			print( TAG[0] )

			with open(TAG[0], mode="wb") as f:
				f.write( urllib.request.urlopen(URL+A[0]).read() )



	for i in range(100000):
		i = i #sleep

