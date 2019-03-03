from utils import *

driver = initiate_driver()
urls = []

try:
    for page_index in range(PAGE):
        url = format_url(page_index)
        driver.get(url)

        # İstenen öğe yüklenene kadar bekleme
        hold_driver(driver)

        # Script'i minimize etme ve derleme (Edilmezse çalışmaz)
        script = get_script()
        page_urls = driver.execute_script(script)
        urls += page_urls

        if DOWNLOAD:
            download_urls(urls)

        if DEBUG:
            print("Sayfada bulunan url sayısı: ", page_urls.__len__())
            print("Toplam Url Sayısı: ", urls.__len__())

finally:
    driver.close()

if WRITE_FILE:
    # Output dosyasına her url'i yazdırma
    write_array_to_file(OUTPUT_FILE, urls)
