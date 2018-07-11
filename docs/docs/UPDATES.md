---
title: Handling updates
description: Update handling can be done in different ways: 
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Handling updates

Update handling can be done in different ways: 

* [Event driven](#event-driven)
  * [Event driven multithreaded](#event-driven-multithreaded)
* [Multi-account: Combined Event driven update handling](#combined-event-driven)
* [Webhook](#webhook)
  * [Webhook multithreaded](#webhook-multithreaded)
* [Long polling (getupdates)](#long-polling)
* [Callback](#callback)
  * [Callback multithreaded](#callback-multithreaded)

IMPORTANT: Note that you should turn off update handling if you don't want to use it anymore because the default get_updates update handling stores updates in an array inside the MadelineProto object, without deleting old ones unless they are read using get_updates.  
```php
$MadelineProto->settings['updates']['handle_updates'] = false;
```

## Event driven

```php
class EventHandler extends \danog\MadelineProto\EventHandler
{
    public function __construct($MadelineProto)
    {
        parent::__construct($MadelineProto);
    }
    public function onAny($update)
    {
        \danog\MadelineProto\Logger::log("Received an update of type ".$update['_']);
    }
    public function onLoop()
    {
        \danog\MadelineProto\Logger::log("Working...");
    }
    public function onUpdateNewChannelMessage($update)
    {
        $this->onUpdateNewMessage($update);
    }
    public function onUpdateNewMessage($update)
    {
        if (isset($update['message']['out']) && $update['message']['out']) {
            return;
        }
        $res = json_encode($update, JSON_PRETTY_PRINT);
        if ($res == '') {
            $res = var_export($update, true);
        }

        try {
            $this->messages->sendMessage(['peer' => $update, 'message' => $res, 'reply_to_msg_id' => $update['message']['id'], 'entities' => [['_' => 'messageEntityPre', 'offset' => 0, 'length' => strlen($res), 'language' => 'json']]]);
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            $this->messages->sendMessage(['peer' => '@danogentili', 'message' => $e->getCode().': '.$e->getMessage().PHP_EOL.$e->getTraceAsString()]);
        }

        try {
            if (isset($update['message']['media']) && ($update['message']['media']['_'] == 'messageMediaPhoto' || $update['message']['media']['_'] == 'messageMediaDocument')) {
                $time = microtime(true);
                $file = $this->download_to_dir($update, '/tmp');
                $this->messages->sendMessage(['peer' => $update, 'message' => 'Downloaded to '.$file.' in '.(microtime(true) - $time).' seconds', 'reply_to_msg_id' => $update['message']['id'], 'entities' => [['_' => 'messageEntityPre', 'offset' => 0, 'length' => strlen($res), 'language' => 'json']]]);
            }
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            $this->messages->sendMessage(['peer' => '@danogentili', 'message' => $e->getCode().': '.$e->getMessage().PHP_EOL.$e->getTraceAsString()]);
        }
    }
}


$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setEventHandler('\EventHandler');
$MadelineProto->loop();
```

This will create an event handler class `EventHandler`, create a MadelineProto session, and set the event handler class to our newly created event handler.

When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the corresponding `onUpdateType` event handler method is called. To get a list of all possible update types, [click here](https://docs.madelineproto.xyz/API_docs/types/Update.html). 
If such a method does not exist, the `onAny` event handler method is called.  
If the `onAny` event handler method does not exist, the update is ignored.  
The `onLoop` method, if it exists, will be called every time the update loop finishes one cycle, even if no update was received.  
It is useful for scheduling actions.

To access the `$MadelineProto` instance inside of the event handler, simply access `$this`:
```php
$this->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
```

If you intend to use your own constructor in the event handler, make sure to call the parent construtor with the only parameter provided to your constructor.

The update handling loop is started by the `$MadelineProto->loop()` method, and it will automatically restart the script if execution time runs out.

To break out of the loop just call `die();`


## Event driven multithreaded

To enable multithreaded update handling, pass `-1` to the `$MadelineProto->loop` method:
```php
$MadelineProto->loop(-1);
```

This way, each update will be managed in its own fork.  
Note that multiprocessing is not the same as multithreading, and should be avoided unless lengthy operations are made in the update handler.

## Combined event driven

```php
class EventHandler extends \danog\MadelineProto\CombinedEventHandler
{
    public function __construct($CombinedMadelineProto)
    {
        parent::__construct($CombinedMadelineProto);
    }
    public function onAny($update, $session)
    {
        \danog\MadelineProto\Logger::log("Received an update of type ".$update['_']);
    }
    public function onLoop()
    {
        \danog\MadelineProto\Logger::log("Working...");
    }
    public function onUpdateNewChannelMessage($update, $session)
    {
        $this->onUpdateNewMessage($update, $session);
    }
    public function onUpdateNewMessage($update, $session)
    {
        if (isset($update['message']['out']) && $update['message']['out']) {
            return;
        }
        $res = json_encode($update, JSON_PRETTY_PRINT);
        if ($res == '') {
            $res = var_export($update, true);
        }

        try {
            $this->{$session}->messages->sendMessage(['peer' => $update, 'message' => $res, 'reply_to_msg_id' => $update['message']['id'], 'entities' => [['_' => 'messageEntityPre', 'offset' => 0, 'length' => strlen($res), 'language' => 'json']]]);
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            $this->{$session}->messages->sendMessage(['peer' => '@danogentili', 'message' => $e->getCode().': '.$e->getMessage().PHP_EOL.$e->getTraceAsString()]);
        }

        try {
            if (isset($update['message']['media']) && ($update['message']['media']['_'] == 'messageMediaPhoto' || $update['message']['media']['_'] == 'messageMediaDocument')) {
                $time = microtime(true);
                $file = $this->{$session}->download_to_dir($update, '/tmp');
                $this->{$session}->messages->sendMessage(['peer' => $update, 'message' => 'Downloaded to '.$file.' in '.(microtime(true) - $time).' seconds', 'reply_to_msg_id' => $update['message']['id'], 'entities' => [['_' => 'messageEntityPre', 'offset' => 0, 'length' => strlen($res), 'language' => 'json']]]);
            }
        } catch (\danog\MadelineProto\RPCErrorException $e) {
            $this->{$session}->messages->sendMessage(['peer' => '@danogentili', 'message' => $e->getCode().': '.$e->getMessage().PHP_EOL.$e->getTraceAsString()]);
        }
    }
}

$settings = [];
$CombinedMadelineProto = new \danog\MadelineProto\CombinedAPI('combined_session.madeline', ['bot.madeline' => $settings, 'user.madeline' => $settings, 'user2.madeline' => $settings]);

\danog\MadelineProto\Logger::log('Bot login', \danog\MadelineProto\Logger::WARNING);
$CombinedMadelineProto->instances['bot.madeline']->start();

\danog\MadelineProto\Logger::log('Userbot login');
$CombinedMadelineProto->instances['user.madeline']->start();

\danog\MadelineProto\Logger::log('Userbot login (2)');
$CombinedMadelineProto->instances['user2.madeline']->start();

$CombinedMadelineProto->setEventHandler('\EventHandler');
$CombinedMadelineProto->loop();
```

This will create an event handler class `EventHandler`, create a **combined** MadelineProto session with session files `bot.madeline`, `user.madeline`, `user2.madeline`, and set the event handler class to our newly created event handler.

When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the corresponding `onUpdateType` event handler method is called. To get a list of all possible update types, [click here](https://docs.madelineproto.xyz/API_docs/types/Update.html). 
If such a method does not exist, the `onAny` event handler method is called.  
If the `onAny` event handler method does not exist, the update is ignored.  
The first paramter of the event handler method will always be the [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html), the second parameter will always be the **session name**.

The `onLoop` method, if it exists, will be called every time the update loop finishes one cycle, even if no update was received.  
It is useful for scheduling actions.

To access the `$MadelineProto` instance of the account that sent the update, from inside of the event handler, simply access `$this->{$session_name}` (`$session_name` is the second parameter value of the event handler method, or just the session filename):
```php
$this->{$session_name}->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
$this->{'user2.madeline'}->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi2']);
```

If you intend to use your own constructor in the event handler, make sure to call the parent construtor with the only parameter provided to your constructor.

The update handling loop is started by the `$MadelineProto->loop()` method, and it will automatically restart the script if execution time runs out.

To break out of the loop just call `die();`



## Webhook
```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setWebhook('http://mybot.eu.org/madelinehook.php');
$MadelineProto->loop();
```

When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, a POST request is made to the provided webhook URL, with json-encoded payload containing the Update. To get a list of all possible update types, [click here](https://docs.madelineproto.xyz/API_docs/types/Update.html).  
DO NOT provide the current script URL as webhook URL.  
The webhook can also respond with a JSON payload containing the name of a method to call and the arguments:
```json
{"method":"messages->sendMessage", "peer":"@danogentili", "message":"hi"}
```

The loop method will automatically restart the script if execution time runs out.

## Webhook multithreaded

To enable multithreaded update handling, pass `-1` to the `$MadelineProto->loop` method:
```php
$MadelineProto->loop(-1);
```

This way, each update could be managed faster.


## Long polling
```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');
$MadelineProto->start();

while (true) {
    $updates = $MadelineProto->get_updates(['offset' => $offset, 'limit' => 50, 'timeout' => 0]); // Just like in the bot API, you can specify an offset, a limit and a timeout
    \danog\MadelineProto\Logger::log($updates);
    foreach ($updates as $update) {
        $offset = $update['update_id'] + 1; // Just like in the bot API, the offset must be set to the last update_id
        switch ($update['update']['_']) {
            case 'updateNewMessage':
            case 'updateNewChannelMessage':
                if (isset($update['update']['message']['out']) && $update['update']['message']['out']) {
                    continue;
                }
                $res = json_encode($update, JSON_PRETTY_PRINT);
                if ($res == '') {
                    $res = var_export($update, true);
                }

                try {
                    $MadelineProto->messages->sendMessage(['peer' => $update, 'message' => $res, 'reply_to_msg_id' => $update['update']['message']['id'], 'entities' => [['_' => 'messageEntityPre', 'offset' => 0, 'length' => strlen($res), 'language' => 'json']]]);
                } catch (\danog\MadelineProto\RPCErrorException $e) {
                    $MadelineProto->messages->sendMessage(['peer' => '@danogentili', 'message' => $e->getCode().': '.$e->getMessage().PHP_EOL.$e->getTraceAsString()]);
                }
        }
    }
}
```

The get_updates function accepts an array of options as the first parameter, and returns an array of updates (an array containing the update id and an object of type [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html)).  



## Callback

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setCallback(function ($update) use ($MadelineProto) { \danog\MadelineProto\Logger::log("Received an update of type ".$update['_']); });
$MadelineProto->loop();
```
When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the provided callback function is called.

The update handling loop is started by the `$MadelineProto->loop()` method, and it will automatically restart the script if execution time runs out.  

To break out of the loop just call `die();`

## Callback multithreaded

To enable multithreaded update handling, pass `-1` to the `$MadelineProto->loop` method:
```php
$MadelineProto->loop(-1);
```

This way, each update will be managed in its own fork.  
Note that multiprocessing is not the same as multithreading, and should be avoided unless lengthy operations are made in the update handler.

<a href="https://docs.madelineproto.xyz/docs/SETTINGS.html">Next section</a>