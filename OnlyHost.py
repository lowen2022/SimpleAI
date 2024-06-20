import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 定义URL
url = 'https://www.amazon.com/dp/B0D4DCSLQH/ref=sr_1_2_sspa?currency=USD&dib=eyJ2IjoiMSJ9.JTcIO1IE91g-JlgkwKwFdGQ1m8k0NwT9vgVaEwtnfqq1m9NiPe9BFFWepyCHvW118I2oRnlSjwr8gkuTN-4Ig6hZKa0QwRgn5ulm36cB0N-ifHgmXbyJZWAf4STv9f346hnn8lVTRzma607u_Wdn3B291wNMN5S8q6LIQVS6U09bB27wez7IwwVeKwhryprNe6qT0radcCSPSC880YA7f9vFaqMAqJaK-Zskwt2myUXQjOZwxLFKe1MoHUcMwnUlZGMm3jg2pcMCRpX0E2_M1LfzxIz33sZDj9HceSm3qOg.GzQUXxM9tlhhYVOl8QmvqmaduALY5ompvkJrjuFOrUY&dib_tag=se&keywords=robot+vacuum+accessories&qid=1718778502&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
url='https://www.amazon.com/Lefant-M320-Robotic-Powerful-Self-Charging/dp/B0CR6HCH2B/ref=sr_1_3_sspa?c=ts&dib=eyJ2IjoiMSJ9.tcyU6D2IpMoV81Rrc64RJpngG77sTStc7AEw1UGLD8btN3IPoTNyoIvzC-VqLGa4EFHVzbmGEJRaWlk1xfCtZOaHtXChG82MCr_oegZy7acwmM0jwyaMKJP4n8CEKDAtWhTiQEE34IMrkdyd-mXtyUWnp-O5euPWloHsjWZlNLApFfxz4F9ZXojsWaDQ4bkbQhjv6-VfexUfJY2DKg55fdwsHPId5ti4y_VIWRcjTztl7qZVTSlsYlBNBWIYinN5SKGyNpZUENZ58-wm5dLRtR9HZz2sHxUovTAWVWEj1mA.i4Arz0VST3IL1uLJquQCiUGCG8dgJVMEA69238bcrwY&dib_tag=se&keywords=Robotic%2BVacuums&qid=1718777656&s=vacuums&sr=1-3-spons&ts_id=3743561&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'
url='https://www.amazon.com/Shark-%E8%B6%85%E8%AA%9E%E9%9F%B3%E6%8E%A7%E5%88%B6%E6%A9%9F%E5%99%A8%E4%BA%BA%E7%9C%9F%E7%A9%BA%E5%90%B8%E5%A1%B5%E5%99%A8%E6%90%AD%E9%85%8D%E7%9F%A9%E9%99%A3%E6%B8%85%E6%BD%94%E5%B0%8E%E8%88%AA-%E5%AE%B6%E5%BA%AD%E5%9C%B0%E5%9C%96-%E8%87%AA%E7%A9%BA%E5%BA%95%E5%BA%A7-%E9%81%A9%E7%94%A8%E6%96%BC%E5%B8%B6%E5%AF%B5%E7%89%A9%E7%9A%84%E5%AE%B6%E5%BA%AD%E3%80%81%E5%9C%B0%E6%AF%AF%E5%92%8C%E7%A1%AC%E5%9C%B0%E6%9D%BF/dp/B09T4YZGQR/ref=sr_1_5?c=ts&dib=eyJ2IjoiMSJ9.h1stBvTlPpq7FwiawTUl0uvILbJ6Zm5KQ40jnf4hlC2CkPO-v0nABL9QgZKKyWpaxPh7jce0EOP6Ue0M9fdEghCxtPKwEezM3KdzveElFBpq0bEYhJx0Y_Zxdcf4u2_gLpyj4MipvXf859LrM5P5vxQc8giBmT0knLaxKfSxoz1zZTWSQbXeArQj-Pg0f2BZCPm00vReg2ElTGJuRVGW74GakDBZ62HXg-w29JU5J33yIFCJHfiFXAM6CgphOaw_-MZBiKWs3JGmp8pMEz_Xani94JcAYeCp3nf3lT_ycpw.atVIPw5i9DvxGfc06zV7p9NKxM0dLr24GLbZ2A_4toE&dib_tag=se&keywords=%E6%8E%83%E5%9C%B0%E6%A9%9F%E5%99%A8%E4%BA%BA&qid=1718910069&s=vacuums&sr=1-5&ts_id=3743561&th=1'
#url='https://www.amazon.com/dp/B0D4DCSLQH/ref=sr_1_2_sspa?currency=USD&dib=eyJ2IjoiMSJ9.JTcIO1IE91g-JlgkwKwFdGQ1m8k0NwT9vgVaEwtnfqq1m9NiPe9BFFWepyCHvW118I2oRnlSjwr8gkuTN-4Ig6hZKa0QwRgn5ulm36cB0N-ifHgmXbyJZWAf4STv9f346hnn8lVTRzma607u_Wdn3B291wNMN5S8q6LIQVS6U09bB27wez7IwwVeKwhryprNe6qT0radcCSPSC880YA7f9vFaqMAqJaK-Zskwt2myUXQjOZwxLFKe1MoHUcMwnUlZGMm3jg2pcMCRpX0E2_M1LfzxIz33sZDj9HceSm3qOg.GzQUXxM9tlhhYVOl8QmvqmaduALY5ompvkJrjuFOrUY&dib_tag=se&keywords=robot+vacuum+accessories&qid=1718778502&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}


cookies = {'cookie_name': 'cookie_value'}

#response = requests.get(url, headers=headers)
response = requests.get(url, cookies=cookies)

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.text
print('页面标题:', title)


if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # 定位
    div_element = soup.find('div', id='prodDetails')

    # 提取
    if div_element:
        table_element = div_element.find('table', id='productDetails_detailBullets_sections1')

        if table_element:
            rows = table_element.find_all('tr')

            for row in rows:
                th_element = row.find('th', class_='a-color-secondary a-size-base prodDetSectionEntry')
                td_element = row.find('td', class_='a-size-base prodDetAttrValue')

                if th_element and td_element:
                    attribute = th_element.text.strip()
                    value = td_element.text.strip()
                    
                    print(f"{attribute}: {value}")
        else:
            print("未找到目标表格")
    else:
        print("未找到目标元素")
else:
    print('请求失败，响应码:', response.status_code)
