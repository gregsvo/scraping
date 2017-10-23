import os

bash_scrapy = 'scrapy crawl jobs -o test.json'

def main():
    os.system(bash_scrapy)

if __name__ == '__main__':
    main()