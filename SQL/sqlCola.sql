CREATE SCHEMA IF NOT EXISTS `colaImpresionTfg` DEFAULT CHARACTER SET utf8 ;
USE `colaImpresionTfg` ;


CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Pedidos` (
  `idPedido` INT NOT NULL AUTO_INCREMENT,
  `Cliente` VARCHAR(45) NOT NULL,
  `Prioridad` INT NOT NULL,
  PRIMARY KEY (`idPedido`),
  UNIQUE INDEX `idPedido_UNIQUE` (`idPedido` ASC))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Trabajos` (
  `idTrabajos` INT NOT NULL AUTO_INCREMENT,
  `Id_Pedido` INT NOT NULL,
  `Id_Boquilla` INT NOT NULL,
  UNIQUE INDEX `idTrabajos_UNIQUE` (`idTrabajos` ASC),
  CONSTRAINT `id_Pedido`
    FOREIGN KEY ()
    REFERENCES `colaImpresionTfg`.`Pedidos` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Boquillas` (
)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Rollos` (
)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `colaImpresionTfg`.`Maquinas` (
)
ENGINE = InnoDB;

