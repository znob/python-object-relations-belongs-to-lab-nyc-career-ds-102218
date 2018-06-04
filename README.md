
# Python Object Relationships - Belongs To Lab

## Introduction

We have worked with many classes and domains that all seem to be related in some way. That is the point of a domain model after all, right? So, we know that our classes and domain models should mirror real world structures for our programs to operate the way we want them to. Another concept to accomplish this is Object Relationships. Don't worry, these relationships will be a lot less complex than our real world relationships -- hopefully. Basically, object relationships attempt to show how one object relates with another in a given environment or domain. So, let's take for example a `Person` class and a `Dog` class. A person could have one or many dogs and since dogs are notoriously loyal, a dog has one owner. In an object relationship this would mean that a dog *belongs to* a person. Below, we are going to practice translating this type of relationship into code.

## Objectives
* Define a car class where instances have an `owner` attribute
* Translate this ownership attribute into a **belongs to** relationship
* Practice querying a belongs to relationship

## Defining Our Class
Alright, we are going to use a Car class to demonstrate a "belongs to" relationship. So, to get started, let's define a Car class with an `__init__` method that takes in parameters for make, model, year, and owner. The make and model are will be strings representing the name of the car manufacturer and the name of the car model, the year will be a number representing the year the car was produced, and the owner will be a string with the name of the car's owner. Again, these instance variables should follow convention and use leading underscores. Let's make intance methods to both get and set (read and write) these instance variables. Use the appropriate decorators and call these methods `make`, `model`, `year`, and `owner`. We should also have a class variable `_all` which points to a list of all car instance objects and a class method called `all` that allows us to get (read) this class variable. 


```python
from car import Car
chrysler = Car("Chrysler", "Sebring Convertible", 2004, "Michael Scott")
```

## Defining Belongs To Relationship
Great, so, we now have these car instances that we can see have an owner. But who is the owner of the Sebring Convertible? Let's investigate:


```python
type(chrysler.owner) # str
```

Hmm... So, we have a string that is the name of the owner. That is okay, but what if we want to know more about this owner? Maybe we can switch this string with a dictionary so we can add some more attributes? Let's try that out.


```python
datsun = Car("Datsun", "280Z", 1978, {'name': "Dwight Schrute", 'occupation': "Paper Salesperson", 'favotite_tv_show': "Battlestar Galactica"})
datsun.owner['occupation'] # 'Paper Salesperson'
```

Alright, that's definitely better. We have way more information about the owner and it's beginning to give us more functionality as well. In fact, this dictionary kind of resembles an instance object. Let's define a Person class and have it initialize instances with a name and occupation (`_name`, `_occupation`). Make sure to include instance methods to get (read) these attributes with the appropriate decorator. 


```python
from person import Person
pam = Person("Pam Beasley", "Secretary")
```

Awesome, we now have this class that represents an actual person. We can define instance methods and all kinds of things on the Person class to make the person instance object more life-like and complex. For now, let's just relate it to our Car class.  We can do so by passing the relevant Person instance, `pam` in this case, into our Car class upon instantiation of a new Car instance.


```python
toyota = Car("Toyota", "Yaris", 2007, pam)
```


```python
type(toyota.owner)
```


```python
toyota.owner.name # 'Pam Beasley'
```


```python
toyota.owner.occupation # 'Secretary'
```

Wow, that looks so much more straightforward! Also, the car's owner is basically a real person now (okay, maybe not *basically* but definitely closer than we were with just a string.)
This relationship is a **belongs to relationship**. The car *belongs to* an owner. 

Notice that the car knows who its owner is but does the owner have a car attribute?


```python
pam.car
```

It doesn't look like it! This is partly because we don't have an instance method or variable called car, but it also kind of makes sense. Let's think about a cars registration -- it lists the owner of the car. There's only one person on the registration because there is one main driver for that car. Let's now think about a person. Let's say this person is quite affluent and also interested in cars. So, they have several cars. Does it make sense to have several cars on this person's license or other document? Not really. It could get messy and also duplicates the information about ownership. So, it is the job of the car to know its owner -- since it only has one owner.

Before moving forward, let's delete the `chrysler` instance so our queries won't break when reading this example instance.


```python
del Car.all()[0]
```

## Querying a "Belongs To" Relationship
We still want to know how many cars and what types of cars Pam has, so, we'll need to find a way to accomplish this. 

Let's think about the fact that the cars all know their owners. Where can we find a list of all the cars we have created? 

We should be able to use the car class to answer our questions about who owns which cars, how many they own, and even if there is an occupation that lends itself to driving a certain make or model car. 


```python
# let's first fix our first couple car instances and set them equal to the person instances that represent them:
# make sure you have defined your setter instance methods for the car class!
michael = Person("Michael Scott", "Regional Manager")
sebring = Car("Chrysler", "Sebring Convertible", 2004, michael)
dwight = Person("Dwight Schrute", "Paper Salesperson")
datsun.owner = dwight
# let's create more people
meredith = Person("Meredith Palmer", "Purchaser - Supplier Relations")
ford_minivan = Car("Ford", "Aerostar Minivan", 1997, meredith)
jim = Person("Jim Halpert", "Paper Salesperson")
corolla = Car("Toyota", "Corolla", 2000, jim)
stanley = Person("Stanley Hudson", "Paper Salesperson")
chrylser300 = Car ("Toyota", "Camry", 2008, stanley)
```

Alright, now let's try figuring out the employees drive toyotas, the average age of a Dunder Mifflin Employee's car, the person that owns the oldest car, and the most popular car manufacturer.


```python
Person.has_oldest_car() # class method that returns the person instance object that owns the oldest car
```


```python
Person.drives_a("Toyota") 
# class method that returns a list of person instance objects that own a Toyota
# example: [jim, pam, stanley]
Person.drives_a("Ford")
# class method that returns a list of person instance objects that own a Ford
# example: [meredith]
```


```python
jim.drives_same_make_as_me()
# instance method that returns a list of other dunder mifflin employees 
# that drive the same make car as the instance object it was called on
# example: [pam, stanley]
```


```python
Car.cars_driven_by("Paper Salesperson")
# class method that returns a list of car instance objects that are driven 
# by people whose occupation is "Paper Salesperson"
# example: [dwight, jim, stanley]
```

## Summary


Great work! In this lab we successfully created a belongs to relationship between different Python classes. We were able to create a domain that more closely resembles a real world structure by translating the real world relationship between cars and people into code. We were then able to leverage this relationship in order to query information about our classes and their instances. Object relationships, although more straight forward than relationships between living people, can get quite complex and it is important to think critically about how to set them up properly. In a belongs to relationship, we learned it is the responsibilty of the *belongs to* class (the Car class) to know what it belongs to. 
