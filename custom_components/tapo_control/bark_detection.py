from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from . import TapoCoordinator
from .const import DOMAIN

BARK_DETECTION = "bark_detection"

class TapoBarkDetectionBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Representation of a Tapo Camera Bark Detection binary sensor."""

    def __init__(self, coordinator: TapoCoordinator, device):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._device = device
        self._attr_name = f"{device.name} Bark Detection"
        self._attr_unique_id = f"{device.device_id}_{BARK_DETECTION}"
        self._attr_device_class = "sound"

    @property
    def is_on(self):
        """Return true if bark detection is active."""
        return self.coordinator.data.get(BARK_DETECTION, False)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Tapo binary sensors."""
    coordinator: TapoCoordinator = hass.data[DOMAIN][entry.entry_id]
    device = coordinator.device
    
    entities = []
    if device.has_bark_detection:
        entities.append(TapoBarkDetectionBinarySensor(coordinator, device))
    
    async_add_entities(entities)
