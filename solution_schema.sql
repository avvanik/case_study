create table `people` (
  `id` int not null auto_increment,
  `given_name` varchar(80) default null,
  `family_name` varchar(80) default null,
  `date_of_birth` date default null,
  `place_of_birth` varchar(80) default null,
  primary key (`id`)
);


