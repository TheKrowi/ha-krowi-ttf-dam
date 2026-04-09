# Changelog

## [1.1.0] - 2026-04-09

### Changed
- Unit changed from `€/MWh` to `EUR/kWh` (values divided by 1000).
- Sensor values and history attribute rounded to 7 decimal places.

## [1.0.0] - 2026-04-09

### Added
- Initial release.
- `sensor.ttf_dam_30_day_average`: 30-day average TTF DAM gas price.
- `sensor.ttf_dam_today`: Today's TTF DAM gas price with 30-day history attribute.
- Data fetched from the unauthenticated Elindus market info API, refreshed every 6 hours.
