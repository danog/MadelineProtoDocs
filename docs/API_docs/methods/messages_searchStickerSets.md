---
title: messages.searchStickerSets
description: Find a sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.searchStickerSets  
[Back to methods index](index.md)


Find a sticker set

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exclude\_featured|[Bool](../types/Bool.md) | Optional|Exclude featured sticker sets from the search?|
|q|[string](../types/string.md) | Yes|The search query|
|hash|[int](../types/int.md) | Yes|$MadelineProto->gen_vector_hash(ids of previously searched stickers, or []);|


### Return type: [messages\_FoundStickerSets](../types/messages_FoundStickerSets.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FoundStickerSets = $MadelineProto->messages->searchStickerSets(['exclude_featured' => Bool, 'q' => 'string', 'hash' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.searchStickerSets
* params - `{"exclude_featured": Bool, "q": "string", "hash": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.searchStickerSets`

Parameters:

exclude_featured - Json encoded Bool

q - Json encoded string

hash - Json encoded int




Or, if you're into Lua:

```
messages_FoundStickerSets = messages.searchStickerSets({exclude_featured=Bool, q='string', hash=int, })
```

