---
title: "danog\\MadelineProto\\EventHandler\\Message\\Service\\DialogWebView: Data from an opened [reply keyboard bot web app](https://core.telegram.org/api/bots/webapps) was relayed to the bot that owns it (user & bot side service message)."
description: "Clients should display a service message with the text Data from the «$text» button was transferred to the bot.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Message\Service\DialogWebView`
[Back to index](../../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Data from an opened [reply keyboard bot web app](https://core.telegram.org/api/bots/webapps) was relayed to the bot that owns it (user & bot side service message).  

Clients should display a service message with the text Data from the «$text» button was transferred to the bot.


## Properties
* `$text`: `string` Text of the [keyboardButtonSimpleWebView](https://docs.madelineproto.xyz/API_docs/constructors/keyboardButtonSimpleWebView.html) that was pressed to open the web app.
* `$data`: `?string` Relayed data. (bot side service message)
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
* [`__construct(\danog\MadelineProto\MTProto $API, array $rawMessage, array $info, string $text, ?string $data)`](#__construct)
* [`isReply(): boolean`](#isReply)
* [`getReply(class-string<T> $class = 'danog\\MadelineProto\\EventHandler\\AbstractMessage'): ?T`](#getReply)
* [`delete(boolean $revoke = true): void`](#delete)
* [`reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $noWebpage = false, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#reply)
* [`sendText(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $noWebpage = false, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`](#sendText)
* [`block(): boolean`](#block)
* [`unblock(): boolean`](#unblock)
* [`getStories(): list<\danog\MadelineProto\EventHandler\AbstractStory>`](#getStories)
* [`setAction(\danog\MadelineProto\EventHandler\Action $action = \danog\MadelineProto\EventHandler\Action\Typing::__set_state(array(]]): boolean`](#setAction)
* [`read(boolean $readAll = false): boolean`](#read)
* [`enableTTL(int<1, max> $seconds = 86400): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`](#enableTTL)
* [`disableTTL(): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`](#disableTTL)
* [`enableAutoTranslate(): boolean`](#enableAutoTranslate)
* [`disableAutoTranslate(): boolean`](#disableAutoTranslate)

## Methods:
### <a name="__construct"></a> `__construct(\danog\MadelineProto\MTProto $API, array $rawMessage, array $info, string $text, ?string $data)`




Parameters:

* `$API`: `\danog\MadelineProto\MTProto`   
* `$rawMessage`: `array`   
* `$info`: `array`   
* `$text`: `string`   
* `$data`: `?string`   


#### See also: 
* `\danog\MadelineProto\MTProto`




### <a name="isReply"></a> `isReply(): boolean`

Check if the current message replies to another message.



### <a name="getReply"></a> `getReply(class-string<T> $class = 'danog\\MadelineProto\\EventHandler\\AbstractMessage'): ?T`

Get replied-to message.
  
May return null if the replied-to message was deleted or if the message does not reply to any other message.  


Parameters:

* `$class`: `class-string<T>` Only return a reply if it is of the specified type, return null otherwise.  



### <a name="delete"></a> `delete(boolean $revoke = true): void`

Delete the message.


Parameters:

* `$revoke`: `boolean` Whether to delete the message for all participants of the chat.  



### <a name="reply"></a> `reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $noWebpage = false, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Reply to the message.


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$noWebpage`: `boolean` Set this flag to disable generation of the webpage preview  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Only for bots, disallows further re-forwarding and saving of the messages, even if the destination chat doesn’t have [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) enabled  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../../danog/MadelineProto/EventHandler/Message.html)




### <a name="sendText"></a> `sendText(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|string|null) $sendAs = NULL, (integer|null) $scheduleDate = NULL, boolean $noWebpage = false, boolean $silent = false, boolean $noForwards = false, boolean $background = false, boolean $clearDraft = false, boolean $updateStickersetsOrder = false, ?\Amp\Cancellation $cancellation = NULL): \danog\MadelineProto\EventHandler\Message`

Send a text message.


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$sendAs`: `(integer|string|null)` Peer to send the message as.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$noWebpage`: `boolean` Set this flag to disable generation of the webpage preview  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$noForwards`: `boolean` Only for bots, disallows further re-forwarding and saving of the messages, even if the destination chat doesn’t have [content protection](https://telegram.org/blog/protected-content-delete-by-date-and-more) enabled  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../../danog/MadelineProto/ParseMode.html)
* `\Amp\Cancellation`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../../danog/MadelineProto/EventHandler/Message.html)




### <a name="block"></a> `block(): boolean`

Adds the user to the blacklist.



### <a name="unblock"></a> `unblock(): boolean`

Deletes the user from the blacklist.



### <a name="getStories"></a> `getStories(): list<\danog\MadelineProto\EventHandler\AbstractStory>`

Get user stories.


#### See also: 
* [`\danog\MadelineProto\EventHandler\AbstractStory`: Represents a Telegram Story.](../../../../../danog/MadelineProto/EventHandler/AbstractStory.html)




### <a name="setAction"></a> `setAction(\danog\MadelineProto\EventHandler\Action $action = \danog\MadelineProto\EventHandler\Action\Typing::__set_state(array(]]): boolean`

Sends a current user typing event
(see [SendMessageAction](https://docs.madelineproto.xyz/API_docs/types/SendMessageAction.html) for all event types) to a conversation partner or group.  


Parameters:

* `$action`: `\danog\MadelineProto\EventHandler\Action`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Action`: In-progress actions.](../../../../../danog/MadelineProto/EventHandler/Action.html)




### <a name="read"></a> `read(boolean $readAll = false): boolean`

Mark selected message as read.


Parameters:

* `$readAll`: `boolean`   


Return value: if set, read all messages in current chat.


### <a name="enableTTL"></a> `enableTTL(int<1, max> $seconds = 86400): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`

Set maximum Time-To-Live of all messages in the specified chat.


Parameters:

* `$seconds`: `int<1, max>` Automatically delete all messages sent in the chat after this many seconds  


#### See also: 
* `max`
* [`\danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`: The Time-To-Live of messages in this chat was changed.](../../../../../danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html)




### <a name="disableTTL"></a> `disableTTL(): \danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`

Disable Time-To-Live of all messages in the specified chat.


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL`: The Time-To-Live of messages in this chat was changed.](../../../../../danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html)




### <a name="enableAutoTranslate"></a> `enableAutoTranslate(): boolean`

Show the [real-time chat translation popup](https://core.telegram.org/api/translation) for a certain chat.



### <a name="disableAutoTranslate"></a> `disableAutoTranslate(): boolean`

Hide the [real-time chat translation popup](https://core.telegram.org/api/translation) for a certain chat.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
