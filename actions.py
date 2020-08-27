# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionPaperSearch(Action):

    def name(self) -> Text:
        return "action_paper_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        paper_type = tracker.get_slot("paper_type")
        link = f"https://www.revolut.com/link={paper_type}.pdf"
        dispatcher.utter_message(text=link)

        return [ SlotSet("link", link) ]
