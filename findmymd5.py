#! -*-coding:utf-8 -*-

try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import hashlib
except ImportError as e:
    print("缺少必要库")


md5 = None


class HASHCRACK():

    name = "hashcrack"
    url = "http://hashcrack.com"

    def crack(self, hashValue):
        post = {'auth': '8272hgt',
                'hash': hashValue,
                'string': None,
                'Submit': 'Submit'}
        url = 'http://hashcrack.com/index.php'
        resonse = requests.post(url, data=post, timeout=3)
        html = resonse.text
        file = open('log.txt', 'w')
        file.write(html)
        file.close()
        soup = BeautifulSoup(html, 'lxml')
        # <span class=hervorheb2>123</span></div></TD>
        t = soup.find('span', attrs={'class': 'hervorheb2'})
        return t.string


def isSuccess(answer):
    m = hashlib.md5()
    md5s = m.update(answer).hedigest()
    if(md5s != md5):
        raise Exception


def main():
    ALLCRACK = [HASHCRACK]
    global md5
    md5 = '202cb962ac59075b964b07152d234b70'
    for i in range(len(ALLCRACK)):
        cracker = ALLCRACK[i]()
        print('%s is cracking.' % cracker.url, end='')
        try:
            answer = cracker.crack(hashValue=md5)
            isSuccess(answer)
            print(answer)
        except:
            pass


if __name__ == '__main__':
    main()
