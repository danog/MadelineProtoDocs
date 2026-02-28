---
title: "payments.getSavedStarGifts"
description: "Fetch the full list of [gifts](https://core.telegram.org/api/gifts) owned by a peer."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getSavedStarGifts.html
---
# Method: payments.getSavedStarGifts
[Back to methods index](index.html)



Fetch the full list of [gifts](https://core.telegram.org/api/gifts) owned by a peer.

Note that unlike what the name suggests, the method can be used to fetch both "saved" and "unsaved" gifts (aka gifts both pinned and not pinned) to the profile, depending on the passed flags.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_unsaved|[Bool](/API_docs/types/Bool.html) | Exclude gifts not pinned on the profile. | Optional|
|exclude\_saved|[Bool](/API_docs/types/Bool.html) | Exclude gifts pinned on the profile. | Optional|
|exclude\_unlimited|[Bool](/API_docs/types/Bool.html) | Exclude gifts that do not have the [starGift](../constructors/starGift.html).`limited` flag set. | Optional|
|exclude\_unique|[Bool](/API_docs/types/Bool.html) | Exclude [collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts). | Optional|
|sort\_by\_value|[Bool](/API_docs/types/Bool.html) | If set, sorts the gifts by price instead of reception date. | Optional|
|exclude\_upgradable|[Bool](/API_docs/types/Bool.html) | Exclude gifts that can be [upgraded to collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts). | Optional|
|exclude\_unupgradable|[Bool](/API_docs/types/Bool.html) | Exclude gifts that cannot be [upgraded to collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts). | Optional|
|peer\_color\_available|[Bool](/API_docs/types/Bool.html) |  | Optional|
|exclude\_hosted|[Bool](/API_docs/types/Bool.html) |  | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Fetch only gifts owned by the specified peer, such as: a user, with peer=[inputPeerUser](../constructors/inputPeerUser.html); a channel, with peer=[inputPeerChannel](../constructors/inputPeerChannel.html); a [connected business user](https://core.telegram.org/api/bots/connected-business-bots) (when executing the method as a bot, over the business connection), with peer=[inputPeerUser](../constructors/inputPeerUser.html). | Optional|
|collection\_id|[int](/API_docs/types/int.html) | Only returns gifts within the specified [collection »](https://core.telegram.org/api/gifts#gift-collections). | Optional|
|offset|[string](/API_docs/types/string.html) | [Offset for pagination](https://core.telegram.org/api/offsets). | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [payments.SavedStarGifts](/API_docs/types/payments.SavedStarGifts.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_SavedStarGifts = $MadelineProto->payments->getSavedStarGifts(exclude_unsaved: $Bool, exclude_saved: $Bool, exclude_unlimited: $Bool, exclude_unique: $Bool, sort_by_value: $Bool, exclude_upgradable: $Bool, exclude_unupgradable: $Bool, peer_color_available: $Bool, exclude_hosted: $Bool, peer: $InputPeer, collection_id: $int, offset: 'string', limit: $int, );
```

