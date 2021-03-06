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

        #Returns list of visible child views by recursively traversing through parent view
        def getFamilyRec(parent):
            family = []
            if parent.children != []:
                    family.append(parent)
                    for ch in parent.children:
                            family += getFamilyRec(ch)
            else:
                    family.append(parent)
            return family

        def removeDuplicates(list):
            newlist = []
            for i in list:
                if i not in newlist:
                    newlist.append(i)
            return newlist

        def getAllViews(parent, collisions):

            view_family = getFamilyRec(parent)

            child_list = removeDuplicates(view_family)

            while (len(view_family) - len(child_list)) <= collisions:
                if (self.vc.findViewWithTextOrRaise(u'My cps', root=self.vc.findViewByIdOrRaise('id/no_id/3'))):
                    #All Cubes
                    self.vc.sleep(_s)
                    self.vc.dump(window=-1)

                    owner = self.vc.findViewByIdOrRaise("com.cp.cubepager:id/textViewCubeOwner")
                    print owner.text()
                    result = re.search('You', owner.text())
                    if result:
                        print "Check for My cps: Passed..."
                    else:
                        print "Failed..."

                #parent.uiScrollable.flingForward()
                self.vc.sleep(_s)
                child_views = getFamilyRec(parent)

                view_family.append(child_views)

                child_list = removeDuplicates(view_family)

            return child_list

        print "Test Case: CubeFilter- My cps"

        #print [method for method in dir(android___id_list) if callable(getattr(android___id_list, method))]

        android___id_list = self.vc.findViewByIdOrRaise("android:id/list")

        all_views = getAllViews(android___id_list , 1)

        if (self.vc.findViewWithTextOrRaise(u'My cps', root=self.vc.findViewByIdOrRaise('id/no_id/3'))):
            self.vc.findViewWithTextOrRaise(u'My cps', root=self.vc.findViewByIdOrRaise('id/no_id/3')).touch()
            self.vc.sleep(_s)
            self.vc.dump(window=-1)

            if (self.vc.findViewWithTextOrRaise(u'Shared cps')):
                print "CubeFilter- Shared cps"
                self.vc.findViewWithTextOrRaise(u'Shared cps').touch()
                self.vc.sleep(_s)
                self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
