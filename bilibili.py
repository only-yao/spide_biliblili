import requests
import time
from concurrent import futures
import bilibili_sql

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

total = 0
result = []


def spider_bili(url):
    global total
    try:
        req = requests.get(url, headers=headers).json()
        data = req["result"]
        time.sleep(1)
        for anime in data:
            if "rating" in anime:
                video = (
                    anime["rating"]["count"],  # 番剧评论
                    int(anime["rating"]["score"] * 10),  # 评分
                    anime["season_id"],  # id
                    anime["stat"]["danmaku"],  # 弹幕数
                    anime["stat"]["follow"],   # 追番人数
                    anime["stat"]["view"],     # 播放数
                    anime["title"],  # 视频名称
                       )
            else:
                video = (
                    0,                          # 番剧评论
                    0,                          # 评分
                    anime["season_id"],  # id
                    anime["stat"]["danmaku"],   # 弹幕数
                    anime["stat"]["follow"],    # 追番人数】
                    anime["stat"]["view"],  # 播放数
                    anime["title"],  # 视频名称
                )
            result.append(video)
            total += 1
    except:
        pass


if __name__ == "__main__":
    # bilibili_sql.create_db()
    print("启动爬虫，开始爬取数据")
    for i in range(1, 60):
        s = i*200
        urls = [
                'https://api.bilibili.com/pgc/web/recommend/related/recommend?season_id={}'.format(j)
                for j in range(s-200, s)
               ]
        with futures.ThreadPoolExecutor(8) as executor:
                executor.map(spider_bili, urls)
        bilibili_sql.save_db(result)
    print("爬虫结束，共为您爬取到 {} 条数据".format(total))
    bilibili_sql.cursor.close()
    bilibili_sql.conn.close()

