create table if not exists user
(
	first_name nvarchar not null,
	last_name nvarchar not null,
	intro nvarchar,
	birthday nchar(50) not null,
	id INTEGER not null
		constraint user_pk
			primary key autoincrement
);

create unique index if not exists user_id_uindex
	on user (id);

alter table user
	add username nvarchar(100) not null;

alter table user
	add password nvarchar(100) not null;

alter table user
	add nationality nvarchar(80);

alter table user
	add email nvarchar(90) not null;

alter table user
	add address nvarchar(200);

alter table user
	add "tel num" nvarchar(20);

create unique index if not exists user_username_uindex
	on user (username);


create table if not exists skill
(
	user_id INTEGER not null
		constraint skill_user_id_fk
			references user
				on update cascade on delete cascade,
	id INTEGER not null
		constraint skill_pk
			primary key autoincrement,
	text nvarchar not null
);

create unique index if not exists "skill_id _uindex"
	on skill (id);

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

create unique index if not exists Experience_id_uindex
	on Experience (id);

alter table Experience
	add start_time nvarchar(50) not null;

alter table Experience
	add end_time nvarchar(50);

create table if not exists Connection
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

create unique index if not exists Connection_id_uindex
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

create unique index if not exists Room_id_uindex
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

create unique index if not exists Message_id_uindex
	on Message (id);

create table if not exists Post
(
	user_id INTEGER not null
		constraint Post_user_id_fk
			references user
				on update cascade on delete cascade,
	id INTEGER not null
		constraint Post_pk
			primary key autoincrement,
	picture blob,
	text text,
	time nvarchar(50) not null,
	share INTEGER
		constraint Post_Post_id_fk
			references Post
				on update cascade
);

create unique index if not exists Post_id_uindex
	on Post (id);

create table if not exists Comment
(
	id INTEGER not null
		constraint Comment_pk
			primary key autoincrement,
	time varchar(50) not null,
	user_id INTEGER not null
		constraint Comment_user_id_fk
			references user
				on update cascade on delete cascade,
	text text not null,
	comment_reply_id INTEGER
		constraint Comment_Comment_id_fk
			references Comment
				on update cascade on delete cascade,
	post_id INTEGER
		constraint Comment_Post_id_fk
			references Post
				on update cascade on delete cascade
);

create unique index if not exists Comment_id_uindex
	on Comment (id);

create table if not exists Like
(
    id         INTEGER     not null
        constraint Like_pk
            primary key autoincrement,
    comment_id INTEGER
        references Comment
            on update cascade on delete cascade,
    post_id    INTEGER
        references Post
            on update cascade on delete cascade,
    time       varchar(50) not null,
    user_id    integer     not null
        references user
            on update cascade on delete cascade
);

create unique index Like_id_uindex
    on Like (id);


create table if not exists Endorse
(
	id INTEGER not null
		constraint Endorse_pk
			primary key autoincrement,
	skill_id INTEGER not null
		constraint "Endorse_skill_id_fk"
			references skill
				on update cascade on delete cascade,
	user_id INTEGER not null
		constraint Endorse_user_id_fk
			references user
				on update cascade on delete cascade
);

create unique index if not exists Endorse_id_uindex
	on Endorse (id);


create table if not exists Notification
(
    id      integer      not null
        constraint Notification_pk
            primary key autoincrement,
    user_id integer      not null
        references user
            on update cascade on delete cascade,
    type_id integer      not null,
    type    nvarchar(50) not null,
    time    nvarchar(50) not null,
    event   nvarchar(50),
    visited boolean default false not null
);

create unique index if not exists Notification_id_uindex
    on Notification (id);

create table if not exists Language
(
	id integer not null
		constraint Language_pk
			primary key autoincrement,
	user_id integer not null
		constraint Language_user_id_fk
			references user
				on update cascade on delete cascade,
	language integer not null
);

create unique index if not exists Language_id_uindex
	on Language (id);


