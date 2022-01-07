---
title: "statsGroupTopAdmin"
description: "Information about an active admin in a supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: statsGroupTopAdmin  
[Back to constructors index](/API_docs/constructors/index.md)



Information about an active admin in a supergroup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|deleted|[int](/API_docs/types/int.md) | Yes|Number of deleted messages for [statistics](https://core.telegram.org/api/stats) period in consideration|
|kicked|[int](/API_docs/types/int.md) | Yes|Number of kicked users for [statistics](https://core.telegram.org/api/stats) period in consideration|
|banned|[int](/API_docs/types/int.md) | Yes|Number of banned users for [statistics](https://core.telegram.org/api/stats) period in consideration|



### Type: [StatsGroupTopAdmin](/API_docs/types/StatsGroupTopAdmin.md)


### Example:

```php
$statsGroupTopAdmin = ['_' => 'statsGroupTopAdmin', 'user_id' => long, 'deleted' => int, 'kicked' => int, 'banned' => int];
```  
