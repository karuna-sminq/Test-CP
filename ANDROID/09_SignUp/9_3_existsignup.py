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
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.5, 'find-views-with-content-description': False, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'drop-shadow': False, 'output': 'chartsignin1.py', 'unit-test-method': None, 'interactive': False}
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

        print "Test Case: Sign Up - Existing User"
        self.vc.findViewByIdOrRaise("com.cp.cubepager:id/imageViewSettings").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.vc.findViewWithTextOrRaise(u'Sign Out').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.vc.findViewWithTextOrRaise(u'Yes').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        self.vc.findViewWithTextOrRaise(u'Create Account').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        print "Typing Email Address"
        self.vc.findViewWithTextOrRaise(u'Email').setText("karuna.lingham@codepandora.com")
        self.vc.sleep(3)
        self.vc.dump(window=-1)

        print "Typing Full Name"
        self.vc.findViewWithTextOrRaise(u'Full Name').setText("K lingham")
        self.vc.sleep(3)
        self.vc.dump(window=-1)

        print "Typing Password"
        self.vc.findViewByIdOrRaise("com.cp.cubepager:id/create_account_password_edit").setText("karuna@cp2015")
        self.vc.sleep(3)
        self.vc.dump(window=-1)

        print "Typing Confirm Password"
        self.vc.findViewByIdOrRaise("com.cp.cubepager:id/create_account_confirm_edit").setText("karuna@cp2015")
        self.vc.sleep(3)
        self.vc.dump(window=-1)

        print "Clicked Create Account Button"
        self.vc.findViewByIdOrRaise("com.cp.cubepager:id/create_account_create_account_button").touch()

        if self.vc.findViewByIdOrRaise("com.cp.cubepager:id/create_account_create_account_button"):
            print "Email Id is already registered!"
        else:
            print "Signed up successfully!"
        self.vc.sleep(8)
        self.vc.dump(window=-1)

        print "Back to Home"
        self.vc.findViewWithTextOrRaise(u'Create Account').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
