__author__ = 'dl'
__version__= '1.0'

import urllib,sys
from lxml import etree
from lxml.html import document_fromstring
import logging


def enablelog():
    log=logging.getLogger('main')
    if (len(log.handlers)==0):
        log.setLevel(logging.DEBUG)
        log.addHandler(logging.StreamHandler(sys.stdout))
    return log

def loadxml(url):
    '''
    Loading XML to cortage (categories[],products[])
    '''
    log=enablelog()
    log.info('Loading XML from %s'%(url))
    page=urllib.urlopen(url)
    root=etree.XML(page.read())
    nodes_version=root.xpath('/load')
    categories,products=[],[]
    try:
        version=nodes_version[0].get('version')
        if (version==__version__):
            nodes_categories=root.xpath('/load/categories/item')
            for node in nodes_categories:
                categories.append({'id':node.get('id'),'name':node.get('name'),'parent':node.get('parent')})
            nodes_products=root.xpath('/load/products/item')
            for node in nodes_products:
                products.append({'id':node.get('id'),'name':node.get('name'),'category':node.get('category'),'cost':node.get('cost'),'count':node.get('count')})
            log.info('Load complete. Categories ({%s}).Products ({%s})'%(len(categories),len(products)))
        else:
            log.critical('Error in version check your version in <load version=%s> required %s'%(version,__version__))
    except Exception, e:
            log.critical(e)
    return (categories,products);
