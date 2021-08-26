#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
from src.dirs import DirsExport
from src.xls import ExcelExport
from src.postgre import Postgre

class TestExcel2DBExport(unittest.TestCase):

  def testXLS2DB(self):

    e = ExcelExport({ 'sheet': 'posts', 'filename': 'data/news/posts.xlsx', 'row_title': 0, 'row_data': 1, 'fields': ['id', 'name'] }, True)
    data, ok = e.run()
    self.assertEqual(ok, True)
    self.assertEqual(e.getColumns(), {'0': 'id', '4': 'name'})
    
    pg = Postgre({'name': 'test-db', 'port': 17432, 'user': 'user', 'password': 'pwd', 'table': 'news', 'unique_field': 'id', 'fields': {'id': {'type':'int'}} }, True)

    sql = pg.makeSQLIU('news', 'id', e.getColumns(), {'id': 'id', 'name': 'name'}, data[0])
    self.assertEqual(sql, "INSERT INTO news (id,name) VALUES (1,'Title 1') ON CONFLICT (id) DO UPDATE SET id=1,name='Title 1';")
    
    self.assertIsNotNone(pg.reconnect())
    cnt = pg.insertData(e.getColumns(), data)
    self.assertEqual(cnt, 4)

  
if __name__ == '__main__':
  unittest.main()
