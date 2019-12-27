---
title: updateBotInlineSend
description: The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotInlineSend  
[Back to constructors index](index.md)



The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|The user that chose the result|
|query|[string](../types/string.md) | Yes|The query that was used to obtain the result|
|id|[string](../types/string.md) | Yes|The unique identifier for the result that was chosen|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotInlineSend = ['_' => 'updateBotInlineSend', 'user_id' => int, 'query' => 'string', 'id' => 'string'];
```  


Or, if you're into Lua:

```lua
updateBotInlineSend={_='updateBotInlineSend', user_id=int, query='string', id='string'}

```


