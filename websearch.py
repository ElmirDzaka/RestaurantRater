import sys
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def main(argv):
    #hard code url for testing for now 
    #mexican testaurants salt lake city
    url = "https://www.google.com/search?q=mexican+restaurants+salt+lake+city&biw=1920&bih=937&tbm=lcl&sxsrf=AB5stBiGgszI3DR2usnoki1IvhrmZb5a5Q%3A1688619334295&ei=RkmmZMrUEZXNkPIP4oyM6Aw&oq=mexican+restaurants+salt+lake+&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMYADIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgQIIxAnOgsIABCABBCxAxDJAzoICAAQgAQQkgM6CwgAEIoFEJIDEIsDUKkGWIwOYKQUaABwAHgAgAFUiAHGBpIBAjEymAEAoAEBuAECwAEB&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[40.7954642,-111.8854613],[40.7217882,-111.9439294]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!1m4!1u22!2m2!21m1!1e1!2m1!1e2!2m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:9"
    get_results(url)

def get_results(url):
    """Return the source code for the provided URL. 
    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv[1:]) 