import urllib
import urllib2
import json


class EtherpadLiteClient:

    API_VERSION             = 1

    CODE_OK                 = 0
    CODE_INVALID_PARAMETERS = 1
    CODE_INTERNAL_ERROR     = 2
    CODE_INVALID_FUNCTION   = 3
    CODE_INVALID_API_KEY    = 4
    TIMEOUT = 20

    apiKey = "EtherKey54"
    baseUrl = "http://localhost:9001/api"

    def __init__(self,apiKey = None, baseUrl = None):
        if apiKey:
          self.apiKey  = apiKey

        if baseUrl:
            self.baseUrl = baseUrl

        '''
        # No validation of url
        raise Exception("[:self.baseUrl] is not a valid URL")
        '''



    def call(self,function, arguments = {}):
        #Create a dictionary of all parameters
        params = arguments
        params.update({'apikey': self.apiKey})

        query= urllib.urlencode(params, True)

        url = self.baseUrl + "/" + str(self.API_VERSION) + "/" + function + "?" + query

        try:
            opener = urllib2.build_opener()
            request = urllib2.Request(url=url)
            response = opener.open(request, timeout=self.TIMEOUT)
            result = response.read()
            response.close()
        except urllib2.HTTPError as e:
            raise
        #raise RequestError("Failed to send request: %e" str(e))



        result = json.loads(result)
        if (result == None):
            raise ValueError("JSON response could not be decoded")

        return self.handleResult(result)


    def handleResult(self,result):
        if not 'code' in result:
            raise Exception("API response has no code")

        if not 'message' in result:
            raise Exception("API response has no message")

        if not 'data' in result:
            result['data'] = None


        if result['code'] == self.CODE_OK:
            return result['data']
        elif result['code'] == self.CODE_INVALID_PARAMETERS or result['code'] == self.CODE_INVALID_API_KEY:
            raise ValueError(result['message'])
        elif result['code'] == self.CODE_INTERNAL_ERROR:
            raise Exception(result['message'])
        elif result['code'] == self.CODE_INVALID_FUNCTION:
            raise Exception(result['message'])
        else:
            raise Exception("An unexpected error occurred whilst handling the response")




    # GROUPS
    # Pads can belong to a group. There will always be public pads that doesnt belong to a group (or we give this group the id 0)

    # creates a new group
    def createGroup(self):
        return self.call("createGroup")


    # this functions helps you to map your application group ids to etherpad lite group ids
    def createGroupIfNotExistsFor(self,groupMapper):
        return self.call("createGroupIfNotExistsFor", {
            "groupMapper": groupMapper
            })


        # deletes a group
    def deleteGroup(self,groupID):
        return self.call("deleteGroup", {
            "groupID": groupID
            })


        # returns all pads of this group
    def listPads(self,groupID):
        return self.call("listPads", {
            "groupID": groupID
            })


        # creates a new pad in this group
    def createGroupPad(self,groupID, padName, text):
        return self.call("createGroupPad", {
            "groupID": groupID,
            "padName": padName,
            "text": text
            })


        # AUTHORS
    # Theses authors are bind to the attributes the users choose (color and name).

    # creates a new author
    def createAuthor(self,name):
        return self.call("createAuthor", {
            "name": name
            })


        # this functions helps you to map your application author ids to etherpad lite author ids
    def createAuthorIfNotExistsFor(self,authorMapper, name):
        return self.call("createAuthorIfNotExistsFor", {
            "authorMapper": authorMapper,
            "name": name
            })


        # SESSIONS
    # Sessions can be created between a group and a author. This allows
    # an author to access more than one group. The sessionID will be set as
    # a cookie to the client and is valid until a certian date.

    # creates a new session
    def createSession(self,groupID, authorID, validUntil):
        return self.call("createSession", {
            "groupID": groupID,
            "authorID": authorID,
            "validUntil": validUntil
            })


        # deletes a session
    def deleteSession(self,sessionID):
        return self.call("deleteSession", {
            "sessionID": sessionID
            })


        # returns informations about a session
    def getSessionInfo(self,sessionID):
        return self.call("getSessionInfo", {
            "sessionID": sessionID
            })


        # returns all sessions of a group
    def listSessionsOfGroup(self,groupID):
        return self.call("listSessionsOfGroup", {
            "groupID": groupID
            })


        # returns all sessions of an author
    def listSessionsOfAuthor(self,authorID):
        return self.call("listSessionsOfAuthor", {
            "authorID": authorID
            })


        # PAD CONTENT
    # Pad content can be updated and retrieved through the API

    # returns the text of a pad
    # should take optional rev
    def getText(self,padID):
        return self.call("getText", {
            "padID": padID
            })


        # sets the text of a pad
    def setText(self,padID, text):
        return self.call("setText", {
            "padID": padID,
            "text": text
            })


        # PAD
    # Group pads are normal pads, but with the name schema
    # GROUPIDPADNAME. A security manager controls access of them and its
    # forbidden for normal pads to include a  in the name.

    # creates a new pad
    def createPad(self,padID, text):
        return self.call("createPad", {
            "padID": padID,
            "text": text
            })


        # returns the number of revisions of this pad
    def getRevisionsCount(self,padID):
        return self.call("getRevisionsCount", {
            "padID": padID
            })


        # deletes a pad
    def deletePad(self,padID):
        return self.call("deletePad", {
            "padID": padID
            })


        # returns the read only link of a pad
    def getReadOnlyID(self,padID):
        return self.call("getReadOnlyID", {
            "padID": padID
            })


        # sets a boolean for the public status of a pad
    def setPublicStatus(self,padID, publicStatus):
        return self.call("setPublicStatus", {
            "padID": padID,
            "publicStatus": publicStatus
            })


        # return true of false
    def getPublicStatus(self,padID):
        return self.call("getPublicStatus", {
            "padID": padID
            })


        # returns ok or a error message
    def setPassword(self,padID, password):
        return self.call("setPassword", {
            "padID": padID,
            "password": password
            })


        # returns true or false
    def isPasswordProtected(self,padID):
        return self.call("isPasswordProtected", {
            "padID": padID
            })




