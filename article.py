import wikipedia
import string


def get_random_article_title():
    article_title = wikipedia.random(1)
    return article_title


def get_content_from_title(title):
    content = wikipedia.page(title, auto_suggest=False).content
    return content


##### DATA/STAT MODULE #####

def count_of_words(content):
    words = content
    return len(words)


def count_of_images(title):
    images = wikipedia.page(title, auto_suggest=False).images
    return len(set(images))


def count_of_hyperlinks(title):
    links = wikipedia.page(title, auto_suggest=False).links
    return len(links)


def get_rid_of_punctuation_with_numbers(content):
    text_without_punctuation = ""
    for char in content:
        if char in string.ascii_letters + string.digits + string.whitespace:
            text_without_punctuation += char
    return text_without_punctuation


def get_rid_of_punctuation_without_numbers(content):
    text_without_punctuation = ""
    for char in content:
        if char in string.ascii_letters + string.whitespace:
            text_without_punctuation += char
    return text_without_punctuation


def length_of_longest_word(content):
    content_without_special_characters = get_rid_of_punctuation_without_numbers(content)
    longest_word = max(content_without_special_characters.split(), key=len)
    return len(longest_word)


def highest_number_on_page(content):
    content_without_special_characters = get_rid_of_punctuation_with_numbers(content)
    number_list = []
    for item in content_without_special_characters.split():
        if item.isnumeric():
            number = int(item)
            number_list.append(number)
    if not number_list:
        return 1000
    return max(number_list)


def lowest_number_on_page(content):
    content_without_special_characters = get_rid_of_punctuation_with_numbers(content)
    number_list = []
    for item in content_without_special_characters.split():
        if item.isnumeric():
            number = int(item)
            number_list.append(number)
    if not number_list:
        return 10
    return min(number_list)


def get_article_stats(title, article_content):
    stats = {"Count of words": count_of_words(article_content),
             "Count of images": count_of_images(title),
             "Count of hyperlinks": count_of_hyperlinks(title),
             "Length of longest word": length_of_longest_word(article_content),
             "Highest number on page": highest_number_on_page(article_content),
             "Lowest number on page": lowest_number_on_page(article_content)}
    return stats


def prep_article_data():
    while True:
        try:
            title = get_random_article_title()
            content = get_content_from_title(title)
        except wikipedia.exceptions.DisambiguationError:
            continue
        stats = get_article_stats(title, content)
        return title, stats


