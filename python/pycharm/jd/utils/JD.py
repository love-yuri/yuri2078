'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-27 22:02:48
LastEditTime: 2024-06-11 11:39:46
Description: jd-Utils
'''
import json
import pathlib
import sys
from collections import Counter
from datetime import datetime

import requests
import time
import csv
import numpy as np

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication

from utils.yuri_util import info, Utils, error


class Comment:
  def __init__(self, creationTime, content: str, productColor, productSize, location, nickname, **kwargs):
    self.creationTime = creationTime
    self.content = content.replace('\n', '')
    self.productColor = productColor
    self.productSize = productSize
    self.location = location
    self.nickname = nickname
  
  def __str__(self) -> str:
    return f'评论: {self.content}'


class GlobalConfig(object):
  def __init__(self, page: int, productId: int, pageSize: int, **kwargs):
    self.page = page
    self.productId = productId
    self.pageSize = pageSize


class JD(QThread):
  update = Signal(int)
  baseUrl = 'https://api.m.jd.com/'
  isAlive = True
  
  params = {
    'appid': 'item-v3',
    'functionId': 'pc_club_productPageComments',
    "productId": 100107613740,
    "score": 0,
    "sortType": 5,
    "page": 0,
    "pageSize": 30,
    "isShadowSku": 0,
    "fold": 1,
  }
  
  headers = {
    'Cookie': 'unpl=JF8EAJ5nNSttCBgBBUwKGRJAHl4BWwpdHERXZmRVUAoLSlANSQQaQBZ7XlVdWBRKEx9sYBRUX1NJVA4eCysSEHtdVV9eDkIQAmthNWRVUCVXSBtsGHwQBhAZbl4IexcCX2cDVFpeSlQBGgocGxhMXlFYWAtIFApfZjVUW2h7ZAQrAysTIAAzVRNdDksQBW5nAVVVX0JcAhgHHRcTSF5dblw4SA; __jdv=76161171|direct|-|none|-|1716701510349; __jdu=1716701509689624742228; areaId=12; shshshfpa=0fbfd44f-cd8e-e4f4-5590-972efb0f6563-1716701512; shshshfpx=0fbfd44f-cd8e-e4f4-5590-972efb0f6563-1716701512; 3AB9D23F7A4B3CSS=jdd03RE3PS5F6QUA6ROBNLBQAXU2I6BRF5G7YL3R2EP3CW2H6F6AJJJZZXLF3OXOC3NZYG5LJFKQX35NCJ4E5MFEAHGYWBAAAAAMPWNV6TEQAAAAAC5QSCSLQSAVRHAX; _gia_d=1; TrackID=1DS74aEwojsDZDs7qeBXylVSRft4QQyJPoMumWmrckYWnYGU3BYlFRt-7JYFOJZeKY8KqSVuVrJZLbCs8FdmcAYrOgCoyqxvxUOux9YK_y18; thor=25CBE492AC2D37C47722F98CCDCCD87E42172A720CA66B182EA1EA005DA8E5F7E143A04CB26B490452B87A4595018D80F783E0DA562D8590783B951F2BAA6D2AF9C2313FE0B8930411E92B3E8182B207C42E1AE6395EEE00875FC7809EE8A45ED3A1B308D16FC4DBF9741028973C7EAC0BFCD892170E36B957C305EC877A780DAF94035486D323C13306F8B319673028; pinId=45Wtd6d6lNaxuL8Wc0tgzw; pin=wdFpxtjMnQHTBj; unick=%E8%B7%AF%E8%BF%87%E7%9A%84%E6%99%93%E7%BE%8E%E7%84%B0; ceshi3.com=103; _tp=rEisCL2gKHaJ%2FjgWRSKvvw%3D%3D; _pst=wdFpxtjMnQHTBj; jsavif=1; 3AB9D23F7A4B3C9B=RE3PS5F6QUA6ROBNLBQAXU2I6BRF5G7YL3R2EP3CW2H6F6AJJJZZXLF3OXOC3NZYG5LJFKQX35NCJ4E5MFEAHGYWBA; token=f17b5cc295dbbd568e21f32397856b0e,3,953723; __tk=mDVvZnK0lAmlpLThonzLjCZfZBTlmmVPmczTZKTmnMTkjmZgmKmKZbVflBVnYmKUmKmkZmrT,3,953723; __jda=181111935.1716701509689624742228.1716701509.1716701509.1716701510.1; __jdb=181111935.12.1716701509689624742228|1.1716701510; __jdc=181111935; flash=2_n_5OWKvXD61_YgAmWp7M03_mhqzCG6BWLpshy7phFUFLfZO_gx2axtE2FTZjJI53WgkCrLemKkVWlaYPazhoQu3zTAYa1m-5xCqR6ovnFh91tG3zNz4op__BT_3RPBEq8N6P3Pqhkas3rLtiXnJoRqdbnkxV4j1zznD_xCnP07q*; ipLoc-djd=12-988-993-58088; shshshfpb=BApXc5mBksOpASXpfP8kKQOdZ_llAydS5BlQxEj1o9xJ1MvHyT4C2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  }
  
  def __init__(self, basePath: str):
    super().__init__()
    
    self.comment = []
    self.basePath = basePath
    self.loadComment()
    # 加载配置文件
    self.config: GlobalConfig = Utils.LoadConfig(f'{basePath}/config.json', GlobalConfig)
  
  def run(self):
    while self.isAlive:
      comments = self.getcomment()
      if comments is None or len(comments) == 0:
        break
      self.comment.extend(comments)
      self.config.page += 1
      self.update.emit(len(self.comment))
      time.sleep(1)
    else:
      info() << "正在保存评论..."
      self.saveComment()
      Utils.SetConfig(f'{self.basePath}/config.json', self.config)
  
  def getcomment(self):
    # 发送请求获取评论数据
    try:
      comments: list = []
      self.params['page'] = self.config.page
      self.params['productId'] = self.config.productId
      self.params['pageSize'] = self.config.pageSize
      response = requests.get(self.baseUrl, params=self.params, headers=self.headers)
      if response.status_code == 200:
        if response.text is None or response.text == "":
          return []
        info() << response.text
        for comment in response.json()['comments']:
          comments.append(Comment(**comment))
      else:
        error() << "请求发送失败 -> " << response.status_code
        return []
      info() << f"一共读取到了{len(comments)}条评论"
      return comments
    except requests.exceptions.RequestException as e:
      error() << "请求发送异常 -> " << e
      return []
  
  def TimelineChart(self):
    times = []
    for item in self.comment:
      item: Comment
      data = datetime.strptime(item.creationTime, '%Y-%m-%d %H:%M:%S')
      times.append(data.day)
    counter = Counter(times)
    counter = dict(sorted(counter.items()))
    return counter.keys(), counter.values()
  
  def ProductColorChart(self):
    colors = []
    for item in self.comment:
      item: Comment
      colors.append(item.productColor)
    counter = Counter(colors)
    return counter.keys(), counter.values()
  
  def ProductSizeChart(self):
    colors = []
    for item in self.comment:
      item: Comment
      colors.append(item.productSize)
    counter = Counter(colors)
    return counter.keys(), counter.values()
  
  def LocationChart(self):
    locations = []
    for item in self.comment:
      item: Comment
      locations.append(item.location)
    counter = Counter(locations)
    return counter.keys(), counter.values()
  
  def saveComment(self, path=None):
    fieldnames = ['nickname', 'creationTime', 'content', 'productSize', 'productColor', 'location']
    if path is None:
      path = pathlib.Path(f'{self.basePath}/csv')
      if not path.exists():
        path.mkdir()
      path = path.joinpath(f'comment.csv')
    with open(path, 'w', encoding='utf-8', newline='') as f:
      writer = csv.DictWriter(f, fieldnames=fieldnames)
      writer.writeheader()
      for comment in self.comment:
        writer.writerow({
          'nickname': comment.nickname,
          'creationTime': comment.creationTime,
          'content': comment.content,
          'productSize': comment.productSize,
          'productColor': comment.productColor,
          'location': comment.location
        })
  
  def loadComment(self):
    try:
      with open(f'{self.basePath}/csv/comment.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
          row: dict
          com = Comment(**row)
          self.comment.append(com)
    except FileNotFoundError:
      pass
