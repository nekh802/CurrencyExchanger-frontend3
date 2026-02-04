from pathlib import Path
from requests.exceptions import Timeout, ConnectionError

from fastapi import FastAPI, HTTPException, Request

from Core import convert_amount, format_money
from rates_api import get_live_rates

from fastapi.middleware.cors import CORSMiddleware


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Exchange Rate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/convert")
def convert(amount: float, from_currency: str, to_currency: str):
    try:
        base, rates, updated_at = get_live_rates()

        src_u = from_currency.strip().upper()
        dst_u = to_currency.strip().upper()

        supported = set(rates.keys()) | {base}
        if src_u not in supported:
            raise HTTPException(status_code=400, detail=f"지원하지 않는 통화(src): {src_u}")
        if dst_u not in supported:
            raise HTTPException(status_code=400, detail=f"지원하지 않는 통화(dst): {dst_u}")

        raw_result = convert_amount(amount, src_u, dst_u, rates, base)
        formatted_result = format_money(raw_result, dst_u)

        return {
            "amount": amount,
            "from": src_u,
            "to": dst_u,
            "result": formatted_result,
            "base": base,
            "updated_at": updated_at,
        }
    

    except HTTPException:
        raise
    except ValueError:
        raise HTTPException(status_code=400, detail="amount 값이 올바르지 않습니다.")
    except Timeout:
        raise HTTPException(status_code=504, detail="환율 서버 응답 지연")
    except ConnectionError:
        raise HTTPException(status_code=503, detail="환율 서버 연결 실패")
    except Exception as e:
        # 개발용: 에러 메시지 노출 (배포에선 조심)
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")
