---
title: "danog\\MadelineProto\\EventHandler\\Query\\ChatGameQuery: Represents a query sent by the user by clicking on a \"Play game\" button in a chat."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Query\ChatGameQuery`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents a query sent by the user by clicking on a "Play game" button in a chat.  



## Properties
* `$gameShortName`: `string` Short name of a Game to be returned, serves as the unique identifier for the game
* `$queryId`: `int` Query ID
* `$userId`: `int` ID of the user that pressed the button
* `$chatInstance`: `int` Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
* `$chatId`: `int` Chat where the inline keyboard was sent
* `$messageId`: `int` Message ID

## Method list:
* [`answer(string $message, bool $alert = false, string|null $url = NULL, int $cacheTime = 300): bool`](#answer-string-message-bool-alert-false-string-null-url-null-int-cachetime-300-bool)
* [`editText(string $message, array|null $replyMarkup = NULL, \ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, bool $noWebpage = false, int|null $scheduleDate = NULL): \danog\MadelineProto\EventHandler\Message`](#edittext-string-message-array-null-replymarkup-null-parsemode-parsemode-danog-madelineproto-parsemode-text-bool-nowebpage-false-int-null-scheduledate-null-danog-madelineproto-eventhandler-message)
* [`editReplyMarkup(array $replyMarkup): \danog\MadelineProto\EventHandler\Message`](#editreplymarkup-array-replymarkup-danog-madelineproto-eventhandler-message)
* [`delete(bool $revoke = true): void`](#delete-bool-revoke-true-void)
* [`pin(bool $pmOneside = false, bool $silent = false): void`](#pin-bool-pmoneside-false-bool-silent-false-void)
* [`unpin(bool $pmOneside = false, bool $silent = false): ?\danog\MadelineProto\EventHandler\Update`](#unpin-bool-pmoneside-false-bool-silent-false-danog-madelineproto-eventhandler-update)
* [`report(\ReportReason $reason, string $message): bool`](#report-reportreason-reason-string-message-bool)

## Methods:
### `answer(string $message, bool $alert = false, string|null $url = NULL, int $cacheTime = 300): bool`




Parameters:

* `$message`: `string` Popup to show  
* `$alert`: `bool` Whether to show the message as a popup instead of a toast notification  
* `$url`: `string|null` URL to open  
* `$cacheTime`: `int` Cache validity (default set to 5 min based on telegram official docs ...)  



### `editText(string $message, array|null $replyMarkup = NULL, \ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, bool $noWebpage = false, int|null $scheduleDate = NULL): \danog\MadelineProto\EventHandler\Message`

Edit message text.


Parameters:

* `$message`: `string` New message  
* `$replyMarkup`: `array|null` Reply markup for inline keyboards  
* `$parseMode`: `\ParseMode` Whether to parse HTML or Markdown markup in the message  
* `$noWebpage`: `bool` Disable webpage preview  
* `$scheduleDate`: `int|null` Scheduled message date for scheduled messages  


#### See also: 
* `\ParseMode`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### `editReplyMarkup(array $replyMarkup): \danog\MadelineProto\EventHandler\Message`

Edit message keyboard.


Parameters:

* `$replyMarkup`: `array` Reply markup for inline keyboards  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### `delete(bool $revoke = true): void`

Delete the message.


Parameters:

* `$revoke`: `bool` Whether to delete the message for all participants of the chat.  



### `pin(bool $pmOneside = false, bool $silent = false): void`

Pin a message.


Parameters:

* `$pmOneside`: `bool` Whether the message should only be pinned on the local side of a one-to-one chat  
* `$silent`: `bool` Pin the message silently, without triggering a notification  



### `unpin(bool $pmOneside = false, bool $silent = false): ?\danog\MadelineProto\EventHandler\Update`

Unpin a message.


Parameters:

* `$pmOneside`: `bool` Whether the message should only be pinned on the local side of a one-to-one chat  
* `$silent`: `bool` Pin the message silently, without triggering a notification  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Update`: Represents a generic update.](../../../../danog/MadelineProto/EventHandler/Update.html)




### `report(\ReportReason $reason, string $message): bool`

Report a message in a chat for violation of telegram’s Terms of Service.


Parameters:

* `$reason`: `\ReportReason` Why are these messages being reported  
* `$message`: `string` Comment for report moderation  


#### See also: 
* `\ReportReason`




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
