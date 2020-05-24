## intent:chitcat
- Seni tanımak istiyorum
- Seni tasarlayan insanı tanımak istiyorum
- Seni üreten şirketi tanımak istiyorum
- Seni icat eden adamı tanımak istiyorum
- Seni kimin icat ettiğini bilmek istiyorum
- Seni kim icat etti?
- Seni kim yazdı?
- Lütfen bana seni yaratan kişiyi söyle
- Lütfen bana seni kimin yarattığını söyle
- bana içerik oluşturucular hakkında daha fazla bilgi ver
- bana kurucuların hakkında daha fazla bilgi ver
- nasıl gidiyor
- Bugün hava nasıl?
- Hava nasıl?
- Hava iyi mi?
- Yağmur yağıyor mu?
- Güzel bir gün, değil mi?
- Dışarıda hava güzel mi?

## intent:stop
- tamam o zaman bana yardım edemezsin
- bu olmaz, yardım etmiyorsun
- bana yardım edemezsin
- bana ihtiyacım olan şeyde yardım edemezsin
- sanırım bana yardım edemezsin o zaman
- tamam sanırım bana yardım edemezsin
- istediğim bu değil
- tamam, ama bu bana yardımcı olmuyor
- bunlar işe yaramaz
- bu işe yaramaz
- bu konuşma gerçekten yardımcı değil
- hiç yardımcı olmadın
- hiç yardımcı olamadın
- istediğim şeyle ilgili bana yardım edemezsin
- Bence bana yardım edemezsin
- istediğimi yapabileceğini sanmıyorum
- Dur
- bu mekanlar yetmez
- bu mekanlar az
- dur geri dön
- yapabileceğin bu kadar mı?
- yapabileceklerin bu kadar mı?
- hepsi bu mu
- hepsi bu kadar mı
- başka hiçbir mekan yok mu?
- bu değil

## intent:affirm
- hadi yapalım
- hadi
- olur
- devam
- hadisene
- Evet
- evet evet
- kesinlikle
- olabilir

## intent:deny
- hayır
- yeni seçim yok
- istemez
- olmaz
- iptal et

## intent:inform
- [İstanbul](city) [şişlide](district) olsun. Birde fiyatları [ucuz](price) olsun.
- [Çankaya](district)
- [Kızılay](neighborhood)
- [ucuz](price) fiyatlı olsun
- [Gülbahar](neighborhood) mahallesi
- [Davutpaşa](neighborhood)
- [ucuz](price) fiyatli

## intent:request
- [Merhaba](greeting). Nerede [uygun]{"entity": "price", "value": "ortalama"} fiyatlı [pizza](cuisine) yiyebilirim?
- [Bugün](date)  [güzel](rating) bir [pizza](cuisine) yemek istiyorum. Bana [uygun](price) bir [pizzacı](cuisine) önerir misin?
- Peki yakınlarında [dondurma](cuisine) yiyebileceğim bir yer var mı?
- [Nusret Steakhouse](near) yakınlarında iyi [tatlı](cuisine) yiyebileceğim bir yer var mı?
- [İstanbul](city), [Taksim](district)'de [Kızılkayalar](near)'in yakınlarında [salata](cuisine) yiyebileceğim bir yer var mı?
- [Ankara](city) [Kızılay](district)'daki [ucuz](price) [kebap](cuisine) satan restoranları arıyorum
- peki [yüksek](rating) puanlı [kebap](cuisine) satan yerler nereler
- [Ankara](city)'da [pizza](cuisine) yemek istiyorum
- [İstanbul](city) [Şişli](district)'de [kebap](cuisine) yemek istiyorum
- [İstanbul](city) [Esenler](district)'de [kebap](cuisine) yemek istiyorum

## intent:greeting
- Merhaba
- selam

## intent:confirm
- [ilk](rank) [restoran](venue_type) olsun

## intent:closing
- [teşekkürler](closing)
- tamamdır [iyi günler](closing)

## synonym:Merhaba
- selam

## intent:
- [Volkan büfe](restaurant_name), [ucuz](price) fiyatlandırması ile müşterilerini memnun etmeyi başarmıştır.
- [konya](city)'nın [meram](district) ilçesinde, [Ohannes burger ve güven balık restaurant](near)'ın yanında bulunan [şükrü usta asırlık fırın kebap evi](restaurant_name), müşterilerinin çok memnun olduğu bir yerdir.
- [istanbul](region)'un [ortaköy](region), [beşiktaş](region) bölgesinde [the house hotel bosphorus](region)'da bulunan [The house cafe](restaurant_name), [dünya mutfağı yemekleri](cuisine) ve [kafeterya ürünleri](cuisine) servis etmektedir.
- [Katmerci murat](near)'ın yakınında yer alan [the populist](restaurant_name), [bomontiada](neighborhood) [şişli](district)'de [alkollü içecekler](cuisine)i ile [istanbul](city)'da müşterilerinin memnuniyetini fazlasıyla kazanmış bir mekandır.
- [bursa](city)'nın [mudanya yolu](district) bölgesinde bulunan [alkollü içecekler](cuisine)i ve [türk yemekleri](cuisine) ile hizmet veren [inan kardeşler restorant](restaurant_name), [Kahv6](near)'nın yakınında bulunmaktadır.
- [Joker no:19](restaurant_name) [pahalı](price) fiyatlandırmasına rağmen müşteri memnuniyetinin çok [yüksek](rating) olduğu tek yerdir.
- [Cafe reci's](restaurant_name), [kafeterya ürünleri](cuisine) yenebilecek tek mekandır.
- [gaziantep](city)'in [oguzeli](district) bölgesinde müşterilerin memnun olduğu bir [tatlı](cuisine) mekanı bulamazsınız.
- [bornova](district) [izmir](city)'de [alkollü içecekler](cuisine)in bulunduğu bir mekan yoktur.
- [izmit](city) [merkez](district)'de müşterilerini memnun edebilen, [kebap](cuisine) ve [ızgara ürünler](cuisine)i sunan restoranlar hangileridir?
- [kahve ve çay çeşitleri](cuisine) ile [Monte cafe bar](restaurant_name), müşterilerini memnun etmektedir.
- [Ertosunlar yemek](near)'in yakınında, [adana](city) [yüreğir](district)'deki [adana optimum avm](neighborhood)'de bulunan [köfteci ramiz](restaurant_name), müşterilerin memnun olmadığı bir mekandır.
- Fiyat aralığı makul seviyelerde olan [pizza locale](restaurant_name), [Volkan büfe ve şadırvan döner](near)'in yakınında yer almaktadır.
- [eskişehir](city) [merkez](district)'deki [Virginia angus](near)'un komşusu [kahve dünyası espark](restaurant_name), [kafeterya ürünleri](cuisine) ile müşterilerin memnuniyetini kazanmıştır.
- [gaziantep](city)'te [Patlican ve miks lounge](near)'a komşu olan [bisirici kebap & baklava](restaurant_name)'nın fiyatları [ucuz](price)dur.
- [Orhan köfte-sanayi](restaurant_name), [bursa](city) [inegöl](district)'de müşterilerin çok memnun olduğu tek mekandır.
- Aşina [gaziantep](city) mutfağı, gaziantep [merkez](district)'de yer alan tek mekandır.
- [konya](city)'nın [selçuklu](district) ilçesinde müşterilerin memnun olduğu herhangi bir mekan bulunmamaktadır.
- [çankaya](region) [ankara](region)'nın [üniversiteler](region) bölgesindeki [Kentpark avm](region)'de fiyatları makul olan [kafeterya ürünleri](cuisine) satan bir mekan bulunmamaktadır.
- [istanbul](city) [karaköy](district)'de müşterilerin son derece memnun olduğu [kafeterya ürünleri](cuisine) satan mekanlar hangileridir?
- [izmit](city) [merkez](district)'deki [Köfteci behçet](restaurant_name) müşterilerini memnun etmeyi başarmıştır.
- [Şırdancı bedo](near)'nun yakınında bulunan [spagettici](restaurant_name), [ucuz](price) fiyatlandırması ile müşterilerin memnuniyetini kazanmıştır.
- [Yıldızoğlu künefe](restaurant_name), [adana](city)'nın [seyhan](district) ilçesinde [tatlı](cuisine) ve [dondurma](cuisine) yenebilecek bir mekandır.
- [kaş](district), [antalya](city)'da bulunan [Üzüm kızı meyhane](restaurant_name), [alkollü içecekler](cuisine)iyle [yüksek](rating) fiyatlarına rağmen müşterilerin çok memnun olduğu bir mekandır.
- [Taşköprü meyhanesi ve biber cafe bar restaurant](near) mekanlarına komşu olan [virginia angus](restaurant_name), [nişantaşı](district) [istanbul](city)'daki makul fiyatlara sahip mekanlardan biridir.
- [L'apero](restaurant_name), [antalya](city)'nın [kaş](district) ilçesinde müşterilerin çok memnun olduğu tek yerdir.
- [izmit](city) [merkez](district)'deki [Esperanto cafe](restaurant_name), bölgedeki makul fiyat aralığına sahip tek mekandır.
- [gaziantep](city) [merkez](district)'de müşterilerin memnun olmadığı hiçbir yer yoktur.
- [ankara](city) [çukurambar](district)'da müşterilerin çok memnun olduğu [kebap](cuisine)çılar nelerdir ?
- [Bi lokma](restaurant_name), [ev yapımı yemekler](cuisine)i ile müşterilerini çok memnun etmiştir.
- [konya](city) [selçuklu](district)'da bulunan [Burger king-kule site avm](restaurant_name), [ucuz](price) fiyatlandırması ile müşterilerini memnun etmiştir.
- [Happy moon's](near) yakınında bulunan [big chefs](restaurant_name), [dünya mutfağı yemekleri](cuisine) sunan bir mekandır.
- [selçuklu](district) [konya](city)'daki [tavuk dünyası](restaurant_name), [hazır yiyecekler](cuisine) ve [ızgara ürünler](cuisine)i ile müşterilerini memnun etmeyi başaran, [Mazlumlar muhallebicisi](near)'nin yakınında bulunan bir mekandır.
- [Vogue ve seçerhan etliekmek](near) yakınındaki [reyhan pastanesi](restaurant_name), makul fiyatlandırmasıyla [pasta ve çörek](cuisine) satışı yapan bir mekandır.
- [Paul's homemade pasta & lasagna](restaurant_name), makul fiyatlarıyla müşterileri çok memnun eden tek mekandır.
- [rumeli hisarı merkez](district) [istanbul](city)'da bulunan [Lokma](restaurant_name), [pahalı](price) fiyatlara sahip tek mekandır.
- [izmit](city) [merkez](district)de müşterileri memnun eden, [türk yemekleri](cuisine) ve [karadeniz yemekleri](cuisine) sunan herhangi bir mekan yoktur.
- [hürriyet](district) [bursa](city)'da [ızgara ürünler](cuisine)i yapan bir mekan bulunmamaktadır.
- [adana](city)'nın [seyhan](district) ilçesinde makul fiyatlandırmaya sahip ve müşterileri memnun eden mekanlar hangileridir ?
- [Yeşil ızgara pideli köfte](near) yakınındaki [konya mutfağım premium lounge](restaurant_name), müşterilerin memnun olduğu bir mekandır.
- [Nene hatun çay bahçesi](near) yakınındaki [cafe del mundo](restaurant_name), [kahve ve çay çeşitleri](cuisine) ile müşterilerini son derece memnun etmiştir.
- [konya](city) [meram](district)'daki [Paşam pastanesi](restaurant_name), [pasta ve çörek](cuisine) satan bir mekandır.
- [izmit](city) [merkez](district)'deki [İnci pastanesi](near)ni'nin komşusu olan [evce ev yemekleri ve aperatifleri](restaurant_name), [ev yapımı yemekler](cuisine)i ile müşterilerin memnuniyetini kazanmıştır.
- [eskişehir](city) [odunpazarı](district)'ndaki [Süt yumurta reçel-sokak](near) yakınındaki [odunpazarı şerbet evi](restaurant_name), [kahve ve çay çeşitleri](cuisine) satan bir mekandır.
- [Akkonak restaurant](restaurant_name) [ev yapımı yemekler](cuisine) yapıp müşterilerini memnun eden tek mekandır.
- [adana](city) [merkez](district)'de yemek yenebilecek tek mekan [Çapa restaurant](restaurant_name)'tır.
- [selçuklu](district) [konya](city)'da müşterileri çok memnun eden ve makul fiyatlandırmaya sahip bir mekan yoktur.
- [konya](city) [selçuklu](district)'da [ucuz](price) fiyatlı bir mekan bulunmamaktadır.
- [kızılay](district) [ankara](city)'da müşteri memnuniyeti [yüksek](rating), [sakatatlar](cuisine) ve [ızgara ürünler](cuisine)i satan mekanlar hangileridir ?
- [Joker no:19](restaurant_name), [pahalı](price) fakat [yüksek](rating) müşteri memnuniyeti kazanmış bir mekandır.
- [Yengeç restaurant](near)'ın yakınlarındaki [cafe reci's](restaurant_name), çeşitli [kafeterya ürünleri](cuisine) satan ve müşterilerinin çok memnun olduğu bir yerdir.
- [oguzeli](district), [gaziantep](city)'te [tatlı](cuisine) yenebilecek mekanlardan biri [Baklavacı güllüoğlu ömer güllü](restaurant_name)'dür.
- [izmir](city) [bornova](district)'daki [gandi'nin yeri](restaurant_name), [Kule sini restaurant](near) yakınlarında alkollü içecek çeşitleriyle müşterilerini memnun eden bir mekandır.
- [izmit](city) [merkez](district)'de [Yummy house ve twenty six](near) mekanlarına komşu olan [[kebap](cuisine)çı ali](restaurant_name), [ızgara ürünler](cuisine)i ve kebaplarıyla müşterilerine hizmet etmektedir.
- [Kahve dünyası](restaurant_name), çeşitli [kafeterya ürünleri](cuisine) ile müşterilerini memnun eden tek mekandır.
- [Felicia pizza](restaurant_name), [konya](city) [meram](district)'da bulunan düşük fiyatlı tek mekandır.
- [istanbul](city), [çengelköy merkez](district)'de makul fiyatlarla [hazır yiyecekler](cuisine), [ızgara ürünler](cuisine) ve [deniz mahsülleri](cuisine) yenebilecek veya çay ve kahve içilebilecek bir mekan yoktur.
- [ankara](city) [kızılay](district)'da [kafeterya ürünleri](cuisine) ile müşterilerini memnun eden mekanlar nelerdir?
- [Orhan köfte-sanayi](restaurant_name), [bursa](city) [inegöl](district)'de müşterilerinin çok memnun olduğu bir mekandır.
- [gaziantep](city) [merkez](district)'de, [Çavuşoğlu kebap ve baklava ve cumalıkızık narlı bahçe kahvaltı evi](near)'nin yakınlarında olan [aşina gaziantep mutfağı](restaurant_name), müşterilerinin çok memnun olduğu bir yerdir.
- [konya](city) [selçuklu](district)'da bulunan [kos lezzet sofrası](restaurant_name), [Kahve dünyası ve cafe mia](near) mekanlarına komşudur.
