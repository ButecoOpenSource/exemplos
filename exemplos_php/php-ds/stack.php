<?php

use Ds\Stack;

$stack = new Stack;

for($x = 0; $x < 1000000; $x++){
    $stack->push($x);
}

echo memory_get_usage(); //19208792
