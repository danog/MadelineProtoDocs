---
title: "birthday"
description: "Birthday information for a user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: birthday  
[Back to constructors index](/API_docs/constructors/index.html)



[Birthday](https://core.telegram.org/api/profile#birthday) information for a user.

Also used to invite users to gift [Telegram Premium subscriptions »](https://core.telegram.org/api/premium#gifting-telegram-premium) to other users with birthdays within a +1/-1 day time range, related to the current day.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|day|[int](/API_docs/types/int.html) | Yes|Birth day|
|month|[int](/API_docs/types/int.html) | Yes|Birth month|
|year|[int](/API_docs/types/int.html) | Optional|(Optional) birth year.|



### Type: [Birthday](/API_docs/types/Birthday.html)


### Example:

```
$birthday = ['_' => 'birthday', 'day' => int, 'month' => int, 'year' => int];
```  
