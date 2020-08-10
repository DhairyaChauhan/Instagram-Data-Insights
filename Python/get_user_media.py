# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:31:52 2020

@author: dhair
"""


  
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

params = getCreds() # get creds
params['debug'] = 'no' # set debug
response = getUserMedia( params ) # get users media from the api
print (response['json_data']['data'])
data_file = open('user_media.csv', 'w',encoding="utf-8") 
user_data = response['json_data']['data']
csv_columns = getList(user_data[0])
csv_writer = csv.DictWriter(data_file, fieldnames=csv_columns) 
csv_writer.writeheader()
for post in user_data:
    print(type(post))
    csv_writer.writerow(post)


#params['debug'] = 'no' # set debug
#response = getUserMedia( params, response['json_data']['paging']['next'] ) # get next page of posts from the api

