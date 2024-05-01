---
title: "statsGroupTopInviter"
description: "Information about an active supergroup inviter"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopInviter  
[Back to constructors index](/API_docs/constructors/index.html)



Information about an active supergroup inviter

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|invitations|[int](/API_docs/types/int.html) | Yes|Number of invitations for [statistics](https://core.telegram.org/api/stats) period in consideration|



### Type: [StatsGroupTopInviter](/API_docs/types/StatsGroupTopInviter.html)


### Example:

```
$statsGroupTopInviter = ['_' => 'statsGroupTopInviter', 'user_id' => long, 'invitations' => int];
```  
