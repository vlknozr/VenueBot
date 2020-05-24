## 1
* greeting
  - utter_greeting
  - utter_guide
* request{"price": "uygun"}
  - slot{"price": "uygun"}
  - utter_request
* inform{"cuisine": "Doğu yemekleri"}
  - slot{"cuisine": "Doğu yemekleri"}
  - action_inform_restaurant
* closing
  - utter_closing

## 2
* greeting
  - utter_greeting
  - utter_guide
* request{"rating": "memnun"}
  - slot{"rating": "memnun"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 3
* greeting
  - utter_greeting
  - utter_guide
* request{"restaurant_name": "Starbucks"}
  - slot{"restaurant_name": "Starbucks"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 4
* greeting
  - utter_greeting
  - utter_guide
* request{"venue_type": "restoran"}
  - slot{"venue_type": "restoran"}
  - action_inform_restaurant
* closing
  - utter_closing

## 5
* greeting
  - utter_greeting
  - utter_guide
* request{"cuisine": "kebap"}
  - slot{"cuisine": "kebap"}
  - action_inform_restaurant
* closing
  - utter_closing

## 6
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "İstanbul", "district": "Şişli"}
  - slot{"city": "İstanbul", "district": "Şişli"}
  - action_inform_restaurant
* closing
  - utter_closing

## 7
* greeting
  - utter_greeting
  - utter_guide
* request{"price": "uygun", "rating": "iyi"}
  - slot{"price": "uygun", "rating": "iyi"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 8
* greeting
  - utter_greeting
  - utter_guide
* request{"price": "ucuz", "cuisine": "balık"}
  - slot{"price": "ucuz", "cuisine": "balık"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 9
* greeting
  - utter_greeting
  - utter_guide
* request{"price": "pahalı", "venue_type": "restoran"}
  - slot{"price": "pahalı", "venue_type": "restoran"}
  - utter_request
* inform{"cuisine": "deniz ürünleri"}
  - slot{"cuisine": "deniz ürünleri"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 10
* greeting
  - utter_greeting
  - utter_guide
* request{"rating": "memnun", "cuisine": "ızgara"}
  - slot{"rating": "memnun", "cuisine": "ızgara"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 11
* greeting
  - utter_greeting
  - utter_guide
* request{"rating": "çok memnun", "venue_type": "bar"}
  - slot{"rating": "çok memnun", "venue_type": "bar"}
  - action_inform_restaurant
* closing
  - utter_closing

## 12
* greeting
  - utter_greeting
  - utter_guide
* request{"venue_type": "restoran", "cuisine": "kafeterya ürünleri"}
  - slot{"venue_type": "restoran", "cuisine": "kafeterya ürünleri"}
  - action_inform_restaurant
* closing
  - utter_closing

## 13
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "Eskişehir", "district": "Tepebaşı", "neighborhood":"Mamure"}
  - slot{"city": "Eskişehir", "district": "Tepebaşı", "neighborhood":"Mamure"}
  - action_inform_restaurant
* closing
  - utter_closing

## 14
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "Eskişehir", "district": "Odunpazarı", "cuisine":"döner"}
  - slot{"city": "Eskişehir", "district": "Odunpazarı", "cuisine":"döner"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 15
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "İzmir", "cuisine":"tatlı"}
  - slot{"city": "İzmir", "cuisine":"tatlı"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 16
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "İstanbul", "district": "Ortaköy", "price":"ucuz"}
  - slot{"city": "İstanbul", "district": "Ortaköy", "price":"ucuz"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 17
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "İstanbul", "district": "Şişli", "rating":"iyi"}
  - slot{"city": "İstanbul", "district": "Şişli", "rating":"iyi"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 18
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "İstanbul", "district": "Şişli", "neighborhood": "Teşvikiye", "rating":"memnun"}
  - slot{"city": "İstanbul", "district": "Şişli", "neighborhood": "Teşvikiye", "rating":"memnun"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 19
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "İstanbul", "district": "Şişli", "neighborhood": "Teşvikiye", "rating":"memnun", "price":"pahalı", "cuisine":"kebap"}
  - slot{"city": "İstanbul", "district": "Şişli", "neighborhood": "Teşvikiye", "rating":"memnun", "price":"pahalı", "cuisine":"kebap"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 20
* greeting
  - utter_greeting
  - utter_guide
* request{"city": "Adana", "district": "Seyhan", "rating":"memnun", "price":"pahalı", "cuisine":"kebap"}
  - slot{"city": "Adana", "district": "Seyhan", "rating":"memnun", "price":"pahalı", "cuisine":"kebap"}
  - action_inform_restaurant
* closing
  - utter_closing
  
## 21
* greeting
  - utter_greeting
  - utter_guide
* request{"cuisine": "suşi", "rating": "iyi"}
  - slot{"cuisine": "suşi", "rating": "iyi"}
  - utter_request
* inform{"city": "İzmir", "district": "Çeşme"}
  - slot{"city": "İzmir", "district": "Çeşme"}
  - action_inform_restaurant
* closing
  - utter_closing

## interactive_story_1
* request{"greeting": "Merhaba", "price": "ortalama", "cuisine": "pizza"}
    - slot{"cuisine": "pizza"}
    - slot{"greeting": "Merhaba"}
    - slot{"price": "ortalama"}
    - utter_greeting
    - utter_request
* inform+request{"city": "İstanbul", "district": "Şişli", "rating": "güzel"}
    - slot{"city": "İstanbul"}
    - slot{"district": "Şişli"}
    - slot{"rating": "güzel"}
    - action_inform_restaurant
* closing+confirm{"closing": "Bye"}
    - slot{"closing": "Bye"}
    - utter_closing

## interactive_story_2
* greeting
    - utter_greeting
    - utter_guide
* request{"date": "Bugün", "rating": "güzel", "cuisine": "pizzacı", "price": "uygun"}
    - slot{"cuisine": "pizzacı"}
    - slot{"date": "Bugün"}
    - slot{"price": "uygun"}
    - slot{"rating": "güzel"}
    - action_inform_restaurant
* request{"cuisine": "dondurma"}
    - slot{"cuisine": "dondurma"}
    - action_inform_restaurant
* confirm_restaurant
    - utter_closing

## interactive_story_3
* request{"city": "Ankara", "district": "Kızılay", "price": "ucuz", "cuisine": "kebap"}
    - slot{"city": "Ankara"}
    - slot{"cuisine": "kebap"}
    - slot{"district": "Kızılay"}
    - slot{"price": "ucuz"}
    - action_inform_restaurant
* request{"rating": "yüksek", "cuisine": "kebap"}
    - slot{"cuisine": "kebap"}
    - slot{"rating": "yüksek"}
    - action_inform_restaurant
    - utter_multiple_choice
* confirm{"rank": "ilk", "venue_type": "restoran"}
    - slot{"rank": "ilk"}
    - slot{"venue_type": "restoran"}
    - utter_confirm
