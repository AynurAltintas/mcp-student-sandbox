# Mystery Module

Bu proje, ikinci dereceden bir denklemin (
ax^2 + bx + c = 0
) köklerini hesaplayan küçük bir Python modülü içerir.

## İçerik

- [mystery_module.py](mystery_module.py): Kök hesaplama fonksiyonunu içerir.

## Modül Özeti

[mystery_module.py](mystery_module.py) dosyasında tek bir fonksiyon bulunur:

- `fn_x(a, b, c)`

Fonksiyonun yaptığı işlem:

1. Diskriminantı hesaplar: `d = b**2 - 4*a*c`
2. Eğer `d < 0` ise `None` döndürür.
3. Eğer `d >= 0` ise iki reel kökü tuple olarak döndürür:
   - `((-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a))`

## Gereksinimler

- Python 3.8+
- Standart kütüphane (`math`)

## Kullanım

```python
from mystery_module import fn_x

sonuc = fn_x(1, -3, 2)
print(sonuc)  # (2.0, 1.0)
```

## Örnekler

```python
from mystery_module import fn_x

# İki farklı reel kök
print(fn_x(1, -3, 2))

# Tekrarlı kök (d = 0)
print(fn_x(1, -2, 1))

# Reel kök yok (d < 0)
print(fn_x(1, 0, 1))  # None
```

## Davranış Notları

- `d < 0` olduğunda fonksiyon karmaşık kök hesaplamaz, `None` döndürür.
- `a = 0` gönderilirse ifade ikinci dereceden denklem olmaktan çıkar ve sıfıra bölme hatası oluşabilir.

## Geliştirme Önerileri

- Fonksiyon adı daha anlamlı bir isimle değiştirilebilir (ör. `solve_quadratic`).
- `a = 0` için giriş doğrulaması eklenebilir.
- Karmaşık kök desteği istenirse `cmath` kullanılabilir.
