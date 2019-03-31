
from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://notifier-be786.firebaseio.com/', None)


def submit(number, cat):
    mapping = {1: 'Laundry', 2: 'Courier', 3: 'Library'}
    print(number, cat)
    prov = firebase.put('/', '/', {'number': number, 'type': mapping[cat]})


def griev():
    return firebase.get("/", None)


'''
gt = firebase.get('/provider', None)

for i in gt:
    print(gt[i]['name'])

pprint(gt)
'''
