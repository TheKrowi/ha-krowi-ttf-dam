from datetime import date, timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import API_URL, DOMAIN


class KrowiTtfDamCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant) -> None:
        super().__init__(
            hass,
            logger=__import__("logging").getLogger(__name__),
            name=DOMAIN,
            update_interval=timedelta(hours=6),
        )

    async def _async_update_data(self):
        today = date.today()
        from_date = (today - timedelta(days=30)).isoformat()
        to_date = today.isoformat()
        params = {
            "from": from_date,
            "to": to_date,
            "market": "GAS",
            "granularity": "DAY",
        }
        session = async_get_clientsession(self.hass)
        try:
            async with session.get(API_URL, params=params) as resp:
                resp.raise_for_status()
                payload = await resp.json()
        except Exception as err:
            raise UpdateFailed(f"Error fetching TTF DAM data: {err}") from err

        try:
            average = float(payload["statistics"]["averagePrice"])
            data_points = sorted(payload["dataSeries"]["data"], key=lambda e: e["x"])
            today_price = float(data_points[-1]["y"])
            history = {entry["name"]: entry["y"] for entry in data_points}
        except (KeyError, IndexError, TypeError, ValueError) as err:
            raise UpdateFailed(f"Error parsing TTF DAM response: {err}") from err

        return {"average": average, "today": today_price, "history": history}
