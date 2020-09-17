import bs4 as bs
import io
import pandas as pd
import requests
from requests.compat import urljoin

def print_classes():
    classes = pd.read_pickle('swg-grm-extractor/data/classes.pkl')
    for i, c in classes.iterrows():
        print(i, c['description'])
    #print(classes)

def print_server_list(url):
    servers = []
    response = requests.get(urljoin(url, '/resources/'))
    soup = bs.BeautifulSoup(response.content, 'html.parser')
    servers = soup.find('select', id='server').find_all('option')
    
    for server in servers[1:]:
        print(server.text, ':', server.attrs['value'])

def get_resources_classes(url):
    params = { 'file' : 'resourcetree.csv' }
    response = requests.get(urljoin(url, 'dev/sendfile.php'), params=params)
    classes = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    classes = classes[['swgcraft_id', 'description']]
    
    return classes

def get_resources_mapping(url):
    params = { 'file' : 'class_map.csv' }
    response = requests.get(urljoin(url, 'dev/sendfile.php'), params=params)
    mapping = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    
    return mapping

def aggregate_classes(classes, mapping):
    result = pd.merge(classes, mapping, how='inner', on='swgcraft_id')
    result.set_index('internal_id').sort_index().to_pickle('swg-grm-extractor/data/classes.pkl')

def get_resources(url, server):
    resources = [__aggregate_resource(url, server, i) for i in range(1, 4)]
    
    pd.concat(resources, sort=False).to_pickle('swg-grm-extractor/data/resources.pkl')

def __scrape_resource(url, server, class_id, page, start):
    params = { 'server': server, 'class': class_id, 'page': page, 'start': start }
    response = requests.get(urljoin(url, '/resources/find.php'), params=params)
    soup = bs.BeautifulSoup(response.content, 'html.parser')
    resources = pd.read_html(str(soup.find('table', id='restree')))
    return resources[0]

def __aggregate_resource(url, server, class_id):
    start = 0
    page = 1
    tables = []

    while True:
        try:
            tables.append(__scrape_resource(url, server, class_id, page, start))
            start = page * 50
            page += 1
        except:
            break
    resource = pd.concat(tables, sort=False)
    
    return resource
        