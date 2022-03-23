set datestyle to "ISO , DMY";

drop view IF EXISTS PASSAGERSEXE;
drop view IF EXISTS PASSAGERCLASSE;
drop table IF EXISTS TICKETS;
drop table IF EXISTS LIENS;
drop table IF EXISTS PASSENGERS;

create Table PASSENGERS(PassengerId integer primary key, Name varchar(85) ,Sex varchar(15), Age float  );

create Table TICKETS(Ticket varchar(20) ,PassengerId integer references PASSENGERS,Pclass integer,Fare float,Cabin varchar(15),Embarked varchar(4),primary Key(PassengerId) );

Create Table LIENS(PassengerId integer references PASSENGERS,Survived varchar(1),Sibsp integer ,Parch integer,Primary key( PassengerId ));
