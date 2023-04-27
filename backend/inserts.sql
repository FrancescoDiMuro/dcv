INSERT INTO Users (name, surname, email, password, created_at, updated_at, deleted_at, access_level_id)
VALUES ('Francesco', 'Di Muro', 'test@email.com', 'somepassword', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 100)

INSERT INTO Customers (name, created_at, updated_at, deleted_at)
VALUES ('Merck KGaA', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL)

INSERT INTO Jobs (name, description, created_at, updated_at, deleted_at, customer_id)
VALUES ('C062-SYS-18', 'Revamping SCADA', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 1)

INSERT INTO Documents (name, description, created_at, updated_at, deleted_at, job_id)
VALUES ('MAN-C062-SYS-18-01', 'Manuale Operatore SCADA', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 1)

INSERT INTO Revisions (version, description, file_path, created_at, updated_at, deleted_at, document_id, user_id)
VALUES ('A', 'Prima emissione', '/Area Tecnico Operativa/Archivio Old Tecnico Operativa/Tecnico 2018/Commesse/C062-SYS-18 MERCK Revamping SCADA/Doc_Tecnica/Convalida/MAN e MAN iFix Config', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 1, 1)

INSERT INTO Revisions (version, description, file_path, created_at, updated_at, deleted_at, document_id, user_id)
VALUES ('B', 'Nuovo reparto ADB-EL', '/Area Tecnico Operativa/Tecnico 2020/Commesse/C105-SYS-20 MERCK SERONO Fornitura JB e modifica Q.E. con Inserimento nuovi strum SCADA Labs BD Merck/Doc_Tecnica/Convalida/Documentazione_Tecnica/Master', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 1, 1)