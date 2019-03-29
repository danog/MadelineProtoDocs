---
title: chatInvite
description: Chat invite
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvite  
[Back to constructors index](index.md)



Chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[Bool](../types/Bool.md) | Optional|Channel?|
|broadcast|[Bool](../types/Bool.md) | Optional|Broadcast?|
|public|[Bool](../types/Bool.md) | Optional|Public?|
|megagroup|[Bool](../types/Bool.md) | Optional|Megagroup?|
|title|[string](../types/string.md) | Yes|Title|



### Type: [ChatInvite](../types/ChatInvite.md)


### Example:

```php
$chatInvite = ['_' => 'chatInvite', 'channel' => Bool, 'broadcast' => Bool, 'public' => Bool, 'megagroup' => Bool, 'title' => 'string'];
```  


Or, if you're into Lua:

```lua
chatInvite={_='chatInvite', channel=Bool, broadcast=Bool, public=Bool, megagroup=Bool, title='string'}

```


