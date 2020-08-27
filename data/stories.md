## Suggestion Path 1

* greet
    - utter_greet
* paper_search
    - utter_what_type
* inform{"paper_type":"Physics"}
    - action_paper_search
    - utter_approve
* affirm
    - utter_send_link
* goodbye
    - utter_goodbye

## Suggestion Path 2
* greet
    - utter_greet
* paper_search{"paper_type": "chatbots"}
    - action_paper_search
    - utter_approve
* affirm+authors
    - utter_send_link
    - utter_authors
* thanks
    - utter_happy_reading
