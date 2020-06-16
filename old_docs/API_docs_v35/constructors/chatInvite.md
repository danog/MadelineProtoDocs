---
title: chatInvite
description: Chat invite info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvite  
[Back to constructors index](index.md)



Chat invite info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[Bool](../types/Bool.md) | Optional|Whether this is a [channel/supergroup](https://core.telegram.org/api/channel) or a [normal group](https://core.telegram.org/api/channel)|
|broadcast|[Bool](../types/Bool.md) | Optional|Whether this is a [channel](https://core.telegram.org/api/channel)|
|public|[Bool](../types/Bool.md) | Optional|Whether this is a public [channel/supergroup](https://core.telegram.org/api/channel)|
|megagroup|[Bool](../types/Bool.md) | Optional|Whether this is a [supergroup](https://core.telegram.org/api/channel)|
|title|[string](../types/string.md) | Yes|Chat/supergroup/channel title|
|photo|[Photo](../types/Photo.md) | Optional|Chat/supergroup/channel photo|
|participants\_count|[int](../types/int.md) | Yes|Participant count|
|participants|Array of [User](../types/User.md) | Optional|A few of the participants that are in the group|



### Type: [ChatInvite](../types/ChatInvite.md)


### Example:

```php
$chatInvite = ['_' => 'chatInvite', 'channel' => Bool, 'broadcast' => Bool, 'public' => Bool, 'megagroup' => Bool, 'title' => 'string', 'photo' => Photo, 'participants_count' => int, 'participants' => [User, User]];
```  


Or, if you're into Lua:

```lua
chatInvite={_='chatInvite', channel=Bool, broadcast=Bool, public=Bool, megagroup=Bool, title='string', photo=Photo, participants_count=int, participants={User}}

```


