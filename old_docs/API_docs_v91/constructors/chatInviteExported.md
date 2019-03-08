---
title: chatInviteExported
description: Exported chat invite
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteExported  
[Back to constructors index](index.md)



Exported chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|link|[string](../types/string.md) | Yes|Link|



### Type: [ExportedChatInvite](../types/ExportedChatInvite.md)


### Example:

```php
$chatInviteExported = ['_' => 'chatInviteExported', 'link' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatInviteExported", "link": "string"}
```


Or, if you're into Lua:

```lua
chatInviteExported={_='chatInviteExported', link='string'}

```


