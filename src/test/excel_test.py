#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
from src.xls import ExcelExport

class TestExcelExport(unittest.TestCase):

  def testXLSBad(self):
    e = ExcelExport({'excel' :{ 'sheet': 'posts', 'filename': 'data/www-dg/e-library/posts.xlsx', 'row_title': 0, 'row_data': 2, 'fields': ['id111', '111title'] }}, True)
    data, ok = e.run()
    self.assertEqual(ok, False)

    e = ExcelExport({'excel' :{ 'sheet': 'posts', 'filename': 'data/news/posts.xlsx', 'row_title': 0, 'row_data': 2, 'fields': ['id111', '111title'] }}, True)
    data, ok = e.run()
    self.assertEqual(ok, False)
    self.assertEqual(data, [])
    self.assertEqual(e.getColumns(), {})

    e = ExcelExport({'excel' :{ 'sheet': 'posts', 'filename': 'data/news/posts.xlsx', 'row_title': 0, 'row_data': 2}}, True)
    data, ok = e.run()
    self.assertEqual(ok, True)
    self.assertEqual(e.getColumns(), {'0': 'id', '1': 'author', '2': 'public_at', '3': 'article', '4': 'name', '5': 'main_image', '6': 'images'})

  def testXLS(self):

    e = ExcelExport({'excel' :{ 'sheet': 'posts', 'filename': 'data/news/posts.xlsx', 'row_title': 0, 'row_data': 1, 'fields': ['id', 'name', 'images'] }}, True)
    data, ok = e.run()
    self.assertEqual(ok, True)
    self.assertEqual(data, [{'id': 1, 'name': 'Title 1', 'images': "data/news/images/n-01.jpg\ndata/news/images/n-02.jpg"},{'id': 2, 'name': 'Title 2', 'images': 'data/news/images/n-02.jpg'},{'id': 3, 'images': '', 'name': 'Title 3'},{'id': 4, 'images': '', 'name': 'Title 4'}])
  
if __name__ == '__main__':
  unittest.main()
