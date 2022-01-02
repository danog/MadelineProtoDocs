---
title: "updateBotWebhookJSON"
description: "A new incoming event; for bots only"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotWebhookJSON  
[Back to constructors index](index.md)



A new incoming event; for bots only

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[DataJSON](../types/DataJSON.md) | Yes|The event|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotWebhookJSON = ['_' => 'updateBotWebhookJSON', 'data' => DataJSON];
```  


Or, if you're into Lua:

```lua
updateBotWebhookJSON={_='updateBotWebhookJSON', data=DataJSON}

```


