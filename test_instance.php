<?php

class Person
{

    private $name;
    public $age;

    // public $gender;

    public function __construct($name)
    {
        $this->name = $name;

    }

    public function getName(){
          return $this->name;
    }

    function set_age($age)
    {
        $this->age = $age;

    }

    // function set_gender($gender){
    //       $this->gender;

    // }
}




$person = new Person('sang', 20);

echo $person->getName();

echo $person->age;
var_dump($person);
?>
