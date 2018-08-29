---
title: addRecentSticker
description: Manually adds new sticker to the list of recently used stickers. New sticker is added to the beginning of the list. If the sticker is already in the list, at first it is removed from the list. Only stickers belonging to a sticker set can be added to the list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: addRecentSticker  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Manually adds new sticker to the list of recently used stickers. New sticker is added to the beginning of the list. If the sticker is already in the list, at first it is removed from the list. Only stickers belonging to a sticker set can be added to the list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|is\_attached|[Bool](../types/Bool.md) | Pass true to add the sticker to the list of stickers recently attached to photo or video files, pass false to add the sticker to the list of recently sent stickers | Yes|
|sticker|[InputFile](../types/InputFile.md) | Sticker file to add | Yes|


### Return type: [Stickers](../types/Stickers.md)

