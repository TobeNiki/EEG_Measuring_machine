class Ambient2(object):
    def __init__(self,channelId, writeKey, *args):
        import requests
        self.requests = requests
        self.url = 'http://ambidata.io/api/v2/channels/' + str(channelId) + '/dataarray'
        self.channelId = channelId
        self.writeKey = writeKey
        if len(args) >= 2:
            self.userKey = args[1]
        if len(args) >= 1:
            self.readKey = args[0]

    def send(self,data,timeout=5.0):
        if isinstance(data, list):
            __d = data
        else:
            __d = [data]
        headers = {'Content-Type' : 'application/json'}
        r = self.requests.post(self.url, json = {'writeKey': self.writeKey, 'data': __d}, headers = headers, timeout = timeout)
        return r

if __name__ == "__main__":
    #timestamp wo kotiradeyoui
    import time
    import datetime
    datadict = {'created':str(datetime.datetime.now()),'d1': 0,'d2':2}
    
    poster = Ambient2(channelId=27393,writeKey="be92e5a413e04622")
    count = 0
    data = []
    while count <=20:
        time.sleep(1)
        print(str(datetime.datetime.now()))
        data.append({'created': str(datetime.datetime.now()), 'd1': 2.1, 'd2': 3.2})
        if count%5 == 0:  
            #poster.send(data)
            print(data)
            print("poster")
            data = []
        count += 1
        print(count)
    