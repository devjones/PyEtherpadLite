#!/usr/bin/env python
"""Module to test py_etherpad."""

import py_etherpad
import unittest


class TestEtherpadLiteClient(unittest.TestCase):
    """Class to test EtherpadLiteClient."""

    def setUp(self):
        """Assign a shared EtherpadLiteClient instance to self."""
        self.ep_client = py_etherpad.EtherpadLiteClient()

    def testCreateLargePad(self):
        """Initialize a pad with a large body of text, and remove the pad if that succeeds."""
        with open('tell-tale.txt') as read_handle:
            content = read_handle.read()

        #Create and remove pad
        print self.ep_client.createPad('telltale', content)
        print self.ep_client.deletePad('telltale')

    def testCreateHTMLPad(self):
        """Create an initially empty pad, add a HTML text body and remove the pad if that succeeds."""
        content = "<div><u>Underlined text</u><ul><li>this</li><li>is a</li><li><strong>unordered</strong></li>" + \
        "<li>list</li></ul>after the list a newline is automatically <u>added</u>" + \
        "<br>BR can also be used to force new <em>lines</em><p><strong>Or you can use paragraphs</strong></p></div>"

        #Create and remove pad
        print self.ep_client.createPad('htmlpad')
        print self.ep_client.setHTML('htmlpad', content)
        print self.ep_client.deletePad('htmlpad')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCreateLargePad']
    unittest.main()
