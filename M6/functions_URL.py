"""
Author: Lee Taylor

Example usage from my Data-Science Hackathon:
https://github.com/LeeTaylorNewcastle/Data-Science-Hackathon-02-03-2023
"""
import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
import re
from perform_set_expansion import read_words_from_file

INTERVAL = 3600
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}


def url_to_soup_obj(url: str) -> BeautifulSoup | None:
    """

    :param url:
    :return:
    """
    try:
        page = requests.get(url, headers=HEADERS)
    except:
        print(f"<ERROR: {url}>")
        return
    # except requests.exceptions.MissingSchema:
    #     print(f"\n[WARINING] - <link: {url}> - INVALID!")
    #     print("LINK DOES NOT CONTAIN PROTOCOL i.e 'https://'")
    #     return
    return bs(page.content, 'html5lib')


def extract_elements(html_text, elm='p'):
    """

    :param html_text:
    :param elm:
    :return:
    """
    soup = bs(html_text, 'html.parser')
    paragraphs = []
    for p in soup.find_all(elm):
        paragraphs.append(p.text.strip())
    return paragraphs


def google_search_wikipedia(search_str: str, debug: bool = True):
    """

    :param debug:
    :param search_str:
    :return:
    """
    # Convert search to google search URL
    gsearch_url = f"https://www.google.com/search?q={'+'.join(search_str.lower().split())}"
    # Generate 'soup' object of google search
    gsearch_soup = url_to_soup_obj(gsearch_url)
    # Debug info
    if debug:
        ...
        # print(gsearch_soup)
    # Extract URLs
    elms = extract_elements(str(gsearch_soup), elm='cite')
    href = extract_elements(str(gsearch_soup), elm='a')
    # Debug info
    if debug:
        print(f"href-list: {href}")
    # Store 'cite' and 'a' elements in elms list
    for item in href:
        elms.append(item)
    # For-loop extracts URLs into list
    urls_ = []
    for string in elms:
        # Skip blank strings
        if string == '':
            continue
        # Debug info
        if debug:
            ...
            print(f"debug-string-in-elms: {string}, {string.split()}")
        # String must contain 'https:' but not '...' and 'category'
        if string.split()[0].__contains__("https:") and \
                not string.split()[-1].__contains__('...') and \
                not string.lower().__contains__('category'):
            # Convert arrows to slashes for URL functionality
            string = string.replace(' ', '')
            urls_.append(string.replace('›', '/'))
    # Return list of URLs
    return list(set(urls_))


def remove_code(text):
    """

    :param text:
    :return:
    """
    # Use a regular expression to find any instances of code and scripts
    code = re.findall(r'<.*?>', text)
    # Remove all instances of code and scripts from the text
    clean_text = re.sub(r'<.*?>', '', text)
    # Return the resulting text
    return clean_text


def extract_text(soup, headers=True, debug=True):
    """

    :param soup:
    :param headers:
    :return:
    """
    # Find all HTML elements that contain the main content
    if headers:
        content_elements = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5",
                                          "h6", "a", "li", "span", "strong", "em"])
    elif not headers:
        content_elements = soup.find_all(["p", "a", "li", "span", "strong", "em"])
    # Concatenate the text from all content elements
    content = [element.text.strip() for element in content_elements]
    for i, v in enumerate(content):
        content[i] = v.replace('\n', '')
        content[i] = content[i].replace('  ', '')
    # Remove keywords
    content = [element for element in content if element.strip() != '']  # Remove blanks
    content = [element for element in content if len(element.split()) > 9]  # Remove lines with less than X words
    content = [element for element in content if not element.lower().__contains__('site')]
    content = [element for element in content if not element.lower().__contains__('cookie')]
    content = [element for element in content if not element.lower().__contains__('sign in')]
    content = [element for element in content if not element.lower().__contains__('instagram')]
    content = [element for element in content if not element.lower().__contains__('contact us')]
    # print(content)
    # Combine content into a string
    content = '\n'.join(set(content))
    content = remove_code(content)
    if debug:
        print(content)
    # content = [element for element in content if len(element) != '']
    # Return the resulting text
    return content


def query_to_text(search_str, page_limit=3, debug=True):
    """

    :param page_limit:
    :param search_str:
    :param debug:
    :return:
    """
    # Define storage for extracted text
    rv = []
    # Extract URLs to scrape from
    urls = google_search_wikipedia(search_str=search_str)
    # For each URL append extracted readable text
    for url in urls[:page_limit]:
        if debug:
            print(url)
        soup_url = url_to_soup_obj(url)
        if soup_url is None:
            return ['']
        rv.append(extract_text(soup_url))
    # Mark EOF
    return rv


def write_to_file(fn, text):
    """

    :param fn:
    :param text:
    """
    with open(fn, "w", encoding='utf-8-sig') as f:
        for elm in text:
            f.write(str(elm) + '\n')


if __name__ == '__main__':
    # # Example usage URL and .html processing and storage (for later)
    # urls = URL_Functions.google_search(search_str=company_name)
    # soup = URL_Functions.url_to_soup_obj(urls[0])
    # text = URL_Functions.extract_text(soup, headers=False)

    # Read list of words to search
    entity_set = read_words_from_file('data_prep/entity_set.txt')
    # Parse webapage for text
    for word in entity_set:
        try:
            search_term = f'wikipedia {word}'
            parsed_webpage_text = query_to_text(search_term, debug=False)
            write_to_file(f"scrapings/{search_term}.txt", parsed_webpage_text)
        except:
            print(f"'{word}' could not be written to a file!")

    # # Parse webapage for text
    # parsed_webpage_text = query_to_text("wikipedia psychology")
    # write_to_file("wikipedia psychology.txt", parsed_webpage_text)

    # Mark end of if-name-main section
    pass
