create table manzano (
	id integer PRIMARY KEY AUTOINCREMENT, 
	numero integer not null,
	superficie_total integer not null,
	precio_total integer not null
);

create table lote (
	id integer PRIMARY KEY AUTOINCREMENT,
	numero integer not null,
	superficie integer not null,
	valor_m2 integer not null,
	precio integer not null,
	codigo varchar (11) not null,
	estado varchar(1) not null default 'D',
	manzano_id integer not null,
	foreign key(manzano_id) references manzano(id)
);

create table representante (
	id integer PRIMARY KEY AUTOINCREMENT,
	nombres varchar (35) not null,
	apellidos varchar (35) not null,
	genero varchar (1) not null,
	telefono varchar (10) not null
);

create table cliente (
	id integer PRIMARY KEY AUTOINCREMENT,
	nombres varchar (35)not null,
	apellidos varchar (50) not null,
	telefono varchar (10) not null,
	email varchar (50) not null,
	genero varchar (1) not null ,
	fecha_nacimiento date not null
);

create table contrato (
	id integer PRIMARY KEY AUTOINCREMENT,
	fecha_inicial date not null,
	fecha_final date not null,
	monto_total integer not null,
	tipo_pago varchar(1) not null,
	cliente_titular_id integer not null,
	cliente_testigo_id integer not null,
	lote_id integer not null,
	representante_id integer not null,
	foreign key (cliente_titular_id) references cliente(id),
	foreign key (cliente_testigo_id) references cliente(id),
	foreign key (lote_id) references lote(id),
	foreign key (representante_id) references representante(id)
);

create table cuota (
	id integer PRIMARY KEY AUTOINCREMENT,
	fecha date not null,
	numero integer not null,
	vencimiento date not null,
	total_pago integer not null,
	deuda_inicial integer not null,
	saldo integer not null,
	contrato_id integer not null,
	foreign key (contrato_id) references contrato(id)
);

create table recibo (
	id integer PRIMARY KEY AUTOINCREMENT,
	numero integer not null,
	fecha date not null,
	cuota_id integer not null,
	foreign key (cuota_id) references cuota(id)
);
