---
title: createNewStickerSet
description: Bots only. Creates new sticker set. Returns created sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: createNewStickerSet  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Bots only. Creates new sticker set. Returns created sticker set

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[int](../types/int.md) | Sticker set owner | Yes|
|title|[string](../types/string.md) | Sticker set title, 1-64 characters | Yes|
|name|[string](../types/string.md) | Sticker set name. Can contain only english letters, digits and underscores. Should end on *"_by_<bot username>"*. *<bot_username>* is case insensitive, 1-64 characters | Yes|
|is\_masks|[Bool](../types/Bool.md) | True, is stickers are masks | Yes|
|stickers|Array of [inputSticker](../constructors/inputSticker.md) | List of stickers to add to the set | Yes|


### Return type: [StickerSet](../types/StickerSet.md)

