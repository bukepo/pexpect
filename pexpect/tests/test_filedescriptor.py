#!/usr/bin/env python
import pexpect
import unittest
import sys
import os

class ExpectTestCase(unittest.TestCase):

    def test_fd (self):

	fd = os.open ('README.txt', os.O_RDONLY)
	s = pexpect.spawn (fd)
	s.expect ('License:')
	s.expect (pexpect.EOF)
	assert s.before == ' Python Software Foundation License\n\nNoah Spurrier\nhttp://pexpect.sourceforge.net/\n\n\n'

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(ExpectTestCase, 'test')

#fout = open('delete_me_1','wb')
#fout.write(the_old_way)
#fout.close
#fout = open('delete_me_2', 'wb')
#fout.write(the_new_way)
#fout.close
