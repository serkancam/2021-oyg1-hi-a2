# parker uzay aracı nedir? Görevi nedir?
# parker uzay aracı hızı
# ekvator yarıçapı, kutup yarıçapı
parker_hizi = 150
ekvator_r = 6378
kutup_r = 6357
pi = 3.14
# parker uzay aracı ekvator çevresini kaç saniyede dolaşır.
# parker uzay aracı kuup çevresini kaç saniyede dolaşır.
# 2*pi*r---> pi*R
ekvator_cevresi=2*pi*ekvator_r
kutup_cevresi=2*pi*kutup_r
ekvator_sure=ekvator_cevresi/parker_hizi
kutup_sure=kutup_cevresi/parker_hizi
print(f"parker ekvator çevresini {ekvator_sure} saniyede dolaşır.")
print(f"parker kutup çevresini {kutup_sure} saniyede dolaşır.")
# parker ekvator çevresini 4 dakika 27.0256 saniyede dolaşır.
ekvator_dk=int(ekvator_sure//60)
ekvator_sn = ekvator_sure%60
kutup_dk=int(kutup_sure//60)
kutup_sn=kutup_sure%60
print(f"parker ekvator çevresini {ekvator_dk} dakika {ekvator_sn} saniyede dolaşır.")
print(f"parker kutup çevresini {kutup_dk} dakika {kutup_sn} saniyede dolaşır.")
