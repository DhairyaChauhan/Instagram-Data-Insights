# -*- coding: utf-8 -*-


from defines import getCreds, makeApiCall
from get_user_media import getUserMedia
import csv

def getList(dict): 
    return dict.keys() 


def getMediaInsights( params ) :
	""" Get insights for a specific media id
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}
	Returns:
		object: data from the endpoint
	"""
	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['metric'] = params['metric'] # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['latest_media_id'] + '/insights' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


def getUserInsights( params ) :
	""" Get insights for a users account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['metric'] = 'impressions,profile_views,reach' # fields to get back
	endpointParams['period'] = 'day' # period
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/insights' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


def extractInsights(user_data,media_insights):
    
    for user_media in user_data:

        params['latest_media_id'] = user_media['id']
        params['metric'] = 'engagement,impressions,reach,saved'
    
        insightresponse = getMediaInsights( params ) # get insights for a specific media id
        post_insights = insightresponse['json_data']['data']
        split_response = dict()     #dictionary to store insights of a particular media
        split_response['id'] = user_media['id']
        
        for insights in post_insights:
            split_response[insights['title']] = insights['values'][0]['value']
            #print(insights)
        media_insights.append(split_response)
    
    return 0

#saving the json data to a file
def saveToCsv(media_insights) :
    
    data_file = open('media_insights.csv', 'w',encoding="utf-8") 
    csv_columns = getList(media_insights[0])
    csv_writer = csv.DictWriter(data_file, fieldnames=csv_columns) 
    csv_writer.writeheader()
    for insights in media_insights:
        csv_writer.writerow(insights)
    
    return 0

params = getCreds() # get creds
params['debug'] = 'no' # set debug
response = getUserMedia( params ) # get users media from the api
user_data = response['json_data']['data']
next = response['json_data']['paging']['next']
media_insights = list() #list to store insights

extractInsights(user_data, media_insights) #function call to extract insights from json data

#looping thorugh multiple pages of data
i = 0
while (i < 2):
    i += 1
    response = getUserMedia( params, next ) #get users media from the api on the next page
    next = response['json_data']['paging']['next']
    user_data = response['json_data']['data']
    extractInsights(user_data, media_insights)

saveToCsv(media_insights)
print(media_insights)


    



