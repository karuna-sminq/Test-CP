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

        print "Test Case: Internet Connectivity"

        #Open Notifications Panel
        self.device.dragDip((168.0, 17.0), (184.0, 476.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.device.dragDip((166.0, 230.0), (172.0, 540.0), 1000, 20, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Switch off WiFi
        self.vc.findViewWithContentDescriptionOrRaise(u'''Wi-Fi signal full..''').touch()
        print "WiFi turned off!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Close Notifications Panel
        self.device.dragDip((163.0, 561.0), (163.0, 52.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.device.dragDip((166.0, 221.0), (170.0, 37.0), 1000, 20, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Check for No Connectivity message
        if (self.vc.findViewByIdOrRaise("com.cp.cubepager:id/notification_for_no_network_textview")):
            print "No Internet Connection!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Cube click should be disabled
        if not (self.vc.findViewByIdOrRaise("com.cp.cubepager:id/textViewCubeTitle").clickable()):
            print "Passed! Cube cannot be loaded! Connect to the internet first!"
        else:
            print "Failed! Cube load successful!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Open Notifications Panel
        self.device.dragDip((168.0, 17.0), (184.0, 476.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.device.dragDip((166.0, 230.0), (172.0, 540.0), 1000, 20, 0)
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Switch on WiFi
        self.vc.findViewWithContentDescriptionOrRaise(u'''Wi-Fi off..''').touch()
        print "WiFi turned on!"
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        #Close Notifications Panel
        self.device.dragDip((163.0, 561.0), (163.0, 52.0), 1000, 20, 0)
        self.vc.sleep(1)
        self.vc.dump(window=-1)

        self.device.dragDip((166.0, 221.0), (170.0, 37.0), 1000, 20, 0)
        self.vc.sleep(_s)

if __name__ == '__main__':
    CulebraTests.main()
