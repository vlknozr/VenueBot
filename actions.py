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

        host = 'http://127.0.0.1:8000/'
        
        url = host + "api/post/getVenuesAround/"

        data = json.dumps({"neighborhood": "40700", "cuisine": [1, 2, 3], "price": "4", "rating": "1"})
        response = requests.post(url, data=data).json()
        print("---->", response[0]["description"][0])

        dispatcher.utter_message(text=response[0]["description"][0])

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
