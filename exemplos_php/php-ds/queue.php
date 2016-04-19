<?php

use Ds\Queue;

$queue = new Queue;

for($x = 0; $x < 1000000; $x++){
    $queue->push($x);
}

echo memory_get_usage(); //17138208
