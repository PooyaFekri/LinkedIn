create table if not exists user
(
	"first name" nvarchar not null,
	"last name" nvarchar not null,
	intro nvarchar,
	birthday nchar(50) not null,
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

create table if not exists Experience
(
	id INTEGER not null
		constraint Experience_pk
			primary key autoincrement,
	user_id INTEGER not null
		constraint Experience_user_id_fk
			references user
				on update cascade on delete cascade,
	text nvarchar not null
);

create unique index Experience_id_uindex
	on Experience (id);

create table Connection
(
	id INTEGER not null
		constraint Connection_pk
			primary key autoincrement,
	user_caller_id INTEGER not null
		constraint Connection_user_id_fk
			references user
				on update cascade on delete cascade,
	user_invited_id INTEGER not null
		constraint Connection_user_id_fk_2
			references user
				on update cascade on delete cascade,
	connected INTEGER not null
);

create unique index Connection_id_uindex
	on Connection (id);


create table if not exists Room
(
	id INTEGER not null
		constraint Room_pk
			primary key autoincrement,
	name nvarchar(200) not null,
	started_time varchar(50) not null,
	archive boolean not null
);

create unique index Room_id_uindex
	on Room (id);


create table if not exists Message
(
	id INTEGER not null
		constraint Message_pk
			primary key autoincrement,
	user_sender_id INTEGER not null,
	user_receiver_id INTEGER not null
		constraint Message_user_id_fk
			references user
				on update cascade on delete cascade
		constraint Message_user_id_fk_2
			references user
				on update cascade on delete cascade,
	text TEXT not null,
	room_id INTEGER not null
		constraint Message_Room_id_fk
			references Room
				on update cascade on delete cascade,
	time varchar(50) not null
);

create unique index Message_id_uindex
	on Message (id);

