CREATE TABLE `authors` (
    `sid` BIGINT NOT NULL,
    `name` VARCHAR(500) NOT NULL,
    PRIMARY KEY (`sid`)
);

CREATE TABLE `addons` (
    `wsid` VARCHAR(32) NOT NULL,
    `name` VARCHAR(500) NULL,
    `author` BIGINT NOT NULL,
    `lastup` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`wsid`),
    FOREIGN KEY (`author`) REFERENCES `authors`(`sid`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `files` (
    `path` VARCHAR(500) NOT NULL,
    `addon` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`path`, `addon`),
    FOREIGN KEY (`addon`) REFERENCES `addons`(`wsid`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `errors` (
      `eid` INTEGER NOT NULL AUTO_INCREMENT,
      `path` VARCHAR(500) NOT NULL,
      `addon` VARCHAR(32) NOT NULL,
      `error` VARCHAR(500) NOT NULL,
      PRIMARY KEY (`eid`),
      FOREIGN KEY (`addon`) REFERENCES `addons`(`wsid`) ON DELETE CASCADE ON UPDATE CASCADE,
      FOREIGN KEY (`path`) REFERENCES `files`(`path`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `components` (
    `cid` VARCHAR(500) NOT NULL,
    `addon` VARCHAR(32) NOT NULL,
    `name` VARCHAR(500) NOT NULL,
    `model` VARCHAR(500) NOT NULL,
    PRIMARY KEY (`cid`, `addon`),
    FOREIGN KEY (`addon`) REFERENCES `addons`(`wsid`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `vehicles` (
    `vid` VARCHAR(500) NOT NULL,
    `addon` VARCHAR(32) NOT NULL,
    `name` VARCHAR(500) NOT NULL,
    `model` VARCHAR(500) NOT NULL,
    PRIMARY KEY (`vid`, `addon`),
    FOREIGN KEY (`addon`) REFERENCES `addons`(`wsid`) ON DELETE CASCADE ON UPDATE CASCADE
);
