from python_scraper.news_list_generator import news_list_generator
from python_scraper.news_list_generator import news_parser
import subprocess
import argparse


# Set globals:
pagination = 20
out_file = 'out.csv'
out_urls_file = 'links_to_news.txt'
chromedriver_path = './python_scraper/chromedriver'


def parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--pages", type=int, default=pagination,
                    help="Number of pages to scrape.")
    ap.add_argument("-cd", "--chromedriver", default=chromedriver_path,
                    help="Path to chromedriver.")
    ap.add_argument("-f", "--file", default=out_urls_file,
                    help="File to save the news list.")
    ap.add_argument("-o", "--outcsv", default=out_file,
                    help="Number of pages to scrape.")
    args = vars(ap.parse_args())

    return args


if __name__ == '__main__':
    # Python link to news generator:
    args = parser()
    pagination = args['pages']
    chromedriver_path = args['chromedriver']
    out_urls_file = args['file']
    out_file = args['outcsv']

    news_list_generator(chromedriver_path, pagination, out_urls_file)

    # Ruby parser:
    out_file = open(out_file, 'w+')
    with open(out_urls_file, 'r') as in_file:
        articles = in_file.readlines()
        for article in articles:
            command = 'ruby main.rb {}'.format(article)
            subprocess.call(command, shell=True, stdout=out_file)
    out_file.close()
