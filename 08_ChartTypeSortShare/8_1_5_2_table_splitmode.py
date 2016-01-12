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

        print "Test Case: Chart Type - Table View: Split View Mode"

        self.device.dragDip((343.0, 521.0), (348.0, 192.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.vc.findViewWithTextOrRaise(u'Spend Analysis - Pizza Chain').touch()
        self.vc.sleep(8)
        self.vc.dump(window=-1)

        self.device.longTouch(492.0, 204.0, 2000, 0)
        self.vc.sleep(5)
        self.vc.dump(window=-1)

        self.device.dragDip((318.0, 354.0), (313.0, 247.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        print "Selected: Unit Dimension"
        self.device.touchDip(255.0, 405.0, 0)
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


        print "Split View Mode: Scroll table on Overlay"
        self.vc.findViewWithTextOrRaise(u'Add Comment').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        overlay_text = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/view_table_overlay")
#        print overlay_text.enabled()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        if overlay_text.enabled():
            print "Overlay: Visible- scroll! "

            last1 = self.vc.findViewByIdOrRaise("id/no_id/36").text()
        #    print last1
            self.device.dragDip((338.0, 282.0), (335.0, 182.0), 1000, 20, 0)
            self.vc.sleep(1)
            self.vc.dump(window=-1)
            last2 = self.vc.findViewByIdOrRaise("id/no_id/36").text()
        #    print last2

            if last1 == last2:
                print "List did not scroll, list ends"
            else:
                print "List scroll successful!"

        else:
            print "No Overlay!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "In Chart Mode:"
        self.vc.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        last = self.vc.findViewByIdOrRaise("id/no_id/34").text()
        #print last

        if last == last2:
            print "Overlay scroll not required. Table contents visible."
            self.vc.sleep(1)
            self.vc.dump(window=-1)
        else:
            print "Scrolling through..."
            self.device.dragDip((338.0, 282.0), (335.0, 182.0), 1000, 20, 0)
            self.vc.sleep(1)
            self.vc.dump(window=-1)

        print "Back to Home"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/imageViewBackButton").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        android___id_list = self.vc.findViewByIdOrRaise("android:id/list")

        android___id_list.uiScrollable.flingToBeginning()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
