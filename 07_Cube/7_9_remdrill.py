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

        print "Test Case: Excluding Drilldown"
        self.vc.findViewWithTextOrRaise(u'Sales Data - Departmental Stores_karuna_copy').touch()
        self.vc.sleep(8)

        self.device.longTouch(520.0, 110.0, 2000, 0)
        self.vc.sleep(5)

        self.device.dragDip((179.0, 377.0), (181.0, 113.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.device.longTouch(304.0, 648.0, 2000, 0)
        self.vc.sleep(5)

        self.vc.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        if (self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewCloseDrill")):
            print "Drilldown filter found..."
            self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewCloseDrill").touch()
            self.vc.sleep(_s)
            self.vc.dump(window=-1)

            #Check if Drilldown is closed
            if self.vc.findViewWithTextOrRaise(u'Add Comment'):
                print "Drilldown filter Closed!"
            else:
                print "Close Drilldown!"
        else:
            print "No filter found!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Back to Home"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewBackButton").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
