---
title: bytes
description: A string of variable length
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Type: bytes  
[Back to constructor index](index.md)

An object of type `\danog\MadelineProto\TL\Types\Bytes`.  
When casted to string, turns into a string of bytes of variable length, with length smaller than or equal to 16777215.  
When JSON-serialized, turns into an array of the following format:  
```
[
   '_'     => 'bytes',
   'bytes' => base64_encode($contents)
];
```
