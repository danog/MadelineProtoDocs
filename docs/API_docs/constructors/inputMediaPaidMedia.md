---
title: "inputMediaPaidMedia"
description: "Paid media, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPaidMedia  
[Back to constructors index](/API_docs/constructors/index.html)



[Paid media, see here »](https://core.telegram.org/api/paid-media) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|The price of the media in [Telegram Stars](https://core.telegram.org/api/stars).|
|extended\_media|Array of [MessageMedia, Message, Update or InputMedia](/API_docs/types/InputMedia.html) | Yes|Photos or videos.|
|payload|[string](/API_docs/types/string.html) | Optional|Bots only, specifies a custom payload that will then be passed in [updateBotPurchasedPaidMedia](../constructors/updateBotPurchasedPaidMedia.html) when a payment is made (this field will not be visible to the user)|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaPaidMedia = ['_' => 'inputMediaPaidMedia', 'stars_amount' => long, 'extended_media' => [InputMedia, InputMedia], 'payload' => 'string'];
```  
