
CREATE SCHEMA IF NOT EXISTS `colaImpresionTfg` DEFAULT CHARACTER SET utf8 ;
USE `colaImpresionTfg` ;

-- -----------------------------------------------------
-- Tabla "Pedido"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Pedido` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `Cliente` VARCHAR(45) NULL,
  `Prioridad` INT NULL,
  PRIMARY KEY (`idPedido`),
  UNIQUE INDEX `idPedido_UNIQUE` (`idPedido` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabla "Boquilla"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Boquilla` (
  `idBoquilla` INT NOT NULL AUTO_INCREMENT,
  `Tamaño` FLOAT NOT NULL,
  PRIMARY KEY (`idBoquilla`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabla "Rollo"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Rollo` (
  `idRollo` INT NOT NULL AUTO_INCREMENT,
  `Color` VARCHAR(45) NOT NULL,
  `T_Impresion` VARCHAR(45) NOT NULL,
  `Peso` VARCHAR(45) NULL,
  PRIMARY KEY (`idRollo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabla "Maquina"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Maquina` (
  `idMaquina` INT NOT NULL AUTO_INCREMENT,
  `idBoquilla` VARCHAR(45) NULL,
  `IdRollo` VARCHAR(45) NULL,
  `Boquilla_idBoquilla` INT NOT NULL,
  `Rollo_idRollo` INT NOT NULL,
  PRIMARY KEY (`idMaquina`),
  INDEX `fk_Maquina_Boquilla1_idx` (`Boquilla_idBoquilla` ASC),
  INDEX `fk_Maquina_Rollo1_idx` (`Rollo_idRollo` ASC),
  CONSTRAINT `fk_Maquina_Boquilla1`
    FOREIGN KEY (`Boquilla_idBoquilla`)
    REFERENCES `colaImpresionTfg`.`Boquilla` (`idBoquilla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Maquina_Rollo1`
    FOREIGN KEY (`Rollo_idRollo`)
    REFERENCES `colaImpresionTfg`.`Rollo` (`idRollo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Tabla "Trabajo"
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Trabajo` (
  `idTrabajo` INT NOT NULL,
  `Volumen` VARCHAR(45) NULL,
  `Fecha_Entrega` DATE NULL,
  `Pedido_idPedido` INT NOT NULL,
  `Rollo_idRollo` INT NOT NULL,
  `Boquilla_idBoquilla` INT NOT NULL,
  `Maquina_idMaquina` INT NOT NULL,
  PRIMARY KEY (`idTrabajo`, `Pedido_idPedido`),
  INDEX `fk_Trabajo_Pedido_idx` (`Pedido_idPedido` ASC),
  INDEX `fk_Trabajo_Rollo1_idx` (`Rollo_idRollo` ASC),
  INDEX `fk_Trabajo_Boquilla1_idx` (`Boquilla_idBoquilla` ASC),
  INDEX `fk_Trabajo_Maquina1_idx` (`Maquina_idMaquina` ASC),
  CONSTRAINT `fk_Trabajo_Pedido`
    FOREIGN KEY (`Pedido_idPedido`)
    REFERENCES `colaImpresionTfg`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Trabajo_Rollo1`
    FOREIGN KEY (`Rollo_idRollo`)
    REFERENCES `colaImpresionTfg`.`Rollo` (`idRollo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Trabajo_Boquilla1`
    FOREIGN KEY (`Boquilla_idBoquilla`)
    REFERENCES `colaImpresionTfg`.`Boquilla` (`idBoquilla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Trabajo_Maquina1`
    FOREIGN KEY (`Maquina_idMaquina`)
    REFERENCES `colaImpresionTfg`.`Maquina` (`idMaquina`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
