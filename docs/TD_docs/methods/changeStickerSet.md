---
title: changeStickerSet
description: Installs/uninstalls or enables/archives sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: changeStickerSet  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Installs/uninstalls or enables/archives sticker set

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|set\_id|[int64](../constructors/int64.md) | Identifier of the sticker set | Yes|
|is\_installed|[Bool](../types/Bool.md) | New value of is_installed | Yes|
|is\_archived|[Bool](../types/Bool.md) | New value of is_archived. A sticker set can't be installed and archived simultaneously | Yes|


### Return type: [Ok](../types/Ok.md)

