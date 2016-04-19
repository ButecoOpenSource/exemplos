<?php

use Ds\Deque;

$deque = new Deque;

for($x = 0; $x < 1000000; $x++){
    $deque->push($x);
}

echo memory_get_usage(); //17138208
