import aiohttp


class Frankfurter:
    
    @staticmethod
    async def get_currency_rate(amount: int, from_currency: str, to_currency: str):
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data["rates"][to_currency]
                    elif response.status == 404:
                        return "Валюта не найдена!"
                    else:
                        return "Неверный формат."
            except Exception:
                return "API."
    
    @staticmethod
    async def get_currency_list():
        url = f"https://api.frankfurter.app/latest"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return ", ".join(data["rates"].keys())
                    else:
                        return "Некая ошибка."
            except Exception:
                return "Ошибка API."