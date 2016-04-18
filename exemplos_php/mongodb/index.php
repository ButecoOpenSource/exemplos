<?php

// Importação do autoload do composer
require_once __DIR__.'/vendor/autoload.php';

// Conexão ao banco de dados, porta padrão 27017
$client = new MongoDB\Client();

// Retorna uma referência a coleção "users" do banco "demo"
$collection = $client->demo->users;

// Insere um novo usuário, passando como usuário (username) "admin" e como senha (password) "secret"
$result = $collection->insertOne(
    [
        'username' => 'admin',
        'password' => 'secret',
    ]
);

// Imprime o _id do último registro inserido
var_dump('Inserido novo usuário com o _id '.$result->getInsertedId());

// Busca todos os registros com nome de usuário igual a "admin"
$result = $collection->find(
    [
        'username' => 'admin',
    ]
);

// Imprime o campo _id de cada usuário no banco
foreach ($result as $entry) {
    echo $entry['_id'].' : '.$entry['username'].PHP_EOL;
}

// Atualiza um registros, alterando o usuário para "user" e a senha para "secret"
$collection->updateOne(
    [
        'username' => 'admin',
    ],
    [
        '$set' => [
                'username' => 'user',
                'password' => 'secret',
            ],
    ]);

// Atualiza vários registros, alterando o usuário para "user" e a senha para "secret"
$collection->updateMany(
    [
        'username' => 'admin',
    ],
    [
        '$set' => [
                'username' => 'user',
                'password' => 'secret',
            ],
    ]);

// Imprime os novos registros com 'username' = 'user'
$result = $collection->find(
    [
        'username' => 'user',
    ]
);

foreach ($result as $entry) {
    echo $entry['_id'].' : '.$entry['username'].PHP_EOL;
}

// Excluí um registro
$result = $collection->deleteOne(
    [
        'username' => 'user',
    ]
);

echo $result->getDeletedCount().' registro excluido'.PHP_EOL;

// Excluí vários registros
$result = $collection->deleteMany(
    [
        'username' => 'user',
    ]
);

echo $result->getDeletedCount().' registro(s) excluido(s)'.PHP_EOL;
