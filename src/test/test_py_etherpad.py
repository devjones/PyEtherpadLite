import py_etherpad
import unittest


class TestEtherpadLiteClient(unittest.TestCase):

    def testCreateLargePad(self):
        with open('tell-tale.txt') as read_handle:
            content = read_handle.read()

        #Create client
        ep_client = py_etherpad.EtherpadLiteClient()

        #Create and remove pad
        print ep_client.createPad('telltale', content)
        print ep_client.deletePad('telltale')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCreateLargePad']
    unittest.main()
