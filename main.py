import asyncio, aiohttp
import os, re
from time import perf_counter

def clear(numlines=100):
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print('\n' * numlines)
    
def generate_urls(tag, page_count):
    base_url = f'https://mrcong.com/tag/{tag}'
    urls = [base_url]
    urls.extend(f'{base_url}/page/{i}' for i in range(2, page_count + 1))
    return urls

def parse(pattern, html):
    results = []
    for url in html:
        results.extend(iter(re.findall(pattern, url)))
    return results

async def get_html(url, session):
    async with session.get(url) as response:
        return await response.text()

async def tasker(urls, session):
    tasks = [get_html(url, session) for url in urls]
    return await asyncio.gather(*tasks)

async def make_session(urls):
    async with aiohttp.ClientSession() as session:
        return await tasker(urls, session)

def urls_method():
    gen_urls = input('Choose method to generate url (Type "1" to generate url, type "2" to use list of urls): ')

    if gen_urls == '1':
        tag = input('Input tag that you want to scrape: ')
        page_count = input('How many page you want to scrape: ')
        return generate_urls(tag, int(page_count))
    elif gen_urls == '2':
        txt_file = input('Input txt file that contains list of urls: ')
        with open(txt_file, 'r') as f:
            return f.read().split()
    else:
        print('Choose correct options!!!')
        return urls_method()

def pattern_method():
    pattern =['post\-box\-title\"\>\s+\<a\shref\=\"(.*?)\"', '\<a\shref\=\"(.*?)\starget\=\"\_blank\"\sclass\=\"shortc\-button\smedium\s']
    
    pattern_use = input('Which regex pattern to use? (Type "1" to find posts url, type "2" to find downloads url): ')
    if pattern_use == '1':
        return pattern[0]
    elif pattern_use == '2':
        return pattern[1]
    else:
        print('Choose correct options!!!')
        return pattern_method()
    
def main():
    clear()
    urls = urls_method()
    pattern = pattern_method()
    filename = input('Input filename to store the results: ')
    
    start = perf_counter()
    html = asyncio.run(make_session(urls))
    results = parse(pattern, html)

    with open(filename, 'w') as outfile:
        for url in results:
            outfile.write(f'{url}\n')

    end = perf_counter()
    time_consumed = end - start

    print(f'Total items scraped: {len(results)}
    print(f'Results saved to {filename}')
    print(f'Time consumed: {time_consumed}')

if __name__ == '__main__':
    while True:
        main()
        if input('Scrape again? (Press enter to continue, type "No" to exit): ') == 'No':
            exit()
