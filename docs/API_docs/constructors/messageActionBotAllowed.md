---
title: "messageActionBotAllowed"
description: "The domain name of the website on which the user has logged in. More about Telegram Login »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionBotAllowed  
[Back to constructors index](index.md)



The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|domain|[string](../types/string.md) | Yes|The domain name of the website on which the user has logged in.|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionBotAllowed = ['_' => 'messageActionBotAllowed', 'domain' => 'string'];
```  


Or, if you're into Lua:

```lua
messageActionBotAllowed={_='messageActionBotAllowed', domain='string'}

```


