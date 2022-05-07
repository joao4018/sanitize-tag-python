# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def sanitize(json, is_value=True, tag_removal=''):

    if isinstance(json, dict) and tag_removal in json.keys() and is_value:
        del json[tag_removal]
    elif isinstance(json, dict) and tag_removal not in json.keys() and is_value:
        json = {sanitize(k, False, tag_removal): sanitize(v, True, tag_removal) for k, v in json.items()}
    elif isinstance(json, list):
        json = [sanitize(v, True, tag_removal) for v in json]

    return json


if __name__ == '__main__':
    value = {
        "column": {
            "columns": [
                {
                    "data": "Doc.",
                    "title": "Doc."
                },
                {
                    "data": "Order no.",
                    "title": "Order no."
                },
                {
                    "data": "Nothing",
                    "title": "data"
                }
            ],
            "columns2": [
                {
                    "data": "Doc.",
                    "title": "Doc."
                },
                {
                    "data": "Order no.",
                    "title": "Order no."
                },
                {
                    "data": "Nothing",
                    "title": "Nothing"
                }
            ]
        },
        "data": [
            {
                "Doc.": "564251422",
                "Nothing": 0.0,
                "Order no.": "56421"
            },
            {
                "Doc.": "546546545",
                "Nothing": 0.0,
                "Order no.": "98745"
            }
        ]
    }
    tags = ['columns','column']
    for v in tags:
        value = sanitize(value, True, v)
    sanitize(value)
    print(sanitize(value))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
