--======== DROP TABLE ==============
DROP TABLE gender;
DROP TABLE testgroup;
DROP TABLE class_label;
DROP TABLE difficulty;
DROP TABLE video;
DROP TABLE user;
DROP TABLE classification;

--======== CREATE TABLES ===========
CREATE TABLE gender (
	label_id INTEGER NOT NULL,
	label_name TEXT NOT NULL,
	PRIMARY KEY(label_id)
);

CREATE TABLE testgroup (
	label_id INTEGER NOT NULL,
	label_name TEXT NOT NULL,
	PRIMARY KEY (label_id)
);

CREATE TABLE class_label (
	label_id INTEGER NOT NULL,
	label_name TEXT NOT NULL,
	PRIMARY KEY(label_id)
);

CREATE TABLE difficulty (
	label_id INTEGER NOT NULL,
	label_name TEXT NOT NULL,
	PRIMARY KEY(label_id)
);

CREATE TABLE video (
	video_id TEXT NOT NULL,
	video_link_id TEXT NOT NULL UNIQUE,
	label INTEGER NOT NULL,
	FOREIGN KEY (label) REFERENCES class_label(label_id),
	PRIMARY KEY(video_id)
);

CREATE TABLE user (
	session_id TEXT NOT NULL UNIQUE,
	gender INTEGER NOT NULL,
	testgroup INTEGER NOT NULL,
	age INTEGER NOT NULL,
	pixel_width	INTEGER NOT NULL,
	pixel_height INTEGER NOT NULL,
	fps	NUMERIC NOT NULL,
	FOREIGN KEY(session_id) REFERENCES django_session(session_key),
	FOREIGN KEY(gender) REFERENCES gender(label_id),
	FOREIGN KEY(testgroup) REFERENCES testgroup(label_id),
	PRIMARY KEY(session_id)
);

CREATE TABLE classification (
	session_id TEXT NOT NULL,
	video_id TEXT NOT NULL,
	class_label INTEGER NOT NULL,
	difficulty INTEGER NOT NULL,
	play_pause INTEGER NOT NULL,
	replay INTEGER NOT NULL,
	fullscreen INTEGER NOT NULL,
	playback INTEGER NOT NULL,
	duration_in_sec INTEGER NOT NULL,
	text TEXT NOT NULL,
	FOREIGN KEY(session_id) REFERENCES user(session_id),
	FOREIGN KEY(video_id) REFERENCES video(video_id),
	PRIMARY KEY(session_id, video_id),
	FOREIGN KEY (class_label) REFERENCES class(label_id),
	FOREIGN KEY (difficulty) REFERENCES difficulty(label_id)
);

--============== BASIC DATA DOMAINS ===============

INSERT INTO gender 
VALUES (1, 'male');

INSERT INTO gender 
VALUES (2, 'female');

INSERT INTO gender 
VALUES (3, 'other');

INSERT INTO testgroup
VALUES (1, 'feedback');

INSERT INTO testgroup
VALUES (2, 'no_feedback');

INSERT INTO difficulty
VALUES (1, 'easy');

INSERT INTO difficulty
VALUES (2, 'medium');

INSERT INTO difficulty
VALUES (3, 'hard');

INSERT INTO class_label
VALUES (1, 'REAL');

INSERT INTO class_label
VALUES (2, 'FAKE');
