import os

from e_client import Client

default_client = Client()


def get_user_main_language(user_name, client=default_client):
    data = client.list_for_users(user_name)
    if not data:
        return None

    languages = map(lambda repo: repo["language"], data)
    languages_count = {}
    for language in languages:
        if language not in languages_count:
            languages_count[language] = 1
        else:
            languages_count[language] += 1
    return max(languages_count, key=lambda k: languages_count[k])


def _wrong1(user_name, client=default_client):
    data = client.list_for_users(user_name)
    if not data:
        return ''
    return get_user_main_language(user_name, client)


def _wrong2(user_name, client=default_client):
    data = client.list_for_users(user_name)
    if not data:
        return None
    languages = map(lambda repo: repo["language"], data)
    languages_count = {}
    for language in languages:
        if language not in languages_count:
            languages_count[language] = 1
        else:
            languages_count[language] += 1
    return min(languages_count, key=lambda k: languages_count[k])


functions = {
    "right": get_user_main_language,
    "fail1": _wrong1,
    "fail2": _wrong2,
}


def get_function():
    # name = os.environ['FUNCTION_VERSION']
    name = "right"
    return functions[name]
