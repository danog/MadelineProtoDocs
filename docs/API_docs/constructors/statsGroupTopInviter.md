---
title: statsGroupTopInviter
description: Information about an active supergroup inviter
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopInviter  
[Back to constructors index](index.md)



Information about an active supergroup inviter

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|invitations|[int](../types/int.md) | Yes|Number of invitations for [statistics](https://core.telegram.org/api/stats) period in consideration|



### Type: [StatsGroupTopInviter](../types/StatsGroupTopInviter.md)


### Example:

```php
$statsGroupTopInviter = ['_' => 'statsGroupTopInviter', 'user_id' => long, 'invitations' => int];
```  


Or, if you're into Lua:

```lua
statsGroupTopInviter={_='statsGroupTopInviter', user_id=long, invitations=int}

```


