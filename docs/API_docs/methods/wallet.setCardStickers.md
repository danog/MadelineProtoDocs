---
title: "wallet.setCardStickers"
description: "wallet.setCardStickers parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_setCardStickers.html
---
# Method: wallet.setCardStickers
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stickers|Array of [InputWalletCardSticker](/API_docs/types/InputWalletCardSticker.html) | Yes|
|bg\_nft\_address|[string](/API_docs/types/string.html) | Optional|


### Return type: [wallet.Card](/API_docs/types/wallet.Card.html)

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

$wallet_Card = $MadelineProto->wallet->setCardStickers(stickers: [$InputWalletCardSticker, $InputWalletCardSticker], bg_nft_address: 'string', );
```

