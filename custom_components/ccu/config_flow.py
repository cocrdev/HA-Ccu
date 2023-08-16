# config_flow.py
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST
from .const import DOMAIN

class CcuConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CCU."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Validate the user input
            if CONF_HOST in user_input and user_input[CONF_HOST]:
                return self.async_create_entry(title="CCU", data=user_input)
            else:
                errors[CONF_HOST] = "host_required"
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                }
            ),
            errors=errors,
        )
