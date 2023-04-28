INSERT INTO Users (name, surname, email, password, created_at, updated_at, deleted_at, access_level_id)
VALUES ('Francesco', 'Di Muro', 'test@email.com', 'somepassword', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 100)

-- Customer 1

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

-- Customer 2

INSERT INTO Customers (name, created_at, updated_at, deleted_at)
VALUES ('Takeda S.p.A.', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL)

INSERT INTO Jobs (name, description, created_at, updated_at, deleted_at, customer_id)
VALUES ('C103-SYS-19', 'Sviluppo Software Pastorizzatore', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 2)

INSERT INTO Documents (name, description, created_at, updated_at, deleted_at, job_id)
VALUES ('LRAT-C103-SYS-19-01', 'Lista Records Audit Trail', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 2)

INSERT INTO Revisions (version, description, file_path, created_at, updated_at, deleted_at, document_id, user_id)
VALUES ('A', 'Prima emissione', '/Area Tecnico Operativa/Tecnico 2019/Commesse/C103-SYS-19 STB VALITECH Sviluppo software e fornitura licenze iFix pastorizzazione Takeda Pisa/Doc_Tecnica/Convalida', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 2, 1)

INSERT INTO Documents (name, description, created_at, updated_at, deleted_at, job_id)
VALUES ('MAN-C103-SYS-19-01', 'Manuale Operatore SCADA', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 2)

INSERT INTO Revisions (version, description, file_path, created_at, updated_at, deleted_at, document_id, user_id)
VALUES ('A', 'Prima emissione', '/Area Tecnico Operativa/Tecnico 2019/Commesse/C103-SYS-19 STB VALITECH Sviluppo software e fornitura licenze iFix pastorizzazione Takeda Pisa/Doc_Tecnica/Convalida', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 3, 1)

INSERT INTO Revisions (version, description, file_path, created_at, updated_at, deleted_at, document_id, user_id)
VALUES ('B', 'Emissione per qualifica', '/Area Tecnico Operativa/Tecnico 2019/Commesse/C103-SYS-19 STB VALITECH Sviluppo software e fornitura licenze iFix pastorizzazione Takeda Pisa/Doc_Tecnica/Convalida', strftime('%Y-%m-%dT%H:%M:%f', 'now'), strftime('%Y-%m-%dT%H:%M:%f', 'now'), NULL, 3, 1)
