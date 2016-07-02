# http://nicholasjackson.github.io/azure/python/python-packages-and-azure-webjobs/
import sys, getopt
import urllib.parse
from http.cookiejar import Cookie
from http.cookiejar import CookieJar
from http.cookiejar import CookiePolicy
import requests
from applicationinsights import TelemetryClient
from datetime import datetime
import json
from RegistrationQueueClient import RegistrationQueueClient
import CheckinQueueClient

# To deploy this as a webjob, include the site-packages dir from your python distro in the zip file and uncomment the line below
#sys.path.append("site-packages")

swaDomain = 'mobile.southwest.com'
urlBase = 'https://mobile.southwest.com/middleware/MWServlet'           
headers = {'user-agent':'Apache-HttpClient/android/Nexus 5', 'Host':'mobile.southwest.com:443'}
defaultData = { 'platform':'android',                
                'appID':'swa',
                'appver':'2.25.0',
                'channel':'rc',
                'cacheid':'',
                'platformver':'5.0.GA_v201604271620'
    }

#script example
#argv: -c ABC123 -l Doe -f Jonh -e john.doe@yahoo.com

def main(argv):
    helpMsg1='SouthwestRequests.py -c <confirmation #> -l <lastName> -f <firstName> -e <email>'
    helpMsg2='SouthwestRequests.py --confirmationNumber=<confirmation #> --lastName=<lastName> --firstName=<firstName> --email <email>'

    try:
        opts, args = getopt.getopt(argv, "hc:l:f:e:", ["confirmationNumber=,lastName=,firstName=,email="])
    except getopt.GetoptError:
      print (helpMsg1)
      sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(helpMsg1)
            print('\tor use: ' + helpMsg2)
            sys.exit()
        elif opt in ("-c", "--confirmationNumber"):
            confirmationNumber = arg
        elif opt in ("-l", "--lastName"):
            lastname = arg
        elif opt in ("-f", "--firstName"):
            firstname = arg
        elif opt in ("-e", "--email"):
            email = arg
    
    if(confirmationNumber):
        print('Confirmation #: ', confirmationNumber)
    if(firstname):
        print('Firstname:\t', firstname)
    if(lastname):
        print('Lastname:\t', lastname)
    if(email):
        print('Email:\t\t', email)
    return {'confirmationNumber':confirmationNumber,
            'lastName':lastname,
            'firstName':firstname,
            'email':email,
            }

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def _getCookies(headers):
    cj = CookieJar()
    cookies = headers.split(',')
    for cookie in cookies:
        attrs = cookie.split(';')
        cookieNameValue = name = attrs[0].strip().split('=')
        pathNameValue = name = attrs[1].strip().split('=')
        ck = Cookie(version=1, name=cookieNameValue[0],
                              value=cookieNameValue[1],
                              port=443,
                              port_specified=False,
                              domain=swaDomain,
                              domain_specified=True,
                              domain_initial_dot=False,
                              path=pathNameValue[1],
                              path_specified=True,
                              secure=True,
                              expires=None,
                              discard=True,
                              comment=None,
                              comment_url=None,
                              rest={'HttpOnly': None},
                              rfc2109=False)
        cj.set_cookie(ck)
    return cj

def _getNewSession(cj):
    if( cj == None):
        cj = CookieJar()
        cj = _isSessionExists()
    return cj

def _isSessionExists():
    cookieJar = CookieJar()
    data = {'serviceID':'isSessionExists', 'isLoggedIn':'false'}
    reqData = merge_two_dicts(defaultData, data)    
    req = requests.post(urlBase,
                       headers=headers, data=reqData, cookies=cookieJar)
    #print(r1.status_code)
    cookieJar = _getCookies(req.headers['set-cookie'])
    return cookieJar

def checkReservation(confirmationNumber, lastname, firstname, cj = None):
    now = datetime.now().strftime('%m/%d/%Y') 
    cj = _getNewSession(cj)
    creditCardDepartureDate = urllib.parse.quote_plus(now)
    data = {'confirmationNumber':confirmationNumber,
        'confirmationNumberLastName':lastname,
        'creditCardNumber':'',
        'creditCardDepartureDate': creditCardDepartureDate,
        'confirmationNumberFirstName':firstname,
        'submitButton':'Continue',
        'creditCardLastName':'',       
        'searchType':'ConfirmationNumber',
        'serviceID':'viewAirReservation',
        'creditCardFirstName':''}
    reqData = merge_two_dicts(defaultData, data)    
    req = requests.post(urlBase,
                       headers=headers,
                       data=reqData,
                       cookies=cj)
    return {'payload':req.text, 'cookies':_getCookies(req.headers['set-cookie'])}

def retrieveCheckinReservation(confirmationNumber, lastname, firstname, cj = None):
    cj = _getNewSession(cj)
    data = {'serviceID': 'checkIntravelAlerts'}
    reqData = merge_two_dicts(defaultData, data)
    newHeaders = merge_two_dicts({'Accept-Encoding':'gzip'}, headers)    
    req = requests.post(urlBase,
                        headers=newHeaders,
                        data=reqData,
                        cookies=cj)
    return {'payload':req.text, 'cookies':_getCookies(req.headers['set-cookie'])}

def checkinReservation(confirmationNumber, lastname, firstname, cj = None):
    cj = _getNewSession(cj)
    data = {'firstName':firstname,
            'lastName':lastname,
            'serviceID':'flightcheckin_new',
            'recordLocator':confirmationNumber}    
    reqData = merge_two_dicts(defaultData, data)
    newHeaders = merge_two_dicts({'Accept-Encoding':'gzip'}, headers)
    req = requests.post(urlBase,
                        headers=newHeaders,
                        data=reqData,
                        cookies=cj)
    return {'payload': json.loads(req.text), 'cookies':_getCookies(req.headers['set-cookie'])}

def processRegistration(message):
    print(message)
    return False


# This is the main function that is run when running this as a script or console app
if __name__ == "__main__":
    args = main(sys.argv[1:])
    result = retrieveCheckinReservation(args['confirmationNumber'], args['lastName'], args['firstName'])
    #print(result['cookies'].__str__)
    #print(result['payload'])
    if(isinstance(result['cookies'], CookieJar)):
        result2 = checkinReservation(args['confirmationNumber'], args['lastName'], args['firstName'], result['cookies'])
        print(result2['payload'])
    else:
        print('no cookiejar')

    #checkReservation(args['confirmationNumber'], args['lastName'], args['firstName'])