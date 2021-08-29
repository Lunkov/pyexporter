#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
from src.dirs import DirsExport

class TestDirExport(unittest.TestCase):

  def testDir(self):

    if os.path.exists("data/rsync/dir2/12345.txt"):
      os.remove("data/rsync/dir2/12345.txt")
    self.assertEqual(os.path.exists("data/rsync/dir2/12345.txt"), False)
    
    
    e = DirsExport({ 'rsync': { 'src': 'data/rsync/dir1/', 'dest': 'data/rsync/dir2/'} }, True)
    
    ok = e.run()
    self.assertEqual(ok, True)
    self.assertEqual(os.path.exists("data/rsync/dir2/12345.txt"), True)
    os.remove("data/rsync/dir2/12345.txt")
  
if __name__ == '__main__':
  unittest.main()
