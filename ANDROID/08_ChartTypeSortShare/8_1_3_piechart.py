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

        print "Test Case: Chart Type - Pie Chart"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/textViewCubeTitle").touch()
        self.vc.sleep(8)
        self.vc.dump(window=-1)

        self.vc.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Options Menu: "
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewChartCubeOptionsMenu").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.device.longTouch(516.0, 310.0, 2000, 0)
        self.vc.sleep(5)
        self.vc.dump(window=-1)

        print "Selected: Pie Chart"
        self.vc.findViewWithTextOrRaise(u'Pie chart', root=self.vc.findViewByIdOrRaise('id/no_id/8')).touch()
        print "Pie Chart is displayed!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Check for Pie Chart option disabled"
        self.vc.findViewWithTextOrRaise(u'Add Comment').touch()
        self.vc.sleep(5)
        self.vc.dump(window=-1)

        self.device.longTouch(410.0, 94.0, 2000, 0)
        self.vc.sleep(5)
        self.vc.dump(window=-1)

        self.device.dragDip((181.0, 375.0), (178.0, 102.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.device.longTouch(222.0, 300.0, 2000, 0)
        self.vc.sleep(5)
        self.vc.dump(window=-1)

        self.vc.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Check for negative axis value & pie chart option
        self.device.touch(252.0, 790.0, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        val = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/textViewAxis2Value").text()

        new_val = re.search('-',val)
        if new_val:
            print "Negative axis value found!"
            self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewChartCubeOptionsMenu").touch()
            self.vc.sleep(_s)
            self.vc.dump(window=-1)

            self.device.longTouch(516.0, 310.0, 2000, 0)
            self.vc.sleep(5)
            self.vc.dump(window=-1)

            print "Selected: Pie Chart"
            if not self.vc.findViewWithTextOrRaise(u'Pie chart').clickable():
                print "Passed! Pie Chart is disabled!"
                self.vc.device.press('KEYCODE_BACK')
            else:
                print "Failed! Pie Chart is not disabled!"
            self.vc.sleep(_s)
            self.vc.dump(window=-1)
        else:
            "No negative axis value!"

        print "Back to Home"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewBackButton").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
