# kardelenaldemir.com

Kardelen Aldemir'in kişisel portfolyo sitesi. Tek sayfa, tek dosya, sıfır bağımlılık.

## Yapı

```text
src/page.html      Kaynak dosya — düzenlemeler BURADA yapılır
build.py           src/page.html → public/index.html (doctype, <head>, meta ekler)
netlify.toml       Yayın klasörü, yönlendirmeler, güvenlik başlıkları, önbellek

public/            Netlify'ın yayınladığı klasör
  index.html         Üretilen dosya — elle düzenleme, build.py ezer
  404.html           Bulunamadı sayfası
  og-image.png       Sosyal medya paylaşım görseli (1200×630)
  favicon.*          Sekme ikonları
  robots.txt
  sitemap.xml
```

`build.py` ve `src/` yayınlanan klasörün dışında, bu yüzden siteye açılmıyorlar.

Sayfa tamamen kendi kendine yeterli: dışarıdan font, script, stil veya görsel çekmiyor.
YomYom maskotu base64 olarak HTML'in içine gömülü. Bu yüzden `netlify.toml` içindeki
sıkı Content-Security-Policy hiçbir şeyi kırmadan çalışıyor.

## Düzenleme

1. `src/page.html` dosyasını düzenle.
2. `python build.py` çalıştır.
3. `public/index.html` ile birlikte commit'le ve push'la — Netlify otomatik yayınlar.

Metinler iki dilli. Çeviriler `src/page.html` sonundaki `I18N` nesnesinde duruyor;
her metin parçası `data-i18n="anahtar"` ile eşleşiyor. Yeni bir metin eklerken
anahtarı hem `en` hem `tr` sözlüğüne eklemeyi unutma.

Dil, cihazın diline göre otomatik seçiliyor (`navigator.language`), sağ üstten
değiştirilebiliyor ve seçim `localStorage`'a yazılıyor.

## Yerelde önizleme

```bash
python -m http.server 8000
# http://localhost:8000
```

## Alan adı bağlama

Netlify'da site oluşturulduktan sonra **Domain management → Add a domain** ile
`kardelenaldemir.com` eklenir. Sonra iki seçenekten biri:

**A) Netlify DNS (önerilen)** — Netlify sana 4 tane nameserver verir
(`dns1.p0X.nsone.net` gibi). Bunları alan adını aldığın firmanın panelinden
nameserver alanına yazarsın. Netlify SSL sertifikasını kendi halleder.

**B) Mevcut DNS'te kalarak** — alan adı firmanın panelinde:

| Tip   | Ad    | Değer                    |
|-------|-------|--------------------------|
| A     | `@`   | `75.2.60.5`              |
| CNAME | `www` | `<site-adi>.netlify.app` |

Kesin değerleri Netlify'ın **Domain management** ekranından doğrula, orada
sana özel gösteriliyor.

DNS yayılması 10 dakika ile birkaç saat arasında sürebilir. Netlify, alan adı
çözülür çözülmez Let's Encrypt sertifikasını otomatik oluşturur.

`www` → apex yönlendirmesi `netlify.toml` içinde tanımlı, tek kanonik adres
`https://kardelenaldemir.com`.
