import requests as r

def getRequest(url, params = None):
    head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'zh-CN,zh;q=0.8', 'Cookie':None, 'Host':'www.jianpopo.com', 'Proxy-Connection':'keep-alive', 'Referer':'http://www.jianpopo.com/vehicle', 'Upgrade-Insecure-Requests':1, 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    proxy = {"http":"10.1.156.87:8080"}
    session = r.Session()
    rsp = session.get(url, headers = head, params = params, proxies = proxy)
    session.close()
    return(rsp.status_code, rsp.headers, rsp.text)

if __name__ == '__main__':
    raise Exception("Should not launch here.")
    '''parameters = {'series': '1%27'}
    res = getRequest("http://www.jianpopo.com/vehicle/advancedSearch.html", para=parameters)
    print res[0]
    print res[1]
    print res[2]'''
