---
title: "danog\\MadelineProto\\EventHandler\\Message\\Service\\DialogSuggestProfilePhoto: A new profile picture was suggested using [photos.uploadContactProfilePhoto](https://docs.madelineproto.xyz/API_docs/methods/photos.uploadContactProfilePhoto.html)."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Message\Service\DialogSuggestProfilePhoto`
[Back to index](../../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

A new profile picture was suggested using [photos.uploadContactProfilePhoto](https://docs.madelineproto.xyz/API_docs/methods/photos.uploadContactProfilePhoto.html).  



## Properties
* `$photo`: `?\danog\MadelineProto\EventHandler\Media\Photo` The photo that the user suggested we set as profile picture.
* `$id`: `int` Message ID
* `$out`: `bool` Whether the message is outgoing
* `$chatId`: `int` ID of the chat where the message was sent
* `$senderId`: `int` ID of the sender of the message
* `$replyToMsgId`: `?int` ID of the message to which this message is replying
* `$date`: `int` When was the message sent
* `$topicId`: `?int` ID of the forum topic where the message was sent
* `$threadId`: `?int` ID of the message thread where the message was sent
* `$replyToScheduled`: `bool` Whether this is a reply to a scheduled message
* `$mentioned`: `bool` Whether we were mentioned in this message
* `$silent`: `bool` Whether this message was sent without any notification (silently)
* `$ttlPeriod`: `?int` Time-to-live of the message

## Method list:
* [`__construct(\danog\MadelineProto\MTProto $API, array $rawMessage, array $info, ?\danog\MadelineProto\EventHandler\Media\Photo $photo)`](#__construct)
* [`isReply(): bool`](#isreply)
* [`getReply(class-string<\T> $class = 'danog\\MadelineProto\\EventHandler\\AbstractMessage'): ?\T`](#getreply)
* [`delete(bool $revoke = true): void`](#delete)
* [`reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $noWebpage = false, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`](#reply)
* [`block(): bool`](#block)
* [`unblock(): bool`](#unblock)
* [`getStories(): list<\danog\MadelineProto\EventHandler\AbstractStory>`](#getstories)
* [`setAction(\danog\MadelineProto\EventHandler\Action $action = \danog\MadelineProto\EventHandler\Action\Typing::__set_state(array(]]): bool`](#setaction)
* [`read(bool $readAll = false): \bool if set, read all messages in current chat.`](#read)
* [`enableTTL(int $seconds = 86400): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`](#enablettl)
* [`disableTTL(): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`](#disablettl)

## Methods:
### `__construct(\danog\MadelineProto\MTProto $API, array $rawMessage, array $info, ?\danog\MadelineProto\EventHandler\Media\Photo $photo)`




Parameters:

* `$API`: `\danog\MadelineProto\MTProto`   
* `$rawMessage`: `array`   
* `$info`: `array`   
* `$photo`: `?\danog\MadelineProto\EventHandler\Media\Photo`   


#### See also: 
* `\danog\MadelineProto\MTProto`
* [`\danog\MadelineProto\EventHandler\Media\Photo`: Represents a photo.](../../../../../danog/MadelineProto/EventHandler/Media/Photo.html)




### `isReply(): bool`

Check if the current message replies to another message.



### `getReply(class-string<\T> $class = 'danog\\MadelineProto\\EventHandler\\AbstractMessage'): ?\T`

Get replied-to message.
May return null if the replied-to message was deleted or if the message does not reply to any other message.

Parameters:

* `$class`: `class-string<\T>` Only return a reply if it is of the specified type, return null otherwise.  


#### See also: 
* `\T`




### `delete(bool $revoke = true): void`

Delete the message.


Parameters:

* `$revoke`: `bool` Whether to delete the message for all participants of the chat.  



### `reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, array|null $replyMarkup = NULL, int|null $sendAs = NULL, int|null $scheduleDate = NULL, bool $noWebpage = false, bool $silent = false, bool $noForwards = false, bool $background = false, bool $clearDraft = false, bool $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`

Reply to the message.


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `array|null` Keyboard information.  
* `$sendAs`: `int|null` Peer to send the message as.  
* `$scheduleDate`: `int|null` Schedule date.  
* `$noWebpage`: `bool` Set this flag to disable generation of the webpage preview  
* `$silent`: `bool` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `bool`   
* `$background`: `bool` Send this message as background message  
* `$clearDraft`: `bool` Clears the draft field  
* `$updateStickersetsOrder`: `bool` Whether to move used stickersets to top  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../../danog/MadelineProto/ParseMode.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../../danog/MadelineProto/EventHandler/Message.html)




### `block(): bool`

Adds the user to the blacklist.



### `unblock(): bool`

Deletes the user from the blacklist.



### `getStories(): list<\danog\MadelineProto\EventHandler\AbstractStory>`

Get user stories.


#### See also: 
* [`\danog\MadelineProto\EventHandler\AbstractStory`: Represents a Telegram Story.](../../../../../danog/MadelineProto/EventHandler/AbstractStory.html)




### `setAction(\danog\MadelineProto\EventHandler\Action $action = \danog\MadelineProto\EventHandler\Action\Typing::__set_state(array(]]): bool`

Sends a current user typing event
(see [SendMessageAction](https://docs.madelineproto.xyz/API_docs/types/SendMessageAction.html) for all event types) to a conversation partner or group.


Parameters:

* `$action`: `\danog\MadelineProto\EventHandler\Action`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Action`: In-progress actions.](../../../../../danog/MadelineProto/EventHandler/Action.html)




### `read(bool $readAll = false): \bool if set, read all messages in current chat.`

Mark selected message as read.


Parameters:

* `$readAll`: `bool`   


Return value: if set, read all messages in current chat.


### `enableTTL(int $seconds = 86400): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`

Set maximum Time-To-Live of all messages in the specified chat.


Parameters:

* `$seconds`: `int` Automatically delete all messages sent in the chat after this many seconds  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`: The Time-To-Live of messages in this chat was changed.](../../../../../danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html)




### `disableTTL(): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`

Disable Time-To-Live of all messages in the specified chat.


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`: The Time-To-Live of messages in this chat was changed.](../../../../../danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
