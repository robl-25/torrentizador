import sys
import logging

import requests
from bs4 import BeautifulSoup


NEXT_EPISODE_URL = 'http://next-episode.net/'
THE_PIRATE_BAY_URL = 'http://thepiratebay.se/search/'


LOGGER = logging.getLogger(__name__)


def _int_formatter(number):
    if int(number) in range(10):
        return '0' + number
    if int(number) < 0:
        raise ValueError('There is no such thing as negative episode number')
    return number


def format_series_name(series_name):
    ''' Returns series name formated properly (like asdasd-asdasd-asdasd) '''
    return '-'.join(series_name.lower().split())


def get_next_episode(series_name):
    ''' Returns dict with information about next episode of `series_name`
        raises exception if given series is not found or is over '''
    original_name = series_name
    series_name = format_series_name(series_name)

    html = requests.get(NEXT_EPISODE_URL + series_name).text
    parsed_obj = BeautifulSoup(html, 'html.parser')

    next_episode = parsed_obj.body.find('div', id='next_episode')

    if next_episode is None:
        raise ValueError('Next episode for: "{}" not found. Maybe its over?'.format(original_name))

    data = [x.replace('\t', '') for x in next_episode.text.split('\n') if ':' in x]

    next_episode_dict = {row.split(':')[0]: row.split(':')[1] for row in data}
    next_episode_dict['Original Name'] = original_name.capitalize()
    next_episode_dict.pop('Summary')

    return next_episode_dict


def all_next_episodes(series_list):
    ''' Generator for all the next episodes in `series_list` '''
    for series in series_list:
        try:
            yield get_next_episode(series)
        except ValueError as error:
            LOGGER.warn('WARNING: {}'.format(error))


def schedule_download(next_episode):
    print(next_episode)
    actually_download(next_episode)


def actually_download(episode):
    url = THE_PIRATE_BAY_URL + episode['Original Name'] + '/0/99/0'

    html = requests.get(url).text
    parsed_obj = BeautifulSoup(html, 'html.parser')

    results = parsed_obj.body.find('table', id='searchResult')

    print(results.contents)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('[usage]: python {} [SERIES_NAME...]'.format(sys.argv[0]))
        sys.exit()

    series_list = sys.argv[1:]

    for next_episode in all_next_episodes(series_list):
        schedule_download(next_episode)
