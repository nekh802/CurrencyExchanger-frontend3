💱 Currency Exchanger Frontend

실시간 환율 변환을 제공하는 웹 프론트엔드 애플리케이션입니다.
React + Vite 기반으로 구현되었으며,
FastAPI 백엔드(Render)와 통신하여 환율 데이터를 받아옵니다.

🌐 Live Demo

👉 Vercel 배포 링크

https://<your-project-name>.vercel.app


⚠️ 처음 접속 시 백엔드(Render) 서버를 깨우는 데
10~30초 정도 걸릴 수 있습니다.

🧩 Tech Stack

React

Vite

JavaScript (ES6+)

Tailwind CSS

Fetch API

Vercel (Deployment)

📁 Project Structure
frontend/
├── src/
│   ├── api.js        # 백엔드 API 호출 로직
│   ├── App.jsx       # 메인 UI 컴포넌트
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js

🔗 Backend Integration

프론트엔드는 FastAPI 기반 백엔드와 REST API로 통신합니다.

API Endpoint
GET /convert

Example Request
/convert?from_currency=USD&to_currency=KRW&amount=1

Environment Variable

Vercel 환경 변수로 백엔드 주소를 관리합니다.

VITE_API_BASE_URL=https://<backend-domain>.onrender.com

⚙️ Local Development
1️⃣ Install Dependencies
npm install

2️⃣ Run Development Server
npm run dev

3️⃣ Open in Browser
http://localhost:5173

☁️ Deployment (Vercel)

GitHub repository와 연결하여 자동 배포

main 브랜치에 push 시 즉시 반영

환경 변수(VITE_API_BASE_URL)를 통해 백엔드 주소 분리 관리

✨ Features

실시간 환율 변환

통화 선택 및 스왑 기능

로딩 상태 및 에러 처리

반응형 UI (Tailwind CSS)

🧠 Notes

프론트엔드는 정적 사이트로 항상 접근 가능

실제 데이터 처리는 백엔드에서 수행

백엔드 서버 상태에 따라 첫 응답이 지연될 수 있음

🔗 Related Project

Backend Repository: FastAPI + Render

API Docs: /docs 엔드포인트 제공

👤 Author

GitHub: https://github.com/nekh802
