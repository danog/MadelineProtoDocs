---
title: "starsSubscriptionPricing"
description: "Pricing of a Telegram Star subscription »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsSubscriptionPricing  
[Back to constructors index](/API_docs/constructors/index.html)



Pricing of a [Telegram Star subscription »](https://core.telegram.org/api/invites#paid-invite-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|period|[int](/API_docs/types/int.html) | Yes|The user should pay `amount` stars every `period` seconds to gain and maintain access to the channel. <br>Currently the only allowed subscription period is `30*24*60*60`, i.e. the user will be debited amount stars every month.|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the subscription in Telegram Stars.|



### Type: [StarsSubscriptionPricing](/API_docs/types/StarsSubscriptionPricing.html)


### Example:

```
$starsSubscriptionPricing = ['_' => 'starsSubscriptionPricing', 'period' => int, 'amount' => long];
```  
