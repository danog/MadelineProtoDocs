---
title: "updateStarsRevenueStatus"
description: "The Telegram Star balance of a channel/bot we own has changed »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStarsRevenueStatus  
[Back to constructors index](/API_docs/constructors/index.html)



The [Telegram Star balance of a channel/bot we own has changed »](https://core.telegram.org/api/stars#revenue-statistics).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Channel/bot|
|status|[StarsRevenueStatus](/API_docs/types/StarsRevenueStatus.html) | Yes|New Telegram Star balance.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStarsRevenueStatus = ['_' => 'updateStarsRevenueStatus', 'peer' => long, 'status' => StarsRevenueStatus];
```  
