import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjTwo.settings')

import django
django.setup()

# Fake POP SCRIPT
import random
from appTwo.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t

def populate(N = 5):
    for entry in range(N):

        # Get the topic for each entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic= top, url = fake_url, name = fake_name)[0]

        # create the fake access record for that page
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date= fake_date)[0]
        
if __name__ == '__main__':
    print("Populating database!")
    populate(20)
    print("populating database has been completed")


