# .\venv\Scripts\activate

# source venv/bin/activate

# rasa run actions & rasa shell -m models --endpoints endpoints.yml

# npx kill-port 5055

# python -m rasa_sdk --actions actions

# http://localhost:5055/health
# http://localhost:5055/actions

# rasa interactive --debug --skip-visualization

# rasa train --augmentation 0

# rasa data validate stories --max-history 10

# rasa test nlu -f 5 --cross-validation

# tensorboard --logdir /Users/volkanozer/Documents/GitHub/VenueBot/tensorboard
# http://localhost:6006/

# This is a simple example for a custom action which utters "Hello World!"

# -*- coding: utf-8 -*-
import json
import requests

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction, REQUESTED_SLOT



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_inform_restaurant"

    def run(self, dispatcher, tracker, domain):
        price = tracker.get_slot('price')
        rating = tracker.get_slot('rating')
        city = tracker.get_slot('city')
        district = tracker.get_slot('district')
        neighborhood = tracker.get_slot('neighborhood')
        restaurant_name = tracker.get_slot('restaurant_name')
        region = tracker.get_slot('region')
        cuisines = tracker.get_slot('cuisines')

        print(price,rating,city,district,neighborhood,restaurant_name,region,cuisines)

        host = 'http://127.0.0.1:8000/'
        
        url = host + "api/post/rasaGetVenues/"

        data = json.dumps({
            "price": price,
            "rating": rating,
            "city": city,
            "district": district,
            "neighborhood": neighborhood,
            "restaurant_name": restaurant_name,
            "region": region,
            "cuisines": cuisines
        })
        response = requests.post(url, data=data).json()

        fields = "-".join([price, rating, city, district, neighborhood, restaurant_name, region, cuisines])

        field_data = "inform:" + fields


        print("---->", response[0]["description"][0]+";"+field_data)

        fields = json.dumps({
            "city_id": response[0]["city"],
            "district_id": response[0]["district"],
            "neighborhood_id": response[0]["neighborhood"],
            "price": response[0]["price"],
            "rating": response[0]["rating"],
            "description": response[0]["description"][0]
        })

        dispatcher.utter_message(text=fields)

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []


class ActionFilter(Action):

    def name(self) -> Text:
        return "action_send_filter"

    def run(self, dispatcher, tracker, domain):
        price = tracker.get_slot('price')
        rating = tracker.get_slot('rating')
        city = tracker.get_slot('city')
        district = tracker.get_slot('district')
        neighborhood = tracker.get_slot('neighborhood')
        restaurant_name = tracker.get_slot('restaurant_name')
        region = tracker.get_slot('region')
        cuisines = tracker.get_slot('cuisines')

        print(price, rating, city, district, neighborhood, restaurant_name, region, cuisines)

        host = 'http://127.0.0.1:8000/'

        url = host + "post/rasaGetVenues/"

        fields = "-".join([price, rating, city, district, neighborhood, restaurant_name, region, cuisines])
        print(fields)
        data = "inform:"+fields

        dispatcher.utter_message(text=data)

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
