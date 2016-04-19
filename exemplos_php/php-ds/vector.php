<?php

use Ds\Vector;

$vector = new Vector;

for($x = 0; $x < 1000000; $x++){
    $vector->push($x);
}

echo memory_get_usage(); //19208792
