from myselenium.fetch import keyWords
from myselenium.fetch import article
import random
from common import kvStore

title_limit = 10
image_limit = 4
txt_limit = 500


class Fetch():
    def __init__(self):
        super().__init__()

    def img_txt_count(self, s) -> (int, int, list):
        if '||' not in s:
            return 0, 0, []
        arr = s.split('||')
        t_count = 0
        i_count = 0
        res_arr = []
        for a in arr:
            if a.startswith("pp--"):
                t_count += len(a) - 4
                res_arr.append(a[4:])
            elif a.startswith("im--"):
                i_count += 1
                res_arr.append(a[4:])
        return (t_count, i_count, res_arr)

    def exist(self, md5) -> bool:
        v = kvStore.get(md5)
        if v != None:
            return True
        return False

    def check_article(self, dict) -> bool:

        print("check_article",type(dict), dict)
        if dict == None or "md5" not in dict:
            return False

        md5 = dict["md5"]
        if kvStore.get(md5) != None:
            return False
        title = dict["title"]
        if len(title) < title_limit:
            return False

        content = dict["content"]
        tc, ic, con = self.img_txt_count(content)
        if tc < txt_limit or ic < image_limit:
            return False

        return True

    def format_article(self, dict):

        v = self.img_txt_count(dict["content"])

        dict["content"] = v[2]

        return dict

    def fetch_article(self) -> dict:
        words = keyWords.fetch_keywords()
        index = random.randint(0, len(words)-1)
        word = words[index]

        dict = article.fetch_article_with_selector(query=word, func=self.check_article)

        kvStore.set(dict["md5"], "1")

        return dict
        # articles = article.fetch_article(word, None)
        #
        # for ar in articles:
        #     dict = ar.__dict__
        #
        #     md5 = dict["md5"]
        #     if kvStore.get(md5) != None :
        #         continue
        #     title = dict["title"]
        #     if len(title) < title_limit:
        #         continue
        #
        #     content = dict["content"]
        #     tc, ic, con = img_txt_count(content)
        #     if tc < txt_limit or ic < image_limit:
        #         continue
        #
        #     param = {}
        #     param["title"] = title
        #     param["content"] = con
        #     param["md5"] = dict["md5"]
        #     param["cover_image"] = dict["cover_image"]
        #
        #     kvStore.set(md5,"1")
        #
        #     return param