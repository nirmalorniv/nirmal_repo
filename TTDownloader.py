import requests as rq # to send http requests and get content from the webpage
from bs4 import BeautifulSoup # for web scraping of the unstructured html content that we get from request.get
import json # for json parsing

class TT: 

    def __init__(self,url):
        self.URL = url

    def ttvid_downloader(self):
        #if len(sys.argv) > 1:
         #   url = sys.argv[1]
       # else:
          #  sys.exit("Error: Please enter the Ted Talk URL")

        # collect the entire content of the website 
        res = rq.get(self.URL) # response returns lot of stuff like url, status code, content etc
        print("Starting the download")
        sts = res.status_code
        #print(sts) # confirming whether the requests was successful
        content = res.content
        #print(content)
        soup = BeautifulSoup(content,features='html5lib') # res.content returns the content of the request in binary. we can also use htmlparser in features
        nxt_data_script = soup.find(id="__NEXT_DATA__")
        json_strdata = nxt_data_script.string
        #print(json_strdata)
        json_obj = json.loads(json_strdata) # json_strdata is not a json object but a str object, so json,loads will convert it to a json obj
        playerData = json_obj["props"]["pageProps"]["videoData"]["playerData"]
        json_obj = json.loads(playerData)
        mp4_url = json_obj["resources"]["h264"][0]["file"]
        print(mp4_url)
        mp4_res = rq.get(mp4_url)
        #print(mp4_res.status_code)
        file_name = 'tedtalk_video1.mp4'
        with open(file_name,'wb') as f:
            if mp4_res.status_code == 200:
                f.write(mp4_res.content)
                print("file saved")
            else:
                print("failed saving")

if __name__ == "__main__":
    tt = TT("")
    tt.ttvid_downloader("")
