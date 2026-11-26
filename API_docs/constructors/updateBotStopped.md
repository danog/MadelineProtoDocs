# updateBotStopped

> A bot was stopped or re-started.

[Back to constructors index](/API_docs/constructors/index.html)



A bot was stopped or re-started.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|The user ID|
|date|[int](/API_docs/types/int.html) | Yes|When did this action occur|
|stopped|[Bool](/API_docs/types/Bool.html) | Yes|Whether the bot was stopped or started|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotStopped = ['_' => 'updateBotStopped', 'user_id' => long, 'date' => int, 'stopped' => Bool, 'qts' => int];
```
