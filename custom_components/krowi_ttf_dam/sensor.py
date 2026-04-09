from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import KrowiTtfDamCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: KrowiTtfDamCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        KrowiTtfDamAverageSensor(coordinator),
        KrowiTtfDamTodaySensor(coordinator),
    ])


class _KrowiTtfDamBaseSensor(CoordinatorEntity[KrowiTtfDamCoordinator], SensorEntity):
    _attr_native_unit_of_measurement = "EUR/kWh"
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 7

    def __init__(self, coordinator: KrowiTtfDamCoordinator) -> None:
        super().__init__(coordinator)


class KrowiTtfDamAverageSensor(_KrowiTtfDamBaseSensor):
    _attr_name = "TTF DAM 30-day average"
    _attr_unique_id = "krowi_ttf_dam_average_price"

    @property
    def native_value(self):
        return self.coordinator.data["average"]


class KrowiTtfDamTodaySensor(_KrowiTtfDamBaseSensor):
    _attr_name = "TTF DAM current price"
    _attr_unique_id = "krowi_ttf_dam_current_price"

    @property
    def native_value(self):
        return self.coordinator.data["today"]

    @property
    def extra_state_attributes(self):
        return {"history": self.coordinator.data["history"]}
