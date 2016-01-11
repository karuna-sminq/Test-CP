#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C) 2013-2014  Diego Torres Milano
Created on 2015-12-11 by Culebra v11.0.4
                      __    __    __    __
                     /  \  /  \  /  \  /  \
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
'''


import re
import sys
import os


import unittest

from com.dtmilano.android.viewclient import ViewClient, CulebraTestCase

TAG = 'CULEBRA'


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.5, 'find-views-with-content-description': False, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'drop-shadow': False, 'output': 'testnotif.py', 'unit-test-method': None, 'interactive': False}
        cls.sleep = 5

    def setUp(self):
        super(CulebraTests, self).setUp()

    def tearDown(self):
        super(CulebraTests, self).tearDown()

    def preconditions(self):
        if not super(CulebraTests, self).preconditions():
            return False
        return True

    def testSomething(self):
        if not self.preconditions():
            self.fail('Preconditions failed')

        _s = CulebraTests.sleep
        _v = CulebraTests.verbose

        self.vc.dump(window=-1)

        print "Test Case: Adding a Comment"
        self.vc.findViewWithTextOrRaise(u'Sales Data - Departmental Stores_karuna_copy').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        ccount_before = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/textViewCommentCount").text()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.vc.findViewWithTextOrRaise(u'Write a comment...').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Check for Blank comment
        if self.vc.findViewWithTextOrRaise(u'Post').enabled():
            print " "
        else:
            self.vc.findViewWithTextOrRaise(u'Post').touch()
            print "Comment should not be blank! Post button is disabled!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.vc.findViewWithTextOrRaise(u'Write a comment...').setText("test1")
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Check for PostButton
        if self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/bt_add_comment").enabled():
            print "Posting a Comment"
            self.vc.findViewWithTextOrRaise(u'Post').touch()
            self.vc.sleep(_s)
            self.vc.dump(window=-1)

        ccount_after = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/textViewCommentCount").text()

        if ccount_after > ccount_before:
            print "New comment added!"
        else:
            print "No change in comment count!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Back to Home"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewBackButton").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
