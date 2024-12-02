import requests
from datetime import date
from unittest import mock
from project import coming_up_next, related_news, search_fighter, pound4pound_rankings, upcoming_events, todays_date


headers = {
    "x-rapidapi-key": "14656dad08msh0e30e09547ffe31p1c1337jsna4dc6785c261",
    "x-rapidapi-host": "mma-api1.p.rapidapi.com"
}



# Test/Mock datetime.today
@mock.patch('project.date')
def test_todays_date(mock_date):
    mock_date.today.return_value = date(2024, 11, 1)
    result = todays_date()
    assert result == 'Friday, November 01, 2024'



# Test Coming Up Next Exception
@mock.patch('project.requests.get')
def test_coming_up_next_exception(mock_requests_get):
    ''' Mock Coming Up Next Exception  '''
    mock_requests_get.side_effect = requests.exceptions.ConnectionError('Error')
    result = coming_up_next()
    assert result == 'An ERROR Occured'

# Test coming up next API
@mock.patch('project.requests.get')
def test_coming_up_next(mock_request_get):
    querystring = {"year": "2024"}
    url = "https://mma-api1.p.rapidapi.com/getEventId"
    mock_response = mock.Mock(name='mock response', **{'status_code': 200,
                                                       'json.return_value': {'result': [{'event': 'event1'}]}})
    mock_request_get.return_value = mock_response
    coming_up_next()
    mock_request_get.assert_called_once_with(url, headers=headers, params=querystring)



# Test/Mock Related News Exception
@mock.patch('project.requests.get')
def test_related_news_exception(mock_requests_get):
    ''' Mock Related News Exception '''
    mock_requests_get.side_effect = requests.exceptions.ConnectionError()
    result = related_news()
    assert result == 'CONNECTION ERROR! Please Try Again Later'

# Test Related News API
@mock.patch('project.requests.get')
@mock.patch('project.webbrowser.open')
def test_related_news(mock_webbrowser, mock_requests_get):
    url = "https://mma-api1.p.rapidapi.com/news"
    mock_response = mock.Mock(name='related news response', **{'status_code': 200,
                                                               'json.return_value': [{'link': 'link'}]})
    mock_requests_get.return_value = mock_response
    related_news()
    mock_requests_get.assert_called_once_with(url, headers=headers)
    mock_webbrowser.assert_called_once_with('link')



# Search Fighter Exception
def test_search_fighter_keyerror_exception():
    assert search_fighter('willow the cat') == 'ERROR! {} Not Found'.format('willow the cat')

# Test/Mock Search Exception
@mock.patch('project.requests.get')
def test_search_exception(mock_requests_get):
    ''' Mock Search Exception '''
    mock_requests_get.side_effect = requests.exceptions.ConnectionError()
    result = search_fighter('fighter')
    assert result == 'ERROR! Link To {} Not Found...Please Try Another Name'.format('fighter')

# Test Search Fighter API
@mock.patch('project.requests.get')
@mock.patch('project.webbrowser.open')
def test_search_fighter(mock_webbrowser, mock_requests_get):
    url = "https://mma-api1.p.rapidapi.com/search"
    mock_response = mock.Mock(name='search response', **{'status_code': 200,
                                                         'json.return_value': {'players': [{'link': 'link'}]}})
    mock_requests_get.return_value = mock_response
    search_fighter('fighter')
    mock_requests_get.assert_called_once_with(url, headers=headers, params={'query': 'fighter'})
    mock_webbrowser.assert_called_once_with('link')



# Test/Mock p4p Exception
@mock.patch('project.pound4pound_rankings')
def test_p4p_exception(mock_request_get):
    mock_request_get.side_effect = requests.exceptions.ConnectionError()
    result = pound4pound_rankings('gender')
    assert result == None

# Test Mens Pound4Pound API
@mock.patch('project.requests.get')
def test_mens_pound4Pound_api(mock_request_get):
    url = "https://mma-api1.p.rapidapi.com/rankings-ufc"
    mock_response = mock.Mock(name='mock men', **{'status_code': 200,
                                                  'json.return_value': {'rankings': [{'ranks': [{'rank': 'player', 'name': 'fighter'}]}]}})
    mock_request_get.return_value = mock_response
    if pound4pound_rankings('Mens'):
        mock_request_get.assert_called_once_with(url, headers=headers)

# Test Womens Pound4Pound API
@mock.patch('project.requests.get')
def test_womens_p4p_api(mock_requests_get):
    url = "https://mma-api1.p.rapidapi.com/rankings-ufc"
    mock_response = mock.Mock(name='mock women', **{'status_code': 200,
                                                    'json.return_value': {'rankings':
                                                                          [{'ranks': [{'rank': '1', 'name': 'fighter'}, {'rank': '2', 'name': 'fighter'},
                                                                                      {'rank': '3', 'name': 'fighter'}, {'rank': '4', 'name': 'fighter'},
                                                                                      {'rank': '5', 'name': 'fighter'}, {'rank': '6', 'name': 'fighter'},
                                                                                      {'rank': '7', 'name': 'fighter'}, {'rank': '8', 'name': 'fighter'},
                                                                                      {'rank': '9', 'name': 'fighter'}, {'rank': '10', 'name': 'fighter'}]}] * 10}})
    mock_requests_get.return_value = mock_response
    pound4pound_rankings('Womens')
    mock_requests_get.assert_called_once_with(url, headers=headers)




# Test/Mock up_coming_events Exception
@mock.patch('project.requests.get')
def test_upcoming_events_exception(mock_requests_get):
    mock_requests_get.side_effect = requests.exceptions.ConnectionError()
    result = upcoming_events('selected_year')
    assert result == 'CONNECTION ERROR! Please Try Again Later'

# Test upcoming events API
@mock.patch('project.requests.get')
def test_upcoming_events_api(mock_requests_get):
    url = "https://mma-api1.p.rapidapi.com/getEventId"
    querystring = {"year": 'selected_year'}
    mock_response = mock.Mock(name='mock upcoming events', **{'status_code': 200,
                                                              'json.return_value': {'result': [{'event': 'event', 'startDate': 'date', 'endDate': 'endDate', 'eventId': 'numbers'}]}})
    mock_requests_get.return_value = mock_response
    upcoming_events('selected_year')
    mock_requests_get.assert_called_once_with(url, headers=headers, params=querystring)
