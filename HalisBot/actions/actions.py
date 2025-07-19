# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionJournalPrompt(Action):
    def name(self) -> str:
        return "action_journal_prompt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        prompts = [
            "What’s something you’ve survived that you don’t give yourself enough credit for?",
            "What’s been taking up the most space in your mind lately—and why?",
            "What do you wish someone had said to you when you were younger?",
            "How have you changed in the last year—and what caused that change?",
            "What parts of you are growing, even if you can’t see it yet?"
        ]

        chosen_prompt = random.choice(prompts)
        dispatcher.utter_message(text=f"Here’s a journal prompt for you:\n\n*{chosen_prompt}*")

        return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime

class ActionStoreJournal(Action):
    def name(self) -> str:
        return "action_store_journal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        user_message = tracker.latest_message.get('text')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to file (you can switch to database later)
        with open("journal_log.txt", "a", encoding='utf-8') as f:
            f.write(f"{timestamp} - {user_message}\n")

        dispatcher.utter_message(text="Thanks for sharing. That took courage. I've saved that for you.")

        return [SlotSet("journal_response", user_message)]