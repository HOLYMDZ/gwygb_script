import requests
import re
import os
import time
import wget
request_header = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
}

dir = r"/home/thinkpad/文档/中华人民共和国国务院公报/"

gwygb_url = "http://www.gov.cn/ziliao/fgwj/gwygb/lsgb.htm"

page_header = r"http://www.gov.cn"
url_head_pattern = r"""<td height="25"><a href="../../.."""
url_tail_pattern = r"""" target="_blank" class="blue14">"""

folder_head_pattern = r"""<font color="#2A2A2A">"""
folder_tail_pattern = r"</font>"

file_head_pattern = """title=\""""
file_tail_pattern = r"）"


url_content = requests.get(gwygb_url, headers=request_header)
url_content.encoding = "utf-8"
url_content = url_content.text
url_result = re.findall(url_head_pattern + r"(.*?)" + url_tail_pattern, url_content)
folder_result = re.findall(folder_head_pattern + r"(.*?)" + folder_tail_pattern, url_content)
if not os.path.exists(dir):
    os.mkdir(dir)
for i in range(0, len(url_result)):
    print("\n" + folder_result[i])
    time.sleep(5)
    page_content = requests.get(page_header + url_result[i], headers=request_header)
    page_content.encoding = "utf-8"
    page_content = page_content.text
    file_result = re.findall(file_head_pattern + r"(.*?)" + file_tail_pattern, page_content)
    os.mkdir(dir + folder_result[i] + "/")
    for line in file_result:
        pdf = line.split("\">")
        print("\n" + pdf[1] + "）")
        time.sleep(5)
        wget.download(pdf[0], dir + folder_result[i] + "/" + pdf[1] + "）.pdf")
