This python api enables easy interaction with the Etherpad Lite API.  Etherpad Lite is a collaborative editor provided by the Etherpad Foundation.  http://etherpad.org


#1 Preparation

If you are using a self hosted Etherpad Lite server, you will need to specify an API Key after installation before using the API.  (See https://github.com/Pita/etherpad-lite for installation details).

Your secret api key should be placed in the base installation (etherpad-client folder) in a text file named APIKEY.txt.  Many linux text editors automatically create a newline character, so I recommend simply executing the following command to set your api key without a newline character:

    echo -n "myapikey" > APIKEY.txt

#2 Basic usage

    <pre>
    from py_etherpad import EtherpadLiteClient
    myPad = EtherpadLiteClient('EtherpadFTW','http://beta.etherpad.org/api')

    #Change the text of the etherpad
    myPad.setText('testPad','New text from the python wrapper!')

    </pre>

#3 More details

See the py_etherpad.py file for further details on the methods and parameters available for the API

#3 License

Apache License

#4 Credit
This python client was inspired by TomNomNom's php client which can be found at: https://github.com/TomNomNom/etherpad-lite-client
