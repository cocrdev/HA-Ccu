"""Platform for sensor integration."""
from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([CcuSensor()])

class CcuSensor(Entity):
    """Representation of a sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'My Sensor'
        
    @property
    def state(self):
        """Return the state of the sensor."""
        return 23  # We set a constant state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "°C"  # We use the °C as a unit of measurement
