# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# source venv/bin/activate

# npx kill-port 5055

# python -m rasa_sdk --actions actions

# http://localhost:5055/health
# http://localhost:5055/actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_inform_restaurant"

    def run(self, dispatcher, tracker, domain):

        ## prod = tracker.get_slot('product')
        price = tracker.get_slot('price')
        name =  "Mr.Hamza" # later generate through some process

        response = """Your price {} is ordered for you. It will be shipped to your address. Your confirmation number is {}""".format(
            price, name)

        dispatcher.utter_message(text=response)
        return []


    '''
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    '''