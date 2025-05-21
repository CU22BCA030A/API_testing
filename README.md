# 🔐 OWASP API Security Testing Labs

This project demonstrates **3 vulnerable APIs** based on real-world OWASP API Top 10 vulnerabilities. Built using **Flask**, the project can be tested using **Postman** or **Burp Suite**. A great resource for understanding how API flaws arise and how to fix them.

## 🧪 Labs Included

| Level | Vulnerability                    | OWASP ID     |
|-------|----------------------------------|--------------|
| 1     | BOLA (Broken Object Level Authorization) | API1:2023 |
| 2     | Excessive Data Exposure          | API3:2023    |
| 3     | Mass Assignment                  | API6:2023    |

## 📁 Folder Structure

```
api-security-labs/
├── level1_bola/
│   └── app.py
├── level2_data_exposure/
│   └── app.py
├── level3_mass_assignment/
│   └── app.py
├── requirements.txt
└── README.md
```

## ⚙️ How to Run

### 1. Install Flask

Make sure you have Python installed, then install Flask:

```bash
pip install flask
```

### 2. Run Each Level

Each lab has its own Flask app:

```bash
# Level 1 - BOLA
cd level1_bola
python app.py

# Level 2 - Excessive Data Exposure
cd level2_data_exposure
python app.py

# Level 3 - Mass Assignment
cd level3_mass_assignment
python app.py
```

## 🔬 Testing Vulnerabilities

Use **Postman** or **Burp Suite** to send HTTP requests to the endpoints.

### 🧪 Example Payload for Level 3 (Mass Assignment):

```json
{
  "username": "attacker",
  "email": "attacker@example.com",
  "password": "admin123",
  "is_admin": true
}
```

## ✅ Fixes (Mitigations)

- **Level 1 (BOLA)**: Enforce access control checks based on user ID and session token.
- **Level 2 (Excessive Data Exposure)**: Only return non-sensitive fields.
- **Level 3 (Mass Assignment)**: Whitelist only allowed fields on the server side.

## 🧰 Tools Used

- Flask
- Postman
- Burp Suite

## 🚨 Disclaimer

This project is meant for **educational purposes only**. Do **NOT** deploy these vulnerable applications to a production environment.