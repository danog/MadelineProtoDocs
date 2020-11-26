---
title: pageBlockAudio
description: Audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAudio  
[Back to constructors index](index.md)



Audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|audio\_id|[long](../types/long.md) | Yes|Audio ID (to be fetched from the container [page](../constructors/page.md) constructor|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Audio caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockAudio = ['_' => 'pageBlockAudio', 'audio_id' => long, 'caption' => PageCaption];
```  


Or, if you're into Lua:

```lua
pageBlockAudio={_='pageBlockAudio', audio_id=long, caption=PageCaption}

```


