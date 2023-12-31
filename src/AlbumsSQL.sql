-- MySQL Script generated by MySQL Workbench
-- Mon Aug  7 04:56:35 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Grupo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Grupo` (
  `idGrupo` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idGrupo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Album` (
  `idAlbum` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `fecha_pub` DATE NULL,
  `precio` FLOAT NULL,
  `Grupo_idGrupo` INT NOT NULL,
  PRIMARY KEY (`idAlbum`, `Grupo_idGrupo`),
  INDEX `fk_Album_Grupo_idx` (`Grupo_idGrupo` ASC) VISIBLE,
  CONSTRAINT `fk_Album_Grupo`
    FOREIGN KEY (`Grupo_idGrupo`)
    REFERENCES `mydb`.`Grupo` (`idGrupo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Genero` (
  `idGenero` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idGenero`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Album_has_Genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Album_has_Genero` (
  `Album_idAlbum` INT NOT NULL AUTO_INCREMENT,
  `Genero_idGenero` INT NOT NULL,
  PRIMARY KEY (`Album_idAlbum`, `Genero_idGenero`),
  INDEX `fk_Album_has_Genero_Genero1_idx` (`Genero_idGenero` ASC) VISIBLE,
  INDEX `fk_Album_has_Genero_Album1_idx` (`Album_idAlbum` ASC) VISIBLE,
  CONSTRAINT `fk_Album_has_Genero_Album1`
    FOREIGN KEY (`Album_idAlbum`)
    REFERENCES `mydb`.`Album` (`idAlbum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Album_has_Genero_Genero1`
    FOREIGN KEY (`Genero_idGenero`)
    REFERENCES `mydb`.`Genero` (`idGenero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Factura` (
  `idFactura` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `Cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idFactura`, `Cliente_idCliente`),
  INDEX `fk_Factura_Cliente1_idx` (`Cliente_idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_Factura_Cliente1`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `mydb`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`FacturaAlbum`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FacturaAlbum` (
  `idFacturaAlbum` INT NOT NULL AUTO_INCREMENT,
  `cantidad` VARCHAR(45) NULL,
  `Factura_idFactura` INT NOT NULL,
  `Album_idAlbum` INT NOT NULL,
  PRIMARY KEY (`idFacturaAlbum`, `Factura_idFactura`, `Album_idAlbum`),
  INDEX `fk_FacturaAlbum_Factura1_idx` (`Factura_idFactura` ASC) VISIBLE,
  INDEX `fk_FacturaAlbum_Album1_idx` (`Album_idAlbum` ASC) VISIBLE,
  CONSTRAINT `fk_FacturaAlbum_Factura1`
    FOREIGN KEY (`Factura_idFactura`)
    REFERENCES `mydb`.`Factura` (`idFactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FacturaAlbum_Album1`
    FOREIGN KEY (`Album_idAlbum`)
    REFERENCES `mydb`.`Album` (`idAlbum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
