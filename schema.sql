create table user
(
	"first name" nvarchar not null,
	"last name" nvarchar not null,
	intro nvarchar,
	birthday nchar not null,
	id INTEGER not null
		constraint user_pk
			primary key autoincrement
);

create unique index user_id_uindex
	on user (id);

