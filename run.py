from eve import Eve

#fake-useragent will let sending requests as a real browser
from fake_useragent import UserAgent

import requests

UserAgent().chrome

#here there is set with html tags
tagsset = {'<!--', '<!DOCTYPE', '<a', '<abbr', '<address', '<area', '<article', '<aside', '<audio', '<b', '<base', '<bdi', '<bdo', '<body', '<blockquote', 
           '<button', '<br', '<canvas', '<caption', '<cite', '<code', '<col', '<colgroup', '<data', '<datalist', '<dd', '<del', '<details', '<dfn', '<div',
           '<dialog', '<dl', '<dt', '<em', '<embed', '<fieldset', '<figcaption', '<figure', '<footer', '<form', '<head', '<header', '<h1', '<h2', '<h3',
           '<h4', '<h5', '<h6', '<hr', '<html', '<i', '<iframe', '<img', '<input', '<ins', '<kbd', '<label', '<legend', '<li', '<link', '<main', '<map', 
           '<mark', '<meta', '<meter', '<nav', '<noscript', '<object', '<ol', '<optgroup', '<option', '<output', '<p', '<param', '<picture', '<pre', 
           '<progress', '<q', '<ruby', '<rb', '<rt', '<rtc', '<rp', '<s', '<samp', '<script', '<section', '<select', '<small', '<source', '<span', 
           '<strong', '<style', '<sub', '<summary', '<sup', '<table', '<tbody', '<td', '<template', '<textarea', '<tfoot', '<th', '<thead', '<time', '<tr', 
           '<title', '<track', '<u', '<ul', '<var', '<video', '<wbr'}

def pre_tags_post_callback (request):
    print ('A POST request on the tags endpoint has just been received!')
    print (request.json.get('url_id')) #printing url_id from POST request
    url_to_parse = request.json.get('url_input')
#    print (type(url_to_parse)) - here we can check the type url_to_parse - must be 'string'
    
#   here we get html content as a string, so we can make a simple string-searching algorithm
    html_string = requests.get(url_to_parse, headers={'User-Agent': UserAgent().chrome}).text
    
    for tag in tagsset:
        print ((tag) + '>is used')
        print (html_string.count(tag))

app = Eve()

app.on_pre_POST_tags += pre_tags_post_callback

if __name__ == '__main__':
   app.run()