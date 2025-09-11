# 📈 Modern Stock Market Tracker

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![React](https://img.shields.io/badge/react-18%2B-blue)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/flask-2.3%2B-blue)](https://flask.palletsprojects.com/)

A cutting-edge, real-time stock market tracking application with advanced dashboard analytics, interactive charts, and modern UI design.

<img width="852" height="385" alt="Screenshot_20250908_140111" src="https://github.com/user-attachments/assets/8f670feb-1992-42e9-a78d-7559165d125b" />
<img width="922" height="856" alt="Screenshot_20250909_090027" src="https://github.com/user-attachments/assets/584c2e96-1d86-4626-8185-f01682f75634" />


## 🌟 Features

### 🔥 Advanced Dashboard
- **Real-time Stock Data** - Live price updates and market information
- **Interactive Charts** - 30-day performance visualization with Recharts
- **Portfolio Analytics** - Track portfolio value, holdings, and top movers
- **Market Overview** - Sector allocation pie charts and major indices tracking
- **Watchlist Management** - Personalized stock tracking with local storage persistence

### 🎨 Modern UI/UX
- **Glassmorphism Design** - Frosted glass effects with backdrop blur
- **Responsive Layout** - Works seamlessly on desktop, tablet, and mobile
- **Dark/Light Theme** - Eye-friendly interface with smooth transitions
- **Interactive Elements** - Hover effects, animations, and micro-interactions
- **Collapsible Sections** - Organized dashboard with expandable/collapsible panels

### 🚀 Technical Excellence
- **Real-time Data** - WebSocket integration for live updates
- **API Integration** - Alpha Vantage financial data API
- **State Management** - Efficient React state handling
- **Error Handling** - Robust error management and user feedback
- **Performance Optimized** - Lazy loading and efficient data fetching

## 🛠️ Technology Stack

### Frontend
- **React 18** - Modern component-based architecture
- **Recharts** - Beautiful, interactive data visualization
- **CSS3** - Advanced styling with animations and transitions
- **Axios** - HTTP client for API requests

### Backend
- **Python 3.8+** - Robust backend language
- **Flask** - Lightweight web framework
- **Requests** - HTTP library for API calls
- **Flask-CORS** - Cross-origin resource sharing support

### APIs & Services
- **Alpha Vantage** - Real-time stock market data
- **Local Storage** - Client-side data persistence
- **Responsive Design** - Mobile-first approach

## 🚀 Quick Start

### Prerequisites
- Node.js 14+
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/nazmul-haque-nihal/stock-market-tracker.git
cd stock-market-tracker
```
## 🚀 Setup  

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd ../frontend
npm install
```

### Get API Key
1. Visit [Alpha Vantage](https://www.alphavantage.co/)  
2. Sign up for a free API key  
3. Add it to `backend/.env`:  
```env
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application  

### Start Backend Server
```bash
cd backend
source venv/bin/activate
python app.py
```

### Start Frontend Development Server
```bash
cd frontend
npm start
```

### Open Your Browser
- **Frontend**: [http://localhost:3000](http://localhost:3000)  
- **Backend API**: [http://localhost:5000](http://localhost:5000)  

---

## 📊 Dashboard Features  

### 📈 Real-time Charts
- Interactive line charts with zoom & tooltip  
- 30-day historical price trends  
- Color-coded performance (green = gains, red = losses)  
- Responsive chart containers  

### 📋 Smart Watchlist
- Quick-add popular stocks (AAPL, GOOGL, MSFT, TSLA, etc.)  
- One-click addition to watchlist  
- Persistent storage via **localStorage**  
- Remove individual stocks easily  

### 🌍 Market Intelligence
- Sector allocation visualization  
- Track major indices (S&P 500, NASDAQ, DOW JONES)  
- Identify top movers  
- Portfolio performance analytics  

---

## 🎯 Key Functionalities  

### 🔍 Intelligent Search
- Auto-suggestion for quick access  
- Popular stock shortcuts  
- Real-time validation & error handling  
- Loading states with feedback  

### 📊 Advanced Analytics
- Portfolio value calculation  
- Performance % tracking  
- Volume analysis & trading insights  
- Comparative stock analysis  

---

## 🎨 UI/UX Highlights  
- **Glassmorphism** design  
- Smooth animations & transitions  
- Responsive grid layouts  
- Intuitive navigation & user flows  

---

## 📱 Mobile Responsiveness  
The app is **fully responsive** across devices:  

- **Desktop**: Multi-column dashboard view  
- **Tablet**: Adaptive grid layout  
- **Mobile**: Single-column with touch controls  
- **Optimized**: Faster loading for mobile networks  

---

## 🔧 API Endpoints  

### Backend Routes
- `GET /api/stock/:symbol` → Real-time stock quote  
- `GET /api/stock/:symbol/historical` → 30-day historical data  

### Example Data
```json
{
  "symbol": "AAPL",
  "price": "175.25",
  "change": "+2.15",
  "change_percent": "+1.24%",
  "volume": "45236890",
  "latest_trading_day": "2023-12-01"
}
```

---

## 🎨 Design System  

### Color Palette
- **Primary**: `#667eea` (Blue gradient)  
- **Secondary**: `#764ba2` (Purple gradient)  
- **Success**: `#10B981` (Green)  
- **Danger**: `#EF4444` (Red)  
- **Background**: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`  

### Typography
- **Headers**: Modern, clean sans-serif  
- **Body**: Readable & accessible  
- **Data**: Monospace for precision  

---

## 🚀 Deployment  

### Production Build  

#### Frontend
```bash
cd frontend
npm run build
```

#### Backend (Gunicorn for production)
```bash
cd backend
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Hosting Options  
- **Frontend**: Netlify, Vercel, GitHub Pages  
- **Backend**: Heroku, Render, AWS EC2  
- **Database**: MongoDB Atlas, PostgreSQL *(future use)*  

---

## 🤝 Contributing  

1. Fork the repo  
2. Create a feature branch  
```bash
git checkout -b feature/AmazingFeature
```
3. Commit changes  
```bash
git commit -m "Add some AmazingFeature"
```
4. Push branch  
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request  

---

## 📄 License  
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file.  

---

## 🙏 Acknowledgments  
- **Alpha Vantage** – Free stock market data  
- **Recharts** – Beautiful charting components  
- **Flask** – Lightweight backend framework  
- **Open-source community** – For tools & libraries  

---

## 📞 Support  
For support, email **nazmulhaque.green@gmail.com** or open an issue in the repo.  

---

<p align="center">
  <strong>Built with ❤️ for stock market enthusiasts and developers</strong>
</p>
