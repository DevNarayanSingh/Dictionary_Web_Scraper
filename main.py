import re
import html
import urllib.error
from urllib import request
from typing import Literal
_SEARCH_DIRECTION = Literal["left", "right"]


def find_tag_pos(data, tag, pos, direction: _SEARCH_DIRECTION = "right"):
    if direction == "left":
        print("tag: ", tag)
        print("starting pos: ", pos)
        try:
            return data[:pos].rindex(data, pos)
        finally:
            print("not found")
            return pos

    return data.find(tag, pos)


def get_content_between_tags(data, keyword_pos, tag):
    stack = []
    starting_pos = keyword_pos  # find_tag_pos(data, tag, keyword_pos, "left")
    tag_data = data[starting_pos]
    current_pos = starting_pos + 1

    while True:
        if data[current_pos:current_pos + len(f"<{tag}>")] == f"<{tag}>":
            stack.append("<")
        elif data[current_pos:current_pos + len(f"</{tag}>")] == f"</{tag}>":
            if len(stack) == 0:
                break
            stack.pop()

        tag_data += data[current_pos]
        current_pos += 1
        if current_pos > len(data):
            break

    return tag_data


def get_refined_data_without_tags(data):
    include_data = True
    new_data = ""
    for i in range(len(data)):
        x = data[i]
        if x == "<" or (x == "\n" and data[i+1] == "."):
            include_data = False
        elif x == ">" or x == "\n":
            include_data = True
            new_data.strip()
            new_data += "\n"
            continue
        if include_data:
            new_data += x

    return re.sub(r"\n+", "\n", new_data)


if __name__ == '__main__':
    print('Starting of the program')
    word_entered = input("Enter word to search the meaning of: ").lower()
    # url_string = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_entered}"  # api not responding, thus using:
    url_string = f"https://www.dictionary.com/browse/{word_entered}"
    html_data = ""
    try:
        req = request.Request(url_string)
        #, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8'})
        # /AppleWebKit/534.50.2 (KHTML, like Gecko) Version/5.0.6 Safari/533.22.3'})
        html_data = request.urlopen(req).read()
    except urllib.error.HTTPError:
        print("word not found")
        exit()

    html_decoded = html_data.decode("utf-8")
    content_keyword = "<div value=\"1\""
    # content_keyword = "<section class=\"css-109x55k e1hk9ate4"
    content_location = html_decoded.find(content_keyword)
    if content_location == -1:
        print("Content Not Found")
        exit()
    # print(len(html_decoded))
    content_from_tag = get_content_between_tags(html_decoded, content_location, "div")
    # print(repr(get_refined_data_without_tags(content_from_tag)))
    refined_data = get_refined_data_without_tags(content_from_tag)
    html.unescape(refined_data)
    print(refined_data)
