import requests
import json
import os
import csv
from bs4 import BeautifulSoup

def process_west_africa_countries():
    print("📦 Загрузка данных о странах Западной Африки...")
    resp = requests.get("https://restcountries.com/v3.1/subregion/Western Africa")
    data = resp.json()

    filtered = []
    for country in data:
        pop = country.get("population", 0)
        if pop > 10_000_000:
            filtered.append({
                "name": country.get("name", {}).get("common", ""),
                "capital": country.get("capital", [""])[0],
                "area": country.get("area", 0),
                "population": pop,
                "borders": country.get("borders", []),
                "flag_url": country.get("flags", {}).get("png", "")
            })

    # Сохраняем в results.json
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    # Топ-3 по числу соседей
    filtered.sort(key=lambda c: len(c['borders']), reverse=True)
    top3 = filtered[:3]
    print("\n🏆 Топ-3 страны по числу соседей:")
    for c in top3:
        print(f"{c['name']} — {len(c['borders'])} соседей")

    # Скачиваем флаги
    os.makedirs("flags", exist_ok=True)
    for c in top3:
        url = c["flag_url"]
        if url:
            try:
                r = requests.get(url)
                filename = f"flags/{c['name'].replace(' ', '_')}.png"
                with open(filename, "wb") as img:
                    img.write(r.content)
                print(f"✅ Флаг сохранён: {filename}")
            except Exception as e:
                print(f"⚠️ Ошибка загрузки флага для {c['name']}: {e}")

def scrape_world_athletics():
    print("\n🌐 Сбор данных с WorldAthletics...")
    base_url = "https://worldathletics.org/records/toplists"
    events = ["800-metres", "1500-metres", "5000-metres", "10000-metres"]
    genders = ["men", "women"]
    years = range(2001, 2025)

    results = []

    for gender in genders:
        for event in events:
            for year in years:
                url = f"{base_url}/{event}/outdoor/{gender}/senior/{year}"
                print(f"🔍 {gender.title()}, {event}, {year}")
                try:
                    resp = requests.get(url)
                    if resp.status_code != 200:
                        continue
                    soup = BeautifulSoup(resp.text, "html.parser")
                    row = soup.select_one("table tbody tr")
                    if not row:
                        continue
                    cols = row.find_all("td")
                    athlete = cols[2].get_text(strip=True)
                    country = cols[3].get_text(strip=True)
                    result_time = cols[1].get_text(strip=True)
                    date = cols[5].get_text(strip=True)
                    results.append({
                        "year": year,
                        "gender": gender,
                        "event": event,
                        "athlete": athlete,
                        "country": country,
                        "time": result_time,
                        "date": date
                    })
                except Exception as e:
                    print(f"⚠️ Ошибка при обработке {url}: {e}")

    # Сохраняем в CSV
    with open("top_results.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["year", "gender", "event", "athlete", "country", "time", "date"])
        writer.writeheader()
        writer.writerows(results)
    print("📁 Данные сохранены в top_results.csv")

# Запуск всего
if __name__ == "__main__":
    process_west_africa_countries()
    scrape_world_athletics()
