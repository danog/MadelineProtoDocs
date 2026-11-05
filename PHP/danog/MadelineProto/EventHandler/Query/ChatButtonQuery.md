# danog\MadelineProto\EventHandler\Query\ChatButtonQuery: Represents a query sent by the user by clicking on a button in a chat.

[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents a query sent by the user by clicking on a button in a chat.  



## Properties
* `$chatId`: `int` Chat where the inline keyboard was sent
* `$messageId`: `int` Message ID
* `$data`: `string` Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
* `$matches`: `list<string>` Regex matches, if a filter regex is present.
* `$matchesAll`: `array<array-key, (array<array-key, (list{string, int} | null | string)> | mixed)>` 
Regex matches, if a filter multiple match regex is present
* `$queryId`: `int` Query ID
* `$userId`: `int` ID of the user that pressed the button
* `$chatInstance`: `int` Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.

## Method list:
* [`editText(string $message, (array|null) $replyMarkup = NULL, ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, bool $noWebpage = false, (int|null) $scheduleDate = NULL): \danog\MadelineProto\EventHandler\Message`](#editText)
* [`editRich((string|array|RichMessage) $message, (array|null) $replyMarkup = NULL, RichParseMode $parseMode = \danog\MadelineProto\RichParseMode::TEXT, (int|null) $scheduleDate = NULL, array $media = [], boolean $rtl = false, boolean $noAutolink = false): \danog\MadelineProto\EventHandler\Message`](#editRich)
* [`editReplyMarkup(array $replyMarkup): \danog\MadelineProto\EventHandler\Message`](#editReplyMarkup)
* [`delete(boolean $revoke = true): void`](#delete)
* [`pin(bool $pmOneside = false, bool $silent = false): void`](#pin)
* [`unpin(bool $pmOneside = false, bool $silent = false): ?\danog\MadelineProto\EventHandler\Update`](#unpin)
* [`report(ReportReason $reason, string $message): bool`](#report)
* [`answer(?string $message = NULL, bool $alert = false, (string|null) $url = NULL, int $cacheTime = 300): bool`](#answer)

## Methods:
### <a name="editText"></a> `editText(string $message, (array|null) $replyMarkup = NULL, ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, bool $noWebpage = false, (int|null) $scheduleDate = NULL): \danog\MadelineProto\EventHandler\Message`

Edit message text.


Parameters:

* `$message`: `string` New message  
* `$replyMarkup`: `(array|null)` Reply markup for inline keyboards  
* `$parseMode`: `ParseMode` Whether to parse HTML or Markdown markup in the message  
* `$noWebpage`: `bool` Disable webpage preview  
* `$scheduleDate`: `(int|null)` Scheduled message date for scheduled messages  


#### See also: 
* `ParseMode`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### <a name="editRich"></a> `editRich((string|array|RichMessage) $message, (array|null) $replyMarkup = NULL, RichParseMode $parseMode = \danog\MadelineProto\RichParseMode::TEXT, (int|null) $scheduleDate = NULL, array $media = [], boolean $rtl = false, boolean $noAutolink = false): \danog\MadelineProto\EventHandler\Message`

Edit the message, replacing it with a [rich message](https://core.telegram.org/bots/api#sendrichmessage).


Parameters:

* `$message`: `(string|array|RichMessage)` Rich message: Markdown or HTML (depending on $parseMode), a list of blocks (Block objects or Bot API InputRichBlock arrays), a received RichMessage, or a Bot API InputRichMessage (see sendRichMessage)  
* `$replyMarkup`: `(array|null)` Reply markup for inline keyboards  
* `$parseMode`: `RichParseMode` How to parse a string $message: plain text (the default) is sent as a single paragraph, Markdown and HTML are parsed by Telegram.  
* `$scheduleDate`: `(int|null)` Scheduled message date for scheduled messages  
* `$media`: `array` Media referenced by Markdown or HTML messages, as a map from ID to file (see sendRichMessage).  
* `$rtl`: `boolean` Whether the text is right-to-left  
* `$noAutolink`: `boolean` Whether to skip the automatic detection of mentions, hashtags, URLs and so on  


#### See also: 
* `RichMessage`
* `RichParseMode`
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### <a name="editReplyMarkup"></a> `editReplyMarkup(array $replyMarkup): \danog\MadelineProto\EventHandler\Message`

Edit message keyboard.


Parameters:

* `$replyMarkup`: `array` Reply markup for inline keyboards  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### <a name="delete"></a> `delete(boolean $revoke = true): void`

Delete the message.


Parameters:

* `$revoke`: `boolean` Whether to delete the message for all participants of the chat.  



### <a name="pin"></a> `pin(bool $pmOneside = false, bool $silent = false): void`

Pin a message.


Parameters:

* `$pmOneside`: `bool` Whether the message should only be pinned on the local side of a one-to-one chat  
* `$silent`: `bool` Pin the message silently, without triggering a notification  



### <a name="unpin"></a> `unpin(bool $pmOneside = false, bool $silent = false): ?\danog\MadelineProto\EventHandler\Update`

Unpin a message.


Parameters:

* `$pmOneside`: `bool` Whether the message should only be pinned on the local side of a one-to-one chat  
* `$silent`: `bool` Pin the message silently, without triggering a notification  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Update`: Represents a generic update.](../../../../danog/MadelineProto/EventHandler/Update.html)




### <a name="report"></a> `report(ReportReason $reason, string $message): bool`

Report a message in a chat for violation of telegram’s Terms of Service.


Parameters:

* `$reason`: `ReportReason` Why are these messages being reported  
* `$message`: `string` Comment for report moderation  


#### See also: 
* `ReportReason`




### <a name="answer"></a> `answer(?string $message = NULL, bool $alert = false, (string|null) $url = NULL, int $cacheTime = 300): bool`




Parameters:

* `$message`: `?string` Popup to show  
* `$alert`: `bool` Whether to show the message as a popup instead of a toast notification  
* `$url`: `(string|null)` URL to open  
* `$cacheTime`: `int` Cache validity (default set to 5 min based on telegram official docs ...)  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
