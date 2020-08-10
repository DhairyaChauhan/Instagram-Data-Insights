# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:29:48 2020

@author: dhair
"""

import csv
from defines import getCreds, makeApiCall

def getList(dict): 
    return dict.keys() 


def getAccountInfo( params ) :
	""" Get info on a users account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

params = getCreds() # get creds
params['debug'] = 'no' # set debug
response = getAccountInfo( params ) # hit the api for some data!

#print (response['json_data'])
data_file = open('user_data.csv', 'w',encoding="utf-8") 
user_data = response['json_data']['business_discovery']

csv_columns = getList(user_data)
csv_writer = csv.DictWriter(data_file, fieldnames=csv_columns) 
csv_writer.writerow(user_data)



