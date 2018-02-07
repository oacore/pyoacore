from pyoacore.apis.articles_api import ArticlesApi
from pyoacore.configuration import Configuration
import csv
import sys
import argparse

if __name__ == '__main__':

    page = 1
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', default='enter_your_key')
    parser.add_argument('--repo_id', help='add the repository id you want to dump')

    args = parser.parse_args()
    print(args.api_key)
    config = Configuration()
    config.api_key = {"apiKey": args.api_key}
    apis = ArticlesApi()
    with open('results/' + args.repo_id + "-articles.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        res = apis.articles_search_api_call(query="repositories.id:" + args.repo_id, page=page,
                                            pageSize=1000, fulltext=False)
        while res or len(res) != 0:
            for article in res:
                if article:
                    print(article['id'])
                    writer.writerow([article['id'], article['title'], article['authors'], article.get('doi', ''),
                                     article['year']])
            page += 1
            res = apis.articles_search_api_call(query="repositories.id:" + args.repo_id, page=page, pageSize=1000,
                                                fulltext=False)
