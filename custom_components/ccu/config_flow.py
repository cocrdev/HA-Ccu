from homeassistant import config_entries

class CcuConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for CCU."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(step_id="user")

        return self.async_create_entry(title="CCU", data=user_input)
