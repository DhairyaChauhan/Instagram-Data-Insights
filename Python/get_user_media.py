# -*- coding: utf-8 -*-

  
from defines import getCreds, makeApiCall
import csv

def getList(dict): 
    return dict.keys() 

def getUserMedia( params, pagingUrl = '' ) :
	""" Get users media
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	if ( '' == pagingUrl ) : # get first page
		url = params['endpoint_base'] + params['instagram_account_id'] + '/media' # endpoint url
	else : # get specific page
		url = pagingUrl  # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


#saving the json data to a file
def saveToCsv(user_data, csv_writer) :

    for post in user_data:
        csv_writer.writerow(post)
    
    return 0
    
params = getCreds() # get creds
params['debug'] = 'no' # set debug
response = getUserMedia( params ) # get users media from the api
next = response['json_data']['paging']['next']
user_data = response['json_data']['data']

#creating a file to save data and writing the headers
data_file = open('user_media.csv', 'w',encoding="utf-8") 
csv_columns = getList(user_data[0])
csv_writer = csv.DictWriter(data_file, fieldnames=csv_columns) 
csv_writer.writeheader()
saveToCsv(user_data,csv_writer)

#looping thorugh multiple pages of data
i = 0
while (i < 2):
    i += 1
    response = getUserMedia( params, next ) #get users media from the api on the next page
    next = response['json_data']['paging']['next']
    user_data = response['json_data']['data']
   
    for data in user_data:   #printing the json data
        print(data)
        print("\n\n")
        
    saveToCsv(user_data,csv_writer) #saving the data to csv
    









