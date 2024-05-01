---
title: "danog\\MadelineProto\\EventHandler\\Story\\Story: Represents a Telegram story."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Story\Story`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents a Telegram story.  



## Properties
* `$pinned`: `bool` Whether this story is pinned
* `$public`: `bool` Whether this story is visible to everyone
* `$closeFriends`: `bool` Whether this story is visible to only close friends of the user (@see Privacy::AllowCloseFriends)
* `$contacts`: `bool` Whether this story is only visible to your countacts
* `$selectedContacts`: `bool` Whether this story is only visible to a select list of contacts
* `$protected`: `bool` Whether this media is protected
* `$edited`: `bool` Whether this story was edited
* `$date`: `int` When was the story sent
* `$expireDate`: `int` Expiration date of the story
* `$caption`: `string` Story caption
* `$entities`: `list<MessageEntity>` Message [entities](https://core.telegram.org/api/entities) for story caption
* `$media`: `(danog\MadelineProto\EventHandler\Media\Gif | danog\MadelineProto\EventHandler\Media\Photo | danog\MadelineProto\EventHandler\Media\Video)` Attached media.
* `$privacy`: `list<RuleDestination>` 
* `$sentReaction`: `(string | int | null)` Our reaction to the story
* `$reactionCount`: `?int` Reaction counter
* `$views`: `?int` View counter
* `$recentViewers`: `list<int>` List of users who recently viewed the story
* `$matches`: `list<string>` 
Regex matches, if a filter regex is present
* `$matchesAll`: `array<array-key, (array<array-key, (list{string, int} | null | string)> | mixed)>` 
Regex matches, if a filter multiple match regex is present
* `$senderId`: `int` ID of the sender of the story
* `$id`: `int` Story ID

## Method list:
* [`reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $background = false, boolean $clearDraft = false, boolean $noWebpage = false, boolean $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`](#reply)
* [`delete(): void`](#delete)
* [`exportLink(): string`](#exportLink)
* [`report(\danog\MadelineProto\EventHandler\Message\ReportReason $reason, string $message = ''): boolean`](#report)
* [`pin(): void`](#pin)
* [`unpin(): void`](#unpin)
* [`view(): boolean`](#view)
* [`addReaction((integer|string) $reaction, boolean $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`](#addReaction)
* [`delReaction(boolean $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`](#delReaction)
* [`getHTML(bool $allowTelegramTags = false): string`](#getHTML)

## Methods:
### <a name="reply"></a> `reply(string $message, \danog\MadelineProto\ParseMode $parseMode = \danog\MadelineProto\ParseMode::TEXT, (array|null) $replyMarkup = NULL, (integer|null) $scheduleDate = NULL, boolean $silent = false, boolean $background = false, boolean $clearDraft = false, boolean $noWebpage = false, boolean $updateStickersetsOrder = false): \danog\MadelineProto\EventHandler\Message`

Reply to the story.


Parameters:

* `$message`: `string` Message to send  
* `$parseMode`: `\danog\MadelineProto\ParseMode` Parse mode  
* `$replyMarkup`: `(array|null)` Keyboard information.  
* `$scheduleDate`: `(integer|null)` Schedule date.  
* `$silent`: `boolean` Whether to send the message silently, without triggering notifications.  
* `$background`: `boolean` Send this message as background message  
* `$clearDraft`: `boolean` Clears the draft field  
* `$noWebpage`: `boolean` Set this flag to disable generation of the webpage preview  
* `$updateStickersetsOrder`: `boolean` Whether to move used stickersets to top  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../danog/MadelineProto/ParseMode.html)
* [`\danog\MadelineProto\EventHandler\Message`: Represents an incoming or outgoing message.](../../../../danog/MadelineProto/EventHandler/Message.html)




### <a name="delete"></a> `delete(): void`

Delete the story.



### <a name="exportLink"></a> `exportLink(): string`

Export story link e.g: https://t.me/username/s/storyid.



### <a name="report"></a> `report(\danog\MadelineProto\EventHandler\Message\ReportReason $reason, string $message = ''): boolean`

Report a story for violation of telegram’s Terms of Service.


Parameters:

* `$reason`: `\danog\MadelineProto\EventHandler\Message\ReportReason` Why is story being reported  
* `$message`: `string` Comment for report moderation  


#### See also: 
* [\danog\MadelineProto\EventHandler\Message\ReportReason](../../../../danog/MadelineProto/EventHandler/Message/ReportReason.html)




### <a name="pin"></a> `pin(): void`

Pin a story.



### <a name="unpin"></a> `unpin(): void`

Unpin a story.



### <a name="view"></a> `view(): boolean`

Mark story as read.



### <a name="addReaction"></a> `addReaction((integer|string) $reaction, boolean $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`

Reaction to story.


Parameters:

* `$reaction`: `(integer|string)` string or int Reaction  
* `$recent`: `boolean`   


#### See also: 
* [`\danog\MadelineProto\EventHandler\Story\StoryReaction`: Represents a reaction to a story.](../../../../danog/MadelineProto/EventHandler/Story/StoryReaction.html)




### <a name="delReaction"></a> `delReaction(boolean $recent = true): \danog\MadelineProto\EventHandler\Story\StoryReaction`

Delete reaction from story.


Parameters:

* `$recent`: `boolean` string or int Reaction  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Story\StoryReaction`: Represents a reaction to a story.](../../../../danog/MadelineProto/EventHandler/Story/StoryReaction.html)




### <a name="getHTML"></a> `getHTML(bool $allowTelegramTags = false): string`

Get an HTML version of the story caption.


Parameters:

* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
