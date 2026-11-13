# updateMessagePoll

> The results of a poll have changed

[Back to constructors index](/API_docs/constructors/index.html)



The results of a poll have changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|poll\_id|[long](/API_docs/types/long.html) | Yes|Poll ID|
|poll|[Poll](/API_docs/types/Poll.html) | Optional|If the server knows the client hasn't cached this poll yet, the poll itself|
|results|[PollResults](/API_docs/types/PollResults.html) | Yes|New poll results|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessagePoll = ['_' => 'updateMessagePoll', 'peer' => long, 'msg_id' => int, 'top_msg_id' => int, 'poll_id' => long, 'poll' => Poll, 'results' => PollResults];
```
