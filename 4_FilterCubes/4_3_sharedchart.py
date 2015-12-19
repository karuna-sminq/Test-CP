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
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.5, 'find-views-with-content-description': True, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'drop-shadow': False, 'output': None, 'unit-test-method': None, 'interactive': False}
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

        print "Test Case: CubeFilter- Shared Chartcubes"
        if (self.vc.findViewWithTextOrRaise(u'Shared Chartcubes', root=self.vc.findViewByIdOrRaise('id/no_id/3'))):
            self.vc.findViewWithTextOrRaise(u'Shared Chartcubes', root=self.vc.findViewByIdOrRaise('id/no_id/3')).touch()
            self.vc.sleep(_s)
            self.vc.dump(window=-1)

            if (self.vc.findViewWithTextOrRaise(u'All Chartcubes')):
                print "CubeFilter- All Chartcubes"
                self.vc.findViewWithTextOrRaise(u'All Chartcubes').touch()
                self.vc.sleep(_s)
                # com_chartcube_cubepager___id_textViewCubeOwner = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/textViewCubeOwner")
                # com_chartcube_cubepager___id_textViewCubeOwner = self.vc.findViewWithTextOrRaise(u'You, 2 weeks 4 days ago')
                # android___id_list = self.vc.findViewByIdOrRaise("android:id/list")
                # no_id9 = self.vc.findViewByIdOrRaise("id/no_id/9")
                # if (self.vc.findViewWithTextOrRaise(u'You, 2 weeks 4 days ago', root=self.vc.findViewByIdOrRaise('id/no_id/9'))):
                #     print "Passed..."
                # else:
                #     print "Failed..."
                # self.vc.sleep(_s)
                self.vc.dump(window=-1)

                if (self.vc.findViewWithTextOrRaise(u'All Chartcubes', root=self.vc.findViewByIdOrRaise('id/no_id/3'))):
                    self.vc.findViewWithTextOrRaise(u'All Chartcubes', root=self.vc.findViewByIdOrRaise('id/no_id/3')).touch()
                    self.vc.sleep(_s)
                    self.vc.dump(window=-1)

                    if (self.vc.findViewWithTextOrRaise(u'My Chartcubes')):
                        print "CubeFilter- My Chartcubes"
                        self.vc.findViewWithTextOrRaise(u'My Chartcubes').touch()
                        self.vc.sleep(_s)
                        # if (self.vc.findViewWithTextOrRaise(u'Sumedh More, 1 week 6 days ago', root=self.vc.findViewByIdOrRaise('id/no_id/9'))):
                        #     print "Passed..."
                        # else:
                        #     print "Failed..."
                        # self.vc.sleep(_s)
                        self.vc.dump(window=-1)

                        if(self.vc.findViewWithTextOrRaise(u'My Chartcubes', root=self.vc.findViewByIdOrRaise('id/no_id/3'))):
                            self.vc.findViewWithTextOrRaise(u'My Chartcubes', root=self.vc.findViewByIdOrRaise('id/no_id/3')).touch()
                            self.vc.sleep(_s)
                            self.vc.dump(window=-1)

                        print "CubeFilter- Back to Shared Chartcubes"
                        self.vc.findViewWithTextOrRaise(u'Shared Chartcubes').touch()
                        self.vc.sleep(_s)
                        self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
