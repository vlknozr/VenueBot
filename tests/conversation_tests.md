#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greeting: selam
  - utter_greet
* search_restaurant: Ankara'da ucuz kebap restoranları
  - utter_inform_restaurant_cuisine
* closing: bye
  - utter_close

