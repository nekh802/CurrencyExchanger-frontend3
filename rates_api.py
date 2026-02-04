import time
import requests
import os

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
if not API_KEY:
    raise RuntimeError("환경변수 EXCHANGE_RATES_API_KEY가 설정되지 않았습니다.")
URL = "https://api.exchangeratesapi.io/v1/latest"

_cache = None
_cache_saved_at = 0
CACHE_TTL = 600  # 10분

def get_live_rates() -> tuple[str, dict[str, float], float]:
    global _cache, _cache_saved_at

    now = time.time()
    #TTL 판단은 캐시 저장 시각 기준
    if _cache and now - _cache_saved_at < CACHE_TTL:
        return _cache
    
    try:
        resp = requests.get(URL, params={"access_key": API_KEY}, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        if "rates" not in data or "base" not in data:
            raise RuntimeError(f"API 응답 이상: {data}")

        base = data["base"]
        rates = {k: float(v) for k, v in data["rates"].items()}
        rates[base] = 1.0  # base 안전장치

        updated_at = now #데이터 갱신 시각

        _cache = (base, rates, updated_at)
        _cache_saved_at = now
        
        return _cache

    except Exception:
        if _cache:
            return _cache #마지막 캐시 사용, 잠깐 인터넷 끊겨도 앱 안 죽음 
        raise