# Krowi TTF DAM

A HACS-compatible Home Assistant custom integration that fetches TTF Day-Ahead Market (DAM) gas prices from the [Elindus](https://mijn.elindus.be) public API.

## Sensors

| Entity | Description | Unit |
|---|---|---|
| `sensor.ttf_dam_30_day_average` | 30-day average gas price | EUR/kWh |
| `sensor.ttf_dam_today` | Today's gas price | EUR/kWh |

The **today** sensor also exposes a `history` attribute containing a dictionary of the last 30 days of daily prices (`DD/MM/YYYY HH:MM → EUR/kWh`).

## Installation

### HACS (recommended)

1. Open HACS in Home Assistant.
2. Go to **Integrations** → three-dot menu → **Custom repositories**.
3. Add `TheKrowi/ha-krowi-ttf-dam` as an **Integration**.
4. Click **Download**.
5. Restart Home Assistant.

### Manual

Copy the `custom_components/krowi_ttf_dam/` folder into your HA `config/custom_components/` directory and restart.

## Configuration

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **TTF DAM Gas**.
3. Click **Submit** — no credentials required.

Only one instance can be configured at a time.

## Data source

Prices are fetched from the unauthenticated Elindus market info API:

```
GET https://mijn.elindus.be/marketinfo/dayahead/prices
    ?from=YYYY-MM-DD&to=YYYY-MM-DD&market=GAS&granularity=DAY
```

Data is refreshed every **6 hours**. Prices are returned in EUR/kWh (converted from the API's €/MWh values).

## Links

- [Repository](https://github.com/TheKrowi/ha-krowi-ttf-dam)
- [Issue tracker](https://github.com/TheKrowi/ha-krowi-ttf-dam/issues)
