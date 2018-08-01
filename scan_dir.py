# 导入urllib和threading模块
import urllib.request
import threading

threads         = 5     # 定义线程数为5
target_url      = "http://localhost:8101"       # 目标网址
wordlist_file   = "asp.txt"     # 自己的字典文件
user_agent      = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"       # 模拟浏览器的http头
word_list       = []

# 将文件中的路径读入定义的word_list字典中
def build_list(wordlist_file):

    #读入字典文件
    fd = open(wordlist_file,'r')
    raw_words = fd.readlines()
    fd.close()

    for word in raw_words:
        word = word.rstrip()
        if word:
            word_list.append(word)
        else:
            pass

# 将目标网址加上读入的文件目录组合成完整路径进行访问，根据状态码来判断网站的文件是否存在
def dir_bruter(word_list):
    for dir in word_list:
        url = target_url + dir
        try:
            headers = {}
            headers['User-Agent'] = user_agent
            request = urllib.request.Request(url,headers=headers)
            response = urllib.request.urlopen(request)
            if response.code != 404:        # 如果返回的状态码不是404，则返回状态码和对应网址
                print("[%d] => %s" % (response.code,url))
        except:
            pass

# 将文件目录读入字典
build_list(wordlist_file)

# 根据设置的线程数来开启线程
for i in range(threads):
    t = threading.Thread(target=dir_bruter(word_list))
    t.start()


