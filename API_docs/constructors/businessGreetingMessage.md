# businessGreetingMessage

> Describes a Telegram Business greeting, automatically sent to new users writing to us in private for the first time, or after a certain inactivity period.

[Back to constructors index](/API_docs/constructors/index.html)



Describes a [Telegram Business greeting](https://core.telegram.org/api/business#greeting-messages), automatically sent to new users writing to us in private for the first time, or after a certain inactivity period.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|ID of a [quick reply shorcut, containing the greeting messages to send, see here » for more info](https://core.telegram.org/api/business#quick-reply-shortcuts).|
|recipients|[BusinessRecipients](/API_docs/types/BusinessRecipients.html) | Yes|Allowed recipients for the greeting messages.|
|no\_activity\_days|[int](/API_docs/types/int.html) | Yes|The number of days after which a private chat will be considered as inactive; currently, must be one of 7, 14, 21, or 28.|



### Type: [BusinessGreetingMessage](/API_docs/types/BusinessGreetingMessage.html)


### Example:

```
$businessGreetingMessage = ['_' => 'businessGreetingMessage', 'shortcut_id' => int, 'recipients' => BusinessRecipients, 'no_activity_days' => int];
```
