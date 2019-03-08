from selenium import webdriver
from time import sleep
import argparse

# Download and install Chromedriver:
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# Global:
pagination = 5
out_file = 'links_to_news.txt'
chromedriver_path = './chromedriver'  # For downloaded version

# Chromedriver settings:
verbose = True
options = webdriver.ChromeOptions()
if not verbose:
    options.add_argument('headless')


# Construct the argument parser:
def news_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--pages", type=int, default=pagination,
                    help="Number of pages to scrape.")
    ap.add_argument("-cd", "--chromedriver", default=chromedriver_path,
                    help="Path to chromedriver.")
    ap.add_argument("-f", "--file", default=out_file,
                    help="File to save the news list.")
    args = vars(ap.parse_args())

    return args


def news_list_generator(chromedriver_path, pagination, out_file):
    # Browser launch with chromedriver:
    # browser = webdriver.Chrome(chrome_options=options)

    # Or for downloaded version (from specific path):
    browser = webdriver.Chrome(executable_path=chromedriver_path,
                               chrome_options=options)

    # Set url and open it on Chrome:
    url = 'https://www.am.com.mx/seccion/noticias/'
    browser.get(url)

    # Search molecule:
    sleep(2)
    flag = scrape_news(browser, pagination, out_file)

    # Close browser:
    browser.quit()
    return


def scrape_news(browser, pagination, out_file):
    # Look for button and click it:
    button_xpath = '//*[@class="viewmore"]/button'
    browser.find_element_by_xpath(button_xpath).click()
    sleep(1)

    # Get links to news in an iterative way according to pagination:
    with open(out_file, "w+") as fout:
        displayed_news_per_view = 8
        initial_article_index = 6
        for view in range(pagination):
            view *= displayed_news_per_view
            for index in range(displayed_news_per_view):
                xpath = '//*[@class="col__main"]/article[{}]/div/h2/a'
                xpath = xpath.format(initial_article_index + view + index)
                news = browser.find_element_by_xpath(xpath)
                news_url = news.get_attribute('href')
                fout.write(news_url + '\n')

            # Search for button again:
            browser.find_element_by_xpath(button_xpath).click()
            sleep(1)

    return


if __name__ == '__main__':
    args = news_parser()
    pages = args['pages']
    out_file = args['file']
    news_list_generator(chromedriver_path, pages, out_file)
