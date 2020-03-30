## happy path 1
* greeting: selam
    - utter_greet
* search_restaurant: Ankara'da ucuz kebap restoranları   <!-- predicted: search_restaurant: [Ankara](city)'da [ucuz](price) [kebap](cuisine) restoranları -->
    - utter_inform_restaurant_cuisine   <!-- predicted: utter_inform_restaurant_rating -->
* closing: bye
    - utter_close


