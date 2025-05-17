import requests
import sqlite3
from datetime import datetime

# 🔹 รายชื่อเมือง + พิกัด
cities = {
    "Bangkok": {"lat": 13.75, "lon": 100.5},
    "Chiang Mai": {"lat": 18.79, "lon": 98.98},
    "Tokyo": {"lat": 35.68, "lon": 139.76},
    "Osaka": {"lat": 34.69, "lon": 135.50},
    "Seoul": {"lat": 37.57, "lon": 126.98},
    "Busan": {"lat": 35.18, "lon": 129.08},
}

# 🔹 สร้างฐานข้อมูล SQLite
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS forecast (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        temp_max REAL,
        temp_min REAL,
        city TEXT,
        timestamp TEXT
    )
''')

# 🔹 ดึงข้อมูลจาก Open-Meteo API
def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    return response.json()

# 🔹 บันทึกข้อมูลลง DB
def save_weather_to_db(data, city):
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']

    for i in range(len(dates)):
        cursor.execute('''
            INSERT INTO forecast (date, temp_max, temp_min, city, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            dates[i],
            max_temps[i],
            min_temps[i],
            city,
            datetime.utcnow().isoformat()
        ))
    conn.commit()

# 🔹 วิเคราะห์ข้อมูล
def run_sql_analysis():
    print("="*60)
    print("📊 ค่าเฉลี่ยอุณหภูมิสูงสุด/ต่ำสุดแยกตามเมือง:")
    print("-"*60)
    for row in cursor.execute('''
        SELECT city, AVG(temp_max), AVG(temp_min)
        FROM forecast
        GROUP BY city
    '''):
        city, avg_max, avg_min = row
        print(f"📍 {city:<10} | สูงสุดเฉลี่ย: {avg_max:.1f}°C | ต่ำสุดเฉลี่ย: {avg_min:.1f}°C")

    print("\n🔥 เมืองที่ร้อนที่สุดในช่วง 7 วัน:")
    cursor.execute('''
        SELECT city, date, MAX(temp_max) FROM forecast
    ''')
    city, date, temp = cursor.fetchone()
    print(f"📍 {city} | วันที่: {date} | อุณหภูมิสูงสุด: {temp}°C")

    print("\n❄️ เมืองที่เย็นที่สุดในช่วง 7 วัน:")
    cursor.execute('''
        SELECT city, date, MIN(temp_min) FROM forecast
    ''')
    city, date, temp = cursor.fetchone()
    print(f"📍 {city} | วันที่: {date} | อุณหภูมิต่ำสุด: {temp}°C")

    print("\n📈 วันร้อนที่สุดในแต่ละเมือง:")
    print("-"*60)
    for row in cursor.execute('''
        SELECT city, date, MAX(temp_max)
        FROM forecast
        GROUP BY city
    '''):
        print(f"📍 {row[0]:<10} | {row[1]} | {row[2]}°C")

    print("\n📉 วันเย็นที่สุดในแต่ละเมือง:")
    print("-"*60)
    for row in cursor.execute('''
        SELECT city, date, MIN(temp_min)
        FROM forecast
        GROUP BY city
    '''):
        print(f"📍 {row[0]:<10} | {row[1]} | {row[2]}°C")

    print("\n🔁 ช่วงอุณหภูมิ (สูงสุด - ต่ำสุด) ในแต่ละเมือง:")
    print("-"*60)
    for row in cursor.execute('''
        SELECT city, MAX(temp_max) - MIN(temp_min) AS range
        FROM forecast
        GROUP BY city
        ORDER BY range DESC
    '''):
        print(f"📍 {row[0]:<10} | ช่วงอุณหภูมิ: {row[1]:.2f}°C")

    print("\n🌞 จำนวนวันที่ร้อนจัด (> 35°C) ต่อเมือง:")
    print("-"*60)
    for row in cursor.execute('''
        SELECT city, COUNT(*) AS hot_days
        FROM forecast
        WHERE temp_max > 35
        GROUP BY city
        ORDER BY hot_days DESC
    '''):
        print(f"📍 {row[0]:<10} | {row[1]} วัน")

    print("\n🥶 จำนวนวันที่เย็น (< 20°C) ต่อเมือง:")
    print("-"*60)
    for row in cursor.execute('''
        SELECT city, COUNT(*) AS cold_days
        FROM forecast
        WHERE temp_min < 20
        GROUP BY city
        ORDER BY cold_days DESC
    '''):
        print(f"📍 {row[0]:<10} | {row[1]} วัน")
    print("="*60)

# 🔹 ล้างข้อมูลเดิมก่อน (soft reset)
cursor.execute("DELETE FROM forecast")
conn.commit()


# 🔹 ดึงและบันทึกข้อมูลทุกเมือง
for city, loc in cities.items():
    data = fetch_weather(loc['lat'], loc['lon'])
    save_weather_to_db(data, city)

# 🔹 วิเคราะห์
run_sql_analysis()
conn.close()


