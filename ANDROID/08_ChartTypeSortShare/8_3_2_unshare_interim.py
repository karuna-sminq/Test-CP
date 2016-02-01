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

from subprocess import call

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

        print "Test Case: UnShare"

        #Call to selenium web app - share test
        call(["python","/home/cp_android2/Documents/AndroidViewClient/Chartcube/WEB/chart_share.py"])
        self.vc.sleep(10)
        self.vc.dump(window=-1)

        android___id_list = self.vc.findViewByIdOrRaise("android:id/list")

        android___id_list.uiScrollable.flingToBeginning()
        print "Cube List Refreshed!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #If Cube owner: access cannot be removed
        owner = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/textViewCubeOwner")
        print owner.text()
        result = re.search('^[^You]', owner.text())

        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/notifications").touch()
        self.vc.sleep(10)
        self.vc.dump(window=-1)

        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/list_item").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.vc.device.press('KEYCODE_BACK')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Call to selenium web app - unshare test
        call(["python","/home/cp_android2/Documents/AndroidViewClient/Chartcube/WEB/chart_unshare.py"])

        #Check for cube access removal
        if result:
            if self.vc.findViewWithTextOrRaise(u'Chatcube unshared'):
                print "Cube owner has removed your access! Passed!"
        else:
            if self.vc.findViewWithTextOrRaise(u'Chatcube unshared'):
                print "Owner's access cannot be removed! Failed!"

        print "Back to Home"
        self.vc.findViewWithTextOrRaise("OK").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
