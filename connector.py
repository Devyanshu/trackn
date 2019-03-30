from pprint import pprint
from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://notifier-be786.firebaseio.com/')


def submit(number, cat):
    mapping = {1: 'laundry', 2: 'courier', 3: 'library'}
    print(number, cat)
    prov = firebase.post('/'+mapping[cat], {'number': number})


'''
gt = firebase.get('/provider', None)

for i in gt:
    print(gt[i]['name'])

pprint(gt)
'''
# firebase.post('/courier', {'name': '7171'})
