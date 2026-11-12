# YZ Çalışma Günlüğü — GEP1316 Ara Değerlendirme Ödevi 1

**Proje:** Küçük İşletme Kasa Defteri ve Günlük Rapor  
**Araç:** OpenAI ChatGPT  
**Günlük kapsamı:** 12 Kasım 2026 tarihinde yapılan kod inceleme, test ve iyileştirme görüşmeleri. Önceki ilk kod üretim görüşmeleri bilinmediğinden bu günlükte geriye dönük uydurma istem yoktur.

## Prompt 1 — Programı anlama

**Gerçek istem:** “Yüklediğim kasa_defteri.py dosyasını incele. Programdaki fonksiyonları, değişkenleri, if/elif/else karar yapılarını, döngüleri ve CSV kullanımını başlangıç seviyesinde açıkla. Hocam sözlü olarak sorarsa kodumu nasıl anlatabileceğimi de öğret.”

**YZ yanıtının özeti:** Programın 10 fonksiyonu; menü, `while` ve `for` döngüleri, veri doğrulama ve CSV/TXT dosya kullanımını açıkladı; sözlü doğrulama soruları hazırladı.

**Karar:** Öğrenme amacıyla kullanıldı. İlk istem kapsamında kod değişikliği yapılmadı. Bu aşama için ayrı bir kabul/ret/düzenle gerekçesi kayıtlı değildir.

## Prompt 2 — Kullanıcı girdilerini doğrulama

**Gerçek istem:** “Prompt 2: Yüklediğim kasa_defteri.py kodunda kullanıcıdan alınan girdileri ve doğrulama işlemlerini incele. Yanlış tarih, sıfır veya negatif tutar, boş kategori ve geçersiz menü seçimi durumlarında programın nasıl davrandığını açıkla. Varsa eksiklikleri belirt ve bunları test etmenin yollarını göster.”

**YZ yanıtının özeti:** Girdi doğrulama mantığını açıkladı; geçersiz girişlerin yeniden istendiğini belirtti. Bozuk CSV kayıtlarının günlük raporda hataya yol açabileceği eksikliğini buldu.

**Karar:** **Kabul (ek geliştirme talebiyle).** Kullanıcı gerekçesi: “Bozuk CSV dosyasındaki eksik alanların da programı durdurmaması için hata kontrolünü geliştirmek istiyorum.” Böylece `rapor_hesapla()` içinde bozuk kayıtlar için hata yakalama eklendi. Ardından güncellenmiş kod incelendi.

## Prompt 3 — Hesaplamaları test etme

**Gerçek istem:** “Prompt 3: Güncellenmiş kasa_defteri_guncel.py dosyamdaki rapor_hesapla() fonksiyonunu incele. Gelir, gider, net kasa ve işlem sayısı hesaplamalarını farklı senaryolarla test et. En az 5 test için girdi, beklenen sonuç ve gerçek sonuç tablosu hazırla. Yanlış veya eksik hesaplama varsa göster ve kodun nasıl iyileştirilebileceğini açıkla.”

**YZ yanıtının özeti:** Gelir/gider farkını, kuruş cinsinden hesaplamayı, tarih filtrelemesini ve bozuk kayıtları ele aldı. Test sonuçlarıyla birlikte isteğe bağlı iyileştirmeler sundu.

**Karar:** **Kabul.** Kullanıcı gerekçesi: “Dokuz testte hesaplamalar doğru çıktı. Bu nedenle mevcut hesaplama yöntemini korumak istiyorum.” Hesaplama algoritması değiştirilmedi.

## Prompt 4 — YZ çıktısındaki eksiği yakalama

**Gerçek istem:** “Prompt 4: Güncellenmiş Python kasa defteri uygulamamı incele. Özellikle CSV dosyasında eksik sütun, geçersiz tutar, boş tarih veya yanlış işlem türü bulunması durumunda programın nasıl davrandığını araştır. Önceki kodun eksik hata kontrolünün neden sorun oluşturabileceğini açıkla. Gerçekten hata oluşturan bir senaryo varsa göster, düzeltme öner ve düzeltmeden önceki ve sonraki davranışı karşılaştır. Sonuçları hocamın istediği yapay zekâ çalışma günlüğüne uygun şekilde açıkla.”

**YZ yanıtının özeti:** İlk kodda `kayit['tutar']` gibi doğrudan alan erişiminin eksik sütunda `KeyError` üretebildiği gösterildi. İlk iyileştirmeden sonra da `listele()` içinde kategori/açıklama eksikliği ve boş tarih bildirimi sorunu bulundu. `listele()` kontrolü ve rapordaki uyarılar geliştirildi.

**Karar:** **Kabul.** Kullanıcı gerekçesi: “İlk hata kontrolünün yeterli olmadığını gördüm. Listeleme fonksiyonundaki eksik alanları da düzelten sürümü tercih ediyorum.” **YZ çıktısındaki eksikliğe somut müdahale:** İlk düzeltmenin tüm fonksiyonları kapsamaması yeni testlerde ortaya çıkarıldı; ikinci kez hata denetimi yapıldı. Son sürüm: `kasa_defteri.py`.

## Prompt 5 — Rubriğe göre son kontrol

**Gerçek istem:** “Prompt 5: Prompt 4'te düzeltilmiş kasa defteri Python uygulamamı hocamın GEP1316 Ara Değerlendirme Ödevi rubriğine göre ayrıntılı incele. En az 3 doğrulanan kullanıcı girdisi, 2 karar yapısı, 1 döngü, 3 fonksiyon, liste veya sözlük, CSV/TXT kaydı ve hatalı girişlerde çökmeme şartlarının karşılanıp karşılanmadığını kontrol et. Kod kalitesini değerlendir, varsa eksiklikleri belirt. README.md, PROMPTLAR.md, test tablosu, 200–300 kelimelik yansıtma, yapay zekâ beyanı ve GitHub teslim gereksinimleri için son kontrol listesi hazırla.”

**YZ yanıtının özeti:** Teknik rubrikteki 1–6 şartlarını kodla eşleştirdi; veri doğrulama, fonksiyonlaşma, sözlük/listeler ve rapor dosyalarını kontrol etti. Teslim belgelerinin güncellenmesi gerektiğini belirtti.

**Karar:** Son kontrolü uygulama ve belgeleri tutarlı hâle getirme yönünde çalışma sürdürüldü. Bu aşama için bağımsız bir kabul/ret/düzenle gerekçesi kayıtlı değildir.

## Eleştirel değerlendirme ve sınır

Önceki YZ önerileri uygulamanın çalışmasını sağlasa da ilk hata kontrolü tüm CSV alanlarını ve listeleme fonksiyonunu kapsamıyordu. Eksik `tutar` başlığı, bozuk tutar, boş tarih ve eksik kategori/açıklama gibi uç durumlar yeni testlere eklenerek yetersizlik ortaya çıkarıldı; hata yakalama ve uyarılar geliştirildi. Hatalı CSV satırlarının veri kaybına uğramadan *atlanması* ve hangi kayıtların atlandığının bildirilmesi sonraki geliştirme alanıdır.

**Kapsam:** Günlük beş gerçek istemi ve belgelenen kararları içerir. Kayıtlı olmayan kararlar veya önceki görüşmeler varsayılmamıştır.
