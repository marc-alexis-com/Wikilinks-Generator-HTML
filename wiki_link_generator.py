#!/usr/bin/env python3
"""
WikiLinkGenerator: Generate HTML <a> tags linking to Wikipedia articles.

This module provides functionality to search Wikipedia for a given term
in a specified language and generate an HTML anchor tag linking to the
first relevant Wikipedia page.

Usage:
    As a command-line tool:
        python3 wiki_link_generator.py "Search Term" --lang en

    As an imported module:
        from wiki_link_generator import get_wikipedia_link

        html_tag = get_wikipedia_link("Artificial Intelligence", lang="en")
        print(html_tag)
"""

import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse
import argparse

def get_wikipedia_first_link(search_term, lang='en'):
    """
    Searches Wikipedia in the specified language for the given search term
    and returns the URL of the first relevant result.

    Args:
        search_term (str): The term to search for on Wikipedia.
        lang (str): The language code for Wikipedia (default is 'en' for English).

    Returns:
        str or None: The URL of the first search result or None if no result is found.
    """
    # Validate language code
    if not lang.isalpha() or len(lang) > 10:
        print("Invalid language code. Using default 'en'.")
        lang = 'en'
    
    # Encode the search term for use in a URL
    query = urllib.parse.quote(search_term)
    
    # Construct the search URL for the specified language Wikipedia
    url = (
        f'https://{lang}.wikipedia.org/w/index.php?search={query}'
        '&title=Special:Search&go=Go&fulltext=1'
    )
    
    try:
        # Send a GET request to the search URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all search result headings
    search_results = soup.find_all('div', class_='mw-search-result-heading')
    
    # If no search results are found, try to get the canonical link (exact match)
    if not search_results:
        canonical = soup.find('link', rel='canonical')
        if canonical and 'href' in canonical.attrs:
            return canonical['href']
        return None
    
    # Get the first search result link
    first_result = search_results[0].find('a')
    
    # If the first result has an href attribute, construct the full URL
    if first_result and 'href' in first_result.attrs:
        link = urllib.parse.urljoin(f'https://{lang}.wikipedia.org/', first_result['href'])
        return link
    
    return None

def generate_html_a_tag(url, display_text):
    """
    Generates an HTML <a> tag with the given URL and display text.

    Args:
        url (str): The URL for the href attribute.
        display_text (str): The text to display for the link.

    Returns:
        str: An HTML <a> tag.
    """
    return f'<a href="{url}">{display_text}</a>'

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate an HTML <a> tag linking to a Wikipedia article.')
    parser.add_argument('search_term', type=str, help='The term to search for on Wikipedia.')
    parser.add_argument('--lang', type=str, default='en', help='Wikipedia language code (default: en).')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get the first Wikipedia link for the search term in the specified language
    link = get_wikipedia_first_link(args.search_term, args.lang)
    
    if link:
        # Generate HTML <a> tag
        html_a = generate_html_a_tag(link, args.search_term)
        print(html_a)
    else:
        # If no link is found, print the original search term
        print(args.search_term)

if __name__ == "__main__":
    main()