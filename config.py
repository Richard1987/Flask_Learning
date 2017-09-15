CSRF_ENABLED = True
SECRET_KEY = 'pptv-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google','url':'http://www.google.com/accounts/o8/id'},
    {'name':'Yahoo','url':'https://me.yahoo.com'},
    {'name':'AOL','url':'http://openid.aol.com/<username>'},
    {'name':'Flickr','url':'http://www.flickr.com/<username>'},
    {'name':'MyOpenID','url':'https://www.myopenid.com'}
]




##leaning_document_URL:http://www.pythondoc.com/flask-mega-tutorial/helloworld.html