#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
from pyfunctest.fmods import FMods
from src.exporter import Exporter

class TestExporter(unittest.TestCase):

  def testExporter(self):
    # Prepare Tests
    if os.path.exists("data/rsync/dir2/12345.txt"):
      os.remove("data/rsync/dir2/12345.txt")
    self.assertEqual(os.path.exists("data/rsync/dir2/12345.txt"), False)

    # Run PostgreSQL
    fm = FMods("data/mods/", "data/tmp/", True)
    fm.scan()
    srvPg = fm.newDocker('pg')
    self.assertTrue(srvPg.run())
    # Migration
    mgPg = fm.newMigrate('pg')
    self.assertTrue(mgPg.run())

    
    # Load settings for export
    exp = Exporter('data/etc', '', True)
    exp.scan()
    self.assertEqual(exp.count(), 1)
    
    # Export News
    self.assertEqual(exp.run('news'), True)
    
    # Check data
    pg = fm.newPostgre('pg')
    self.assertIsNotNone(pg.reconnect())
    
    res = pg.getData('select * from public.news')
    self.assertEqual(res, [(1, 'Title 1', 'anonymous', 'Article 1'),(2, 'Title 2', 'anonymous', 'Article 2'),(3, 'Title 3', 'author1', 'Article 3'),(4, 'Title 4', 'author2', 'Article 4')])

    self.assertEqual(os.path.exists("data/rsync/dir2/12345.txt"), True)
    os.remove("data/rsync/dir2/12345.txt")

  
if __name__ == '__main__':
  unittest.main()
