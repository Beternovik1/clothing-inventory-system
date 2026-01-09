CREATE DATABASE IF NOT EXISTS products_db;
USE products_db;

CREATE TABLE IF NOT EXISTS products(
	product_id INT NOT NULL AUTO_INCREMENT,
    category ENUM('Pantalon', 'Empaquetado') NOT NULL DEFAULT 'Pantalon',
	color ENUM('Negro', 'Gris', 'Caqui', 'Verde', 'Azul', 'Hueso', 'Dorado', 'Transparente') NOT NULL,
	size ENUM('CH', 'M', 'G', 'XG', 'Unitalla') NOT NULL,
    cost_price DECIMAL(8, 2) NOT NULL COMMENT 'En cuanto se compro (MXN)'
		CONSTRAINT chk_cost_price CHECK (cost_price > 0.00),    
	sell_price DECIMAL(8, 2) NOT NULL COMMENT 'En cuanto se va a vender (MXN)'
		CONSTRAINT chk_sell_price CHECK (sell_price > 0.00),
	currently_stock INT DEFAULT 0 COMMENT 'Inventario actual',
	PRIMARY KEY(product_id),
    UNIQUE KEY uk_color_talla (color, size)
);

CREATE TABLE IF NOT EXISTS inventory_movements(
	mov_id INT NOT NULL AUTO_INCREMENT,
    movement_type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL 
		CONSTRAINT chk_quantity CHECK (quantity > 0),
    movement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (mov_id),
    product_id INT NOT NULL,
	CONSTRAINT fk_pro_inv
		FOREIGN KEY (product_id)
			REFERENCES products (product_id)
            ON UPDATE CASCADE
			ON DELETE RESTRICT  
);