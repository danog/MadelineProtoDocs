---
title: "danog\\MadelineProto\\EventHandler\\Poll\\QuizPoll: Represents a quiz (with wrong and correct answers, results shown in the return type) poll"
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Poll\QuizPoll`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Represents a quiz (with wrong and correct answers, results shown in the return type) poll  



## Properties
* `$solution`: `?string` Explanation of quiz solution
* `$solutionEntities`: `list<MessageEntity>` Message [entities](https://core.telegram.org/api/entities) for styled text in quiz solution
* `$id`: `int` ID of the poll
* `$closed`: `bool` Whether the poll is closed and doesn’t accept any more answers
* `$question`: `string` The question of the poll
* `$questionEntities`: `list<MessageEntity>` Styled text entities in the question of the poll.
* `$answers`: `list<PollAnswer>` The possible answers
* `$closePeriod`: `?int` Amount of time in seconds the poll will be active after creation, 5-600
* `$closeDate`: `?int` Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future
* `$recentVoters`: `list<int>` IDs of the last users that recently voted in the poll
* `$totalVoters`: `?int` Total number of people that voted in the poll

## Method list:
* [`getSolutionHTML(bool $allowTelegramTags = false): ?string`](#getSolutionHTML)
* [`fromRawPoll(array $rawPoll): \danog\MadelineProto\EventHandler\AbstractPoll`](#fromRawPoll)
* [`getQuestionHTML(bool $allowTelegramTags = false): string`](#getQuestionHTML)

## Methods:
### <a name="getSolutionHTML"></a> `getSolutionHTML(bool $allowTelegramTags = false): ?string`

Get an HTML version of the solution.


Parameters:

* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  



### <a name="fromRawPoll"></a> `fromRawPoll(array $rawPoll): \danog\MadelineProto\EventHandler\AbstractPoll`




Parameters:

* `$rawPoll`: `array`   



### <a name="getQuestionHTML"></a> `getQuestionHTML(bool $allowTelegramTags = false): string`

Get an HTML version of the question.


Parameters:

* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
