---
title: "inputInvoiceStarGift"
description: "Used to buy a Telegram Star Gift, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



Used to buy a [Telegram Star Gift, see here »](https://core.telegram.org/api/gifts) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hide\_name|[Bool](/API_docs/types/Bool.html) | Optional|If set, your name will be hidden if the destination user decides to display the gift on their profile (they will still see that you sent the gift)|
|include\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|gift\_id|[long](/API_docs/types/long.html) | Yes|Identifier of the gift, from [starGift](../constructors/starGift.html).`id`|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Optional message, attached with the gift. <br>The maximum length for this field is specified in the [stargifts\_message\_length\_max client configuration value »](https://core.telegram.org/api/config#stargifts-message-length-max).|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceStarGift = ['_' => 'inputInvoiceStarGift', 'hide_name' => Bool, 'include_upgrade' => Bool, 'peer' => InputPeer, 'gift_id' => long, 'message' => TextWithEntities];
```  
