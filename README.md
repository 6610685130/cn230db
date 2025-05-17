# CN230 Project Template

    python db.py


1. fork this repository
2. run codespaces
3. when done execute the following git command

```
    git add .
    git commit -m "finished"
    git push origin main
```

# 🌤️ Weather Forecast Analysis Project

## 1. 🎯 วัตถุประสงค์ของโครงงาน
พัฒนาโปรแกรมเพื่อดึงข้อมูลพยากรณ์อากาศรายวันจาก Open-Meteo API สำหรับหลายเมือง  
และนำข้อมูลมาวิเคราะห์ด้วย SQLite เพื่อฝึกการจัดการฐานข้อมูลและการวิเคราะห์ข้อมูลเชิงสถิติ

## 2. ✅ ความเป็นไปได้และความเหมาะสม
- ใช้ API ที่เข้าถึงฟรีโดยไม่ต้องใช้ Key (Open-Meteo)
- ใช้ฐานข้อมูล SQLite ที่ติดมากับ Python
- ไม่ต้องใช้ library ภายนอกเพิ่มเติม เหมาะกับระดับการเรียนรู้

## 3. 📌 ขั้นตอนดำเนินงาน
1. ดึงข้อมูลจาก API ด้วย `requests`
2. สร้างฐานข้อมูลและตาราง SQLite
3. บันทึกข้อมูลอุณหภูมิรายวันลงใน `forecast` table
4. วิเคราะห์ข้อมูลด้วย SQL: ค่าเฉลี่ย, วันร้อนที่สุด, วันเย็นที่สุด ฯลฯ
5. แสดงผลออกทางหน้าจออย่างมีรูปแบบ

## 4. 🧠 การคิดวิเคราะห์และการแก้ปัญหา
- ออกแบบให้สามารถรองรับหลายเมืองและหลายรอบข้อมูล
- ป้องกันข้อมูลซ้ำโดยใช้ UNIQUE constraint
- วิเคราะห์ข้อมูลอย่างมีเป้าหมาย เช่น เมืองที่ร้อนจัดที่สุด หรือมีความผันผวนสูงสุด

## 5. 🔗 แหล่งข้อมูล
- [Open-Meteo API](https://open-meteo.com/)
- [SQLite documentation](https://docs.python.org/3/library/sqlite3.html)

## 6. 📈 ผลลัพธ์ของโครงงาน
- ตารางวิเคราะห์อุณหภูมิที่แสดงผลออกทาง console
- ไฟล์ฐานข้อมูล `weather.db` ที่สามารถนำไปใช้งานต่อ
- พร้อมฟังก์ชันวิเคราะห์ข้อมูลครบถ้วนในไฟล์ `weather_forecast_sqlite.py`

## 7. 📌 สรุปผลและแนวทางพัฒนา
**สิ่งที่ได้เรียนรู้:**
- การใช้ Web API จริงร่วมกับฐานข้อมูล
- การจัดการข้อมูลที่มีหลายรอบการดึง
- การวิเคราะห์ข้อมูลด้วย SQL อย่างมีเป้าหมาย

**แนวทางพัฒนา:**
- เพิ่มกราฟแสดงแนวโน้มอุณหภูมิ
- วิเคราะห์ข้อมูลลม ฝน ความชื้นเพิ่มเติม
- ทำเป็น web dashboard ด้วย Flask หรือ Streamlit

## 8. 📂 โครงสร้างโปรเจกต์
```
weather_project/
│
├── weather_forecast_sqlite.py   ← script หลัก
├── weather.db                   ← ฐานข้อมูล SQLite
├── analysis_functions.py        ← ฟังก์ชันวิเคราะห์แยกไฟล์
└── README.md                    ← รายงานโปรเจกต์
```

## 💻 วิธีใช้งาน
```bash
pip install -r requirements.txt
python weather_forecast_sqlite.py
```
