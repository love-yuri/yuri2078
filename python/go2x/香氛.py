from os import name
import requests
import csv
import execjs
from bs4 import BeautifulSoup

class Skincare:
  def __init__(self):
    self.name = '' # 名字
    self.introduction = '' #简介
    self.describe = '' # 描述
    self.price = 0 # 价格
    self.label = '' # 标签
    self.category = '' # 分类
    self.img = '' # 图片url
    self.pageUrl = '' # 主页url
    self.spuCode = '' # spuCode

  

baseUrl = 'https://www.dior.cn/api/web/index.php?r=/api/kc/pc/home/getcms&url=%2Fmakeup%2Flips%2Fall-products&getPageType=1'

baseProdectUrl = 'https://www.dior.cn/zh_cn/beauty{}'
baseLabelUrl = 'https://www.dior.cn/api/web/index.php?r=/api/kc/pc/catalog/get-label-list'
urlList = [
  'https://www.dior.cn/api/web/index.php?r=/api/kc/pc/catalog/goods-list&url=%2Ffragrance%2Fmaison-christian-dior-perfumes%2Fall-products'
]
def getData():
  products = []
  for url in urlList:
    res = requests.get(url)
    if(res.status_code == 200) :
      content = res.json()['data']['page']['content']
      for item in content:
        try:
          for product in item['product']:
            try:
              categorys = product['categorys']
              sk = Skincare()
              sk.name = product['name']
              sk.introduction = product['subtitle']
              sk.price = product['price_content']
              sk.img = product['cover_pic']
              sk.noitematt = product['noitematt']
              sk.sku = product['sku']
              sk.pageUrl = baseProdectUrl.format(product['page_url'])
              sk.spuCode = product['spu_code']
              sk.category = '{}/{}/{}'.format(categorys['category_level_1_name'], categorys['category_level_2_name'], categorys['category_level_3_name'])
              getDescribe(sk)
              sk.label = getLabel(sk.spuCode).replace('<br/>', ' ')
              products.append(sk)
              print('{} 解析成功!'.format(sk.name))
            except Exception as e:
              print('{} 解析失败: {}'.format(product['name'], e.__str__()))
              products.append(sk)
        except:
          print('空商品 {}',format(item))
  return products

def getDescribe(sk: Skincare): 
  res = requests.get(sk.pageUrl)
  if(res.status_code == 200) :
    try:
      html = res.text
      soup = BeautifulSoup(html, 'html.parser')
      description_meta = soup.find("meta", {"property": "og:description"})
      sk.introduction = description_meta['content']
      scripts = soup.find('script')
      if scripts is not None:
        sc = scripts.text[scripts.text.index('=') + 1:]
        rest = execjs.eval(sc[0: len(sc) - 1])
        sk.describe = rest['data'][0]['res']['data']['product']['slide_detail_text'][0]['tag_value'][0]['children'][0]['children'][0]['children'][0]['value'].replace('<br/>', ' ')
    except:
      print('描述 解析异常 -> {}'.format(sk.name))

def getLabel(spu) -> str: 
  res = requests.post(baseLabelUrl, data= {
    'spu' : spu
  })
  if(res.status_code == 200) :
    try:
      data = res.json()['data']['labels']
      first_key = list(data.keys())[0]
      return ''.join(data[first_key][0]['label_list'])
    except Exception as e:
      print('解析异常 -> {}, data -> {}'.format(e.__str__, res.json()))
      return ''
  return ''

def writeCsv(fileName):
  fieldnames = ['name', 'sku', 'spuCode', 'introduction', 'noitematt', 'price', 'category', 'describe', 'label', 'img', 'pageUrl', 'nature']
  with open('csv/{}'.format(fileName), 'w', encoding='UTF8') as f:
    # create the csv writer
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    products = getData()
    for product in products:
      writer.writerow({ 
        'name': product.name, 
        'sku': product.sku,
        'spuCode': product.spuCode,
        'introduction': product.introduction, 
        'noitematt': product.noitematt,
        'price': product.price, 
        'category': product.category,
        'describe': product.describe, 
        'label': product.label, 
        'img': product.img,
        'pageUrl': product.pageUrl,
        'nature': f'\n> {product.name}产品信息\n产品名称: {product.name}\n产品SKU: {product.sku}\n产品SPU: {product.spuCode}\n产品简介: {product.introduction}\n产品规格: {product.noitematt}\n产品价格: {product.price}\n产品分类: {product.category}\n产品介绍: {product.describe}\n产品补充说明: {product.label}\n产品图片URL: {product.img}\n官方产品页面链接: {product.pageUrl}\n'
      })


if __name__ == '__main__' :
  writeCsv('香氛.csv')
