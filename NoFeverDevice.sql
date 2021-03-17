CREATE TABLE IF NOT EXISTS NoFeverDevice (
    NoFeverID       INT(4) UNSIGNED AUTO_INCREMENT,
    NoFeverName     VARCHAR(30),
    PRIMARY KEY (NoFeverID)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Adminstration (
    AdmID           INT(8) UNSIGNED AUTO_INCREMENT,
    CompanyName     VARCHAR(30) NOT NULL,
    CompanyAddress  VARCHAR(30) NOT NULL,
    Price           DECIMAL(10,2) NOT NULL,
    ContactPhNo     INT(8) UNSIGNED NOT NULL,
    PurchaseType    VARCHAR(20) NOT NULL,
    Email           VARCHAR(50) NOT NULL,
    NoFeverID       INT(4) UNSIGNED,
    PRIMARY KEY (AdmID),
    CONSTRAINT fk_AdminNoFeverID FOREIGN KEY (NoFeverID)
    REFERENCES NoFeverDevice(NoFeverID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS DataLog (
    FaceID          INT(8) UNSIGNED AUTO_INCREMENT,
    Dato            DATETIME NOT NULL,
    PersonTemp      DECIMAL(3,1) UNSIGNED NOT NULL,
    RoomTemp        DECIMAL(4,2) UNSIGNED NOT NULL,
    mask            VARCHAR(10) NOT NULL,
    age             int(3) UNSIGNED NOT NULL,
    gender          VARCHAR(10) NOT NULL,
    emotion         VARCHAR(20) NOT NULL,
    height          DECIMAL(3,1) UNSIGNED NOT NULL,
    NoFeverID       INT(4) UNSIGNED,
    PRIMARY KEY (FaceID),
    CONSTRAINT fk_DataLogNoFeverID FOREIGN KEY (NoFeverID)
    REFERENCES NoFeverDevice(NoFeverID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS SystemLog (
    ID              INT(8) UNSIGNED AUTO_INCREMENT,
    FileDescription VARCHAR(100) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=INNODB;