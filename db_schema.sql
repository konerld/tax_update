-- Schema for db

create table persons (
    id          number not null primary key,
    name        varchar2(32),
    surname     varchar2(32),
    sex         varchar2(32),
    age         number,
    tax         number
);

create table cars (
    id          number not null references persons(id),
    mark        varchar2(32),
    model       varchar2(32),
    year        number,
    color       varchar2(32),
    tax         number
);

INSERT INTO persons (id, name, surname, sex, age) 
         VALUES (1, 'Ivan', 'Sidorov', 'male', 31),
                (2, 'Sergey', 'Petrov', 'male', 25),
                (3, 'Irina', 'Kozlova', 'female', 23),
                (4, 'Olga', 'Krasenko', 'female', 33);
                
INSERT INTO cars (id, mark, model, year, color, tax) 
         VALUES (1, 'ford', 'mustang', 1969, 'grey', 5000),
                (2, 'kia', 'rio', 2017, 'red', 1500),
                (3, 'mazda', 'cx-5', 2015, 'white', 3000),
                (4, 'opel', 'omega', 1987, 'blue', 2000),
                (3, 'nissan', 'murano', 2019, 'black', 4500),
                (1, 'vw', 'tiguan', 2017, 'brown', 5500),
                (4, 'ford', 'focus', 2009, 'green', 1500),
                (1, 'opel', 'astra', 2014, 'white', 1700),
                (3, 'vw', 'tuareg', 2007, 'pink', 6000);