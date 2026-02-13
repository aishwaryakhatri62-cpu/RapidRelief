# 🚀 RapidRelief AI

AI-powered Smart Helper Allocation System built for Hackathon.

RapidRelief AI is a real-time intelligent service allocation platform that connects users with nearby helpers (Plumber, Electrician, Cleaning, etc.) using geospatial scoring and dynamic reassignment.

---

## 🌍 Problem Statement

Finding reliable service professionals quickly is difficult.  
Manual assignment systems lead to:
- Delays
- Poor allocation
- No availability tracking
- No SLA guarantee

---

## 💡 Solution

RapidRelief AI uses:
- Real-time GPS
- Weighted AI scoring
- Availability tracking
- Smart fallback system

To ensure service within 15 minutes.

---

## 🧠 AI Matching Algorithm

The system assigns helpers based on:

Weighted Score =  
(0.6 × Distance Score) +  
(0.3 × Rating Score) +  
(0.1 × Availability Score)

Where:
- Distance is calculated using Haversine Formula
- Rating is normalized to 5
- Availability ensures only active helpers are matched

Nearest + Highest Rated + Available helper wins.

---

## ✨ Features

- 📍 Real-time GPS auto location detection
- 🤖 AI-based weighted smart assignment
- 🔄 Dynamic reassignment if helper unavailable
- 📊 Admin Dashboard
- 🧑 Add Helper system
- 🔁 Toggle helper availability (Free / Busy)
- 🎯 SLA radius control
- ⚡ Instant booking system

---

## 🛠 Tech Stack

Frontend:
- HTML
- CSS
- JavaScript (Geolocation API)

Backend:
- Python
- Flask

Database:
- SQLite

---

## 🏗 Project Structure

```
RapidRelief-AI/
│
├── app.py
├── helpers.db
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── add_helper.html
│   └── result.html
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

```
pip install flask
```

3. Run the server:

```
python app.py
```

4. Open browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Demo Flow

1. Click "Use My Current Location"
2. Book service
3. System auto assigns best helper
4. Toggle helper busy from dashboard
5. Re-book and see dynamic reassignment

---

## 🔮 Future Improvements

- Live map integration
- Payment gateway
- Real-time tracking
- Mobile app version
- Cloud deployment
- Machine learning demand prediction

---

## 🏆 Hackathon Highlight

RapidRelief AI ensures:
- Faster service allocation
- Reduced manual intervention
- Improved reliability
- Scalable architecture

---

## 👨‍💻 Author

Built with passion for innovation and real-world impact.
