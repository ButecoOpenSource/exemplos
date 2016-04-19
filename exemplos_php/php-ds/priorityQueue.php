<?php

use Ds\PriorityQueue;

$queue = new PriorityQueue;

for($x = 0; $x < 1000000; $x++){
    $queue->push($x, $x);
}

echo memory_get_usage(); //25527000
