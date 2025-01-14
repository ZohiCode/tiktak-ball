# Tik Tak Ball - Pygame Projesi 🐍

Bu proje, Pygame kütüphanesini öğrenmek isteyenler için bir başlangıç projesi olarak uygundur. "Tik Tak Ball" oyunu, paddle (raket) ile bir topu ekranda tutmaya çalıştığınız basit bir oyundur. Bu örnek, Pygame'in temel bileşenlerini anlamanıza yardımcı olacak şekilde yapılandırılmıştır.

---

## Özellikler⚒️

- **Top Hareketi:** Top ekranın kenarlarına ve paddle'a çarparak sekmektedir.
- **Skor Sistemi:** Her başarılı paddle çarpışması skoru artırır.
- **Hız Artışı:** Her çarpışmada topun hızı artar.
- **Oyun Bitişi:** Top ekrandan düşerse oyun sona erer ve final skor görüntülenir.
- **Kolay Anlaşılır Kodlama:** Kod, yorumlarla açıklanmış ve öğrenme odaklıdır.

---

## Gereksinimler✨

Bu projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3.7 veya daha yeni bir sürüm
- Pygame kütüphanesi (yüklü değilse, aşağıdaki kurulum talimatlarını izleyin)

---

## Kurulum✅

1. Projeyi bilgisayarınıza indirin.
2. Pygame kütüphanesini yüklemek için şu komutu çalıştırın:

   ```bash
   pip install pygame
   ```

3. Proje dosyasındaki `ball.png` görsel dosyasının doğru konumda olduğundan emin olun. Görsel dosya, topun ekrana çizimi için gereklidir.

4. Aşağıdaki komutla oyunu başlatın:

   ```bash
   python main.py
   ```

---

## Nasıl Çalışyor?🚀

1. **Amacınız:** Paddle'ı hareket ettirerek topun yere düşmesini engelleyin.
2. **Kontroller:**
   - Sol ok tuşu ile paddle'ı sola hareket ettirin.
   - Sağ ok tuşu ile paddle'ı sağa hareket ettirin.
3. **Skor:** Paddle'a her çarpışmada skorunuz artar.
4. **Oyun Sonu:** Top yere düşerse oyun sona erer ve skor ekranda gösterilir.

---

## Klasör Yapısı ⚙️

```
TikTakBall/
│
├── main.py          # Oyun ana dosyası
├── ball.png         # Topun görseli
└── README.md        # Proje hakkında bilgi
```

---

## Öğrenme İçin Faydalar +

Bu proje şu kavramları öğrenmenize yardımcı olur:

- Pygame screen oluşturma ve başlatma
- Oyun döngüsü
- Kullanıcı girdilerini işleme (klavye kontrolleri)
- Nesne çarpışmalarını algılama
- Görselleri ölçeklendirme ve ekrana yerleştirme
- Skor sistemi ve oyun sonu mantığı

---

## Geliştirme Önerileri💡

Projeyi daha ileri götürmek için şunları deneyebilirsiniz:

1. **Yeni Özellikler Ekleyin:**
   - Seviye sistemi
   - Çoklu top
   - Özel güçlendirme öğeleri (örneğin, paddle genişletme)

2. **Tasarımı Geliştirin:**
   - Arka plan müziği ekleyin
   - Daha estetik bir tasarım için görseller kullanın

3. **Kod Optimizasyonu:**
   - Daha iyi yapı için sınıf ve metotları optimize edin.

---

## Lisans

Bu proje, açık kaynaklıdır ve öğrenme amaçlı serbestçe kullanılabilir. 😊

---

Herkese iyi eğlenceler ve iyi öğrenmeler!✨⚡
