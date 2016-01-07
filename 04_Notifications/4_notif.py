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
        cls.kwargs1 = {'ignoreversioncheck': False,
                       'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False,
                       'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.5, 'find-views-with-content-description': False, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None,
                       'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'drop-shadow': False, 'output': 'testnotif.py', 'unit-test-method': None, 'interactive': False}
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
            # print "############ViewFamily##############"
            # print view_family
            # print "##############ChildList############"
            child_list = removeDuplicates(view_family)
            # print child_list
            # print "###########Before While Loop###############"

            while (len(view_family) - len(child_list)) <= collisions:
                no_id_1 = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/tv_comment_heading")

                title = re.search('shared | commented', no_id_1.text())
                if (title):
                    print " Passed for "+ no_id_1.text()
                else:
                    print "Failed..."

                parent.uiScrollable.flingForward()
                self.vc.sleep(_s)
                child_views = getFamilyRec(parent)
                # print "#############ChildViews#############"
                # print child_views
                view_family.append(child_views)

                child_list = removeDuplicates(view_family)
                # print "##########ChildList in Loop################"
                # print child_list
                # print (len(view_family) - len(child_list))

            return child_list

        print "Test Case: Notifications"
        self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/notifications").touch()
        self.vc.sleep(2)
        self.vc.dump(window=-1)


        android___id_list = self.vc.findViewByIdOrRaise("android:id/list")

        # print "-----------Children-------"
        # print android___id_list.children

        all_views = getAllViews(android___id_list , 1)
        # print "-----------ALL VIEWS-------"
        # print all_views

        # print "-----------Children-------"
        # print android___id_list.children


        # print ViewClient.traverseShowClassIdAndText(android___id_list)
        # android___id_list.uiScrollable.setViewClient(self.vc)
        # #android___id_list.uiScrollable.scrollTextIntoView(''Sumedh More commented on "Sales Data - Departmental Stores_karuna_copy"'')
        # android___id_list.uiScrollable.scrollTextIntoView("test2")
        #
        # view_family = getFamilyRec(android___id_list)
        # print view_family

#        print android___id_list
        #print self.vc.findViewByIdOrRaise("id/no_id/1").getText()
        # com_chartcube_cubepager___id_tv_comment_heading = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/tv_comment_heading")
        # j = 0
        # total = len(android___id_list.getChildren())

        # while (j <= 3):
        #i = 7
        #for j in range(len(android___id_list.getChildren())):
#        while (self.y != y_coord):
    #    while (i >= 7 and i < 31):
            #for i in range(len(android___id_list.getChildren())):
                #print self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/list_item")
                #no_id_1 = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/tv_comment_heading")
                # print "---"+str(no_id_1)
                # title_by_id = self.vc.findViewByIdOrRaise("id/no_id/"+str(i))#7,11,15,19
                # #   print no_id_1.text()
                # title = re.search('shared | commented', title_by_id.text())
                # if (title):
                #     print "Passed for "+ title_by_id.text()
                # else:
                #     print "Failed..."
                #
                # i += 4
                #print "---"+str(no_id_1)
                #com_chartcube_cubepager___id_tv_comment_heading = self.vc.findViewByIdOrRaise("com.chartcube.cubepager:id/tv_comment_heading")
               #print com_chartcube_cubepager___id_tv_comment_heading[i].text()
                # title = re.search('shared | commented', com_chartcube_cubepager___id_tv_comment_heading.text())
                # if (title):
                #     print str(i+1)+" Passed for "+ com_chartcube_cubepager___id_tv_comment_heading.text()
                # else:
                #     print "Failed..."
                #com_chartcube_cubepager___id_tv_comment_heading = com_chartcube_cubepager___id_tv_comment_heading
                # self.vc.sleep(2)
                # self.vc.dump(window=-1)
                #print "length at "+str(i)+ " is "+str(len(android___id_list.getChildren()))
        #print "Iteration: "+ str(j) + " List_Count: " + str(len(android___id_list.getChildren()))
##                total += len(android___id_list.getChildren())
                # print android___id_list.uiScrollable.x
                # print android___id_list.uiScrollable.y
                #android___id_list.uiScrollable.flingForward()

#                self.vc.sleep(_s)
                # print android___id_list.uiScrollable.x
                # print android___id_list.uiScrollable.y
#                self.vc.dump(window=-1)

#            j += 1
#        print "Total notifications: "+str(total)
        #print len(android___id_list.getChildren())

        # print [method for method in dir(android___id_list) if callable(getattr(android___id_list, method))]
        # while (not (android___id_list.uiScrollable.flingToEnd()))
        #
        # self.device.dragDip((174.0, 608.0), (179.0, 161.0), 1000, 20, 0)
        # self.vc.sleep(2)
        # self.vc.dump(window=-1)

        # self.device.press('KEYCODE_BACK')
        # self.vc.sleep(2)
        # self.vc.dump(window=-1)

if __name__ == '__main__':
    CulebraTests.main()
