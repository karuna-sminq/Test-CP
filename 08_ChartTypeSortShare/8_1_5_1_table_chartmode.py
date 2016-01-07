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

        print "Test Case: Chart Type - Table View: Chart Mode"
        self.vc.findViewWithTextOrRaise(u'Sales Data - Departmental Stores_karuna_copy').touch()
        self.vc.sleep(8)
        self.vc.dump(window=-1)

        self.device.longTouch(516.0, 110.0, 2000, 0)
        self.vc.sleep(5)
        self.vc.dump(window=-1)

        self.device.longTouch(184.0, 658.0, 2000, 0)
        self.vc.sleep(5)
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

        print "Selected: Table View"
        self.vc.findViewWithTextOrRaise(u'Table View', root=self.vc.findViewByIdOrRaise('id/no_id/12')).touch()

        print "Table View is displayed!"    

        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Chart Mode: Scroll table on Overlay"
        overlay_text = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/view_table_overlay")
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        if overlay_text.enabled():
            print "Overlay: Visible- scroll! "

            last1 = self.vc.findViewByIdOrRaise("id/no_id/36").text()
            print last1
            self.device.dragDip((343.0, 460.0), (344.0, 362.0), 1000, 20, 0)
            self.vc.sleep(3)
            self.vc.dump(window=-1)
            last2 = self.vc.findViewByIdOrRaise("id/no_id/36").text()
            print last2

            if last1 == last2:
                print "List did not scroll, list ends"
            else:
                print "List scroll successful!"
        else:
            print "Failed..."
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Back to Home"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewBackButton").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
