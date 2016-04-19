<?php

use Ds\Set;

$set = new Set;

for($x = 0; $x < 1000000; $x++){
    $set->add($x);
}

echo memory_get_usage(); //38109824
