<?php

use danog\MadelineProto\API;

require 'vendor/autoload.php';

$a = new API('session.madeline');
var_dump($a->messages->getChatInviteImporters(
    peer: 'https://t.me/+Por5orOjwgccnt2w',
    link: 'https://t.me/+Por5orOjwgccnt2w'
));