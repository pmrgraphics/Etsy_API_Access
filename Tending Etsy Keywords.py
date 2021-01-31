import requests
import json

import time as sleep

class Etsy:
    def gettrendingresponse(self, limit, offset):
        params = {'limit': limit, 'offset': offset}
        r = requests.get('https://openapi.etsy.com/v2/listings/trending?api_key=yb9gwm6403ugxhgfmlknav41', params = params)
        #print "Response Code:", r.status_code
        iterkeywords = []
        keywords = json.loads(r.text)
        for item in keywords['results']:
            #print "Title of listing", item['title']
            if 'tags' in item:
                for mytags in item['tags']:
                    #make lowercase and add to keywords list
                    iterkeywords.append(mytags.lower())
        return iterkeywords
class Words:
    def killunicode(self, iw):
        #change unicode to ASCII. also .encode("ascii", "ignore") is to force removal of
        #of the BOM unicode stuff.
        wordlist = []
        wordlist = [str(unicodes.encode("ascii", "ignore")) for unicodes in iw]
        return wordlist
    def printdict(self, wl):
        #count phrase freq
        wordfreq = [wl.count(p) for p in wl]
        #make the finished dict to print from
        mydict = dict(zip(wl,wordfreq))
        #make our list

        for key, value in (mydict.items()):
            if value > 1:

             print(key, "Freq", value)

        # for key, value in (mydict.items(), key=lambda (k,v): (v,k), reverse=True):
        #     if value <= 1:
        #         pass
        #     else:
        #         print (key, "Freq", value)
if __name__ == '__main__':
    keywords = Etsy()
    ourwords = Words()

    limit = 250
    offset = [0, 250]
    user_data= []
    for number in offset:
        ourkeywords = keywords.gettrendingresponse(limit, number)
        cleanwords = ourwords.killunicode(ourkeywords)

    ourwords.printdict(cleanwords)





