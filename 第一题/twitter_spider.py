import snscrape.modules.twitter as st
import xlwt
import re
# 创建Excel文件
evmos_data = xlwt.Workbook(encoding='utf-8')
sheet = evmos_data.add_sheet('evmosdata')
sheet.write(0, 0, '时间')
sheet.write(0, 1, '文字内容及图片链接')
sheet.write(0, 2, '引用内容链接')
sheet.write(0, 3, '缩略图和图片链接')

# 爬取并装载数据
for i, tweet in enumerate(
        st.TwitterSearchScraper('from:optimismPBC').get_items()):
    sheet.write(i + 1, 0, str(tweet.date))
    sheet.write(i + 1, 1, tweet.content)
    sheet.write(i + 1, 2, str(tweet.quotedTweet))
    sheet.write(i + 1, 3, str(tweet.media))



# 保存文档
evmos_data.save(r"new.xls")
