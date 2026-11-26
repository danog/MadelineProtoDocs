# inlineBotSwitchPM

> The bot requested the user to message them in private

[Back to constructors index](/API_docs/constructors/index.html)



The bot requested the user to message them in private

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Text for the button that switches the user to a private chat with the bot and sends the bot a start message with the parameter `start_parameter` (can be empty)|
|start\_param|[string](/API_docs/types/string.html) | Yes|The parameter for the `/start parameter`|



### Type: [InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.html)


### Example:

```
$inlineBotSwitchPM = ['_' => 'inlineBotSwitchPM', 'text' => 'string', 'start_param' => 'string'];
```
