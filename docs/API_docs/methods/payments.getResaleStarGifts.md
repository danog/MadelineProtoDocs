---
title: "payments.getResaleStarGifts"
description: "Get [collectible gifts](https://core.telegram.org/api/gifts#collectible-gifts) of a specific type currently on resale, see [here »](https://core.telegram.org/api/gifts#reselling-collectible-gifts) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getResaleStarGifts.html
---
# Method: payments.getResaleStarGifts
[Back to methods index](index.html)



Get [collectible gifts](https://core.telegram.org/api/gifts#collectible-gifts) of a specific type currently on resale, see [here »](https://core.telegram.org/api/gifts#reselling-collectible-gifts) for more info.

`sort_by_price` and `sort_by_num` are mutually exclusive, if neither are set results are sorted by the unixtime (descending) when their resell price was last changed.

See [here »](https://core.telegram.org/api/gifts#sending-gifts) for detailed documentation on this method.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sort\_by\_price|[Bool](/API_docs/types/Bool.html) | Sort gifts by price (ascending). | Optional|
|sort\_by\_num|[Bool](/API_docs/types/Bool.html) | Sort gifts by number (ascending). | Optional|
|for\_craft|[Bool](/API_docs/types/Bool.html) |  | Optional|
|attributes\_hash|[long](/API_docs/types/long.html) | If a previous call to the method was made and [payments.resaleStarGifts](../constructors/payments.resaleStarGifts.html).`attributes_hash` was set, pass it here to avoid returning any results if they haven't changed. <br>Otherwise, set this flag and pass `0` to return [payments.resaleStarGifts](../constructors/payments.resaleStarGifts.html).`attributes_hash` and [payments.resaleStarGifts](../constructors/payments.resaleStarGifts.html).`attributes`, **these two fields will not be set** if this flag is not set. | Optional|
|gift\_id|[long](/API_docs/types/long.html) | Mandatory identifier of the base gift from which the collectible gift was upgraded. | Yes|
|attributes|Array of [StarGiftAttributeId](/API_docs/types/StarGiftAttributeId.html) | Optionally filter gifts with the specified attributes. If no attributes of a specific type are specified, all attributes of that type are allowed. | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination. If not equal to an empty string, [payments.resaleStarGifts](../constructors/payments.resaleStarGifts.html).`counters` will not be set to avoid returning the counters every time a new page is fetched. | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [payments.ResaleStarGifts](/API_docs/types/payments.ResaleStarGifts.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_ResaleStarGifts = $MadelineProto->payments->getResaleStarGifts(sort_by_price: $Bool, sort_by_num: $Bool, for_craft: $Bool, attributes_hash: $long, gift_id: $long, attributes: [$StarGiftAttributeId, $StarGiftAttributeId], offset: 'string', limit: $int, );
```

