<?php

use Ds\Map;

$map = new Map;

for($x = 0; $x < 1000000; $x++){
    $map->put($x, $x);
}

echo memory_get_usage(); //38109824
