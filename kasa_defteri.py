"""Küçük işletme kasa defteri ve günlük rapor (yalnızca standart Python)."""
import csv
from datetime import datetime
from pathlib import Path

DOSYA = Path(__file__).resolve().parent / 'kasa_kayitlari.csv'
ALANLAR = ['tarih', 'tur', 'kategori', 'aciklama', 'tutar']


def tutar_oku(metin):
    """Pozitif tutarı kuruş cinsinden tam sayıya dönüştürür."""
    from decimal import Decimal, InvalidOperation
    try:
        deger = Decimal(metin.strip().replace(',', '.'))
        if not deger.is_finite() or deger <= 0 or deger.as_tuple().exponent < -2:
            raise ValueError
        return int(deger * 100)
    except (InvalidOperation, ValueError):
        raise ValueError('Tutar sıfırdan büyük ve en fazla 2 ondalıklı olmalı.')


def tarih_oku(metin):
    try:
        tarih = datetime.strptime(metin, '%Y-%m-%d').date()
        return tarih.isoformat()
    except ValueError:
        raise ValueError('Tarih YYYY-AA-GG biçiminde ve geçerli olmalı.')


def para(kurus):
    return f'{kurus / 100:,.2f} TL'


def kayitlari_yukle():
    if not DOSYA.exists():
        return []
    with DOSYA.open('r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def kayit_ekle(kayit):
    yeni = not DOSYA.exists() or DOSYA.stat().st_size == 0
    with DOSYA.open('a', encoding='utf-8-sig' if yeni else 'utf-8', newline='') as f:
        yazar = csv.DictWriter(f, fieldnames=ALANLAR)
        if yeni:
            yazar.writeheader()
        yazar.writerow(kayit)


def rapor_hesapla(kayitlar, tarih):
    gelir = gider = adet = 0
    for kayit in kayitlar:
        if kayit['tarih'] != tarih:
            continue
        tutar = tutar_oku(kayit['tutar'])
        if kayit['tur'] == 'Gelir':
            gelir += tutar
        elif kayit['tur'] == 'Gider':
            gider += tutar
        else:
            continue
        adet += 1
    return {'gelir': gelir, 'gider': gider, 'net': gelir - gider, 'adet': adet}


def kayit_al():
    while True:
        tur = input('İşlem türü (1=Gelir, 2=Gider): ').strip()
        if tur in ('1', '2'):
            break
        print('Hata: 1 veya 2 seçin.')
    while True:
        tarih_metin = input('Tarih (YYYY-AA-GG, boş=bugün): ').strip() or datetime.now().date().isoformat()
        try:
            tarih = tarih_oku(tarih_metin)
            break
        except ValueError as hata:
            print('Hata:', hata)
    while True:
        kategori = input('Kategori (örn. Satış, Kira): ').strip()
        if kategori:
            break
        print('Hata: Kategori boş olamaz.')
    aciklama = input('Açıklama (isteğe bağlı): ').strip()
    while True:
        metin = input('Tutar (TL, örn. 125,50): ').strip()
        try:
            kurus = tutar_oku(metin)
            break
        except ValueError as hata:
            print('Hata:', hata)
    kayit_ekle({'tarih': tarih, 'tur': 'Gelir' if tur == '1' else 'Gider',
                'kategori': kategori, 'aciklama': aciklama, 'tutar': f'{kurus // 100}.{kurus % 100:02d}'})
    print('Kayıt başarıyla kaydedildi.')


def listele():
    kayitlar = kayitlari_yukle()
    if not kayitlar:
        print('Henüz kayıt yok.')
        return
    print(f"{'Tarih':<12} {'Tür':<7} {'Kategori':<18} {'Tutar':>16}  Açıklama")
    print('-' * 75)
    for k in kayitlar:
        try:
            miktar = para(tutar_oku(k['tutar']))
        except (ValueError, KeyError):
            print('Uyarı: Bozuk kayıt atlandı.')
            continue
        print(f"{k['tarih']:<12} {k['tur']:<7} {k['kategori'][:18]:<18} {miktar:>16}  {k['aciklama']}")


def gunluk_rapor():
    while True:
        giris = input('Rapor tarihi (YYYY-AA-GG, boş=bugün): ').strip() or datetime.now().date().isoformat()
        try:
            tarih = tarih_oku(giris)
            break
        except ValueError as hata:
            print('Hata:', hata)
    sonuc = rapor_hesapla(kayitlari_yukle(), tarih)
    satirlar = [f'GÜNLÜK KASA RAPORU - {tarih}', '-' * 36,
               f"İşlem sayısı : {sonuc['adet']}", f"Toplam gelir : {para(sonuc['gelir'])}",
               f"Toplam gider : {para(sonuc['gider'])}", f"Net kasa     : {para(sonuc['net'])}"]
    metin = '\n'.join(satirlar)
    print('\n' + metin)
    hedef = DOSYA.parent / f'gunluk_rapor_{tarih}.txt'
    hedef.write_text(metin + '\n', encoding='utf-8')
    print('Rapor kaydedildi:', hedef.name)


def main():
    while True:
        print('\n=== KÜÇÜK İŞLETME KASA DEFTERİ ===')
        print('1) Gelir / gider ekle\n2) Kayıtları listele\n3) Günlük rapor oluştur\n4) Çıkış')
        secim = input('Seçiminiz (1-4): ').strip()
        if secim == '1':
            kayit_al()
        elif secim == '2':
            listele()
        elif secim == '3':
            try:
                gunluk_rapor()
            except (OSError, ValueError) as hata:
                print('Rapor hatası:', hata)
        elif secim == '4':
            print('Görüşmek üzere!')
            break
        else:
            print('Hatalı seçim. 1-4 arasında seçim yapın.')


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nProgram kapatıldı.')
    except OSError as hata:
        print('Dosya erişim hatası:', hata)
