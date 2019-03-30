from pprint import pprint
from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://notifier-be786.firebaseio.com/')


def submit(number, cat):
    print(number, cat)
    prov = firebase.post('/'+str(cat.strip()), {'number': number})


'''
gt = firebase.get('/provider', None)

for i in gt:
    print(gt[i]['name'])

pprint(gt)
'''
# firebase.post('/courier', {'name': '7171'})
