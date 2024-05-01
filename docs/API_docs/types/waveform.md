---
title: waveform
description: An array representing the waveform of a voice message
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Type: waveform
[Back to constructor index](index.html)

The waveform of a voice message is represented by an array of 100 elements, containing integers ranging from 0 to 31.  

```php
$waveform = array_fill(0, 100, 0);
$waveform = array_fill(0, 100, 31);
```

