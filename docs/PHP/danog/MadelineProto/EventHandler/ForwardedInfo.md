---
title: "danog\\MadelineProto\\EventHandler\\ForwardedInfo: Info about a forwarded message."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\ForwardedInfo`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Info about a forwarded message.  



## Properties
* `$date`: `int` When was the message originally sent
* `$fromId`: `?int` The ID of the user that originally sent the message
* `$fromName`: `?string` The name of the user that originally sent the message
* `$forwardedChannelMsgId`: `?int` ID of the channel message that was forwarded
* `$forwardedChannelMsgAuthor`: `?string` For channels and if signatures are enabled, author of the channel message that was forwareded
* `$savedFromId`: `?int` Only for messages forwarded to Saved Messages, full info about the user/channel that originally sent the message
* `$savedFromMsgId`: `?int` Only for messages forwarded to Saved Messages, ID of the message that was forwarded from the original user/channel
---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
