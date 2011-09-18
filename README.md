This python api enables easy interaction with the Etherpad Lite API.  Etherpad Lite is a collaborative editor provided by the Etherpad Foundation.  http://etherpad.org

#1 Installation

To install py_etherpad using PIP, add the following line to your requirements.txt file:

    -e git+git://github.com/ozkatz/PyEtherpadLite.git#egg=PyEtherpadLite

#2 Preparation

If you are using a self hosted Etherpad Lite server, you will need to specify an API Key after installation before using the API.  (See https://github.com/Pita/etherpad-lite for installation details).

Your secret api key should be placed in the base installation (etherpad-client folder) in a text file named APIKEY.txt.  Many linux text editors automatically create an extra newline character at the end of the file, so I recommend simply executing the following command to set your api key without a newline character:

    echo -n "myapikey" > APIKEY.txt

Once you have created the APIKEY.txt file, you will need to edit the py_etherpad.py wrapper to set your API key. Edit the 'apiKey' variable and set it to the same key as defined in your APIKEY.txt file.

#3 Basic usage

    from py_etherpad import EtherpadLiteClient
    myPad = EtherpadLiteClient('EtherpadFTW','http://beta.etherpad.org/api')

    #Change the text of the etherpad
    myPad.setText('testPad','New text from the python wrapper!')

#4 More details

See the py_etherpad.py file for further details on the methods and parameters available for the API

#5 License

Apache License

#6 Credit
This python client was inspired by TomNomNom's php client which can be found at: https://github.com/TomNomNom/etherpad-lite-client
