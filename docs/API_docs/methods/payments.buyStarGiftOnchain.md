---
title: "payments.buyStarGiftOnchain"
description: "payments.buyStarGiftOnchain parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_buyStarGiftOnchain.html
---
# Method: payments.buyStarGiftOnchain
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|show\_name|[Bool](/API_docs/types/Bool.html) | Optional|
|slug|[string](/API_docs/types/string.html) | Optional|
|expected\_amount|[long](/API_docs/types/long.html) | Yes|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|


### Return type: [payments.StarGiftOnchainSalePayload](/API_docs/types/payments.StarGiftOnchainSalePayload.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_StarGiftOnchainSalePayload = $MadelineProto->payments->buyStarGiftOnchain(show_name: $Bool, slug: 'string', expected_amount: $long, peer: $InputPeer, message: $TextWithEntities, );
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [payments.StarGiftOnchainSalePayload](../types/payments.StarGiftOnchainSalePayload.html) will be returned instead.


