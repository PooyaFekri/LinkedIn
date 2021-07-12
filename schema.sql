create table if not exists user
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

create table if not exists skill
(
	user_id INTEGER not null
		constraint skill_user_id_fk
			references user
				on update cascade on delete cascade,
	"id " INTEGER not null
		constraint skill_pk
			primary key autoincrement,
	text nvarchar not null
);

create unique index "skill_id _uindex"
	on skill ("id ");

