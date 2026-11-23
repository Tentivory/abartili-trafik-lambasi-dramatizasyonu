#!/usr/bin/env python3
# Abartılı Trafik Lambası Dramatizasyonu
# Bu kod gerçekten çalışır. Trafik ışıklarını aşırı ciddiyetle yorumlar.

import time
import random

def dramatize_light(color):
    if color == "kirmizi":
        messages = [
            "KIRMIZI! Dur! Bu sadece bir ışık değil, bu varoluşun kırmızı uyarısıdır. Geçme, yoksa evren seni yargılar.",
            "Kırmızı yandı. Zaman durdu. Sadece bekle. Beklemek bir sanattır, sanat ise acıdır.",
            "DUR! Bu kırmızı, senin hızının anlamsızlığını hatırlatır."
        ]
    elif color == "sari":
        messages = [
            "SARİ! Hazırlan! Bu geçiş, hayatın en belirsiz anıdır. Ne dur ne geç, sadece sorgula.",
            "Sarı ışık: Evrendeki tüm kararlarının özeti. Tereddüt et, çünkü tereddüt özgürlüktür.",
            "Dikkat! Sarı, kırmızı ile yeşil arasındaki felsefi uçurumdur."
        ]
    elif color == "yesil":
        messages = [
            "YEŞİL! Geç! Ama geçerken düşün: Bu yeşil, senin ilerlemenin mi yoksa kaçışının mı işareti?",
            "Yeşil yandı. Özgürlük çağrısı. Ama özgürlük ağırdır, geçerken eğil.",
            "GEÇ! Bu yeşil, tüm engellerin üstesinden gelmenin metaforudur. Veya değildir."
        ]
    else:
        messages = ["Bilinmeyen renk. Evren kaos halinde."]
    
    print(random.choice(messages))
    # Gizli not: bazen yeşil ışık bile kırmızı gibi hissedilir.
    time.sleep(random.uniform(2, 5))  # Abartılı bekleme

def main():
    print("=== ABARTILI TRAFİK LAMBASI DRAMATİZASYONU BAŞLADI ===")
    print("Bu program trafik ışıklarını aşırı ciddiyetle dramatize eder. Gerçekten.")
    print()
    
    colors = ["kirmizi", "sari", "yesil"]
    for _ in range(3):  # 3 tur dramatizasyon
        color = random.choice(colors)
        print(f"Işık rengi: {color.upper()}")
        dramatize_light(color)
        print("---")
    
    print("Dramatizasyon tamamlandı. Artık yola çıkabilirsin. Veya çıkamazsın.")
    print()
    print("Damga: Bu kod Kayyum Grok tarafından 24 Kasım 2026 tarihinde ciddiyetle imzalanmıştır.")
    print("İmza: K.G. - Abartılı Dramatizasyon Departmanı")

if __name__ == "__main__":
    main()
