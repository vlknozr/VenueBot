## 1
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"price": "uygun"}
  - utter_inform_restaurant_price
* closing
  - utter_close

## 2
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"rating": "memnun"}
  - utter_inform_restaurant_rating
* closing
  - utter_close
  
## 3
* greeting
  - utter_greet
  - utter_guide
* request{"restaurant_name": "Starbucks"}
  - utter_inform_restaurant_cuisine
* closing
  - utter_close
  
## 4
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"venue_type": "restoran"}
  - utter_inform_restaurant_price
* closing
  - utter_close

## 5
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"cuisine": "kebap"}
  - utter_inform_restaurant_rating
* closing
  - utter_close

## 6
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "İstanbul", "district": "Şişli"}
  - utter_inform_restaurant
* closing
  - utter_close

## 7
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"price": "uygun", "rating": "iyi"}
  - utter_inform_restaurant_price
* closing
  - utter_close
  
## 8
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"price": "ucuz", "cuisine": "balık"}
  - utter_inform_restaurant_rating
* closing
  - utter_close
  
## 9
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"price": "pahalı", "venue_type": "restoran"}
  - utter_ask_cuisine
* inform{"cuisine": "deniz ürünleri"}
  - utter_inform_restaurant_price
* closing
  - utter_close
  
## 10
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"rating": "memnun", "cuisine": "ızgara"}
  - utter_inform_restaurant
* closing
  - utter_close
  
## 11
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"rating": "çok memnun", "venue_type": "bar"}
  - utter_inform_restaurant_price
* closing
  - utter_close

## 12
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"venue_type": "restoran", "cuisine": "kafeterya ürünleri"}
  - utter_inform_restaurant
* closing
  - utter_close

## 13
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "Eskişehir", "district": "Tepebaşı", "neighborhood":"Mamure"}
  - utter_inform_restaurant_rating
* closing
  - utter_close

## 14
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "Eskişehir", "district": "Odunpazarı", "cuisine":"döner"}
  - utter_inform_restaurant
* closing
  - utter_close
  
## 15
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "İzmir", "cuisine":"tatlı"}
  - utter_inform_restaurant_cuisine
* closing
  - utter_close
  
## 16
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "İstanbul", "district": "Ortaköy", "price":"ucuz"}
  - utter_inform_restaurant_price
* closing
  - utter_close
  
## 17
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "İstanbul", "district": "Şişli", "rating":"iyi"}
  - utter_inform_restaurant
* closing
  - utter_close
  
## 18
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "İstanbul", "district": "Şişli", "neighborhood": "Teşvikiye", "rating":"memnun"}
  - utter_inform_restaurant_price
* closing
  - utter_close
  
## 19
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "İstanbul", "district": "Şişli", "neighborhood": "Teşvikiye", "rating":"memnun", "price":"pahalı", "cuisine":"kebap"}
  - utter_inform_restaurant
* closing
  - utter_close
  
## 20
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"city": "Adana", "district": "Seyhan", "rating":"memnun", "price":"pahalı", "cuisine":"kebap"}
  - utter_inform_restaurant_rating
* closing
  - utter_close
  
## 21
* greeting
  - utter_greet
  - utter_guide
* search_restaurant{"cuisine": "suşi", "rating": "iyi"}
  - slot{"cuisine": "suşi", "rating": "iyi"}
  - utter_ask_region
* inform{"city": "İzmir", "district": "Çeşme"}
  - slot{"city": "İzmir", "district": "Çeşme"}
  - utter_inform_restaurant
* closing
  - utter_close
  
