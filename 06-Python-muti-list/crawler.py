## 完整程式碼（crawler.py）
# 三民書局暢銷總榜 → MariaDB
# 題目和提示見 README.md
# 執行前先設定帳密：
#   export DB_USER=crawler DB_PASS='crawler-db-2026' DB_NAME=crawler_course
# 執行：python crawler.py

import datetime
import os
import time
from urllib.robotparser import RobotFileParser

import mariadb
import requests
from bs4 import BeautifulSoup

URL = "https://www.sanmin.com.tw/promote/top"
HEADERS = {"User-Agent": "course-crawler/1.0 (Kelly Chen)"}

# 1. 先看 robots.txt 允不允許（提示 2）
#    把結果（True 或 False）存在 allowed
r = requests.get("https://www.sanmin.com.tw/robots.txt", headers=HEADERS, timeout=10)
robots = RobotFileParser()
robots.parse(r.text.splitlines())                       # 讀入 robots.txt 規則
allowed = robots.can_fetch(HEADERS["User-Agent"], URL)  # 判斷排行榜能不能抓
print("robots.txt 允許嗎？", allowed)

books = []
if allowed:
    time.sleep(1)

    # 2. 抓排行榜頁面
    r = requests.get(URL, headers=HEADERS, timeout=10)
    print("狀態碼：", r.status_code)

    # 3. 用 BeautifulSoup 找出每一本書（提示 3、4）
    soup = BeautifulSoup(r.text, "html.parser")
    rank = 0
    items = soup.select("div.sProduct")
    for item in items:
        rank = rank + 1
        title = item.select_one("h3").get_text(strip=True)
        author = item.select_one("span.Author").get_text(strip=True).replace("作者：", "")
        publisher = item.select_one("span.Publisher").get_text(strip=True).replace("出版社：", "")
        link = "https://www.sanmin.com.tw" + item.select_one("a")["href"]
        books.append([rank, title, author, publisher, link])

print("抓到", len(books), "本")

if len(books) > 0:
    # 4. 存進 MariaDB，同一天跑兩次不能重複（提示 5）
    conn = mariadb.connect(
        host="localhost",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        database=os.environ["DB_NAME"],
    )
    cur = conn.cursor()
    today = datetime.date.today()
    sql = ("INSERT INTO books (rank_date, rank_no, title, author, publisher, url) "
           "VALUES (?, ?, ?, ?, ?, ?) "
           "ON DUPLICATE KEY UPDATE title = VALUES(title), author = VALUES(author), "
           "publisher = VALUES(publisher), url = VALUES(url)")
    for rank, title, author, publisher, link in books:
        cur.execute(sql, (today, rank, title, author, publisher, link))
    conn.commit()
    print("已寫入資料庫：", today, len(books), "筆")

    # 5. 從資料庫查回來，印出共幾本、前 10 名（提示 6）
    cur.execute("SELECT COUNT(*) FROM books WHERE rank_date = ?", (today,))
    print("資料庫裡", today, "共", cur.fetchone()[0], "本")
    cur.execute("SELECT rank_no, title FROM books WHERE rank_date = ? ORDER BY rank_no LIMIT 10", (today,))
    for rank_no, title in cur.fetchall():
        print(rank_no, title)
    conn.close()

else:
    print("一本都沒抓到，不寫資料庫")
